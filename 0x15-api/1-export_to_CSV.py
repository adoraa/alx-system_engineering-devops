#!/usr/bin/python3
'''
Gather employee data from API and export to CSV
'''

import csv
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

            csv_filename = f"{user_id}.csv"

            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                for task in todos_response:
                    writer.writerow([user_id, emp_name, task.get('completed'),
                                    task.get('title')])

            print(f"Data exported to {csv_filename}")
        except ValueError:
            print("Employee ID must be an integer.")
    else:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
