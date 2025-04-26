import random
import csv
import os

"""
1. Read address data from address.csv
2. Create random price, size_sq, year, and property_type data
3. Store them into property.csv file

Notes:
property types are 'single house', 'apartment', 'condo', 'farm house', 'cabin'
"""

def property_generator():
    filename = "../data/property.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "price", "size_sq", "year", "property_type"]

    with open(filename, mode="w", newline="") as property_info_file:

        writer = csv.writer(property_info_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/address.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                price = random.randint(100, 500) * 1000

                if price < 200_000:
                    size_sq = random.randint(1200, 1800)
                elif price < 300_000:
                    size_sq = random.randint(1800, 2400)
                elif price < 400_000:
                    size_sq = random.randint(2400, 3200)
                else:
                    size_sq = random.randint(3200, 4000)

                number = line[0]
                street = line[1]
                city = line[2]
                postcode = line[3]
                property_type = random.choice(['single house', 'apartment', 'condo', 'farm house', 'cabin'])
                year = random.randint(1900, 2025)

                data = [number, street, city, postcode, price, size_sq, year, property_type]
                writer.writerow(data)

        address_file.close()
    property_info_file.close()


if __name__ == "__main__":
    property_generator()
