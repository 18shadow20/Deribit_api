from celery import Celery
from celery.schedules import crontab

from deribit_app import add_db

app = Celery("deribit_crypto",  broker="memory://", backend="rpc://")

@app.task(ignore_result=True)
def add_db_min():
    add_db()


app.conf.beat_schedule = {
    "fetch-crypto-every-minute": {
        "task": "add_db_min",
        "schedule": crontab(minute="*/1"),
    },
}

