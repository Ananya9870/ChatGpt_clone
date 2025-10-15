💻 Chatgpt: AI Chatbot for Coders with OCR

Chatgpt is an interactive Streamlit-based AI assistant built for developers and learners.
It integrates with Ollama’s local LLM API (such as llama2:latest) to provide real-time coding help, debugging assistance, and general Q&A — right from your desktop.

It also includes a built-in OCR (Optical Character Recognition) module that allows users to extract text from images (e.g., code snippets, screenshots, or notes) and send it directly to the chatbot for further discussion.

🧠 Key Features
🤖 AI Chat Assistant

Powered by Ollama’s local model (llama2:latest)

Provides context-aware responses

Maintains conversation history across sessions

Chat interface styled like ChatGPT

📸 OCR Integration

Upload images (.jpg, .jpeg, .png)

Extract text instantly using Tesseract OCR

Send extracted text directly to the chat interface

🧾 Persistent Chat History

Saves conversations locally as chat_history.json

Reloads previous sessions automatically

Allows clearing current chat or entire history easily

💬 Modern UI

Built with Streamlit

Clean, ChatGPT-like dark interface

Interactive sidebar with expandable past conversations

⚙️ Tech Stack
Component	Technology
Frontend/UI	Streamlit
Backend AI	Ollama (Local LLM - e.g., Llama 2)
OCR Engine	Tesseract OCR
Language	Python
Persistence	Local JSON file (chat_history.json)
🛠️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/bytebuddy-ai.git
cd bytebuddy-ai

2. Install Dependencies

Make sure you have Python 3.8+ installed.
Then install the required libraries:

pip install streamlit streamlit-chat requests pillow pytesseract

3. Install & Configure Tesseract OCR

Windows:
Download from Tesseract at UB Mannheim

Then set the executable path in the code:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


macOS (Homebrew):

brew install tesseract


Linux (Ubuntu):

sudo apt install tesseract-ocr

4. Install and Run Ollama

Download and install Ollama (for local LLM models):
🔗 https://ollama.ai/download

Then pull a model like Llama 2:

ollama pull llama2


Start the Ollama server locally:

ollama serve

🚀 Run the Application

Once everything is set up, start the Streamlit app:

streamlit run app.py


💡 The app will automatically open in your default browser at
http://localhost:8501

🧩 File Structure
📁 bytebuddy-ai/
│
├── app.py                  # Main Streamlit application
├── chat_history.json       # Persistent local chat history
├── requirements.txt        # Python dependencies (optional)
└── README.md               # Project documentation

🖼️ App Walkthrough
🏠 Main Interface

A clean dark-themed chat UI

Type messages at the bottom input bar

AI responds with contextual answers

📸 OCR Module

Upload an image → Extract text → Send to chat

Perfect for extracting code or notes

🗂️ Sidebar

View and reopen past chats

Buttons to clear chat or full history

💡 Example Use Cases

Ask coding-related questions (Python, Java, C, etc.)

Debug errors by pasting code snippets

Extract text from screenshots (OCR) and analyze it

Discuss algorithms, LeetCode problems, or ML concepts

⚠️ Troubleshooting
Issue	Possible Fix
TesseractNotFoundError	Verify installation path in pytesseract.pytesseract.tesseract_cmd
Ollama not responding	Ensure Ollama server is running locally (ollama serve)
Empty responses	Check that the model name (llama2:latest) is available locally
Streamlit not found	Run pip install streamlit again
🧑‍💻 Contributing

Contributions are welcome!
If you’d like to add new features or improve the UI:

Fork the repository

Create a new branch (feature/improve-ui)

Commit changes

Submit a pull request 🎉

📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute with attribution.
