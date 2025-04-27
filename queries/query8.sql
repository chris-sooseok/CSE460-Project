-- If any tuple in education_population relation contains null for any field, return that zip code

CREATE OR REPLACE FUNCTION find_zip_codes_with_nulls()
RETURNS TABLE(zip_code VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT ep.zip_code
    FROM education_population ep
    WHERE
        ep.total_population IS NULL OR
        ep.pop_less_than_high_school IS NULL OR
        ep.pop_higher_than_high_school IS NULL OR
        ep.pop_higher_than_bachelor_degree IS NULL OR
        ep.pop_higher_than_doctorate_degree IS NULL;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE show_zip_codes_with_nulls()
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN SELECT * FROM find_zip_codes_with_nulls() LOOP
        RAISE NOTICE 'Zip code with nulls: %', rec.zip_code;
    END LOOP;
END;
$$;

CALL show_zip_codes_with_nulls();
