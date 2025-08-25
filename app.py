from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    response = jsonify(tasks)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if not task:
        error_response = jsonify({"error": "Task content is required."})
        error_response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return error_response, 400

    tasks.append(task)
    success_response = jsonify({"message": "Task added!"})
    success_response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return success_response, 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        removed = tasks.pop(task_id)
        response = jsonify({"message": f"Removed: {removed}"})
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except IndexError:
        error_response = jsonify({"error": "Invalid task ID."})
        error_response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return error_response, 404

if __name__ == '__main__':
    app.run(debug=True)
