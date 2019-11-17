import data_access_layer
import recommendations

ratings = data_access_layer.get_ratings()
distance = recommendations.euclidean("7", "4", ratings)

# print(data_access_layer.get_all_data())

recommendations.unseen_movie_ids(
    "7", data_access_layer.get_all_data()["ratings"])
