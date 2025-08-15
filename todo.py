from flask import flask
app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({"message": "Task added!"}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    try:
        removed = tasks.pop(task_id)
        return jsonify({"message": f"Removed: {removed}"})
    except IndexError:
        return jsonify({"error": "Invalid task ID."}), 404

if __name__ == '__main__':
    app.run(debug=True)

def view_tasks():
    if not tasks:
        return jsonify({"message": "No tasks yet."})
    else:
        return jsonify({"tasks": tasks})

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
