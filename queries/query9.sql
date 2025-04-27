-- Deleting a specific property based on 4 input(number, street, city and zipcode)
CREATE OR REPLACE PROCEDURE delete_property(
    p_number INT,
    p_street VARCHAR,
    p_city VARCHAR,
    p_zip_code VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM property
    WHERE number = p_number
      AND street = p_street
      AND city = p_city
      AND zip_code = p_zip_code;
END;
$$;

Number, street, city, and zip code match the primary key columns of the property. It can find exactly one property and delete it safely.

For example to delete the property at 0 CENTER ST, Aurora, 14052

CALL delete_property(0, 'CENTER ST', 'Aurora', '14052');
