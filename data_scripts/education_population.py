import random
import csv
import os

def education_population_generator():
    filename = "../data/education_population.csv"
    file_exists = os.path.exists(filename)
    header = ["zip_code",
                        "pop_less_than_high_school", "pop_high_school_graduate_or_higher",
                        "pop_bachelor_degree_or_higher", "pop_graduate_degree_or_higher"]

    with open(filename, mode="w", newline="") as address_data_file:

        writer = csv.writer(address_data_file)

        if not file_exists:
            writer.writerow(header)

        zip_code_population = {}

        with open("../data/gender_population.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] in zip_code_population:
                    zip_code_population[row[0]] += int(row[3])
                else:
                    zip_code_population[row[0]] = int(row[3])

            print(zip_code_population)

            for zip_code, population in zip_code_population.items():
                numbers = divide_number_randomly(population, 4)
                less_than_high_school = numbers[0]
                higher_than_high_school = numbers[1]
                bachelor_degree = numbers[2]
                graduate_degree = numbers[3]

                data = [zip_code, less_than_high_school, higher_than_high_school, bachelor_degree, graduate_degree]
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