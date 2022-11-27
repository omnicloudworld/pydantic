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


The Firestore's document nama path is `collection`/`document`(`collection`/`document`)* You can pass
to the `save_firestore` both path as document path well as collection path.

If path will be a collection path the method returns the new document id as a string. If path will be
a document path the method write data to this document with no returns.

In the case when a target document exists the method `save_firestore` raise an error DocumentExist. To
avoid this exception you should define one of arguments: `overwrite=True` or `raise_exist=False`. If
`raise_exist` is False will raises a warning.


### reference

The Firestore has a special field type 'reference'. This field contains a link from one document to
another. Unfortunately in this case the developer should been define linked document additionally.

If you define field as `skyant.data.entity.fields.FirestoreRef` you can use string as reference and
the method `save_firestore` make firestore reference correctly.

=== "code"

    ```py linenums='1' title='save with reference'
    from skyant.data.entity.google import Firestore
    from skyant.data.entity.fields import FirestoreRef

    class MyModel(Firestore):
        id: str
        ref: FirestoreRef

    my_data = MyModel(id='some id', ref='collection/doc/collection2/z6BlJhP19Q1nhq7MYcbC')

    my_data.save_firestore('collection/doc/collection2/plusRef')
    ```

=== "result"

    ![Document with reference](/static/firestore-02.png){ loading=lazy }


## Load from Firestore

For making a `skyant.data.entity.google.Firestore` instance from a Firestore document, please use
the class method `load_firestore()`

```py linenums='1' title='save with reference'
from skyant.data.entity.google import Firestore

class MyModel(Firestore):
    id: str
    ref: FirestoreRef

my_data = MyModel.load_firestore('collection/doc/collection2/plusRef')
```
