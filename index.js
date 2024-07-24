const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();
const port = 3000;

// Set EJS as templating engine
app.set('view engine', 'ejs');

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));

// Route to display the HTML form
app.get('/', (req, res) => {
    res.render('form');
});

// Route to handle form submission
app.post('/submit-email', (req, res) => {
    const email = req.body.email;
    const command = `"C:/Python312/python.exe" main.py "${email}"`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.send(`Error: ${error}`);
        }
        res.send(`Python Output: ${stdout}`);
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});