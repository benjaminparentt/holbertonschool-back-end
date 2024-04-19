import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee's name and task data from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch the user's name
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve data for user ID {employee_id}")
        return None
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch the todos for the user
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve todos for user ID {employee_id}")
        return None
    todos_data = todos_response.json()

    # Process todos data
    total_tasks = len(todos_data)
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]

    return employee_name, total_tasks, completed_tasks

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return
    
    employee_id = int(sys.argv[1])
    result = fetch_employee_data(employee_id)
    
    if result:
        employee_name, total_tasks, completed_tasks = result
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")

if __name__ == "__main__":
    main()
