SELECT posts.title, posts.post_date, users.username as author
FROM posts
    JOIN users ON (users.id = posts.user_id);

SELECT posts.title, posts.post_date, users.username as author, comments.comment_text
FROM posts
    JOIN users ON (users.id = posts.user_id) 
    JOIN comments ON (comments.post_id = posts.id);



SELECT users.username, posts.title
FROM users
    JOIN likes ON (users.id = likes.user_id)
    JOIN posts ON (likes.post_id = posts.id)
WHERE posts.id = 1;


-- SELECT musicians.first_name, musicians.last_name
-- FROM instruments
--   JOIN musician_instruments ON (
--     instruments.id = musician_instruments.instrument_id
--   )
--   JOIN musicians ON (musicians.id = musician_instruments.musician_id)

-- WHERE instruments.type = "piano";