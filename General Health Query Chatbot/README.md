#  General Health Query Chatbot

This is a smart, human-like health assistant chatbot built using **Flask** and **Google Gemini 1.5 Flash API**. It responds to user-reported symptoms in a warm, conversational manner and offers general prevention tips (only if the user consents). It is designed to behave logically like a real assistant — without giving any diagnosis or treatment advice.

---

##  Project Objective

The goal of this project is to simulate an AI-based health assistant that can:

- Understand **symptoms** and **timing context**
- Track conversation memory across turns
- Offer **prevention suggestions** after gathering sufficient input
- Behave ethically by avoiding medical diagnosis or medication
- Encourage users to consult a real doctor for evaluation

---

##  Key Features

- ✅ Tracks symptoms and timing from user's responses  
- ✅ Handles vague answers like “yes”, “maybe”, “not yet” logically  
- ✅ Offers prevention tips only **after 3+ symptoms** are gathered  
- ✅ Stores conversations in a `chat_log.txt` file with timestamps  
- ✅ Uses Gemini API to generate realistic, context-aware replies  
- ✅ Avoids repetition by maintaining session memory

---

##  Technologies Used

- **Google Gemini 1.5 Flash** – for smart, human-like responses  
- **Flask** – for running the web-based interface  
- **HTML + CSS** – for frontend chatbot UI  
- **Python** – for backend logic and session handling  
- **Session dictionary** – to store symptoms, timing, and last questions

---
## Alert:

>  Before running this project, make sure to create your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and set it as an environment variable (e.g., `GEMINI_API_KEY`) for secure access.


