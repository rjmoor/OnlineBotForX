const express = require("express");
const axios = require("axios");
const app = express();
const port = 3001;

app.get("/", (req, res) => {
	res.send("Hello - you are in the backend!");
});

app.listen(port, () => {
	console.log(`Server running at http://localhost:${port}`);
});