import random
import csv
import os

"""
1. Read address data from address.csv
2. Create random school ratings for "high_school", "middle_school", "elementary_school" in scale of 10
3. Store them into school_rating.csv file

Notes:
property types are 'single house', 'apartment', 'condo', 'farm house', 'cabin'
"""

def school_rating_generator():
    filename = "../data/school_rating.csv"
    file_exists = os.path.exists(filename)
    header = ["number", "street", "city", "zip_code", "high_school", "middle_school", "elementary_school"]

    with open(filename, mode="w", newline="") as school_rating_info_file:

        writer = csv.writer(school_rating_info_file)

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
                high_school = random.randint(1, 10)
                middle_school = random.randint(1, 10)
                elementary_school = random.randint(1, 10)

                data = [number, street, city, postcode, high_school, middle_school, elementary_school]
                writer.writerow(data)

        address_file.close()
    school_rating_info_file.close()


if __name__ == "__main__":
   school_rating_generator()