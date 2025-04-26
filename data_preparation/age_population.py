import json
import random
import csv
import os

"""
1. Read address data from address.csv
2. For each zip_code, create random population data for each age scope
age_scope = "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99"

3. Store them into age_population.csv file

Notes:
total_population = random.randint(50000, 150000)
zip_code is PK
"""

age_brackets = {
    "0-9": 0.12,
    "10-19": 0.12,
    "20-29": 0.14,
    "30-39": 0.14,
    "40-49": 0.13,
    "50-59": 0.12,
    "60-69": 0.10,
    "70-79": 0.08,
    "80-89": 0.04,
    "90-99": 0.009
}

def population_generator():
    filename = "../data/age_population.csv"

    file_exist = os.path.exists(filename)

    header = ["zip_code", "total_population", "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99"]

    zip_set = set()

    with open(filename, mode="w", newline="") as gender_file:

        writer = csv.writer(gender_file)

        if not file_exist:
            writer.writerow(header)

        with open("../data/address.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                postcode = line[3]

                # preventing duplicate zip code data
                if postcode not in zip_set:
                    zip_set.add(postcode)

                    total_population = random.randint(50000, 150000)

                    distribution = {group: int(total_population * pct) for group, pct in age_brackets.items()}

                    total_assigned = sum(distribution.values())
                    remainder = total_population - total_assigned
                    distribution["20-29"] += remainder

                    data = [postcode, total_population]

                    for age in age_brackets:
                        data.append(distribution[age])

                    writer.writerow(data)

        address_file.close()
    gender_file.close()


if __name__ == "__main__":
    population_generator()