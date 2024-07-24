# Client-Request_AI-Agents_Report-Generator
The project runs with a node.js server => index.js
- you can start the project by typing in the command line: nodemon index.js
- Go to http://localhost:3000/ and add the client request there.

I used:
- VS Code
- Ollama3, model 8b.
  

Dependencies:
"dependencies": {
    "body-parser": "^1.20.2",
    "child_process": "^1.0.2",
    "ejs": "^3.1.10",
    "express": "^4.19.2",
    "html-escaper": "^3.0.3",
    "http": "^0.0.1-security",
    "llm": "^1.0.7",
    "nodemon": "^3.1.4",
    "requests": "^0.3.0"
  }

You will also need npm i crewai

Pasii pentru antrenarea AI-ului:
- Am folosit agenti, pe care i-am definit printr-un scop si un backstory.
- iar apoi am creat Task-uri pentru Agenti, cu o descriere si un expected outcome.
