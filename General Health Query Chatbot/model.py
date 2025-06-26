import os
import google.generativeai as genai
from datetime import datetime

# ✅ Configure Gemini
os.environ["GEMINI_API_KEY"] = "AIzaSyD-dDBxLdn2HH5IGieot5SXr4MaYDVQc8s"
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# 🧠 Memory
session = {
    "symptoms": [],
    "timing": [],
    "last_question": "",
    "consented_to_tips": False,
    "offered_solution": False
}

# ✅ Chat logging
def log_chat(user, bot):
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        ts = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{ts} USER: {user}\n")
        f.write(f"{ts} BOT : {bot}\n\n")

# ✅ Prompt builder
def construct_prompt(user_input, replying_to=None):
    # Extract
    symptom_keywords = ["fever", "cough", "cold", "chills", "pain", "headache", "nausea", "vomit", "sore", "fatigue", "dizzy", "shaky"]
    time_keywords = ["since", "for", "past", "yesterday", "today", "hour", "day", "week", "ago"]

    for word in symptom_keywords:
        if word in user_input.lower() and word not in session["symptoms"]:
            session["symptoms"].append(word)
    for word in time_keywords:
        if word in user_input.lower() and user_input not in session["timing"]:
            session["timing"].append(user_input)

    # If user says yes to tips
    if "yes" in user_input.lower() and "suggest" in session["last_question"].lower():
        session["consented_to_tips"] = True

    # Build context
    symptoms = ", ".join(session["symptoms"])
    timings = ", ".join(session["timing"])
    reply_to = f"User replied to: “{replying_to}”" if replying_to else ""

    # Decide conversation flow
    next_action = ""
    if session["consented_to_tips"]:
        next_action = "The user agreed to get suggestions. Offer 2–3 safe health tips. Then say: “Please consult a doctor immediately for proper medical evaluation.”"
    elif len(session["symptoms"]) >= 3 and not session["offered_solution"]:
        session["offered_solution"] = True
        next_action = f"You've now gathered symptoms: {symptoms}. Ask politely: “Would you like me to share a few tips that might help?”"
    elif session["offered_solution"]:
        next_action = "Wait for user's response about prevention. Do not ask further symptom questions."

    # Master prompt
    return f"""
You are a smart, warm, human-like health assistant.

🎯 GOALS:
- Understand symptoms & timeline contextually.
- If 3+ symptoms shared, move to offering support instead of more questioning.
- If user consents, share 2–3 general prevention tips, then say:
  👉 “Please consult a doctor immediately for proper medical evaluation.”
- Interpret 'yes' or 'no' based on your previous question.
- Never repeat what the user already told you.
- Never suggest medications, diagnosis, or act like a doctor.

📌 CONTEXT MEMORY:
- Symptoms: {symptoms if symptoms else "none"}
- Timeline: {timings if timings else "none"}
- {reply_to}
- {next_action}

User: {user_input}
Assistant:"""

# ✅ Core function
def ask_bot(user_input):
    try:
        vague_replies = ["yes", "no", "not yet", "maybe", "okay", "i don’t know"]
        is_vague = user_input.lower().strip() in vague_replies
        replying_to = session["last_question"] if is_vague else None

        prompt = construct_prompt(user_input, replying_to)
        response = model.generate_content(prompt)
        reply = response.text.strip()

        # Save last question if needed
        if "?" in reply:
            session["last_question"] = reply

        log_chat(user_input, reply)
        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"
