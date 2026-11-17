# TODO List

A simple REST API for managing a TODO list, built with FastAPI and SQLite.

## Features

- Add a task
- List all tasks
- Update a task's status
- Delete a task

## Tech Stack

- Python
- FastAPI
- SQLite

## Getting Started

### Prerequisites

- Python 3.x
- [uv](https://docs.astral.sh/uv/) (package manager)

### Installation

1. Clone the repo:
git clone https://github.com/MrEmcore/todo_list.git

2. Install dependencies
uv sync

3. Start the server
uv run fastapi dev


## Usage

Once the server is running, open the interactive API docs at:

http://127.0.0.1:8000/docs

From there you can test all endpoints directly in the browser.

## Roadmap

1. Tests: Create tests for db.py functions using pytest.

2. Pydantic models — replace the raw query parameters in main.py with proper request/response models. This is how FastAPI is meant to be used and it's a
core TypeScript-adjacent skill (strong typing, schema validation).

3. Error handling: Add proper HTTP responses

4. Add additional columns: Due dates and priorities

5. Add Authentication

6. Frontend: Build a simple UI that interacts with the API