const express = require("express");
const { someData, users }  = require("./data")
const usersRouter = require('./routes/users');
const postsRouter = require('./routes/posts');

require('dotenv').config();


const app = express();
app.use(express.json());

console.log(process.env.SECRET)


const pathPrinter = (req, res, next) => {
    console.log(`Request path is ${req.path}`)
    next()
};

// 3 middleware 

const checkUserInput1 = (req, res, next) => {
    if (req.body.stuff) {
      next();
    } else {
      res.send("Please include a stuff property");
    }
};

const checkUserInput2 = (req, res, next) => {
    if (!req.body.stuff) {
      res.send("Please include a stuff property");
    } else {
      next();
    }
};

const checkUserInput3 = (req, res, next) => {
    if (!req.body.stuff) {
      res.send("Please include a stuff property");
    }
    next();
};

app.use((req, res, next) => {
    console.log("error test");
    const error = "There was an error :(";
    next(error);
});


app.use((err, req, res, next) => {
    console.log(err.message);
    const status = err.statusCode || 500;
    res.status(status);
    res.json({
      message: err.message || "Something went wrong...",
      status,
    });
  });

app.use(pathPrinter)

app.post('/', checkUserInput3, (req, res) => {
    res.json(someData)
})


app.use('/posts', postsRouter)
app.use('/users', usersRouter)



const port = process.env.PORT || 8000;
app.listen(port,  () => console.log(`Server is listening on port ${port}`));