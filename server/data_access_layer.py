import os
import csv


def get_users():
    return get_data(
        get_cwd() + "/movies_example/users.csv",
        ["UserId", "Name"]
    )


def get_movies():
    return get_data(
        get_cwd() + "/movies_example/movies.csv",
        ["MovieId", "Title", "Year"]
    )


def get_ratings():
    return get_data(
        get_cwd() + "/movies_example/ratings.csv",
        ["UserId", "MovieId", "Rating"]
    )


def get_data(filename, columns):
    with open(filename, mode="r") as csv_file:
        csv_rows = csv.DictReader(csv_file, delimiter=';')
        data_sets = []

        for row in csv_rows:
            data = dict()

            for col in columns:
                data[col] = row[col]

            data_sets.append(data)

        return data_sets


def get_cwd():
    return os.getcwd()
