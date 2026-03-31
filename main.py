from flask import Flask, render_template, request, jsonify
from groq import Groq
from database import init_db, save_chat, get_last_chats
import os
import threading
import traceback

import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# ✅ SET YOUR GROQ API KEY HERE (or use env variable)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("GROQ KEY:", os.getenv("GROQ_API_KEY"))
# voice engine
engine = pyttsx3.init()

init_db()

# ---------------- AI RESPONSE ----------------
def generate_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ UPDATED MODEL
            messages=[{"role": "user", "content": user_input}]
        )

        return response.choices[0].message.content

    except Exception as e:
        import traceback
        traceback.print_exc()
        return "⚠️ Error getting response from AI"
# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "⚠️ Empty message"})

    reply = generate_response(user_input)
    return jsonify({"reply": reply})

# ---------------- VOICE INPUT ----------------
@app.route("/voice", methods=["GET"])
def voice():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            audio = r.listen(source)

        text = r.recognize_google(audio)
        reply = generate_response(text)

        return jsonify({"user": text, "reply": reply})

    except Exception as e:
        print("VOICE ERROR:", e)
        return jsonify({"error": "Voice not recognized"})

# ---------------- VOICE OUTPUT ----------------
def speak_text(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS ERROR:", e)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text", "")
    threading.Thread(target=speak_text, args=(text,)).start()
    return jsonify({"status": "spoken"})

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)