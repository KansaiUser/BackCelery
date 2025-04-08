from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def write_log(message: str):
    time.sleep(30)  # simulate delay
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")


@app.post("/notify/")
async def notify_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": f"Email will be sent to {email}"}
