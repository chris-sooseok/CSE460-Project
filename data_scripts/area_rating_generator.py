import random
import csv
import os

"""
1. Read address data from address.csv
2. Create random area ratings for "transportation", "grocery", "park", "quiet", "restaurant" in scale of 10
3. Store them into area_rating.csv file

Notes:
quiet and grocery ratings are dependent on transportation rating
"""

def area_rating_generator():
    filename = "../data/area_rating.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "transportation", "grocery", "park", "quiet", "restaurant"]

    with open(filename, mode="w", newline="") as area_rating_info_file:

        writer = csv.writer(area_rating_info_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/address.csv") as address_file:
            reader = csv.reader(address_file)
            next(reader)
            for line in reader:

                number = line[0]
                street = line[1]
                city = line[2]
                postcode = line[3]
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

                data = [number, street, city, postcode, transportation, grocery, park, quiet, restaurant]

                writer.writerow(data)

        address_file.close()
    area_rating_info_file.close()


if __name__ == "__main__":
   area_rating_generator()