import sys
import re
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

email = sys.argv[1]  # Take email from command line argument

model = Ollama( model = "llama3")

# email = "nigerian prince sending some gold"



# Agents xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
requirement_analyzer = Agent(
    role="requirement analyzer",
    goal="Accurately analyze client requirements from example offers to identify the type of application, necessary technologies, and main functionalities required, in order to build and define everything under the title 'Purpuse of the document'",
    backstory="You are an AI assistant whose job is to analyze client requirements from example offers and provide a detailed summary",
    verbose=True,
    allow_delegation=False,
    llm=model
)
ai_trainer = Agent( 
    role="AI trainer",
    goal="Accurately analyze client requirements to design a structure of their needs, to establish what will be functionalities needed and if it will be needed to split the functionalities by who is going to use them into  multiple applications. ",
    backstory="You are an AI assistant trained to identify for who are going to be meant the functionalities and what are the functionalities be used for in the applications",
    verbose=True,
    allow_delegation=False,
    llm=model
)
offer_generator = Agent(
    role="offer generator",
    goal="Accurately analyze the designed structure of their needs and see if there can be additional tasks needed into the project not-mentioned by the client",
    backstory="You are an AI assistant which identifies the unpredicted needs of the clients",
    verbose=True,
    allow_delegation=False,
    llm=model
)
offer_validator = Agent(
    role="offer validator",
    goal="Review and define the estimated time, number of developers, and price",
    backstory="You are an AI assistant that reviews the agents and generates offers based on the agents description of what the client requested.",
    verbose=True,
    allow_delegation=False,
    llm=model
)

# Tasks xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
analyze_requirements = Task(
    description="Analyze the following client requirements: '{email}' to generate the Purpuse of the document where you to identify application type, necessary technologies, and main functionalities.",
    agent=requirement_analyzer,
    expected_output="A detailed summary of the client requirements, including application type, necessary technologies, and main functionalities, where each title has a \n before an after, and each bullet point (or phrase) ends with a \n. After you completed your entire expected output add add the end \n\n\n\n"
)
train_ai = Task(
    description="Analyze the following client requirements: '{email}' to generate structured a structure of what they are needing.",
    agent=ai_trainer,
    expected_output="The functionalities of the requirements should be organized/structured under specific purpuse type of applications if there are multiple types of users, where each title has a \n before an after, and each bullet point (or phrase) ends with a \n. After you completed your entire expected output add add the end \n\n\n\n"
)
generate_offer = Task(
    description="Anticipates the potential features that the client did not think of, which are mandatory to exist in their requirements for the app/apps to function properly but haven't been mentioned in the '{train_ai}'.",
    agent=offer_generator,
    expected_output="Let the client know what thinks might be needed to be added into their project, in order to function properly, where each title has a \n before an after, and each bullet point (or phrase) ends with a \n. After you completed your entire expected output add add the end \n\n\n\n"
)
validate_offer = Task(
    description="Review and anticipate the following generated description from '{train_ai}' and '{generate_offer}', to generate an offer with all the resourses involved.",
    agent=offer_validator,
    expected_output="An offer will be generated will all the resources needed for the project, such as the estimated time, number of developers, and billing, and what will be the result."
)


crew = Crew(
    agents=[requirement_analyzer, ai_trainer, offer_generator, offer_validator],
    tasks=[analyze_requirements, train_ai, generate_offer, validate_offer],
    verbose=2,
    process=Process.sequential
)


def format_output(text):
    # Ensure the text is a string and remove any leading/trailing whitespace
    if not isinstance(text, str):
        raise ValueError("The input must be a string")
    
    text = text.strip()
    
    # Define patterns to split the text
    patterns = r'(?=(Before:|After:|\* |[1-9]\.|10\.|[a-g]\.|[A-G]\.))'
    lines = re.split(patterns, text)
    
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("Before:") or line.startswith("After:"):
            formatted_lines.append("\n" + line)
        elif line.startswith("*") or re.match(r'^[1-9]\.|^10\.|^[a-g]\.|^[A-G]\.', line):
            formatted_lines.append("\n    " + line)
        else:
            formatted_lines.append(line)
    
    # Join lines with a single newline and ensure it's a proper string
    formatted_output = "\n".join(formatted_lines)
    return formatted_output


output = crew.kickoff()

formatted_output = format_output(output)
print(formatted_output)