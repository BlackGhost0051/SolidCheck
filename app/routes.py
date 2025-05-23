import os
from flask import render_template, current_app, jsonify, request, Response, make_response, url_for, redirect, \
    send_from_directory



@current_app.route('/')
def home():
    return render_template('index.html')
