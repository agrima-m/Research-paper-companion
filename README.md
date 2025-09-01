# 📄 AI Research Paper Companion

An intelligent assistant built with **CrewAI** that helps researchers analyze academic papers.  
Upload a PDF and let the AI do the rest — extracting explanations, summarizing literature, and identifying research gaps.  

---

## 🚀 Features
- 📥 Upload and process research papers (PDFs)  
- 🧑‍💻 Multi-agent system powered by **CrewAI**  
- 📚 Extracts key insights and literature references  
- 🔍 Identifies research gaps and opportunities  
- 🖥️ Simple **Streamlit UI** for easy interaction  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- [CrewAI](https://github.com/joaomdmoura/crewai) – Multi-agent orchestration  
- [CrewAI Tools](https://pypi.org/project/crewai-tools/) – PDF processing utilities  
- [Streamlit](https://streamlit.io/) – Interactive UI  
- [dotenv](https://pypi.org/project/python-dotenv/) – API key management  

---

## 📂 Project Structure
├── agents.py # Defines AI agents (explainer, literature agent, gap analyzer) <br>
├── tasks.py # Research analysis tasks <br>
├── main.py # Runs CrewAI pipeline <br>
├── ui_app.py # Streamlit UI <br>
├── requirements.txt # Dependencies <br>
├── .env # Store your OpenAI API key <br>
└── README.md # Project documentation 

## ⚙️ Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/your-username/research-paper-companion.git
cd research-paper-companion

2. Create & activate virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Add your OpenAI API Key
Create a .env file in the root folder:
OPENAI_API_KEY=your_api_key_here

5. Run the Streamlit app
streamlit run ui_app.py

📌 Usage
Upload a research paper (PDF)
Click Analyze Paper
View extracted insights, literature summary, and research gaps

📜 License
This project is licensed under the MIT License.
