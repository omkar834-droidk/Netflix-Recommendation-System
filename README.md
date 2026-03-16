# 🎬 Aurora Recommender AI

### Intelligent Movie Recommendation Engine

---

## 📌 Project Overview

Aurora Recommender AI is a **content-based movie recommendation system** that suggests similar movies based on movie descriptions.
The system uses **Natural Language Processing (NLP)** techniques and **cosine similarity** to analyze movie metadata and recommend relevant content.

Users can instantly discover movies that are similar in theme, storyline, and context through an interactive **Streamlit web application**.

---

## 🚀 Key Features

* Content-Based Movie Recommendation
* TF-IDF Vectorization for text analysis
* Cosine Similarity based recommendation engine
* Real-time recommendation results
* Clean and interactive Streamlit interface
* Similarity score display
* Fully deployed web application

---

## 🛠 Tech Stack

| Category             | Technology           |
| -------------------- | -------------------- |
| Programming Language | Python               |
| Data Processing      | Pandas, NumPy        |
| Machine Learning     | Scikit-learn         |
| NLP Technique        | TF-IDF Vectorization |
| Similarity Algorithm | Cosine Similarity    |
| Web Framework        | Streamlit            |
| Version Control      | Git & GitHub         |

---

## ⚙️ How the System Works

1. Movie dataset is loaded and preprocessed.
2. Movie descriptions are transformed into **TF-IDF vectors**.
3. Cosine similarity is calculated between movies.
4. Similar movies are ranked based on similarity score.
5. Top recommendations are displayed through the Streamlit interface.

---

## 📂 Project Structure

```text id="az0w9q"
Netflix-Recommendation-System
│
├── app.py                # Streamlit web application
├── main.ipynb            # Model development notebook
├── df.pkl                # Processed movie dataset
├── tfidf_matrix.pkl      # TF-IDF feature matrix
├── movie_indices.pkl     # Movie index mapping
├── requirements.txt      # Project dependencies
└── README.md
```

---

## ▶️ Run the Project Locally

Clone the repository

```id="zj0o4m"
git clone https://github.com/omkar834-droidk/Netflix-Recommendation-System.git
cd Netflix-Recommendation-System
```

Install dependencies

```id="1tm1za"
pip install -r requirements.txt
```

Run the application

```id="ikyyum"
streamlit run app.py
```

---

## 🌐 Live Application

https://netflix-recommendation-system-zsf5uvvrasb88ck5v8tf2d.streamlit.app/

---

## 🎯 Future Improvements

* Add movie posters using TMDB API
* Implement hybrid recommendation system
* Add personalized user recommendations
* Integrate transformer-based embeddings (BERT)
* Improve recommendation accuracy

---

## 👨‍💻 Author

**Omkar Salunke**
AI & Data Science Enthusiast

GitHub:
https://github.com/omkar834-droidk

---

## ⭐ Support

If you found this project useful, consider giving it a **star ⭐ on GitHub**.
