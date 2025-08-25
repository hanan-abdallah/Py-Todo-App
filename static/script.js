async function fetchTasks() {
    const res = await fetch('/tasks');
    const tasks = await res.json();
    const list = document.getElementById('taskList');
    list.innerHTML = '';
    tasks.forEach((task, i) => {
        const item = document.createElement('li');
        item.textContent = task;
        item.onclick = () => deleteTask(i);
        list.appendChild(item);
    });
}

async function addTask() {
    const input = document.getElementById('taskInput');
    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: task })
    });
    input.value = '';
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
}

fetchTasks();
