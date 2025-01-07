# Agentia Hello World with Gemini 2.0

This is a minimal “Hello World” multi-agent project using:

- **LangGraph** for the conceptual flow (two agents: front-end + greeting).
- **Gemini 2.0** (via `langchain_google_genai`) for multilingual greeting detection.
- **Streamlit** for a simple user interface that only shows the final agent response.

## Project Structure

```plaintext
hello_world/
  ├─ .env
  ├─ greeting_agent.py
  ├─ front_end_agent.py
  ├─ graph_definition.py
  ├─ app.py
  └─ README.md


## Summary of “What’s Happening in the Back”

When a user types text in **Streamlit** (`app.py`):

1. The **Front-End Orchestration Agent** (`front_end_agent.py`) receives the input.  
2. It delegates the text to the **Greeting Agent** (`greeting_agent.py`), which:
   - Sends a system prompt and the user’s message as **chat messages** to **Gemini 2.0**.  
   - Gemini checks if it’s a special “assalamu alaikum,” or any other greeting, or something else.  
   - Returns a **friendly** greeting in the same language (or fallback in English).  
3. The **Front-End** returns that single final response to the user.  
4. We only display that response in **Streamlit**, **no** repeated logs or conversation lines.

Meanwhile, `graph_definition.py` shows how you would conceptualize the conversation flow using LangGraph’s `node`, `START`, and `END`, but we do **not** call `run()`—we do everything manually in `app.py`.

---

### Enjoy Your Multi-Agent Project!

You now have:

- **Two Agents** (Front-End, Greeting).  
- **LangGraph** conceptual flow.  
- **Gemini 2.0** for multilingual greeting logic.  
- **Streamlit** front-end that shows **only** the final answer.  
- A **README** clarifying how it all works and how to run the project!
