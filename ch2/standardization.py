# 平均を求める関数
def average(values):
    return sum(values) / len(values)

# 標準偏差を求める関数
def standard_deviation(values):
    avg = average(values)
    return (sum((v - avg) ** 2 for v in values) / len(values)) ** 0.5

def standardization(x_values):
    # x_values はある特徴量の値が格納されたリスト
    standardized_x_values = [ ]
    avg_x = average(x_values)
    sd_x = standard_deviation(x_values)

    for x in x_values:
        standardized_x = (x - avg_x) / sd_x
        standardized_x_values.append(standardized_x)

    return standardized_x_values