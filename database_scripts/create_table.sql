

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



