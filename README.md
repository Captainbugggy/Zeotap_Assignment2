# CDP Support Agent Chatbot

## Project Overview
AI-powered chatbot for answering "how-to" questions across Customer Data Platforms.
-Real time demo https://chatbot-h3mz.onrender.com/

## 🚀 Features
- Support for Segment, mParticle, Lytics, Zeotap
- AI-driven documentation retrieval
- Real-time response generation
- Web-based interface

## 🔧 Technology Stack
- Backend: Flask
- AI: Google Gemini
- Frontend: HTML/jQuery
- Web Scraping: BeautifulSoup

## 🌟 Getting Started

### Prerequisites
- Python 3.8+
- Google Gemini API Key

### Installation
```bash
git clone https://github.com/Captainbugggy/Zeotap_Assignment2.git
cd Zeotap_Assignment2
python -m venv venv
venv\Scripts\activate #for mac source venv/bin/activate
pip install -r requirements.txt
```

### Gemini API Key Setup
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy generated key
4. Update `config.py`:
```python
class Config:
    API_KEY = "YOUR_COPIED_GEMINI_API_KEY"
```

### Running the Application
```bash
python run.py
```

## 📝 Usage
- Open browser to `http://localhost:5000`
- Ask CDP-related questions
- Receive AI-generated guidance

## 🔍 Supported Platforms
- Segment
- mParticle
- Lytics
- Zeotap

## 🤝 Contributing
1. Fork Repository
2. Create Feature Branch
3. Commit Changes
4. Push to Branch
5. Create Pull Request
