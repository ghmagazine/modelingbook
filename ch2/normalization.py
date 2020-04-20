def normalization(x_values):
    # x_values はある特徴量の値が格納されたリスト
    # 最小値/最大値を取得する
    x_min = min(x_values)
    x_max = max(x_values)
    normalized_x_values = [ ]

    for x in x_values:
        normalized_x = (x - x_min) / (x_max - x_min)
        normalized_x_values.append(normalized_x)

    return normalized_x_values