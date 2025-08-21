from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({"message": "Task added!"}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        removed = tasks.pop(task_id)
        return jsonify({"message": f"Removed: {removed}"})
    except IndexError:
        return jsonify({"error": "Invalid task ID."}), 404

if __name__ == '__main__':
    app.run(debug=True)
