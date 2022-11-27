---
title: LOCAL FILES
---

#

For more easy & fast working with local data files `skyant.data.entity` provides class `local.File`.
This class contains an instance method `save_local()` and class method `load_local()` that returns
a class instance.

## Saving

Please compare the saving JSON file with `local.File` and without it:



=== "`skyant.data.entity.local.File`"


    ```py linenums='1' title='saving JSON'
    File.save_local('any/subfolders/test.json')
    ```


=== "pure `pydantic.BaseModel`"

    ```py linenums='1' title='saving JSON'
    with open('test.json', 'w', encoding='utf8') as file_obj:
        json.dump(file_obj, test_model)
    ```


The `skyant.data.entity.local.File` provides not only more shortly syntax but also additional
features:

- auto-creating subfolders

- saving in different formats (json, yaml/yml)

- encapsulated decoder for serialization more field types such as own special field type
    [FirestoreRef](references/entity/fields/FirestoreRef.md) that defines references between documents in [Firestore](https://cloud.google.com/firestore) - NoSQL serverless database[^1]


```py linenums='1' title='saving JSON (you can try it in Jupyter)'
from datetime import datetime as dt
from pydantic import BaseModel
from skyant.data.entity import local


class Nested(BaseModel):
    id: str
    date: dt.now()


class Test(local.File):
    num: int = 1
    ip: 
    nested: Nested


test_model = Test(
    nested=Nested(id='2ww2', name='NAME')
)

test_model.save_local('any/subfolders/test.json')
test_model.save_local('another/folder/test.yaml')
```


The method `dict()` of `pydantic.BaseModel` will receives the next parameters: `by_alias`, `exclude_unset`, `exclude_defaults`, `exclude_none`, all they will be passed to the method
`save_local`.
You can read more details [here](https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeldict).



## Loading

You should pass only one obligatory argument to class method `local_load('path/to/file.json')`
to get the `File` class instance from your file.


```py linenums='1' title='loading JSON'
loaded_model = Test.local_load('any/subfolders/test.json')
```


[^1]:
    Please found [here](google/firestore.md) more details about work with Google Cloud Firestore.
