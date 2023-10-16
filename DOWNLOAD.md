Dataset **Fetal Head UltraSound** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/N/MJ/VYjVkYS8oYBpkdgFlG1RHAOwYbu6bWQOnbkITmfeN3bTfRJ6eE4CE1RFVP0xSSNqLvBpzcaZ0SgbNFLLTPer9dQViDLaB0SntUeVWNXUOfIeniV67CwRSqYEbDhp.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Fetal Head UltraSound', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

