def user_based_collaborative_filtering(u_i, m):
    scores = [ ]
    # u_i以外のすべてのユーザについて計算する
    for u_j in Users:
        if u_i != u_j:
            scores[u_j] = sim(u_i, u_j) * c[u_j][m]

    # 最後にすべての予測値の平均を計算する
    score = sum(scores) / len(scores)
    return score