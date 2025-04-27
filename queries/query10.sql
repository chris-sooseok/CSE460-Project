CREATE OR REPLACE PROCEDURE show_income_and_education_by_zip(
    target_zip_code VARCHAR(10)
)
LANGUAGE plpgsql
AS $$
DECLARE
    avg_income NUMERIC;
    education_level RECORD;
BEGIN
    SELECT AVG(income) INTO avg_income
    FROM household_income
    WHERE zip_code = target_zip_code;

    SELECT *
    INTO education_level
    FROM education_population
    WHERE zip_code = target_zip_code;

    RAISE NOTICE 'Zip Code %', target_zip_code;
    RAISE NOTICE 'Average Income: %', avg_income;
    RAISE NOTICE 'Pop Less Than High School: %', education_level.pop_less_than_high_school;
    RAISE NOTICE 'Pop Higher Than High School: %', education_level.pop_higher_than_high_school;
    RAISE NOTICE 'Pop Higher Than Bachelor Degree: %', education_level.pop_higher_than_bachelor_degree;
    RAISE NOTICE 'Pop Higher Than Doctorate Degree: %', education_level.pop_higher_than_doctorate_degree;

END;
$$;