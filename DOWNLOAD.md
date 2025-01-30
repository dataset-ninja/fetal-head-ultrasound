Dataset **Fetal Head UltraSound** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzIwOTBfRmV0YWwgSGVhZCBVbHRyYVNvdW5kL2ZldGFsLWhlYWQtdWx0cmFzb3VuZC1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICIvUnQ5Nm41Y2p5Wml6R0RKQkhyOFhHK2RUSEZzMC9kVi9CbXM5aElzL1J3PSJ9)

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

