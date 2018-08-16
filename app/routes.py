from flask import Flask, render_template, url_for
import os
from app import app

@app.route('/')
@app.route('/index')
def index():
    names = sorted(os.listdir('C:/Users/winproluhao/Desktop/c8763/app/static/img/outcome/name/'))
    tasks = sorted(os.listdir('C:/Users/winproluhao/Desktop/c8763/app/static/img/outcome/task/'))
    
    return render_template('show.html', names=names, tasks=tasks)