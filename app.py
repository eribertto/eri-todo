from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos: list [None] = []


@app.route("/", methods=['GET'])
def index():
    return render_template("todo.html", todos=todos)


@app.route("/add", methods=['POST'])
def add_todo():
    if request.form['todo']:
        todo = request.form["todo"]
        todos.append(todo)
    return redirect("/")


# /delete/2
# to delete todo with index 2
@app.route("/delete/<int:index>", methods=['GET'])
def delete_todo(index):
    try:
        del todos[index-1]
    except ValueError as e:
        print(e)
    return render_template("todo.html", todos=todos)
