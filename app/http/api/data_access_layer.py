import csv


def get_users():
    # delimiter is ;
    # app/http/api/data_access_layer.py

    # Todo: if works, get workdir first
    with open("/home/edvin/UniCourses/web_intelligence/A1/recommendation-system/movies_large/users.csv", mode="r") as csv_file:
        users = csv.DictReader(csv_file)
        print(users)


get_users()
