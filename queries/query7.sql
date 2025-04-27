
--Given price range and zip code, find property information based on them
CREATE OR REPLACE FUNCTION find_properties_with_price_and_area_rating(
    city_to_search VARCHAR(20),
    max_budget INTEGER,
    transportation_rating INTEGER,
    grocery_rating INTEGER,
    park_rating INTEGER,
    quiet_rating INTEGER,
    restaurant_rating INTEGER
)
RETURNS TABLE (
    number INTEGER,
    street VARCHAR(50),
    city VARCHAR(20),
    zip_code VARCHAR(10),
    price INTEGER,
    size_sq INTEGER,
    year INTEGER,
    property_type VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.number, p.street, p.city, p.zip_code, p.price, p.size_sq, p.year, p.property_type
    FROM
        property AS p
    JOIN
        area_rating AS a
    ON
        p.number = a.number AND p.street = a.street AND p.city = a.city AND p.zip_code = a.zip_code
    WHERE
        p.city = city_to_search
        AND p.price <= max_budget
        AND a.transportation >= transportation_rating
        AND a.grocery >= grocery_rating
        AND a.park >= park_rating
        AND a.quiet >= quiet_rating
        AND a.restaurant >= restaurant_rating;
END;
$$;