from celery import Celery
from random import randint

app = Celery('tasks', broker='redis://0.0.0.0:6379', backend='redis://0.0.0.0:6379')


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'tasks.add',
        'schedule': 5.0,
        'args': (randint(1, 20), randint(1, 50))
    },
}