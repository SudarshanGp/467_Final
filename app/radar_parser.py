from __future__ import division
import pandas as pd
from pprint import pprint
import csv
from collections import defaultdict
import json
CALORIES = "Calories"
CALCIUM = "Calcium (%)"
FAT = "Fat (g)"
CHOLESTEROL = "Cholesterol (mg)"
SODIUM = "Sodium (mg)"
CARBOHYDRATES = "Carbohydrates (g)"
PROTEIN = "Protein (g)"
IRON = "Iron(%)"
FOOD_SCORE = "Food Score"
COST = "Cost"
PARAMS = [CALORIES, CALCIUM, FAT, CHOLESTEROL, SODIUM, PROTEIN, IRON, FOOD_SCORE, COST]

def make_json(json_data,type):
    out_data = []
    cost_dict = {}
    for person in json_data:
        person_list = []
        person_dict = {
            "key":person,
            "values":[],
            "best_food":""
        }
        for param in PARAMS:
            inner_dict = {}

            if param != COST:
                if param != FOOD_SCORE:
                    inner_dict["device"] = person
                    inner_dict["value"] = json_data[person][type][param]
                    inner_dict["reason"] = param
                    inner_dict["best_food"] = json_data[person][type][FOOD_SCORE]
                    person_list.append(inner_dict)
                    person_dict["values"] = (person_list)
                else:
                    cost_dict[person] = json_data[person][type][COST]

        out_data.append(person_dict)

    with open('static/res/radar_data_'+type+'.json','w') as outfile:
        json.dump(out_data, outfile,  sort_keys=True,indent=4, separators=(',', ': '))

    writer = csv.writer(open('static/res/radar_data_'+type+'_cost.tsv','w'), delimiter= "\t")
    writer.writerow(["name", "cost"])
    for key, value in cost_dict.items():
        writer.writerow([key, value])

    # with open('static/res/radar_data_'+type+'_cost.json','w') as outfile:
    #     json.dump(cost_dict, outfile,  sort_keys=True,indent=4, separators=(',', ': '))


def init_food_score():
    food_score = {
        "total":{
            "name":"",
            "score":-30
        },
        "Breakfast":{
            "name":"",
            "score":-30
        },
        "Lunch":{
            "name":"",
            "score":-30
        },
        "Dinner":{
            "name":"",
            "score":-30
        },
        "Drinks":{
            "name":"",
            "score":-30
        },
        "Snacks":{
            "name":"",
            "score":-30
        },
    }
    return food_score
def make_json_data(people_data):

    # Cost, Calories, Fat, Cholestrol, Sodium, Protein, Iron, Carbohydrates

    avg_food_intake = {}
    meal_food_intake = {}
    total_data = defaultdict(float)

    for person, person_data in people_data.iteritems():
        avg_food_intake[person] = defaultdict(float)
        meal_food_intake[person] = {}
        meal_food_intake[person]["total"] = defaultdict(float)
        food_score = init_food_score()
        for timestamp in person_data:
            for meal_type in person_data[timestamp]:
                if meal_type not in meal_food_intake[person].keys():
                    meal_food_intake[person][meal_type] = defaultdict(float)
                for meal in person_data[timestamp][meal_type]:
                    if meal["name"] != 'None':
                        for nutrients in PARAMS:
                            if nutrients != FOOD_SCORE:
                                meal_food_intake[person]["total"][nutrients] += meal["value"][nutrients]
                                meal_food_intake[person][meal_type][nutrients] += meal["value"][nutrients]
                            else:
                                food_val = meal["value"][nutrients]
                                if food_val > food_score[meal_type]["score"]:
                                    food_score[meal_type]["score"] = food_val
                                    food_score[meal_type]["name"] = meal["name"]
                                    meal_food_intake[person][meal_type][nutrients] =  meal["name"] +", "+meal["value"]["Restaurant"] +": " +str(food_val)

                                if food_val > food_score["total"]["score"]:
                                    food_score["total"]["score"] = food_val
                                    food_score["total"]["name"] = meal["name"]
                                    meal_food_intake[person]["total"][nutrients] = meal["name"] +", "+meal["value"]["Restaurant"] +": " +str(food_val)


    for person, person_data in people_data.iteritems():
        NUM_DAYS = len(person_data.keys())
        for meal_type in meal_food_intake[person]:
            for nutrients in PARAMS:
                if nutrients != FOOD_SCORE and nutrients != COST:
                    meal_food_intake[person][meal_type][nutrients] = float(meal_food_intake[person][meal_type][nutrients])/float(NUM_DAYS)
                # if nutrients == COST:
                #     total_data[nutrients] += meal_food_intake[person][[nutrients]

    total_data[CALORIES] = 2000.00
    total_data[FAT] = 65.00
    total_data[CHOLESTEROL] = 300.00
    total_data[SODIUM] = 2400.00
    total_data[PROTEIN] = 80.00
    total_data[IRON] = 70.00
    total_data[CARBOHYDRATES] = 300
    total_data[CALCIUM] = 70
    for person, person_data in people_data.iteritems():
        for meal_type in meal_food_intake[person]:
            for nutrients in PARAMS:
                if nutrients != FOOD_SCORE and nutrients != COST:
                    meal_food_intake[person][meal_type][nutrients] /= total_data[nutrients]

    return meal_food_intake

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
    food_data = pd.DataFrame.from_csv("static/res/curr_dataset_food.csv").fillna("None")
    Aadhya_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_aadhya.csv").fillna("None").T.to_dict()
    Susan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_susan.csv").fillna("None").T.to_dict()
    Nihal_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_nihal.csv").fillna("None").T.to_dict()
    Sudarshan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_sudarshan.csv").fillna("None").T.to_dict()
    Kanishk_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_kanishk.csv").fillna("None").T.to_dict()
    food_dict = food_data.to_dict()

    food_info = {}
    for food_item in food_dict['Fat (g)'].keys():
        food_info[food_item] = {}

    for param in food_dict.keys():
        for food_item in food_dict[param].keys():
            if param != "Restaurant" and param != "Cost":
                food_info[food_item][param] = float(food_dict[param][food_item])
            elif param == "Cost":
                food_info[food_item][param] = float(food_dict[param][food_item][1:])
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


    json_data = make_json_data(people_dict)
    # pprint(json_data["Nihal"]["Breakfast"])
    MEAL_TYPE = ["total", "Snacks", "Dinner", "Lunch", "Breakfast", "Drinks"]
    for meal in MEAL_TYPE:
        make_json(json_data,type=meal)

    # pprint(people_dict)
if __name__ == "__main__":
    parse_file("")

