import json
import random
import csv
import os

"""
1. Read full address from address.csv
2. For each house address, generate random household income in range of (30000, 500000)

Notes: 
Generate more of low income than high income

"""

def household_income_generator():
    filename = "../data/household_income.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "income"]

    with open(filename, mode="w", newline="") as income_data_file:

        writer = csv.writer(income_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/address.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                number = line[0]
                street = line[1]
                city = line[2]
                postcode = line[3]
                income = skewed_income()
                
                data = [number,street,city,postcode,income]

                writer.writerow(data)

        address_file.close()
    income_data_file.close()

def skewed_income(min_income=random.randint(25000, 35000), max_income=200000, skew=5.0):
    # Get a number between 0 and 1
    u = random.random()
    # Skew it: higher skew means more bias toward lower end
    income = min_income + (max_income - min_income) * (u ** skew)
    return int(income)


if __name__ == "__main__":
   household_income_generator()