import csv

from database import connection, cursor

def insert_address():

    insert_script = ('INSERT INTO address (number, street, city, zip_code)'
                     ' VALUES (%s, %s, %s, %s)'
                     ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/address.csv', newline='') as file:
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

    with open('../data/property.csv', newline='') as file:
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

    with open('../data/area_rating.csv', newline='') as file:
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

    with open('../data/school_rating.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()
    
    
def insert_gender_population():
    insert_script = (
        'INSERT INTO gender_population(number, street, city, zip_code, gender, population)'
        ' VALUES (%s, %s, %s, %s, %s, %s)')
        # ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/gender_population.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()


def insert_age_population():
    insert_script = (
        'INSERT INTO age_population(number, street, city, zip_code, age_scope, population)'
        ' VALUES (%s, %s, %s, %s, %s, %s)')
        # ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/age_population.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()
    
    
def insert_education():
    insert_script = (
        'INSERT INTO education(number, street, city, zip_code, pop_less_than_highs_school, pop_high_school_graduate_or_higher, pop_bachelor_degree_or_higher, pop_gradueate_degree_or_higher)'
        ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)')
        # ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/education.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()
    

def insert_income():
    insert_script = (
        'INSERT INTO income(number, street, city, zip_code, household_income)'
        ' VALUES (%s, %s, %s, %s, %s)')
        # ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/income.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_value = tuple(field.strip() for field in row)
            cursor.execute(insert_script, insert_value)

    connection.commit()
    
    
def insert_crime():
    insert_script = (
        'INSERT INTO crime(number, street, city, zip_code, score)'
        ' VALUES (%s, %s, %s, %s, %s)')
        # ' ON CONFLICT (number, street, city, zip_code) DO NOTHING')

    with open('../data/crime.csv', newline='') as file:
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
    insert_gender_population()
    insert_age_population()
    insert_education()
    insert_income()
    insert_crime()
    cursor.close()
    connection.close()