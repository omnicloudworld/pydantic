---
title: GOOGLE TASKS
---

#


The [Google Cloud Tasks](https://cloud.google.com/tasks) is a task manager that delivers any HTTP
requests to any endpoint. The Cloud Tasks can send a request only to single endpoints and waits
a response up to 1 hour.

```py linenums='1' title='send task'
from skyant.data.entity.google import Tasks

class MyModel(Tasks):
    id: str
    num: int

my_data = MyModel(id='some_id', nim=3)

my_data.send_gtasks(
    queue='tasks-queue-name', 
    location=Tasks.location.US_CENTRAL1,
    url='https://your.api',
    method=Tasks.method.POST
)
```
