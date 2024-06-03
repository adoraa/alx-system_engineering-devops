#!/usr/bin/python3
'''
gather employee data from API
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
            user_url = f"{REST_API}/users/{id}"
            todos_url = f"{REST_API}/todos?userId={id}"

            user_response = requests.get(user_url).json()
            todos_response = requests.get(todos_url).json()

            emp_name = user_response.get('name')
            total_tasks = len(todos_response)
            completed_tasks = [task for task in todos_response if task.get('completed')]

            print(f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
            for task in completed_tasks:
                print(f'\t {task.get("title")}')
        except ValueError:
            print("Employee ID must be an integer.")
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
