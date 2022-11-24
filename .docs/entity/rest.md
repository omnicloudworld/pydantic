---
title: REST
---

#

Using the `skyant.data.entity.rest.General` you can easy send your data to a REST endpoint or make
the instance from the data which was got from the REST server.

The `rest.General` made a request and handle a gotten respond for you.

## Sending data

You will got a JSON from
the responding by default or the full respond object if argument `json_only` is False.

```py linenums='1' title='making object'
from skyant.data.entity.rest import General`

class MyModel(General):
    id: str
    count: int

my_data = MyModel(id='some_id', count=33)
```

You can define which data will be send through arguments `exclude_unset`, `exclude_defaults`, `exclude_none`. For mode details see [the documentation of pydantic](https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeldict).

### As POST

```py linenums='1' title='send data as POST request'
returned_data = my_data.send_post('https://endpoint.url')  # JSON only from responding
returned_data = my_data.send_post('https://endpoint.url', json_only=False)  # full responding
```

## Loading data

Using our classmethods you can made an instance of `skyant.data.entity` from respond from REST API.

### From GET


```py linenums='1' title='making object'
from skyant.data.entity.rest import General`

class MyModel(General):
    id: str
    count: int

my_data = MyModel.load_get('https://endpoint.api')
```


### From POST


```py linenums='1' title='making object'
from skyant.data.entity.rest import General`

class MyModel(General):
    id: str
    count: int

my_data = MyModel.load_post(
    'https://endpoint.api',
    {'request': 'data'}
)
```
