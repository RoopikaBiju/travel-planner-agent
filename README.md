# ✈️ Travel Planner Agent (AI-Powered)

This is an AI-powered command-line tool that helps users generate personalized travel itineraries. It uses Google’s Gemini model to provide:

- A multi-day travel plan based on your input  
- Suggested activities, food, and places per location  
- File-saving feature for your itinerary via tools  
- Output formatted as JSON using Pydantic schema  

---

## 🚀 Features

- 🧠 Powered by LangChain + Google Gemini (Generative AI)  
- ✅ Uses Pydantic for structured JSON output  
- 🛠️ Tool integration for saving plans (`save_plan`, `suggest_trip`)  
- 📄 Enforces format via dynamic JSON schema  
- 💬 Interactive command-line interface  

---

## 📂 Project Structure

```bash
travel-planner-agent/
├── main.py              # Main CLI application
├── tools.py             # Tool definitions (save_plan, suggest_trip)
├── schema.py            # Pydantic schema for output
├── requirements.txt     # All required packages
├── .env                 # API key (ignored by Git)
├── plans/               # Directory where plans are saved
└── README.md            # You're here!
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/RoopikaBiju/travel-planner-agent.git
cd travel-planner-agent
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate     #On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Add your API key (Gemini)

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🏃 Run the app

```bash
python main.py
```

Then you'll see a prompt like:
```text
✈️Travel Planner Agent! Type 'exit' to quit.
You: Plan a 3-day trip to Tokyo for food and culture
```

To exit:

```bash
exit
```

---

### 📦 Dependencies

```text
langchain
langchain-google-genai
pydantic
python-dotenv
```

Install them with:

```bash
pip install -r requirement.txt
```

### 📜 Sample Saved Plan Output

Itineraries are saved in the plans/ folder with a name like:

```text
plans/tokyo_2025-08-02_20-56-45.txt
```

Plans are saved in the folder in this format:

```text
Day 1: Visit Senso-ji Temple, Ueno Park, and enjoy dinner in Ginza.
Day 2: Explore Harajuku, Shibuya Crossing, and eat at themed cafés.
Day 3: Enjoy Tsukiji Market, take a cooking class, and end with dinner in Ebisu.
```
---

## 🛡 Disclaimer

This tool is for personal and educational use only. Always verify local travel guidelines and safety precautions when planning trips.