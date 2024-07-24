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

Steps for AI integration: 
- I used agents, which we defined by a goal and a backstory. 
- and then I created Tasks for Agents, with a description and an expected outcome.
- I used the first example (Oferta - Test 1.docx) as a tamplate for the description of the Tasks and Agents.
     I. Purpose of the document:
     II. Structure proposal:
     III. Additional suggestions:
     IV. Billing and implementation time (plus the number of developers, and what will be the result.)



