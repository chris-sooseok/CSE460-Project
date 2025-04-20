import json
import random
import csv
import os
import re

def gender_population_generator():
    filename = "../data/gender_population.csv"

    file_exist = os.path.exists(filename)

    header = ["zip_code", "gender", "age_scope", "population"]

    zip_set = set()

    with open(filename, mode="w", newline="") as gender_file:

        writer = csv.writer(gender_file)

        if not file_exist:
            writer.writerow(header)

        genders = ["male", "female"]
        age_scopes = ["[1,10]", "[11,20]", "[21,30]", "[31,40]","[41,50]",
                      "[51,60]", "[61,70]", "[71,80]", "[81,90]", "[91,100]"]

        with open("../data/address.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                postcode = line[3]

                if postcode not in zip_set:
                    zip_set.add(postcode)
                    for gender in genders:
                        for age_scope in age_scopes:
                            population = random.randint(100, 20000)
                            data = [postcode, gender, age_scope, population]
                            writer.writerow(data)
                
        address_file.close()
    gender_file.close()





if __name__ == "__main__":
   gender_population_generator()