from flask import Flask, render_template, url_for, request, redirect
import os
import json
import glob
from datetime import datetime
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

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = datetime.strftime(datetime.now(), '%Y-%m-%d')

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    if form.get("imgtype", None) == "name":
        target = "app/static/img/name"
    elif form.get("imgtype", None) == "task":
        target = "app/static/img/task"

    print("=== Form Data ===")
    for key, value in list(form.items()):
        print(key, "=>", value)

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0].replace("Screenshot_", "")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    if is_ajax:
        return ajax_response(True, upload_key)
    else:
        return redirect(url_for("upload_complete", uuid=upload_key))


def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))
