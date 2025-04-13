# Celery

Assuming you have already install Redis and you have it running.
You can check it out by doing

```bash
$redis-cli ping
PONG
```

## Start celery worker

```bash
celery -A celery_worker.celery worker --loglevel=info
```

- `-A celery_worker.celery` tells Celery to look for the celery instance inside the `celery_worker.py` file.

- `worker` starts the worker process that listens for tasks.

- `--loglevel=info` gives detailed logs for debugging.

## Run the script to send tasks to Celery

```bash
uvicorn main:app --reload
```
