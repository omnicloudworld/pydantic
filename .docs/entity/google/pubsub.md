---
title: GOOGLE PUBSUB
---

#


The [Google Cloud PubSub](https://cloud.google.com/pubsub/) is an asynchronous messaging middleware
that receives a messages to many subscribers which will be Google Cloud resources.

For deploying a message to a topic you can use method `send_pubsub` from
`skyant.data.entity.google.PubSub`.

```py linenums='1' title='send data to the pubsub topic'
from skuant.data.entity.google import PubSub

class MyModel(PubSub):
    id: str
    num: int

my_data = MyModel(id='some_id', nim=3)

my_data.send_pubsub('topic-name')
```
