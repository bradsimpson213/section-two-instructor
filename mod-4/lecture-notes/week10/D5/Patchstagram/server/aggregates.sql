

SELECT posts.title as post_title, users.username as author, COUNT() as likes
FROM users
    JOIN likes ON (users.id = likes.user_id)
    JOIN posts ON (likes.post_id = posts.id)
WHERE posts.id = 1;


-- SELECT title, MIN(post_date) FROM posts;

-- SELECT title, MAX(post_date) FROM posts;

-- SELECT name, 2024 - age as birth_year FROM users;

-- SELECT AVG(age) FROM users;

-- SELECT DISTINCT breed FROM users;


-- SELECT age, COUNT() FROM users
-- GROUP BY age;


-- SELECT post_id, COUNT() as num_comments FROM comments
-- GROUP by post_id
-- HAVING user_id = 1;

-- SELECT users.username, COUNT() as num_posts
-- FROM users
--     JOIN posts ON (users.id = posts.user_id)
--     ORDER BY posts.id
--     LIMIT 1;

