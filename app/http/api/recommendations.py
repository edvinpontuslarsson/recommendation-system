'''
float euclidean(User A, User B)
    //Init variables
    sim=0
    //Counter for number of matching products
    n = 0
    //Iterate over all rating combinations
    for (Rating rA : A.rating)
        for (Rating rB : B.rating)
            if (rA == rB)
                sim += (rA.score – rB.score)**2 //a*a
                n += 1
    //No ratings in common – return 0
    if (n == 0)
        return 0
    //Calculate inverted score
    inv = 1 / (1 + sim)
    return inv

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
'''


def euclidean(uid_a, uid_b, ratings):
    ratings_a = list(filter(lambda r: r["UserId"] == uid_a, ratings))
    ratings_b = list(filter(lambda r: r["UserId"] == uid_b, ratings))

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
