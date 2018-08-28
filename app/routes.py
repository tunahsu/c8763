from flask import Flask, render_template, url_for
import os
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Windows path
    # names = sorted(os.listdir(os.getcwd() + r'\app\static\img\name'))
    # tasks = sorted(os.listdir(os.getcwd() + r'\app\static\img\task'))
    
    #Linux path
    path1 = os.getcwd() + r'/app/static/img/name'
    path2 = os.getcwd() + r'/app/static/img/task'
    
    names = sorted(os.listdir(path1))
    tasks = sorted(os.listdir(path2))
    
    return render_template('show.html', names=names, tasks=tasks)