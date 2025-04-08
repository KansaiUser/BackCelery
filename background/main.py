from fastapi import FastAPI, BackgroundTasks
import uuid
import time

app = FastAPI()
task_status = {}


def write_log_with_status(task_id: str, message: str):
    task_status[task_id] = "in progress"
    time.sleep(30)
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")
    task_status[task_id] = "done"


@app.post("/notify/")
async def notify_user(email: str, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    background_tasks.add_task(
        write_log_with_status, task_id, f"Notification sent to {email}"
    )
    return {"task_id": task_id}


@app.get("/task-status/{task_id}")
async def get_status(task_id: str):
    return {"status": task_status.get(task_id, "not found")}
