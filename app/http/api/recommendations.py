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
'''


def euclidean(a, b):
    similarity = 0
    matching_products = 0
