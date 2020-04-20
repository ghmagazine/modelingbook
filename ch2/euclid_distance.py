def euclid_distance(u_i, u_j):
    d = 0
    for m in ITEMS:
        d += (c[u_i][m] - c[u_j][m]) ** 2

    return d ** 0.5

# ユークリッド距離に基づく類似度
def euclid_similarity(u_i, u_j):
    return 1.0 / (1.0 + euclid_distance(u_i, u_j))