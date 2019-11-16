def euclidean(user_id_a, user_id_b, ratings):
    ratings_a = list(filter(lambda r: r["UserId"] == user_id_a, ratings))
    ratings_b = list(filter(lambda r: r["UserId"] == user_id_b, ratings))

    similarity = 0
    matching_products = 0

    for r_a in ratings_a:
        for r_b in ratings_b:
            if (r_a["MovieId"] == r_b["MovieId"]):
                matching_products += 1
                similarity += (r_a["Rating"] - r_b["Rating"])**2

    if (matching_products == 0):
        return 0

    inverted_score = 1 / (1 + similarity)
    return inverted_score


def movies_euclidean(user_id, all_data):
    # get movies OP hasn't seen
    for r in all_data["ratings"]:
        pass
        # get movies OP hasn't seen that this person has


def get_unseen_movies(user_id):
    # todo: go through ratings, filter all not rated
    # next step, filter duplicates
    # map return list with just movie IDs
    pass
