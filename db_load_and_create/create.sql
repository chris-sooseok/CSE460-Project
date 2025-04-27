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
	FOREIGN KEY (number, street, city, zip_code) REFERENCES address(number, street, city, zip_code) ON DELETE CASCADE,
    CHECK (property_type IN ('single house', 'apartment', 'condo', 'farm house', 'cabin'))
);

CREATE TABLE IF NOT EXISTS area_rating (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	transportation INTEGER CHECK (transportation BETWEEN 1 AND 10),
	grocery INTEGER CHECK (grocery BETWEEN 1 AND 10),
	park INTEGER CHECK (park BETWEEN 1 AND 10),
	quiet INTEGER CHECK (quiet BETWEEN 1 AND 10),
	restaurant INTEGER CHECK (restaurant BETWEEN 1 AND 10),
	PRIMARY KEY (number, street, city, zip_code),
	FOREIGN KEY (number, street, city, zip_code) REFERENCES property(number, street, city, zip_code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS school_rating (
	number INTEGER,
	street VARCHAR(50),
	city VARCHAR(20),
	zip_code VARCHAR(10),
	high_school INTEGER CHECK (high_school BETWEEN 1 AND 10),
	middle_school INTEGER CHECK (middle_school BETWEEN 1 AND 10),
	elementary_school INTEGER CHECK (elementary_school BETWEEN 1 AND 10),
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


