// Fetch and display tasks
async function fetchTasks() {
  try {
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
  } catch (err) {
    console.error('Failed to fetch tasks:', err);
  }
}

// Add a new task
async function addTask() {
  const input = document.getElementById('taskInput');
  const task = input.value.trim();

  if (!task) return; // Prevent empty tasks

  try {
    await fetch('/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task })
    });
    input.value = '';
    fetchTasks();
  } catch (err) {
    console.error('Failed to add task:', err);
  }
}

// Delete a task by ID
async function deleteTask(id) {
  try {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
  } catch (err) {
    console.error('Failed to delete task:', err);
  }
}

// Allow Enter key to add task
document.getElementById('taskInput').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') addTask();
});

// Initial load
fetchTasks();
