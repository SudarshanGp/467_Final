import csv
import pandas as pd
from pprint import pprint
def parse_file(file_path):
    food_data = pd.DataFrame.from_csv("static/res/curr_dataset_food.csv").fillna("None")
    food_data = food_data.T
    Aadhya_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_aadhya.csv").fillna("None").T.to_dict()
    Susan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_susan.csv").fillna("None").T.to_dict()
    Nihal_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_nihal.csv").fillna("None").T.to_dict()
    Sudarshan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_sudarshan.csv").fillna("None").T.to_dict()
    # Kanishk_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_kanishk.csv").fillna("None").to_dict()

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
                food_info[food_item][param] = float(food_dict[param][food_item][1:])
            else:
                food_info[food_item][param] = food_dict[param][food_item]

    people_dict = {
        "Aadhya":{},
        "Kanishk":{},
        "Nihal":{},
        "Sudarshan":{},
        "Susan":{}
    }

    for timestamp in Aadhya_data:

        people_dict["Aadhya"][timestamp] = Aadhya_data[timestamp]

    for timestamp in Nihal_data:
        people_dict["Nihal"][timestamp] = Nihal_data[timestamp]

    for timestamp in Susan_data:
        people_dict["Susan"][timestamp] = Susan_data[timestamp]

    for timestamp in Sudarshan_data:
        people_dict["Sudarshan"][timestamp] = Sudarshan_data[timestamp]

    # for timestamp in Kanishk_data:
    #     people_dict["Kanishk"][timestamp] = Aadhya_data[timestamp]

    pprint(people_dict)
if __name__ == "__main__":
    parse_file("")