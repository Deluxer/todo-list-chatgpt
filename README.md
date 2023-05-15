# Todo List Flask Application Documentation
This script is a simple Todo List application written in Python using the Flask framework. The application allows users to add, retrieve, and delete tasks on a Todo List per username. The data, however, is not persistent and will be lost upon a Python session restart.

## Installation and Running
To install and run this application, you need Python and pip installed on your system. If you don't have them yet, you can download Python from python.org, and pip will be included in the installation.

Make sure to have Flask and flask_cors packages installed. If you don't have them, you can install using pip:
```bash
pip install flask flask_cors
```

To run the application, save the script into a file, e.g., app.py, and then run the script with Python from the command line:
```bash
python3 app.py
```

The application will run at http://127.0.0.1:3000.

# Usage
The application exposes several HTTP routes for interacting with the Todo List:

- POST /todos/<username>: Add a task to the user's Todo List. The request body should be a JSON in the form {"todo": "The Task"}.

- GET /todos/<username>: Get the user's Todo List. Returns a JSON array of tasks.

- DELETE /todos/<username>: Delete a task from the user's Todo List. The request body should be a JSON in the form {"todo_idx": index} where index is the index of the task to delete in the list.

Additionally, the application also serves an AI plugin manifest at GET /.well-known/ai-plugin.json and an OpenAPI specification at GET /openapi.yaml. These are used to integrate the application with the AI system.

## Testing in postman
- GET :http://127.0.0.1:3000/todos/user
- POST :http://127.0.0.1:3000/todos/user
```bash
{
    "todo": "Mis favoritos"
}
```
- DELETE :http://127.0.0.1:3000/todos/user
```bash
{
    "todo_idx": 1
}
```

### Documentation:
[Build an API](https://platform.openai.com/docs/plugins/getting-started/running-a-plugin)