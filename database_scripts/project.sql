-- insert 
INSERT INTO address VALUES (99, 'MAIN ST', 'Cheektowaga', '14001');
INSERT INTO property VALUES (99, 'MAIN ST', 'Cheektowaga', '14001', 250000, 1800, 2005, 'house');

-- delete
DELETE FROM property WHERE number = 99 AND street = 'MAIN ST' AND city = 'Cheektowaga' AND zip_code = '14001';

-- properties sorted by price (lowest to highest) - ascending
SELECT number, street, city, zip_code, price
FROM property
ORDER BY price ASC; 

-- average income by zip code (GROUP BY)
SELECT zip_code, AVG(household_income) AS avg_income
FROM income
GROUP BY zip_code;

-- count population by gender in a zip code (GROUP BY)
SELECT gender, SUM(population) AS total_population
FROM gender_population
WHERE zip_code = '14001'
GROUP BY gender;

-- find properties in zip codes with income above average (subquery)

SELECT * FROM property
WHERE zip_code IN (
    SELECT zip_code FROM income
    WHERE household_income > (
        SELECT AVG(household_income) FROM income
        )
    );

