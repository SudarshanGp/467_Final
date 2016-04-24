import sys

sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
import pandas as pd
import numpy as np
import pprint as pprint
import itertools
import json


def parse_data(data):
	data_dict = {}
	for idx, row in data.iterrows():
		data_dict[row['Date']] = {}
		breakfast = row['Breakfast']
		breakfast_list = []
		if isinstance(breakfast, basestring) is True:
			breakfast_list = breakfast.split(',')
			if len(breakfast_list) > 0:
				for key, value in enumerate(breakfast_list):
					if 'Breakfast' in data_dict[row['Date']].keys():
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Breakfast'].append(temp_dict)
					else:
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Breakfast'] = [temp_dict]
		else:
			data_dict[row['Date']]['Breakfast'] = []

		lunch = row['Lunch']
		lunch_list = []
		if isinstance(lunch, basestring) is True:
			lunch_list = lunch.split(',')
			if len(lunch_list) > 0:
				for key, value in enumerate(lunch_list):
					if 'Lunch' in data_dict[row['Date']].keys():
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Lunch'].append(temp_dict)
					else:
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]

						data_dict[row['Date']]['Lunch'] = [temp_dict]
		else:
			data_dict[row['Date']]['Lunch'] = []

		dinner = row['Dinner']
		dinner_list = []
		if isinstance(dinner, basestring) is True:
			dinner_list = dinner.split(',')
			if len(dinner_list) > 0:
				for key, value in enumerate(dinner_list):
					if 'Dinner' in data_dict[row['Date']].keys():
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Dinner'].append(temp_dict)
					else:
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Dinner'] = [temp_dict]
		else:
			data_dict[row['Date']]['Dinner'] = []

		snacks = row['Snacks']
		snacks_list = []
		if isinstance(snacks, basestring) is True:
			snacks_list = snacks.split(',')
			if len(snacks_list) > 0:
				for key, value in enumerate(snacks_list):
					if 'Snacks' in data_dict[row['Date']].keys():
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Snacks'].append(temp_dict)
					else:
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Snacks'] = [temp_dict]
		else:
			data_dict[row['Date']]['Snacks'] = []
		drinks = row['Drinks']
		drinks_list = []
		if isinstance(drinks, basestring) is True:
			drinks_list = drinks.split(',')
			if len(drinks_list) > 0:
				for key, value in enumerate(drinks_list):
					if 'Drinks' in data_dict[row['Date']].keys():
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Drinks'].append(temp_dict)
					else:
						temp_dict = data_food.loc[data_food['Food'] == value.strip()].T.to_dict()
						temp_dict = temp_dict[temp_dict.keys()[0]]
						data_dict[row['Date']]['Drinks'] = [temp_dict]
		else:
			data_dict[row['Date']]['Drinks'] = []
	return data_dict

def newDict (data):
	newDict = {}
	for key, val in enumerate(data):
		if val == 'Food' or val == 'Sugars (g)' or val == 'Carbohydrates (g)' or \
		val == 'Protein (g)' or val == 'Calories' \
		or val == 'Fat (g)' or val == 'Cholesterol (mg)' or val == 'Sodium (mg)' \
		or val == 'Calcium (%)' or val == 'Iron(%)' or val == 'Restaurant':
			newDict[val] = data[val]
		if val == 'Cost':
			if data[val] >= 0 and data[val] < 4:
				newDict[val] = data[val]
				newDict['Range'] = 'Low'
			elif data[val] >= 4 and data[val] < 8:
				newDict[val] = data[val]
				newDict['Range'] = 'Medium'
			else:
				newDict[val] = data[val]
				newDict['Range'] = 'High'
	return newDict


def add_to_list(data, name):
	global id_counter
	global json_data
	for key, value in data.iteritems():
		# Each value is a day
		# temp_dict = {'Person':name, value}
		breakfast = value['Breakfast']
		for key, val in enumerate(breakfast):
			val = newDict(val)
			val['Person'] = name
			# val['id'] = id_counter
			json_data.append(val)
			id_counter = id_counter + 1
		lunch = value['Lunch']
		for key, val in enumerate(lunch):
			val = newDict(val)
			val['Person'] = name
			# val['id'] = id_counter
			json_data.append(val)
			id_counter = id_counter + 1
		dinner = value['Dinner']
		for key, val in enumerate(dinner):
			val = newDict(val)
			val['Person'] = name
			# val['id'] = id_counter
			json_data.append(val)
			id_counter = id_counter + 1
		snacks = value['Snacks']
		for key, val in enumerate(snacks):
			val = newDict(val)
			val['Person'] = name
			# val['id'] = id_counter
			json_data.append(val)
			id_counter = id_counter + 1
		drinks = value['Drinks']
		for key, val in enumerate(drinks):
			val = newDict(val)
			val['Person'] = name
			# val['id'] = id_counter
			json_data.append(val)
			id_counter = id_counter + 1


data_food = pd.read_csv('static/res/curr_dataset_food_up.csv')
for col in data_food.columns:
	if 'Unnamed' in col:
		del data_food[col]
data_sudarshan = pd.read_csv('static/res/curr_dataset_food_sudarshan.csv')
for col in data_sudarshan.columns:
	if 'Unnamed' in col:
		del data_sudarshan[col]
data_sudarshan = parse_data(data_sudarshan)

data_nihal = pd.read_csv('static/res/curr_dataset_food_nihal.csv')
for col in data_nihal.columns:
	if 'Unnamed' in col:
		del data_nihal[col]
data_nihal = parse_data(data_nihal)

data_susan = pd.read_csv('static/res/curr_dataset_food_susan.csv')
for col in data_susan.columns:
	if 'Unnamed' in col:
		del data_susan[col]
data_susan = parse_data(data_susan)

data_aadhya = pd.read_csv('static/res/curr_dataset_food_aadhya.csv')
for col in data_aadhya.columns:
	if 'Unnamed' in col:
		del data_aadhya[col]
data_aadhya = parse_data(data_aadhya)

data_kanishk = pd.read_csv('static/res/curr_dataset_food_kanishk.csv')
for col in data_kanishk.columns:
	if 'Unnamed' in col:
		del data_kanishk[col]
data_kanishk = parse_data(data_kanishk)

id_counter = 1000
json_data = []
add_to_list(data_susan, "Susan Jacob")
add_to_list(data_sudarshan, "Sudarshan Govindaprasad")
add_to_list(data_nihal, "Nihal Shah")
add_to_list(data_kanishk, "Kanishk Thareja")
add_to_list(data_aadhya, "Aadhya Gupta")

with open('static/res/line_data.json', 'w') as outfile:
	json.dump(json_data, outfile, indent=4)
