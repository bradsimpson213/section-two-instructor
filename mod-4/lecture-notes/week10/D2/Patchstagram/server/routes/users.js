const express = require('express');
const router = express.Router()
const { users }  = require("../data")



router.get("/search", (req, res) => {
    console.log(req.query.name);
    const selectedUser = users.find( user => user.username.includes(req.query.name));
    res.json(selectedUser);
});


module.exports = router;