from fastapi import FastAPI
from . import db
from .utils.utils import validate_process

app = FastAPI()

@app.post("/add_task")
@validate_process
def add_task(task, process):
    process = process.lower()
    task = task.title()
    return db.add_task(task, process)
    
@app.get("/read_tasks")
def read_tasks():
    tasks = db.read_tasks()
    if len(tasks) < 1:
        return "Currently no tasks"
    else:
        return tasks

@app.post("/update_task")
@validate_process
def update_task(task, process):
    return db.update_task(task, process)

@app.post("/delete_task")
def delete_task(task):
    return db.delete_task(task)

@app.post("/clear_all")
def clear_all():
    return db.clear_all()


# if __name__ == "__main__":
#     add_task("Do the dishes", "Pending")