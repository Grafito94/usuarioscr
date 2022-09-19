from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import User


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/leer')
def views():
    user = User.view()
    return render_template("leer.html", user = user)

@app.route('/create_user', methods = ['POST'])
def create():
    User.save(request.form)
    return redirect('/leer')

@app.route('/delete_one/<int:id>')
def delete(id):
    formulario = {
        "id":id
    }    
    User.delete(formulario)
    return redirect('/leer')


@app.route('/edit_one/<int:id>')
def edit(id):
    formulario = {
        "id":id
    }    
    user = User.buscar(formulario)
    print(user)
    return render_template('edit_one.html', user = user)


@app.route('/edit', methods = ['POST'])
def edits():

    User.edit(request.form)
    return redirect('/leer')

@app.route('/read_one/<int:id>')
def read(id):
    formulario = {
        "id":id
    }    
    user = User.buscar(formulario)
    print(user)
    return render_template('read_one.html', user = user)
    
    





