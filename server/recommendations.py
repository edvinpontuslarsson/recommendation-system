def movies_euclidean(user_id, all_data):
    users = all_data["users"]
    ratings = all_data["ratings"]

    movies = list()
    unseen_movie_ids = get_unseen_movie_ids(user_id, ratings)

    for m_id in unseen_movie_ids:
        m = dict()
        m["id"] = m_id
        m["title"] = get_movie_title(m_id, all_data["movies"])
        m["Σ_weighted_score"] = 0
        m["Σ_similarity"] = 0
        movies.append(m)

    for u in users:
        e_similarity = get_euclidean(user_id, u["UserId"], ratings)
        for m in movies:
            if has_rated(u["UserId"], m["id"], ratings):
                r = get_rating(u["UserId"], m["id"], ratings)
                m["Σ_weighted_score"] += (r * e_similarity)
                m["Σ_similarity"] += e_similarity

    for m in movies:
        m["total_score"] = m["Σ_weighted_score"] / m["Σ_similarity"]

    return movies


def get_movie_title(m_id, movies):
    for m in movies:
        if m["MovieId"] == m_id:
            return m["Title"]


def get_rating(user_id, m_id, ratings):
    for r in ratings:
        if r["UserId"] == user_id and r["MovieId"] == m_id:
            return r["Rating"]


def has_rated(user_id, movie_id, ratings):
    return any(r["UserId"] == user_id
               and r["MovieId"] == movie_id
               for r in ratings)


def get_unseen_movie_ids(user_id, ratings):
    seen = set(item["MovieId"]
               for item in ratings if item["UserId"] == user_id)
    unseen = set(item["MovieId"]
                 for item in ratings if not item["MovieId"] in seen)
    return unseen


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
