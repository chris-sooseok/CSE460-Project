CREATE TABLE IF NOT EXISTS address (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	PRIMARY KEY (number, street, city, zip_code)
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

CREATE TABLE zip_area (
	zip_code VARCHAR(10) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS gender_population (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	gender ENUM('male', 'female')
	age_scope int4range,
	population INT,
	PRIMARY KEY (zip_code, gender, age_scope),
	FOREIGN KEY (zip_code) REFERENCES property(zip_code) ON DELETE CASCADE
);

-- data from address table
-- 8,LUCID DR,Cheektowaga,14001 
-- 79,CRANDON BLVD,Cheektowaga,14001
-- 3619,HARLEM RD,Cheektowaga,14001
-- 525,AERO DR,Cheektowaga,14001

-- 14001 male [0,10]
-- 14001 male [10, 20]
-- 14001 male [20, 30]
-- 14001 male [30, 40]

-- 14001 female [0,10]
-- 14001 female [10, 20]
-- 14001 female [20, 30]
-- 14001 female [30, 40]

-- one-to-many
-- one-to-one
-- many-to-many

CREATE TABLE IF NOT EXISTS education (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	pop_less_than_high_school INT,
	pop_high_school_graduate_or_higher INT,
	pop_bachelor_degree_or_higher INT,
	pop_gradueate_degree_or_higher INT,
	PRIMARY KEY (zip_code),
	FOREIGN KEY (zip_code) REFERENCES address(zip_code) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS income (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	household_income INT,
	PRIMARY KEY (zip_code),
	FOREIGN KEY (zip_code) REFERENCES address(zip_code) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS crime_rate (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	score FLOAT CHECK (score >= 0 AND score <= 1),
	PRIMARY KEY (zip_code, score),
	FOREIGN KEY (zip_code) REFERENCES address(zip_code) ON DELETE CASCADE
);

