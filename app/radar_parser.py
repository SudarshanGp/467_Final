import csv
import pandas as pd
from pprint import pprint


def make_json(data):

    # Cost, Calories, Fat, Cholestrol, Sodium, Protein, Iron, Carbohydrates


def dict_creator(people_dict, name, timestamp):
    for meal_type in people_dict[name][timestamp]:
        meals = people_dict[name][timestamp][meal_type]
        meal_list = list(meals.split(','))
        meals_list = []
        for food in meal_list:
            meal_dict = {}
            meal_dict["name"] = food
            meals_list.append(meal_dict)
        people_dict[name][timestamp][meal_type] = meals_list

def insert_food_info(people_dict, name, timestamp, food_info):
    for meal_type in people_dict[name][timestamp]:
        meals = people_dict[name][timestamp][meal_type]
        for meal in meals:
            if meal["name"] != 'None':
                val = meal["name"]
                if val.startswith(" "):
                    val = meal["name"][1:]
                if val.endswith(" "):
                    val = val[:-1]
                meal["value"] = food_info[val]



def parse_file(file_path):
    food_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_up.csv").fillna("None")
    food_data = food_data.T
    Aadhya_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_aadhya.csv").fillna("None").T.to_dict()
    Susan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_susan.csv").fillna("None").T.to_dict()
    Nihal_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_nihal.csv").fillna("None").T.to_dict()
    Sudarshan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_sudarshan.csv").fillna("None").T.to_dict()
    Kanishk_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_kanishk.csv").fillna("None").T.to_dict()

    # pprint(Aadhya_data.keys())
    food_data = food_data.T
    food_data = food_data.drop(food_data.columns[[19,20,21,22,23,24,25]], axis=1)
    food_dict = food_data.to_dict()

    food_info = {}
    for food_item in food_dict['Fat (g)'].keys():
        food_info[food_item] = {}

    for param in food_dict.keys():
        # print param
        for food_item in food_dict[param].keys():
            if param != "Restaurant" and param != "Cost":
                food_info[food_item][param] = float(food_dict[param][food_item])
            elif param == "Cost":
                food_info[food_item][param] = float(food_dict[param][food_item])
            else:
                food_info[food_item][param] = food_dict[param][food_item]

    people_data = {
        "Aadhya":Aadhya_data,
        "Kanishk":Kanishk_data,
        "Nihal":Nihal_data,
        "Sudarshan":Sudarshan_data,
        "Susan":Susan_data
    }
    people_dict = {
        "Aadhya":{},
        "Kanishk":{},
        "Nihal":{},
        "Sudarshan":{},
        "Susan":{}
    }

    for person, person_data in people_data.iteritems():
        for timestamp in person_data:
            people_dict[person][timestamp] = person_data[timestamp]
            dict_creator(people_dict, person, timestamp)
            insert_food_info(people_dict, person, timestamp, food_info)



    pprint(people_dict)
if __name__ == "__main__":
    parse_file("")