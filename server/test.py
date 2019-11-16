import data_access_layer
import recommendations

ratings = data_access_layer.get_ratings()
distance = recommendations.euclidean("7", "5", ratings)

print(distance)
