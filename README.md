# 🚀 AI LinkedIn Profile Analyzer

An AI-powered beginner project that analyzes a exported PDF profile from LinkedIn using GPT and provides personalized improvement suggestions.

Built as part of my **Daily AI Projects** learning journey.

---

## ✨ Features

✅ Upload LinkedIn profile PDF  
✅ Extract profile text automatically  
✅ Analyze profile with GPT  
✅ Get:

- Profile score (/100)
- Headline suggestions
- About section improvements
- Experience bullet enhancements

---

## 🧠 How It Works

```text
          +----------------------+
          | LinkedIn Profile PDF  |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | PDF Text Extraction   |
          | (pdfplumber)          |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | Prompt Engineering    |
          | + OpenAI GPT Model    |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | AI Profile Feedback   |
          | Scoring + Suggestions |
          +----------------------+
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI API
- pdfplumber
- python-dotenv

---

## 📂 Project Structure

```bash
linkedin-ai-analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sudeepmathew/linkedin-ai-analyzer.git
cd linkedin-ai-analyzer
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Add OpenAI Key

Create `.env`

```bash
OPENAI_API_KEY=your_api_key_here
```

---

## ▶ Run App

```bash
streamlit run app.py
```

Open:

```bash
http://localhost:8501
```

---

## Example Workflow

```text
Upload PDF
   ↓
Extract LinkedIn content
   ↓
Send to GPT
   ↓
Receive:
- Profile Score
- Headline Rewrite
- About Improvements
- Experience Suggestions
```

---

## Example Prompt Used

```python
Act as a LinkedIn profile coach.

Analyze this profile and provide:
1. Profile score
2. Headline improvements
3. About section rewrite
4. Experience bullet enhancements
```

---

## 🔮 Future Enhancements

- Keyword gap analysis
- Resume vs LinkedIn comparison
- Recruiter simulation
- Personal branding score
- Multi-agent profile reviewer

---

## 📸 Screenshot

(Add app screenshot here later)

```bash
![App Screenshot](screenshots/app.png)
```

---

## 📚 Learning Goals

This project was built to learn:

- LLM application development
- Prompt engineering
- Streamlit app building
- PDF parsing
- Git + GitHub workflows

---

## 🧪 Sample Architecture (Future Version)

```text
                    +-------------+
                    | User Upload  |
                    +------+------+
                           |
                 +---------v--------+
                 | Profile Parser    |
                 +---------+--------+
                           |
        +------------------+------------------+
        |                                     |
+-------v--------+                    +-------v--------+
| Scoring Agent  |                    | Rewrite Agent  |
+-------+--------+                    +-------+--------+
        |                                     |
        +------------------+------------------+
                           |
                   +-------v------+
                   | Final Report  |
                   +--------------+
```

---

## 👨‍💻 Author

Built by **Sudeep Mathew** as part of an AI project portfolio.

---

## ⭐ If you like this project

Star the repo and follow my daily AI builds.
