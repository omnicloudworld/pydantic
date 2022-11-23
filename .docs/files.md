---
title: LOCAL FILES
hide:
    - navigation
---

#

For more easy & fast working with local data files `skyant.data.entity` provides class `files.Local`.

Please compare the saving JSON file with `files.Local` and without it:



=== "`skyant.data.entity.files.Local`"


    ```py linenums='1' title='saving JSON'
    Local.save_local('any/subfolders/test.json')
    ```


=== "pure `pydantic.BaseModel`"

    ```py linenums='1' title='saving JSON'
    with open('test.json', 'w', encoding='utf8') as file_obj:
        json.dump(file_obj, test_model)
    ```


The `skyant.data.entity.files.Local` provides not only more shortly syntax but also additional
features:

- auto-creating subfolders

- saving in different formats (json, yaml/yml)

- encapsulated decoder for serialization more field types such as own special field type
    [FirestoreRef](references/entity/fields/FirestoreRef.md) that defines references between documents in NoSQL serverless database [Firestore](https://cloud.google.com/firestore)


```py linenums='1' title='saving JSON (you can try it in Jupyter)'
from datetime import datetime as dt
from pydantic import BaseModel
from skyant.data.entity import files


class Nested(BaseModel):
    id: str
    date: dt.now()


class Test(files.Local):
    num: int = 1
    ip: 
    nested: Nested


test_model = Test(
    nested=Nested(id='2ww2', name='NAME')
)

test_model.save_local('any/subfolders/test.json')
test_model.save_local('another/folder/test.yaml')
```
