from fastapi import FastAPI
from . import db
from .utils.utils import PROCESS_ACCEPTED_VALUES

app = FastAPI()

@app.post("/add_task")
# TODO: create validators for task and process
def add_task(task, process):
    process = process.lower()
    task = task.title()
    if process not in PROCESS_ACCEPTED_VALUES:
        return f"process must be one of {PROCESS_ACCEPTED_VALUES}"
    return db.add_task(task, process)
    
@app.get("/read_tasks")
def read_tasks():
    return db.read_tasks()

@app.post("/update_task")
def update_task(task, process):
    return db.update_task(task, process)

@app.post("/delete_task")
def delete_task(task):
    return db.delete_task(task)

@app.post("/clear_all")
def clear_all():
    return db.clear_all()