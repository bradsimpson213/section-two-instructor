-- SELECT COUNT() FROM cats;

-- SELECT name, MIN(birth_year) FROM cats; 

-- SELECT name, 2024 - MAX(birth_year) as age FROM cats; 


-- SELECT cats.name, COUNT(toys.id) as toy_count
-- FROM toys
--     JOIN cats ON (cats.id = toys.cat_id)
--     GROUP BY toys.cat_id;

SELECT cats.name, COUNT(toys.id) as toy_count
FROM toys
    JOIN cats ON (cats.id = toys.cat_id)
    GROUP BY toys.cat_id
    HAVING toy_count >= 2;