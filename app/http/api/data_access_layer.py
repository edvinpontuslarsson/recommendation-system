import os
import csv


def get_cwd():
    return os.getcwd()


def get_users(columns):
    with open(get_cwd() + "/movies_large/users.csv", mode="r") as csv_file:
        csv_rows = csv.DictReader(csv_file, delimiter=';')
        data_sets = []

        for row in csv_rows:
            data = dict()

            # TODO: re-use this logic for the other funcs
            # column[] as param,
            # for c in column
            #
            # data["UserId"] = row["UserId"]
            # data["Name"] = row["Name"]

            for c in columns:
                data[c] = row[c]

            data_sets.append(data)

        return data_sets


print(get_users(["UserId", "Name"]))
