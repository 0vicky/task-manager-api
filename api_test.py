import requests

# Base URL for the API
base_url = 'http://localhost:5000'

# Test the POST endpoint to create a new task
def create_task(title, description, due_date):
    url = f'{base_url}/tasks'
    data = {
        'title': title,
        'description': description,
        'due_date': due_date
    }
    response = requests.post(url, json=data)
    return response.json()

# Test the GET endpoint to retrieve a specific task
def get_task(task_id):
    url = f'{base_url}/tasks/{task_id}'
    response = requests.get(url)
    return response.json()

# Test the PUT endpoint to update a specific task
def update_task(task_id, title, description, due_date, status):
    url = f'{base_url}/tasks/{task_id}'
    data = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': status
    }
    response = requests.put(url, json=data)
    return response.json()

# Test the DELETE endpoint to delete a specific task
def delete_task(task_id):
    url = f'{base_url}/tasks/{task_id}'
    response = requests.delete(url)
    return response.status_code

# Test the GET endpoint to list all tasks
def list_tasks():
    url = f'{base_url}/tasks'
    response = requests.get(url)
    return response.json()


# Example usage

# Create a new task
created_task = create_task('Task 1', 'Description 1', '2023-06-09')
print(created_task)

# Get the details of a specific task
task_id = created_task['id']
task_details = get_task(task_id)
print(task_details)

# Update the details of a specific task
updated_task = update_task(task_id, 'Updated Task 1', 'Updated Description 1', '2023-06-10', 'Completed')
print(updated_task)

# Delete a specific task
delete_status = delete_task(task_id)
print(delete_status)

# List all tasks
tasks = list_tasks()
print(tasks)

