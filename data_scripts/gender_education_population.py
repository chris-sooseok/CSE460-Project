import json
import random
import csv
import os
import re

def gender_population_generator():
    filename = "../data/gender_population.csv"

    file_exist = os.path.exists(filename)

    header = ["number", "street", "city", "zip_code", "gender", "age_scope", "population"]


    with open(filename, mode="w", newline="") as gender_file:

        writer = csv.writer(gender_file)

        if not file_exist:
            writer.writerow(header)

        genders = ["male", "female"]
        age_scopes = ["[1,10]", "[11,20]", "[21,30]", "[31,40]","[41,50]",
                      "[51,60]", "[61,70]", "[71,80]", "[81,90]", "[91,100]"]

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                zip_code = line["properties"]['postcode']
                zip_code = re.sub(r"\s+", " ", zip_code).strip()

                if not any(item == "" for item in data):
                    writer.writerow(data)
                
                    for gender in genders:
                        for age_scope in age_scopes:
                            population = random.randint(100, 1000)
                            data = [zip_code, gender, age_scope, population]
                            writer.writerow(data)
                
        address_file.close()
    gender_file.close()


def education_generator():
    filename = "../data/income.csv"
    file_exists = os.path.exists(filename)
    header = ["zipcode", "household_income"]

    with open(filename, mode="w", newline="") as address_data_file:

        writer = csv.writer(address_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                zipcode = line["properties"]['number']
                household_income = random.randint(30000, 150000)
                
                data = [zipcode, household_income]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue

        address_file.close()
    address_data_file.close()

def education_population_generatr():
    education_header = ["number", "street", "city", "zip_code",
    "pop_less_than_high_school", "pop_high_school_graduate_or_higher", "pop_bachelor_degree_or_higher", "pop_gradueate_degree_or_higher"]

if __name__ == "__main__":
   gender_population_generator()