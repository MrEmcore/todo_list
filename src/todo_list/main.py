from fastapi import FastAPI
from . import db

app = FastAPI()

@app.post("/add_task")
def add_task(task, process):
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