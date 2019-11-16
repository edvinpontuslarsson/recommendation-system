import data_access_layer
import recommendations

ratings = data_access_layer.get_ratings()
distance = recommendations.euclidean("7", "4", ratings)

print(distance)
print(data_access_layer.get_all_data())
