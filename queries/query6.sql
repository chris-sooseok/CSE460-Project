–- count population by gender in a zip code (GROUP BY) & Union ALL
SELECT 'male' AS gender, male AS total_population
FROM gender_population
WHERE zip_code = '14001'
UNION ALL
SELECT 'female' AS gender, female AS total_population
FROM gender_population
WHERE zip_code = '14001';
