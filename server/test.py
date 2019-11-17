import data_access_layer
import recommendations

ratings = data_access_layer.get_ratings()
distance = recommendations.get_euclidean("7", "4", ratings)

# print(data_access_layer.get_all_data())

print(recommendations.has_rated("1", "1", ratings))
print(recommendations.has_rated("7", "1", ratings))
