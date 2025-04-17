import json
import random
import csv
import os

def income_generator():
    filename = "../data/income.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zipcode", "household_income"]

    with open(filename, mode="w", newline="") as income_data_file:

        writer = csv.writer(income_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                zipcode = line["properties"]['number']
                household_income = random.randint(30000, 150000)
                
                data = [number,street,city,zipcode,household_income]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue

        address_file.close()
    income_data_file.close()


if __name__ == "__main__":
   income_generator()