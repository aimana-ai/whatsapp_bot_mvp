import gspread
import json


import pandas as pd
def collect_and_save_data():
    gs = gspread.service_account(filename="Sheets_Conn/credentials.json")
    sh = gs.open("Zapier_Data")
    wks = sh.worksheet("Página1")
    data = wks.get_all_records()
    print(data)
    with open('Data/data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to data.json")

# Write a function to insert data into a specific cell in a specific column
def insert_data_into_first_empty_row(data):
    gs = gspread.service_account(filename="Sheets_Conn/credentials.json")
    sh = gs.open("Zapier_Data")
    wks = sh.worksheet("Página2")
    wks.append_row(data)
    return "Data inserted successfully"


