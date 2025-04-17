import json
import random
import csv
import os
import re


def property_generator():
    filename = "../data/property.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "price", "size_sq", "year", "property_type"]

    with open(filename, mode="w", newline="") as property_info_file:

        writer = csv.writer(property_info_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                price = random.randint(100, 500) * 1000

                if price < 200_000:
                    size_sq = random.randint(1200, 1800)
                elif price < 300_000:
                    size_sq = random.randint(1800, 2400)
                elif price < 400_000:
                    size_sq = random.randint(2400, 3200)
                else:
                    size_sq = random.randint(3200, 4000)


                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                postcode = line["properties"]['postcode']
                postcode = re.sub(r"\s+", " ", postcode).strip()
                property_type = random.choice(['single house', 'apartment', 'condo', 'farm house', 'cabin'])
                year = random.randint(1900, 2025)

                data = [number, street, city, postcode, price, size_sq, year, property_type]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue
        address_file.close()
    property_info_file.close()


if __name__ == "__main__":
    property_generator()
