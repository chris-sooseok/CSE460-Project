import random
import csv
import os

"""
1. Read total population data from age_population.csv
2. For each education level, distribute total population

Notes:
Age scope [0,10], and [11,20] are excluded since they are too young
"""

def education_population_generator():
    filename = "../data/education_population.csv"
    file_exists = os.path.exists(filename)
    header = ["zip_code", "total_population",
                        "pop_less_than_high_school", "pop_higher_than_high_school",
                        "pop_higher_than_bachelor_degree", "pop_higher_than_doctorate_degree"]

    with open(filename, mode="w", newline="") as address_data_file:

        writer = csv.writer(address_data_file)

        if not file_exists:
            writer.writerow(header)

        with open("../data/age_population.csv") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                zip_code = row[0]
                total_population = int(row[1])
                excluded_population = total_population - int(row[2])
                excluded_population -= int(row[3])

                # randomly distribute the population highest to less_than_high_school to lowest to graduate
                numbers = divide_number_randomly(excluded_population, 4)

                less_than_high_school = numbers[0]
                higher_than_high_school = numbers[1]
                bachelor_degree = numbers[2]
                doctorate_degree = numbers[3]

                data = [zip_code, excluded_population, less_than_high_school, higher_than_high_school, bachelor_degree, doctorate_degree]
                writer.writerow(data)

        file.close()
    address_data_file.close()

def divide_number_randomly(total, parts):
    weights = sorted([random.random() for _ in range(parts)], reverse=True)

    # Normalize weights to sum to total
    total_weight = sum(weights)
    raw_parts = [w / total_weight * total for w in weights]

    # Round and adjust to ensure sum == total
    rounded = [int(round(x)) for x in raw_parts]

    # Fix any rounding issues
    diff = total - sum(rounded)
    while diff != 0:
        for i in range(parts):
            if diff == 0:
                break
            if diff > 0:
                rounded[i] += 1
                diff -= 1
            elif diff < 0 and rounded[i] > 0:
                rounded[i] -= 1
                diff += 1

    return rounded

if __name__ == "__main__":
    education_population_generator()