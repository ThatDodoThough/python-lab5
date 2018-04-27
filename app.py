from flask import Flask, redirect, url_for, render_template, request
import db
from db import checkPresente

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect( url_for("arrival") )

@app.route("/index")
def arrival():
    listato = db.showTasks()
    IDs = db.parallelIDs()
    num = len(listato)
    indici = []
    i=0
    while i<num:
        indici.append(i)
        i=i+1
    return render_template("lab5.html", N = num, lista = listato, indici = indici, IDs = IDs)

@app.route("/insertNewTask", methods=["POST"])
def insert():
    nuovo = request.form["txtbox"]
    presente = db.checkPresente(nuovo)
    if presente==-1:
        db.newTask(nuovo)
        return redirect(url_for("arrival"))
    return render_template("newTaskError.html", task=nuovo, codice=0)

@app.route("/deleteTask/<task_id>")
def delete(task_id):
    print(task_id)
    db.removeTaskByID(task_id)
    return redirect(url_for("arrival"))


if __name__ == '__main__':
    db.init()
    app.run()
