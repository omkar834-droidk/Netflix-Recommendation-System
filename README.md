# Netflix-Recommendation-System
 Machine Learning project using NLP


# 🎬 Netflix Movie Recommendation System

## 📌 Project Overview

The Netflix Movie Recommendation System is designed to suggest movies to users based on similarity and content features.

This project uses Natural Language Processing (NLP) and Machine Learning techniques to recommend movies based on:

- Genre
- Cast
- Director
- Movie Description
- Keywords

The system analyzes movie metadata and suggests similar movies using cosine similarity.

---

## 🎯 Objectives

- Clean and preprocess movie dataset
- Perform text feature extraction using NLP techniques
- Build content-based recommendation system
- Recommend top similar movies based on user input
- Deploy using Streamlit (Optional)

---

## 🧠 Approach

1. Data Cleaning & Preprocessing  
2. Combine important text features (genre, cast, overview)  
3. Apply TF-IDF / Count Vectorizer  
4. Compute Cosine Similarity  
5. Recommend Top 5 Similar Movies  

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit (for deployment)
- Plotly (for visualization)

---

## 📂 Project Structure






📁 Netflix-Movie-Recommendation
## 📁 Project Structure

```
Netflix-Movie-Recommendation/
│
├── data/
│   └── netflix_movies.csv
│
├── notebooks/
│   └── model_building.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```



---

## 📊 Recommendation Logic

- Convert text data into numerical vectors using TF-IDF
- Calculate cosine similarity between movies
- Return top 5 most similar movies

---

## 🚀 Features

- Search movie by name
- Get top 5 similar movie recommendations
- Clean user interface
- Interactive dashboard

---

## 🔮 Future Enhancements

- Collaborative Filtering
- Hybrid Recommendation System
- Deep Learning based recommendation
- Personalized user recommendation

---

## 👨‍💻 Author

Omkar Salunke  
Aspiring Data Scientist | NLP & Recommendation Systems Enthusiast
