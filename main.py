from flask import Flask, request, render_template_string, redirect, url_for
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para la aplicación

todos = []

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        todo = request.form.get('todo')
        todos.append(todo)
        return redirect(url_for('todo_list'))  # Redirigir al usuario a la página principal después de añadir una tarea
    
    return render_template_string("""
    <form method="POST">
        <input type="text" name="todo" placeholder="Add a todo">
        <input type="submit" value="Add">
    </form>
    <ul>
        {% for todo in todos %}
            <li>{{ todo }}</li>
        {% endfor %}
    </ul>
    """, todos=todos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # correr en localhost en el puerto 5000
