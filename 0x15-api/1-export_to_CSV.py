#!/usr/bin/python3

"""CSV"""

import csv
import requests
import sys

if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()
    _name = users.get('username')
    _id = users.get('id')

    with open('{}.csv'.format(sys.argv[1]), mode='w') as id_csv:
        j = csv.writer(id_csv, quoting=csv.QUOTE_ALL)

        for i in todos:
            j.writerow([_id, _name, i.get('completed'), i.get('title')])
