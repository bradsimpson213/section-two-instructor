const express = require('express');
const { someData }  = require("../data")

const router = express.Router();


router.get("/all", (req, res) => {
    res.json(someData);
});


router.get("/:id", (req, res) => {
    const post = someData.find( (post) => (post.id === parseInt(req.params.id)));
    res.json(post);
});


router.post("/new", (req, res) => {
    const randomIndex = Math.floor( Math.random() * users.length);
    const randomUser = users[randomIndex];
    const { title, image } = req.body;

    const newPost = {
        id: someData.length + 1,
        title,
        image,
        author: randomUser,
        date: new Date(),
        comments: ["So great!", "Awesome!"],
        likes: 0
    };

    console.log(newPost);
    someData.push(newPost);
    res.json(newPost);
});



module.exports = router;