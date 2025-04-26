import json
import random
import csv
import os

"""
1. Read number, street, city, postcode from erie-addresses-county.geojson
2. Only take postcode between 14001 and 14280 which are erie county
3. Store them into address.csv file
"""

def address_generator():
    filename = "../data/address.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "state"]

    with open(filename, mode="w", newline="") as address_data_file:

        writer = csv.writer(address_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/us_address_data/ny/erie-addresses-county.geojson") as address_file:
            for line in address_file:
                line = json.loads(line)

                number = line["properties"]['number']
                street = line["properties"]['street']
                city = line["properties"]['city']
                postcode = line["properties"]['postcode'].split(" ")[0].strip()

                try:
                    if 14001 <= int(postcode) and 14280 >= int(postcode):

                        data = [number, street, city, postcode, "NY"]

                        if not any(item == "" for item in data):
                            writer.writerow(data)
                except ValueError:
                    continue

        address_file.close()
    address_data_file.close()


if __name__ == "__main__":
   address_generator()