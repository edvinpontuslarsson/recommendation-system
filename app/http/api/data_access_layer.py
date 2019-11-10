import os
import csv


def get_cwd():
    return os.getcwd()


def get_users():
    return get_data(
        get_cwd() + "/movies_large/users.csv",
        ["UserId", "Name"]
    )


def get_data(filename, columns):
    with open(filename, mode="r") as csv_file:
        csv_rows = csv.DictReader(csv_file, delimiter=';')
        data_sets = []

        for row in csv_rows:
            data = dict()

            for c in columns:
                data[c] = row[c]

            data_sets.append(data)

        return data_sets


print(get_users())
