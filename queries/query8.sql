-- If any tuple in education_population relation contains null for any field, return that zip code

CREATE OR REPLACE FUNCTION find_zip_codes_with_nulls_from_gender_population()
RETURNS TABLE(
    zip_code VARCHAR,
    total_population INT,
    male INT,
    female INT) AS $$
BEGIN
    RETURN QUERY
    SELECT ap.zip_code, ap.total_population, ap.male, ap.female
    FROM age_population ap
    WHERE
        ap.total_population IS NULL OR
        ap.male IS NULL OR
        ap.female IS NULL;
END;
$$ LANGUAGE plpgsql;
