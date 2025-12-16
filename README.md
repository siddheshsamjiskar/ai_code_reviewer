GenAI App – AI Python Code Reviewer

A simple Generative AI–based Python Code Reviewer built using Streamlit and OpenAI.
The application allows users to paste Python code and receive bug detection, suggested fixes, and clear explanations.

Project Objective

# To build a user-friendly AI application that:
> Accepts Python code as input
> Analyzes the code using an LLM
> Identifies bugs, runtime errors, and logic issues
> Provides corrected code with explanations

# Tech Stack
> Python 3.9+
> Streamlit
> OpenAI (latest Python SDK)
> python-dotenv

# Project Structure
ai_code_reviewer/
├── app.py # Streamlit UI
├── reviewer.py # Prompt + response parsing
├── openai_client.py # OpenAI API wrapper
├── .env.example # Sample environment file
├── requirements.txt
└── README.md

# Application Flow
> User pastes Python code into the Streamlit UI
> User clicks "Review Code"
> The code is sent to the reviewer module
> OpenAI analyzes the code using a structured prompt
> The response is returned as JSON
> Issues, fixed code, and explanation are displayed in the UI


## Key Files Explained

# app.py
> Handles only UI logic
> Takes user input
> Calls the reviewer function
> Displays results

# reviewer.py
> Builds system and user prompts
> Sends code to OpenAI
> Extracts and parses JSON response
> Returns structured output

# openai_client.py
> Manages OpenAI client setup
> Handles retries and API errors
> Keeps API logic isolated