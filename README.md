🤖 NEXA – AI Voice Assistant

NEXA is a Python-based personal AI voice assistant designed to interact with users through natural voice commands. It combines speech recognition, AI-powered conversation, text-to-speech, and web search capabilities.

✨ Features

- 🎤 Voice-based user interaction
- 🧠 AI-powered conversational responses
- 🔊 Text-to-speech voice output
- 🌐 Web search using Tavily API
- 👋 Voice-based assistant activation
- 🛑 Voice commands to exit the assistant
- 🧩 Modular Python architecture

🛠️ Tech Stack

- Python
- Groq API
- Tavily API
- Speech Recognition
- Text-to-Speech
- python-dotenv

📁 Project Structure

NEXA-AI/
│
├── main.py
├── modules/
│   ├── brain.py
│   ├── speech.py
│   ├── speak.py
│   └── web_search.py
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/NEXA-AI.git
cd NEXA-AI

2. Install dependencies

pip install -r requirements.txt

3. Configure API Keys

Create a ".env" file in the project root:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Never upload your ".env" file to GitHub.

4. Run NEXA

python main.py

💬 Example Commands

"Hello Nexa"
"Search latest technology news"
"Who is the current Chief Minister of Tamil Nadu?"
"Goodbye"

🚀 Future Development

NEXA V2 will focus on expanding the assistant with more advanced capabilities, including mobile integration and device-level interaction.

👨‍💻 Developer

Praveen

Built with Python, AI APIs, and a passion for creating intelligent assistants.
