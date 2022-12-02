#!/usr/bin/python3
"""
Script to gather data from an API
"""
import json
import requests
from sys import argv


response_API = 'https://jsonplaceholder.typicode.com/'

if __name__ == "__main__":
    res = requests.get("{}users".format(response_API)).json()
    tasks_dict = {}
    for user in res:
        name = user.get("username")
        user_id = user.get("id")
        tasks = requests.get("{}todos?userId={}".format(
            response_API, user_id)).json()
        tasks_list = []
        for task in tasks:
            t_d = {"username": name,
                   "task": task.get("title"),
                   "completed": task.get("completed")}
            tasks_list.append(t_d)

        tasks_dict[str(user_id)] = tasks_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)
