def item_based_collaborative_filtering(u_i, m):
    scores = [ ]
    # すでに購入したアイテムについて考える
    for n in Items_i:
        # アイテム間の類似度とその購買量の積をとる
        scores.append(sim(m, n) * c[u_i][n])

    # 最後に予測値の平均を計算する
    score = sum(scores) / len(scores)
    return score