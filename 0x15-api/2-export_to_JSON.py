#!/usr/bin/python3
'''
Gather employee data from API and export to JSON
'''

import json
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

            emp_name = user_response.get('username')
            user_id = user_response.get('id')

            tasks = [{"task": task.get('title'), "completed": task
                      .get('completed'), "username": emp_name} for task in
                     todos_response]

            json_data = {str(user_id): tasks}
            json_filename = f"{user_id}.json"

            with open(json_filename, 'w') as json_file:
                json.dump(json_data, json_file)

            print(f"Data exported to {json_filename}")
        except ValueError:
            print("Employee ID must be an integer.")
    else:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
