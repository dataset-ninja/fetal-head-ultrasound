Dataset **Fetal Head UltraSound** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjA5MF9GZXRhbCBIZWFkIFVsdHJhU291bmQvZmV0YWwtaGVhZC11bHRyYXNvdW5kLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogInIyRmRPd3p1d1IrdWhXWUtjQlVxN0ZPS1dhTXJoNXpHZVJ0QlU5dStYdms9In0=?response-content-disposition=attachment%3B%20filename%3D%22fetal-head-ultrasound-DatasetNinja.tar%22)

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

