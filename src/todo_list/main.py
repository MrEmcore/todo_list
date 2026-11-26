from fastapi import FastAPI
from . import db
from .utils.utils import validate_process, style_inputs

app = FastAPI()

@app.post("/add_task")
@style_inputs
@validate_process
def add_task(task, process):
    return db.add_task(task, process)
    
@app.get("/read_tasks")
def read_tasks():
    tasks = db.read_tasks()
    if len(tasks) < 1:
        return "There are currently no tasks stored."
    else:
        return tasks

@app.post("/update_task")
@style_inputs
@validate_process
# TODO: add task check before update
def update_task(task, process):
    return db.update_task(task, process)

@app.post("/delete_task")
@style_inputs
# TODO: add task check before delete
def delete_task(task):
    return db.delete_task(task)

@app.post("/clear_all")
def clear_all():
    return db.clear_all()