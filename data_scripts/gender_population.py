import json
import random
import csv
import os

"""
1. Read total population data from age_population.csv
2. For each zip_code, create random male and female distribution data based on total population
3. Store data into gender_population.csv file

"""

def gender_population_generator():
    filename = "../data/gender_population.csv"

    file_exist = os.path.exists(filename)

    header = ["zip_code", "total_population", "male", "female"]

    with open(filename, mode="w", newline="") as gender_file:

        writer = csv.writer(gender_file)

        if not file_exist:
            writer.writerow(header)

        with open("../data/age_population.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                postcode = line[0]
                total_population = int(line[1])
                male_ratio = random.uniform(0.40, 0.60)
                male = int(total_population * male_ratio)
                female = total_population - male

                data = [postcode, total_population, male, female]

                writer.writerow(data)
                
        address_file.close()
    gender_file.close()

if __name__ == "__main__":
   gender_population_generator()