import data_access_layer
import recommendations


print(recommendations.movies_euclidean("3", data_access_layer.get_all_data()))
