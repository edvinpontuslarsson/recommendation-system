import os
import csv


def get_cwd():
    return os.getcwd()


def get_users():
    # delimiter is ;
    # app/http/api/data_access_layer.py

    # Todo: if works, get workdir first
    with open(get_cwd() + "/movies_large/users.csv", mode="r") as csv_file:
        users = csv.DictReader(csv_file)
        print(users)


get_users()
print(get_cwd())
