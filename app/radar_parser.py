import csv
import pandas as pd

def parse_file(file_path):
    food_data = pd.DataFrame.from_csv("static/res/curr_dataset_food.csv")
    food_data = food_data.T
    aadhya_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_aadhya.csv")
    susan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_susan.csv")
    # kanishk_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_kanishk.csv")
    nihal_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_nihal.csv")
    sudarshan_data = pd.DataFrame.from_csv("static/res/curr_dataset_food_sudarshan.csv")
    print food_data['Penne Rosa']
