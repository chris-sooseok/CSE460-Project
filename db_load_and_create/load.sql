INSERT INTO address_gender_population (number, street, city, zip_code, gender, age_scope)
SELECT
    a.number, a.street, a.city, a.zip_code,
    g.gender, g.age_scope
FROM
    address a
JOIN
    gender_population g ON a.zip_code = g.zip_code;

INSERT INTO address_education_population (number, street, city, zip_code, pop_less_than_high_school, pop_high_school_graduate_or_higher, pop_bachelor_degree_or_higher, pop_gradueate_degree_or_higher)
SELECT
    a.number, a.street, a.city, a.zip_code,
    e.pop_less_than_high_school, e.pop_high_school_graduate_or_higher, e.pop_bachelor_degree_or_higher, e.pop_graduate_degree_or_higher
FROM
    address a
JOIN
    education_population e ON a.zip_code = e.zip_code;