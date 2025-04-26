
-- When inserting new address, if zip_code doesn’t exist in gender, age, education relations, this will cause an error. Then, use trigger to create new zip code with null data for rest of the fields, and insert the new address data

CREATE OR REPLACE FUNCTION insert_missing_zip_code()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the zip_code already exists
    IF NOT EXISTS (
        SELECT 1 FROM gender_population WHERE zip_code = NEW.zip_code
    ) THEN
        -- If not exists, insert it with NULL for population data
        INSERT INTO gender_population(zip_code) VALUES (NEW.zip_code);
		INSERT INTO age_population(zip_code)
        VALUES (NEW.zip_code);
		INSERT INTO education_population(zip_code)
        VALUES (NEW.zip_code);

    END IF;
    -- Allow the insert into address to continue
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_insert_missing_zip
BEFORE INSERT ON address
FOR EACH ROW
EXECUTE FUNCTION insert_missing_zip_code();

INSERT INTO address VALUES (99, 'MAIN ST', 'Cheektowaga', '14281', 'NY');
