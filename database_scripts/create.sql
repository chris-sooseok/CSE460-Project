CREATE TABLE IF NOT EXISTS gender_population (
	zip_code VARCHAR(10),
	total_population INT,
	male INT,
	female INT,
	PRIMARY KEY (zip_code)
);

CREATE TABLE IF NOT EXISTS age_population (
	zip_code VARCHAR(10),
	total_population INT,
	"0-9" INT,
    "10-19" INT,
    "20-29" INT,
    "30-39" INT,
    "40-49" INT,
    "50-59" INT,
    "60-69" INT,
    "70-79" INT,
    "80-89" INT,
    "90-99" INT,
	PRIMARY KEY (zip_code)
);


CREATE TABLE IF NOT EXISTS education_population (
	zip_code VARCHAR(10),
    total_population INT,
	pop_less_than_high_school INT,
	pop_higher_than_high_school INT,
	pop_higher_than_bachelor_degree INT,
	pop_higher_than_doctorate_degree INT,
	PRIMARY KEY (zip_code)
);

CREATE TABLE IF NOT EXISTS address (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
    state VARCHAR(10),
	PRIMARY KEY (number, street, city, zip_code),
    FOREIGN KEY (zip_code) REFERENCES gender_population(zip_code) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (zip_code) REFERENCES age_population(zip_code) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (zip_code) REFERENCES education_population(zip_code) ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS property (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	price INTEGER,
	size_sq INTEGER,
	year INTEGER,
	property_type VARCHAR(20),
	PRIMARY KEY (number, street, city, zip_code),
	FOREIGN KEY (number, street, city, zip_code) REFERENCES address(number, street, city, zip_code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS area_rating (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	transportation INTEGER,
	grocery INTEGER,
	park INTEGER,
	quiet INTEGER,
	restaurant INTEGER,
	PRIMARY KEY (number, street, city, zip_code),
	FOREIGN KEY (number, street, city, zip_code) REFERENCES property(number, street, city, zip_code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS school_rating (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	high_school INTEGER,
	middle_school INTEGER,
	elementary_school INTEGER,
	PRIMARY KEY (number, street, city, zip_code),
	FOREIGN KEY (number, street, city, zip_code) REFERENCES property(number, street, city, zip_code) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS household_income (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
    income INT,
	PRIMARY KEY (number, street, city, zip_code),
    FOREIGN KEY (number, street, city, zip_code) REFERENCES property(number, street, city, zip_code) ON DELETE CASCADE
);

-- CREATE TABLE IF NOT EXISTS address_education_population (
--     number INTEGER,
--     street VARCHAR(50),
--     city VARCHAR(20),
--     zip_code VARCHAR(10),
--     PRIMARY KEY (number, street, city, zip_code),
--     FOREIGN KEY (number, street, city, zip_code) REFERENCES address(number, street, city, zip_code) ON DELETE CASCADE,
--     FOREIGN KEY (zip_code) REFERENCES education_population(zip_code) ON DELETE CASCADE
-- );
--
--
-- CREATE TABLE IF NOT EXISTS address_gender_population (
--     number INTEGER,
--     street VARCHAR(50),
--     city VARCHAR(20),
--     zip_code VARCHAR(10),
--     gender gender_type,
--     age_scope int4range,
--     PRIMARY KEY (number, street, city, zip_code, gender, age_scope),
--     FOREIGN KEY (number, street, city, zip_code) REFERENCES address(number, street, city, zip_code) ON DELETE CASCADE,
--     FOREIGN KEY (zip_code, gender, age_scope) REFERENCES gender_population(zip_code, gender, age_scope) ON DELETE CASCADE
-- );
-- CREATE TABLE IF NOT EXISTS income (
-- 	number INTEGER,
-- 	street VARCHAR(50),
-- 	city VARCHAR(20),
-- 	zip_code VARCHAR(10),
-- 	household_income INT,
-- 	PRIMARY KEY (zip_code),
-- 	FOREIGN KEY (zip_code) REFERENCES address(zip_code) ON DELETE CASCADE
-- );
--
--
-- CREATE TABLE IF NOT EXISTS crime_rate (
-- 	number INTEGER,
-- 	street VARCHAR(50),
-- 	city VARCHAR(20),
-- 	zip_code VARCHAR(10),
-- 	score FLOAT CHECK (score >= 0 AND score <= 1),
-- 	PRIMARY KEY (zip_code, score),
-- 	FOREIGN KEY (zip_code) REFERENCES address(zip_code) ON DELETE CASCADE
-- );

