from flask import render_template, current_app, jsonify, request, render_template_string

from app.Managers.AiManager import AiManager
import markdown


@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/solid', methods=['POST'])
def solid():
    uploaded_file = request.files.get('codefile')
    if not uploaded_file:
        return "<p>No file uploaded.</p>"

    code_content = uploaded_file.read().decode('utf-8')
    markdown_result = AiManager.verify_solid(code_content)
    html_result = markdown.markdown(markdown_result, extensions=['fenced_code', 'codehilite'])

    # Return HTML as plain string, not full page
    return render_template_string('<div class="markdown-body">{{ result|safe }}</div>', result=html_result)
