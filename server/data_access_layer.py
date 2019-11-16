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

# squared = list(map(lambda x: x**2, items))


def get_ratings():
    ratings = get_data(
        get_cwd() + "/movies_example/ratings.csv",
        ["UserId", "MovieId", "Rating"]
    )

    for r in ratings:
        r["Rating"] = float(r["Rating"])

    return ratings


def get_data(filename, columns):
    with open(filename, mode="r") as csv_file:
        csv_rows = csv.DictReader(csv_file, delimiter=';')
        data_set = []

        for row in csv_rows:
            data = dict()

            for col in columns:
                data[col] = row[col]

            data_set.append(data)

        return data_set


def get_cwd():
    return os.getcwd()
