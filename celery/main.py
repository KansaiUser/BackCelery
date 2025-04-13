from fastapi import FastAPI
from celery_worker import write_log_celery

app = FastAPI()


@app.post("/notify/")
async def notify_user(email: str):
    write_log_celery.delay(f"Notification sent to {email}")
    return {"message": f"Email will be sent to {email}"}
