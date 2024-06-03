#!/usr/bin/python3
'''
Gather all employees' task data from API and export to JSON
'''

import json
import requests

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_data():
    users_url = f"{REST_API}/users"
    todos_url = f"{REST_API}/todos"

    users_response = requests.get(users_url).json()
    todos_response = requests.get(todos_url).json()

    return users_response, todos_response


def main():
    users, todos = fetch_data()

    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [
            {"username": username, "task": task.get('title'), "completed":
                task.get('completed')}
            for task in todos if task.get('userId') == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

    print("Data exported to todo_all_employees.json")


if __name__ == '__main__':
    main()
