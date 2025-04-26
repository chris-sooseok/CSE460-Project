import csv

from database import connection, cursor

def load_gender_population():
    load_script = (
        'INSERT INTO gender_population( zip_code, total_population, male, female)'
        ' VALUES (%s, %s, %s, %s)'
        ' ON CONFLICT (zip_code) DO NOTHING')
    with open('../data/gender_population.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()

def load_age_population():
    load_script = (
        'INSERT INTO age_population(zip_code, total_population, "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99")'
        ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        ' ON CONFLICT (zip_code) DO NOTHING')
    with open('../data/age_population.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()


def load_education_population():
    load_script = (
        'INSERT INTO education_population(zip_code, total_population, pop_less_than_high_school, pop_higher_than_high_school, pop_higher_than_bachelor_degree, pop_higher_than_doctorate_degree)'
        ' VALUES (%s, %s, %s, %s, %s, %s)'
        ' ON CONFLICT (zip_code) DO NOTHING')

    with open('../data/education_population.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)

    connection.commit()

def load_address():

    load_script = ('INSERT INTO address (number, street, city, zip_code, state)'
                     ' VALUES (%s, %s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')
    with open('../data/address.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()

def load_property():
    load_script = ('INSERT INTO property (number, street, city, zip_code, price, size_sq, year, property_type)'
                     ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')
    with open('../data/property.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()

def load_area_rating():
    load_script = ('INSERT INTO area_rating (number, street, city, zip_code, transportation, grocery, park, quiet, restaurant)'
                     ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')
    with open('../data/area_rating.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()


def load_school_rating():
    load_script = (
        'INSERT INTO school_rating (number, street, city, zip_code, high_school, middle_school, elementary_school)'
        ' VALUES (%s, %s, %s, %s, %s, %s, %s)'
        ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')
    with open('../data/school_rating.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)

    connection.commit()

def load_household_income():
    load_script = (
        'INSERT INTO household_income(number,street,city,zip_code,income)'
        ' VALUES (%s, %s, %s, %s, %s)'
        ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')
    with open('../data/household_income.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(load_script, insert_value)
    connection.commit()

if __name__ == '__main__':
    load_gender_population()
    load_education_population()
    load_age_population()
    load_address()
    load_property()
    load_area_rating()
    load_school_rating()
    load_household_income()

    cursor.close()
    connection.close()