# 🎬 Movie Recommendation System

A personalized movie recommendation system built using **Python, Streamlit, and SVD-based collaborative filtering** to suggest movies based on user preferences.

---

## 🚀 Features

- 🎯 **Personalized Recommendations** using collaborative filtering (SVD)
- 🧠 **User-Item Matrix** for learning user behavior
- ❄️ **Cold-Start Handling** for new users (trending movies fallback)
- 📊 **Real-Time Recommendations** with interactive Streamlit UI
- 🎬 **Netflix-style Layout** for better user experience

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **NumPy / Pandas** (Data Processing)
- **SVD (Matrix Factorization)** for recommendations

---

## 📂 Project Structure


movie-recommendation/
│
├── app.py # Streamlit UI
├── model.py # Data loading, matrix creation, model training
├── requirements.txt


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone [https://github.com/your-username/movie-recommendation.git](https://github.com/mouktikzz/Movie-Recommendation-System/)
2️⃣ Create virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
