-- find properties in zip codes with income above average (subquery)
SELECT * FROM property
WHERE zip_code IN (
   	 SELECT zip_code FROM household_income
    	WHERE income > (
       	 	SELECT AVG(income) FROM household_income
       	 	)
   	 )