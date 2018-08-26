from flask import Flask, render_template, url_for
import os
from app import app

@app.route('/')
@app.route('/index')
def index():
    print(os.getcwd())
    names = sorted(os.listdir(os.getcwd() + r'\app\static\img\name'))
    tasks = sorted(os.listdir(os.getcwd() + r'\app\static\img\task'))
    
    return render_template('show.html', names=names, tasks=tasks)