import json
import random
import csv
import os

def address_generator():
    filename = "../data/address_data.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "postcode"]

    with open("../data/address_data.csv", mode="w", newline="") as address_data_file:

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

                address_info = [number, street, city, postcode]

                writer.writerow(address_info)
        address_file.close()
    address_data_file.close()


if __name__ == "__main__":
   address_generator()