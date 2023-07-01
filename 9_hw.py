# Task 40
import pandas as pd
from pprint import pprint


pd.set_option('display.max_columns', None)
df = pd.read_csv("california_housing_train.csv")
pop = df[df['population'] <= 500]
Sum = sum(pop['median_house_value'])
Count = len(pop['median_house_value'])

print("Средняя стоимость дома с населением меньше 500 человек:", round(Sum/Count, 3), "\n")


# Task 42
min_pop = min(pop['population'])
max_households = pop[pop['population'] == min(pop['population'])]['households']
print("maximum households with mininmum population(3) =", max_households.tolist()[0])
