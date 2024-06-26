DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    profile VARCHAR(250),
    age INTEGER,
    fav_toy VARCHAR(50) DEFAULT 'mouse'
);


INSERT INTO users (name, username, profile, age, fav_toy)
VALUES
    ('Patch', 'Patchenator', 'https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg', 8, 'plush avocado'),
    ('Blue', 'Blueberry', 'https://res.cloudinary.com/app-academy4/image/upload/v1647912128/Patchstagram/66346842095__0566A55A-DF10-4E86-A59A-F5694436FA4E_wmoi1w.jpg', 8, 'orange fish'),
    ('Mimi', 'Mimi24/7', 'https://res.cloudinary.com/app-academy4/image/upload/v1684861055/Patchstagram/Mimi2_nzcfiy.png"', 12, 'mouse');


-- INSERT INTO users (name, username, profile, age)
-- VALUES
--     ('Brad', 'BradS213', 'https://ca.slack-edge.com/T3BTYDL2V-U01ACELS8V6-22995686aae5-512', 46);