---
title: GOOGLE FIRESTORE
---

#


The [Firestore](https://cloud.google.com/firestore) is a simple and featured NoSQL serverless
database from Google.

You get easy methods for an interaction to Firestore an object `skyant.data.entity.google.Firestore` from.


## Save to Firestore

=== "code"

    ```py linenums='1' title='save data'
    from skyant.data.entity.google import Firestore

    class MyModel(Firestore):
        id: str
        num: int

    my_data = MyModel(id='some id', num=4)

    my_data.save_firestore('collection/doc/collection2')
    ```

=== "result"

    ![New document](/static/firestore-01.png){ loading=lazy }


### known doc


### unknown doc


### reference


## Load from Firestore
