#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/23 18:50
# @Author : bao
# @Site : 
# @File : aa.py
# @Software: PyCharm
# depends on flask, werkzeug
import os
from string import Template
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import socket

app = Flask(__name__)
pwd = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = 'uploadfolder/'  # modify to your folder
HOST = ""
PORT = 8282

''' export FLASK_APP=uploader.py;python -m flask run -h 0.0.0.0 -p 8282 
'''


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


@app.route('/', methods=['GET', 'POST'])
def default():
    return redirect(url_for('uploader'))


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        html = Template("""
            <!DOCTYPE html>
            <html>
               <body>
                 <div><a href="http://$HOST:$PORT/uploader" target="_self">http://$HOST:$PORT/uploader</a>
                 </div>

                 <div> </div>
                  <form action = "http://$HOST:$PORT/uploader" method = "POST"
                     enctype = "multipart/form-data">
                     <input type = "file" name = "file" />
                     <input type = "submit"/>
                  </form>
               </body>
            </html>
            """)
        HOST = extract_ip()
        html = html.substitute({"HOST": HOST, "PORT": PORT})
        print(HOST)
        return html
