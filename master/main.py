from fastapi import FastAPI, Request
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_worker import celery_app

app = FastAPI()

class AddRequest(BaseModel):
    x: int
    y: int

@app.post("/add")
def add(request: AddRequest):
    task = celery_app.send_task("celery_worker.add", args=[request.x, request.y])
    return {"task_id": task.id}

@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }
    
@app.get("/status/{task_id}")
def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.successful() else None
    }
