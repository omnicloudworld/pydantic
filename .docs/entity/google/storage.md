---
title: STORAGE
---


#

For work with [Google Cloud Storage](https://cloud.google.com/storage) you should use the Cloud
SDK client which needs an additional skills.

With `skyant.data.entity.google.Blob` this process is more easy.

## Saving

```py linenums='1' title='save to google cloud storage'
from skyant.data.entity.google import Blob

class MyModel(Blob):
    id: str
    num: int

my_data = MyModel(id='some-id', num=45)

my_data.save_gcs('gs://your-bucket/my-data.json')
my_data.save_gcs('gs://your-bucket/my-data.yaml')
```

## Loading

```py linenums='1' title='loading from google cloud storage'
from skyant.data.entity.google import Blob

class MyModel(Blob):
    id: str
    num: int
    
data_from_json = MyModel.load_gcs('gs://your-bucket/my-data.json')
data_from_yaml = MyModel.load_gcs('gs://your-bucket/my-data.yaml')
```
