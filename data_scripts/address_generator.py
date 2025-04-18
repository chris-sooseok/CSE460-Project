import json
import random
import csv
import os

def address_generator():
    filename = "../data/address.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code"]

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
                postcode = line["properties"]['postcode']

                data = [number, street, city, postcode]

                if not any(item == "" for item in data):
                    writer.writerow(data)
                else:
                    continue

        address_file.close()
    address_data_file.close()


if __name__ == "__main__":
   address_generator()