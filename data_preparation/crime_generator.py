import json
import random
import csv
import os

def crime_generator():
    filename = "../data/crime.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "score"]

    with open(filename, mode="w", newline="") as crime_data_file:

        writer = csv.writer(crime_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                zipcode = line["properties"]['number']
                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                score = round(random.uniform(0, 1), 2)

                data = [number, street, city, zip_code, score]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue

        address_file.close()
    crime_data_file.close()


if __name__ == "__main__":
   crime_generator()