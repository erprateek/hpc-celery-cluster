from fastapi import FastAPI, Request
from celery_worker import add

app = FastAPI()

@app.post("/add")
async def submit_add_task(request: Request):
    data = await request.json()
    x = data.get("x", 0)
    y = data.get("y", 0)
    task = add.delay(x, y)
    return {"task_id": task.id, "status": "submitted"}
