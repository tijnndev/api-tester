from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

app.config['STATIC_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/test', methods=['POST'])
def api_test():

    if not request.json:
        return jsonify({
            'status': 404,
            'response': "Not found"
        })
    
    url = request.json.get('url')
    method = request.json.get('method', 'GET')
    headers = request.json.get('headers', {})
    params = request.json.get('params', {})
    auth_token = request.json.get('auth_token', '')

    if auth_token:
        headers['Authorization'] = f'Bearer {auth_token}'

    try:
        response = requests.request(method, url, headers=headers, json=params)
        return jsonify({
            'status': response.status_code,
            'response': response.json() if response.content else response.text
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
