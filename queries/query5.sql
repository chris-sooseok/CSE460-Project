-- average income by zip code (GROUP BY)
SELECT zip_code, AVG(income) AS avg_income
FROM household_income
GROUP BY zip_code;
