import os
import csv


def get_cwd():
    return os.getcwd()


def get_users():
    # delimiter is ;
    # app/http/api/data_access_layer.py

    with open(get_cwd() + "/movies_large/users.csv", mode="r") as csv_file:
        csv_rows = csv.DictReader(csv_file, delimiter=';')
        users = []

        for row in csv_rows:
            user = dict()
            user["UserId"] = row["UserId"]
            user["Name"] = row["Name"]
            users.append(user)

        return users


print(get_users())
