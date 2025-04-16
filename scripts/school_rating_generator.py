import json
import random
import csv
import os
import re

def school_rating_info_generator():
    filename = "../data/school_rating_data.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "postcode", "high_school", "middle_school", "elementary_school"]

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
                postcode = line["properties"]['postcode']
                postcode = re.sub(r"\s+", " ", postcode).strip()

                high_school = random.randint(1, 10)
                middle_school = random.randint(1, 10)
                elementary_school = random.randint(1, 10)

                school_rating_info = [number, street, city, postcode, high_school, middle_school, elementary_school]

                writer.writerow(school_rating_info)
        address_file.close()
    school_rating_info_file.close()


if __name__ == "__main__":
   school_rating_info_generator()