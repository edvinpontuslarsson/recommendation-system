def movies_euclidean(user_id, all_data):
    ratings = all_data["ratings"]

    for r in ratings:
        e_diff = get_euclidean(user_id, r["UserId"], ratings)
        diff_ratings = get_diff_ratings(user_id, r["UserId"], ratings)
        # get movies OP hasn't seen that this person has


def get_diff_ratings(user_id_a, user_id_b, ratings):
    '''
    Ratings of user_id_b not rated by user_id_a
    '''
    seen_by_a = get_ratings(user_id_a, ratings)
    seen_by_b = get_ratings(user_id_b, ratings)

    diff_ids = set(item["MovieId"]
                   for item in ratings if not item["MovieId"] in seen_by_a
                   and item["MovieId"] in seen_by_b)

    return list(filter(lambda r: r["UserId"] == user_id_b
                       and r["MovieId"] in diff_ids, ratings))


def get_ratings(user_id, ratings):
    return set(item["MovieId"]
               for item in ratings if item["UserId"] == user_id)


def get_euclidean(user_id_a, user_id_b, ratings):
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
