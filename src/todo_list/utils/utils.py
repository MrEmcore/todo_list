from fastapi import HTTPException
from functools import wraps

PROCESS_ACCEPTED_VALUES = ["pending", "in process", "complete"]

def validate_process(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      process = kwargs.get("process").lower() or (args[1].lower() if len(args) > 1 else None)
      if process not in PROCESS_ACCEPTED_VALUES:
          raise HTTPException(status_code=422, detail=f"process must be one of {PROCESS_ACCEPTED_VALUES}")
      return func(*args, **kwargs)
  return wrapper