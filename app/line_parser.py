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
for col in data_susan.columns:
    if 'Unnamed' in col:
        del data_susan[col]

susan_dict = {}
for idx, row in data_susan.iterrows():
	print(idx)
	susan_dict[row['Date']] = {}
	print(row)
	breakfast = row['Breakfast']
	# Parse breakfast
	breakfast_list = []
	if isinstance(breakfast, basestring) is True:
		breakfast_list = breakfast.split(',')
	lunch = row['Lunch']
	lunch_list = []
	if isinstance(lunch, basestring) is True:
		lunch_list = lunch.split(',')
	dinner = row['Dinner']
	dinner_list = []
	if isinstance(dinner, basestring) is True:
		print(dinner)
		dinner_list = dinner.split(',')
	snacks = row['Snacks']
	snacks_list = []
	if isinstance(snacks, basestring) is True:
		snacks_list = snacks.split(',')
	drinks = row['Drinks']
	drinks_list = []
	if isinstance(drinks, basestring) is True:
		drinks_list = drinks.split(',')
	print(breakfast_list, lunch_list, dinner_list, snacks_list, drinks_list)