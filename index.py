import os
import json
import yaml
from flask import Flask, jsonify, Response, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

PORT = 3000

# Note: Setting CORS to allow chat.openapi.com is required for ChatGPT to access your plugin
CORS(app, origins=[f"http://localhost:{PORT}", "https://chat.openai.com"])

api_url = 'http://localhost:3000'

_TODOS = {}

@app.post("/todos/<string:username>")
def add_todo(username):
    requestTodo = request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(requestTodo["todo"])
    return Response(response='OK', status=200)

@app.get("/todos/<string:username>")
def get_todos(username):
    return Response(response=json.dumps(_TODOS.get(username, [])), status=200)

@app.delete("/todos/<string:username>")
def delete_todo(username):
    requestTodo = request.get_json(force=True)
    print('REquest: ', requestTodo)
    todo_idx = requestTodo["todo_idx"]
    # fail silently, it's a simple plugin
    if 0 <= todo_idx < len(_TODOS[username]):
        _TODOS[username].pop(todo_idx)
    return Response(response='OK', status=200)

@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    host = request.headers['Host']
    print(f'Host: {host}')
    return send_from_directory(os.path.dirname(__file__) + "/.well-known", 'ai-plugin.json')

@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
    yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return jsonify(yaml_data)

@app.route('/openapi.json')
def serve_openapi_json():
    return send_from_directory(os.path.dirname(__file__), 'openapi.json')

def main():
    app.run(debug=True, host="127.0.0.1", port=PORT)

if __name__ == "__main__":
    main()