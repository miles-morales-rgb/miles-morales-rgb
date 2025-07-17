
# AI Mini Projects Hub

This project is a collection of beginner-friendly AI mini tools.  
It combines frontend (HTML, CSS, JavaScript) with a backend using Python (Flask).

---

## ✨ Included Projects:
- ✅ Sentiment Analysis (Text)
- ✅ Resume Screening (Keyword Matching)
- ✅ Image Colorization (UI Only – Backend not implemented here)

---

## 📁 Project Structure:

ai-mini-projects/

├── frontend/ → Contains HTML, CSS, JavaScript files

│ └── index.html

├── backend/ → Contains Python Flask server files

│ ├── server.py

│ └── requirements.txt

└── README.md 

---

## 🚀 How to Set Up Locally

### 1️⃣ Clone This Repository:

```bash
git clone https://github.com/miles-morales-rgb/ai-mini-projects.git
cd ai-mini-projects
```

### 2️⃣ Run the Backend (Python Flask)
Make sure Python is installed on your system.
```bash
cd backend
pip install -r requirements.txt
python server.py
```
- The backend will run at:
```bash
http://127.0.0.1:5000
```
### 3️⃣ Open the Frontend
Go to frontend folder and open index.html in your browser:
- Windows: Double-click index.html
- Mac/Linux: Right-click → Open With → Your Browser
---

### ⚙️ How It Works:
- HTML/JS sends requests to Flask backend (for example, Sentiment Analysis).
- Flask processes and sends back JSON response.
- UI updates with the result.
---

### ✅ Technologies Used:
- Frontend: HTML, CSS, JavaScript (Fetch API)
- Backend: Python, Flask, Flask-CORS, TextBlob
- AI/NLP: TextBlob for Sentiment Analysis
---

### 📢 Notes:
- Image Colorization is UI Only here. You’ll need to connect it to a Python model if required.
- You can deploy frontend separately using GitHub Pages, Vercel, or Netlify.
- Backend can be deployed using platforms like Render, Railway, or PythonAnywhere.
---

### 🤝 Contributions :
- Feel free to fork, improve, or suggest features.
---

### 📄 License:
Open-source project for educational purposes.
