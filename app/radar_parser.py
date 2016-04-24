import csv
import pandas as pd
from pprint import pprint
def parse_file(file_path):
    food_data = pd.DataFrame.from_csv("static/res/curr_dataset_food.csv").fillna("None")
    food_data = food_data.T
    aadhya_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_aadhya.csv").fillna("None")
    susan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_susan.csv").fillna("None")

    # kanishk_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_kanishk.csv")
    nihal_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_nihal.csv").fillna("None")
    sudarshan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_sudarshan.csv").fillna("None")
    food_data = food_data.T
    food_data = food_data.drop(food_data.columns[[19,20,21,22,23,24,25]], axis=1)
    food_dict = food_data.to_dict()
    print aadhya_data


if __name__ == "__main__":
    parse_file("")