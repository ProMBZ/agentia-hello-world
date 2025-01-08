# Agentia Hello World with Gemini 2.0, LangGraph, and Streamlit

A minimal, 2-agent “Hello World” that handles multilingual greetings and a special "assalamu alaikum" case using Google's Gemini 2.0 (via `langchain_google_genai`).

## Files

- **.env**  
  Contains `GEMINI_API_KEY=your_key`. Not committed to source control.

- **greeting_agent.py**  
  A specialized agent that uses `ChatGoogleGenerativeAI` to respond to greetings in any language.

- **front_end_agent.py**  
  A front-end orchestration agent that delegates to `greeting_agent.py`.

- **graph_definition.py**  
  Shows a `StateGraph` with two nodes: "front_end_agent" and "greeting_agent", connected from `START` to `END`.  
  We do **not** call `.build()` or `runner.run()`, so no version conflicts.

- **app.py**  
  A `streamlit` web app that:
  1. Loads `.env`,
  2. Lets the user type a greeting,
  3. Displays only the single final response from the greeting agent.

- **requirements.txt**  
  Lists all packages required, ensuring no “module not found” errors.

## Setup & Run

1. **Install** dependencies in a **fresh** virtual environment:
   ```bash
   pip install -r requirements.txt
