-- Given price range and zip code, find property information based on them
CREATE OR REPLACE PROCEDURE find_properties_in_price_range(
    p_min_price INTEGER,
    p_max_price INTEGER,
    p_zip_code VARCHAR(10)
)
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT number, street, city, zip_code, price, size_sq, year, property_type
        FROM property
        WHERE price BETWEEN p_min_price AND p_max_price
          AND zip_code = p_zip_code
    LOOP
        RAISE NOTICE 'Property => Number: %, Street: %, City: %, Zip: %, Price: %, Size: %, Year: %, Type: %',
            rec.number, rec.street, rec.city, rec.zip_code,
            rec.price, rec.size_sq, rec.year, rec.property_type;
    END LOOP;
END;
$$;

CALL find_properties_in_price_range(200000, 500000, '14001');
