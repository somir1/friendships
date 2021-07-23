from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.friend import User

@app.route('/')
def index ():
    users = User.get_all()
    mains = User.get_all_users()
    return render_template('index.html', users = users, mains = mains)

@app.route('/adduser', methods = ['POST'])
def add_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/newfriend', methods = ['POST'])
def new_friend():
    print(request.form)
    User.make_friends(request.form)
    return redirect('/')


