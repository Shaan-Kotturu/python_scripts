import pandas as pd

data = [100,103,201]
series = pd.Series(data, index=['a', 'b', 'c'])
series.loc["c"] = 300
# print(series[series<150])
series.loc["b"] += 100
print(series)

calories = {"day1": 420, "day2": 380, "day3": 390}
calorie_series = pd.Series(calories)
# print(calorie_series)
