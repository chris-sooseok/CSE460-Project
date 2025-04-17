import csv

from database import connection, cursor

def insert_address():

    insert_script = ('INSERT INTO address (number, street, city, zip_code)'
                     ' VALUES (%s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/address_data.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()

def insert_property():
    insert_script = ('INSERT INTO property (number, street, city, zip_code, price, size_sq, year, property_type)'
                     ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/property_data.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()

def insert_area_rating():
    insert_script = ('INSERT INTO area_rating (number, street, city, zip_code, transportation, grocery, park, quiet, restaurant)'
                     ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/area_rating_data.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()


def insert_school_rating():
    insert_script = (
        'INSERT INTO school_rating (number, street, city, zip_code, high_school, middle_school, elementary_school)'
        ' VALUES (%s, %s, %s, %s, %s, %s, %s)'
        ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/school_rating_data.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()

if __name__ == '__main__':
    insert_address()
    insert_property()
    insert_area_rating()
    insert_school_rating()
    cursor.close()
    connection.close()