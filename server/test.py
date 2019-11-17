import data_access_layer
import recommendations

ratings = data_access_layer.get_ratings()
distance = recommendations.get_euclidean("7", "4", ratings)

# print(data_access_layer.get_all_data())

diff_ratings = recommendations.get_diff_ratings("7", "6", ratings)
print(diff_ratings)
