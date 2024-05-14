const express = require("express");
const { someData, users }  = require("./data")


const app = express();
app.use(express.json());


app.get("/posts/all", (req, res) => {
    res.json(someData);
});


app.get("/posts/:id", (req, res) => {
    const post = someData.find( (post) => (post.id === parseInt(req.params.id)));
    res.json(post);
});


app.post("/posts/new", (req, res) => {
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

app.get("/users/search", (req, res) => {
    console.log(req.query.name);
    const selectedUser = users.find( user => user.username.includes(req.query.name));
    res.json(selectedUser);
});


const port = 8000;
app.listen(port,  () => console.log(`Server is listening on port ${port}`));