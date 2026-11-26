from fastapi import HTTPException
from functools import wraps

PROCESS_ACCEPTED_VALUES = ["pending", "in process", "complete"]

def style_inputs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("process"):
            task = kwargs.get("task").title()
            process = kwargs.get("process").lower()
            return func(task, process)
        else:
            task = kwargs.get("task").title()
            return func(task)
    return wrapper

def validate_process(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      process = args[1]
      if process not in PROCESS_ACCEPTED_VALUES:
          raise HTTPException(status_code=422, detail=f"process must be one of {PROCESS_ACCEPTED_VALUES}")
      return func(*args)
  return wrapper


