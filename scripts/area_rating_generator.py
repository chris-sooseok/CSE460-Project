import json
import random
import csv
import os
import re

def area_rating_info_generator():
    filename = "../data/area_rating_data.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "postcode", "transportation", "grocery", "park", "quiet", "restaurant"]

    with open(filename, mode="w", newline="") as area_rating_info_file:

        writer = csv.writer(area_rating_info_file)

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

                transportation = random.randint(1, 10)
                if transportation >= 7:
                    grocery = random.randint(7, 10)
                    quiet = random.randint(1, 3)
                elif transportation > 3 and transportation < 7:
                    grocery = random.randint(4, 6)
                    quiet = random.randint(4, 6)
                else:
                    grocery = random.randint(1, 3)
                    quiet = random.randint(7, 10)

                park = random.randint(1, 10)
                restaurant = random.randint(1, 10)

                area_rating_info = [number, street, city, postcode, transportation, grocery, park, quiet, restaurant]

                writer.writerow(area_rating_info)
        address_file.close()
    area_rating_info_file.close()


if __name__ == "__main__":
   area_rating_info_generator()