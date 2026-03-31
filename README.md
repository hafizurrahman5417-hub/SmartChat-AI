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

##Main

<img width="980" height="734" alt="Screenshot 2026-03-31 192853" src="https://github.com/user-attachments/assets/e8a2f089-117e-4395-b21b-3a01176bb1c2" />
<img width="765" height="779" alt="Screenshot 2026-03-31 193058" src="https://github.com/user-attachments/assets/d5c88881-4590-48b3-ad26-867bccd18abb" />





##Dtabase

<img width="657" height="552" alt="Screenshot 2026-03-31 193122" src="https://github.com/user-attachments/assets/3f4d05c1-34de-40c8-95bd-306692aa4987" />





##Index

<img width="801" height="853" alt="Screenshot 2026-03-31 193224" src="https://github.com/user-attachments/assets/90755d23-29c1-46d5-afda-e4ce50f4221f" />
           <img width="596" height="878" alt="Screenshot 2026-03-31 193249" src="https://github.com/user-attachments/assets/e82ce00a-3e90-4511-823f-c7aff0755d1d" />
           <img width="587" height="638" alt="Screenshot 2026-03-31 193307" src="https://github.com/user-attachments/assets/57c095be-08c5-4814-8b2e-eb4f23cc0c1d" />



###Output

<img width="1900" height="914" alt="Screenshot 2026-03-31 194845" src="https://github.com/user-attachments/assets/93ab1542-98f4-45b4-b523-4343dcb2ed8d" />



### 2. Installation
Clone the repository and install the required Python packages:

```bash
git clone [https://github.com/hafizurrahman5417/SmartChat-AI.git](https://github.com/hafizurrahman5417/SmartChat-AI.git)
cd SmartChat-AI
pip install flask groq pyttsx3 SpeechRecognition
