import os
from urllib.parse import unquote, urlparse

import cv2
import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import file_exists, get_file_name
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...", total=fsize
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(
                        team_id, teamfiles_path, local_path, progress_cb=pbar
                    )

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    test_path = os.path.join("test_set", "test_set")
    train_path = os.path.join("training_set", "training_set")
    batch_size = 50

    project_dict = {
        "test": [
            os.path.join(test_path, file)
            for file in os.listdir(test_path)
            if file.endswith(".png")
        ],
        "train": [
            os.path.join(train_path, file)
            for file in os.listdir(train_path)
            if file.endswith(".png")
        ],
    }

    def fill_area(mask_np):
        res = cv2.findContours(
            mask_np.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        contours = res[-2]
        img_pl = np.zeros((mask_np.shape[0], mask_np.shape[1]))
        cv2.fillPoly(img_pl, pts=contours, color=(255))
        return img_pl

    def create_ann(image_path):
        labels = []
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        base_path, file_name = os.path.split(image_path)
        mask_name = get_file_name(file_name) + "_Annotation.png"
        mask_path = os.path.join(base_path, mask_name)
        if file_exists(mask_path):
            obj_class = meta.get_obj_class("fetal head circumference")
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            mask = fill_area(mask_np)
            obj_mask = mask == 0
            geometry = sly.Bitmap(~obj_mask)
            curr_label = sly.Label(geometry, obj_class)
            labels.append(curr_label)
        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_classes = [sly.ObjClass("fetal head circumference", sly.Bitmap)]
    project = api.project.create(
        workspace_id, project_name, change_name_if_conflict=True
    )
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    dataset_train = api.dataset.create(
        project.id, "train", change_name_if_conflict=True
    )
    dataset_test = api.dataset.create(project.id, "test", change_name_if_conflict=True)

    progress = sly.Progress(
        "Create dataset {}".format("ds"),
        len(project_dict["test"]) + len(project_dict["train"]),
    )

    for ds in project_dict:
        if ds == "test":
            dataset = dataset_test
        else:
            dataset = dataset_train
        for img_paths_batch in sly.batched(project_dict[ds], batch_size=batch_size):
            img_paths = [
                file_path
                for file_path in img_paths_batch
                if "Annotation" not in file_path
            ]
            img_names_batch = [os.path.basename(img_path) for img_path in img_paths]
            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_paths)
            img_ids = [im_info.id for im_info in img_infos]
            anns_batch = [create_ann(image_path) for image_path in img_paths]
            api.annotation.upload_anns(img_ids, anns_batch)
            progress.iters_done_report(len(img_names_batch))
    return project
