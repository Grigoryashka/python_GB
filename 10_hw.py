import pandas as pd
import random
from matplotlib import pyplot as pl

h_to_r = {'human': 1, 'robot': 0}
r_to_h = {'human': 0, 'robot': 1}
lst = ['human'] * 10
lst += ['robot'] * 10
random.shuffle(lst)
print(lst)
data = pd.DataFrame(lst)
data['human'] = data[0]
data = data.drop(columns=[0], axis=1)
bool_data = data.replace(h_to_r)
verse_bool_data = data.replace(r_to_h)
verse_bool_data_lst = verse_bool_data['human'].tolist()
print(verse_bool_data_lst)

# data.head()
bool_data['robot'] = verse_bool_data_lst
print(bool_data)

# one_hot = pd.get_dummies(data, dtype=int)
# print(one_hot)
# pl.plot(one_hot["0_1"])
# pl.show()

