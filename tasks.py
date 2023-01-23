from celery_app import app
import time
from random import randint

@app.task
def hello():
    print(f"Hello at {time.time()}")

@app.task(bind=True, max_retries=1)
def add(self, x, y):
    try:
        if randint(1, 100) > 0:
            raise Exception("Failed")
        return x + y
    except:
        self.retry(countdown=5)