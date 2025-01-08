
---

## Agentia Hello World

1. **`.env`**  
   - Put your **GEMINI_API_KEY** here (e.g., `GEMINI_API_KEY=your_real_key`).  
   - This file is **not** committed to version control if it contains secrets.

2. **`greeting_agent.py`**  
   - Contains a **Greeting Agent** that uses `ChatGoogleGenerativeAI` from `langchain_google_genai` to handle greetings in **any** language.  
   - Special rules for “assalamu alaikum” → “Wa alaikum as salam” + emojis, plus a fallback for non-greetings.

3. **`front_end_agent.py`**  
   - A **Front-End Agent** that receives user text and forwards it to the Greeting Agent.  
   - If you had multiple specialized agents, you’d add routing logic here.

4. **`graph_definition.py`**  
   - Demonstrates a **LangGraph** flow: `START -> front_end_agent -> greeting_agent -> END`.  
   - We do **not** call `run()` or `.build()`, just define the conceptual flow using `node`, `START`, `END`.

5. **`app.py`**  
   - A **Streamlit** application that loads the environment (`.env`), takes user input, calls the **Front-End Agent**, and displays **only** the final greeting text.  
   - No conversation logs or repeated lines—just a single final response.

6. **`requirements.txt`**  
   - Ensures you have all the Python packages needed to avoid “module not found” errors.  
   - Includes `langchain_google_genai`, `langgraph`, `streamlit`, etc.

7. **`README.md`** (this file)  
   - Explains how to install, run, and customize the project.

---

## How It Works Behind the Scenes

1. **User Interface (Streamlit UI)**  
   - You enter a message, e.g. “Hi” or “assalamu alaikum.”  
   - Press **Send**, and Streamlit triggers a function call to the **Front-End Agent**.

2. **Front-End Agent**  
   - Currently, it **always** delegates user text to the Greeting Agent.  
   - In a larger system, you’d parse the message (greeting vs. something else) and route accordingly.

3. **Greeting Agent**  
   - Uses `ChatGoogleGenerativeAI` to call **Gemini 2.0** with a **system prompt** that has rules for greetings.  
   - If it detects “assalamu alaikum,” returns “Wa alaikum as salam” + emojis.  
   - If it’s any other recognized greeting, it responds in **that same language** with a friendly phrase and emojis.  
   - If not recognized, fallback: “I only handle greetings right now. 🤖 Please try a greeting next time.”

4. **Response**  
   - The final text from the Greeting Agent is passed back through the **Front-End Agent** to **Streamlit**.  
   - Streamlit updates a `last_response` field in the session state and displays it.  
   - You see just **one** final line (no conversation log).

5. **LangGraph**  
   - The file `graph_definition.py` shows how you **could** orchestrate these agents if you used the full graph approach.  
   - We define nodes for `front_end_agent` and `greeting_agent`, connected from `START` → `END`, but we don’t run them automatically.  
   - This is a “hello world” demonstration of multi-agent flow with minimal overhead.

---

## Setup & Installation

1. **Clone or Download** the repository containing these files.  
2. **Create** a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
