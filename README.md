# 🤖 AI Chatbot with Voice & Memory

A full-stack AI Chatbot application featuring **Groq (Llama 3.3 70B)** for lightning-fast responses, **SQLite** for conversation history, and built-in **Voice-to-Text** and **Text-to-Speech** capabilities.

---

## ✨ Features

* **⚡ High-Speed AI:** Powered by Groq's LPU inference engine using the `llama-3.3-70b-versatile` model.
* **🧠 Persistent Memory:** Saves every conversation to a local SQLite database, allowing the bot to remember past context.
* **🎤 Voice Interaction:** * **Speech-to-Text:** Uses Google Speech Recognition to process your voice commands.
    * **Text-to-Speech:** Uses `pyttsx3` with threading to speak responses back to you without freezing the UI.
* **💻 Modern UI:** A clean, responsive web interface with a real-time typing effect and auto-scrolling chat.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **AI Model** | Groq (Llama 3.3) |
| **Database** | SQLite3 |
| **Voice** | SpeechRecognition, Pyttsx3 |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will also need a **Groq API Key**. Get one [here](https://console.groq.com/).
### Codes
# main
C:\Users\Lenovo LOQ\OneDrive\Pictures\Screenshots


### 2. Installation
Clone the repository and install the required Python packages:

```bash
git clone [https://github.com/hafizurrahman5417/SmartChat-AI.git](https://github.com/hafizurrahman5417/SmartChat-AI.git)
cd SmartChat-AI
pip install flask groq pyttsx3 SpeechRecognition
