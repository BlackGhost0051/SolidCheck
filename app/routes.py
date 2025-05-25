from flask import render_template, current_app, jsonify, request, render_template_string

from app.Managers.AiManager import AiManager
import markdown


@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/solid', methods=['POST'])
def solid():
    code_content = None

    if 'codefile' in request.files:
        uploaded_file = request.files.get('codefile')
        if uploaded_file:
            code_content = uploaded_file.read().decode('utf-8')
    elif 'code' in request.form:
        code_content = request.form['code']

    if not code_content:
        return "<p>No code provided.</p>"

    markdown_result = AiManager.verify_solid(code_content)
    html_result = markdown.markdown(markdown_result, extensions=['fenced_code', 'codehilite'])
    return render_template_string('<div class="markdown-body">{{ result|safe }}</div>', result=html_result)

