import json
import random
import csv
import os
import re

def school_rating_generator():
    filename = "../data/school_rating.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "high_school", "middle_school", "elementary_school"]

    with open(filename, mode="w", newline="") as school_rating_info_file:

        writer = csv.writer(school_rating_info_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                zip_code = line["properties"]['postcode']
                zip_code = re.sub(r"\s+", " ", zip_code).strip()

                high_school = random.randint(1, 10)
                middle_school = random.randint(1, 10)
                elementary_school = random.randint(1, 10)

                data = [number, street, city, zip_code, high_school, middle_school, elementary_school]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue
        address_file.close()
    school_rating_info_file.close()


if __name__ == "__main__":
   school_rating_generator()