import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
import pandas as pd
import numpy as np
import pprint as pprint
data_food = pd.read_csv('static/res/curr_dataset_food.csv')
for col in data_food.columns:
    if 'Unnamed' in col:
        del data_food[col]
data_susan = pd.read_csv('static/res/curr_dataset_food_susan.csv')