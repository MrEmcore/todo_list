import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'tasks.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS tasks (task_name, process)")

def add_task(task, process):
  with sqlite3.connect(DB_PATH) as conn:
      conn.execute('INSERT INTO tasks VALUES (?, ?)', (task, process))
      return f"task added: {task}"

def read_tasks():
  with sqlite3.connect(DB_PATH) as conn:
      result = conn.execute("SELECT task_name, process FROM tasks")
      return result.fetchall()

def update_task(task, process):
  with sqlite3.connect(DB_PATH) as conn:
      conn.execute('UPDATE tasks SET process = ? WHERE task_name = ?', (process, task))
      result = conn.execute('SELECT task_name, process FROM tasks WHERE task_name = ?', (task,))
      return result.fetchall()

def delete_task(task):
  with sqlite3.connect(DB_PATH) as conn:
      conn.execute('DELETE FROM tasks WHERE task_name = ?', (task,))

init_db()