def cosine_similarity(u_i, u_j):
    num = 0.0
    denom_i = 0.0
    denom_j = 0.0

    for m in ITEMS:
        num += c[u_i][m] * c[u_j][m]
        denom_i += c[u_i][m] ** 2
        denom_j += c[u_j][m] ** 2

    denom = denom_i ** 0.5 + denom_j ** 0.5
    num = num ** 0.5
    return num / denom
