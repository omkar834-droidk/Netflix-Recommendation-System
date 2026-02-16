import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Aurora Recommender AI",
    page_icon="🎬",
    layout="wide"
)

# ------------------------------------------------
# CLEAN MINIMAL CSS (SMALL CARDS)
# ------------------------------------------------
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}

/* HEADER */
.brand-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.brand-sub {
    font-size: 18px;
    color: #e0e0e0;
    margin-bottom: 8px;
}

.brand-author {
    font-size: 13px;
    color: #cccccc;
    margin-bottom: 40px;
}

/* SMALL CARD */
.card {
    background: rgba(255,255,255,0.12);
    padding: 18px;
    border-radius: 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.08);

    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;
    margin-bottom: 25px;
    transition: 0.2s ease-in-out;
}

.card:hover {
    transform: translateY(-4px);
}

.card h4 {
    margin: 0;
    font-size: 15px;
    font-weight: 600;
}

.similarity {
    font-size: 12px;
    color: #00FFB2;
    margin-top: 8px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    color: white;
    font-weight: 600;
    border-radius: 25px;
    height: 42px;
    width: 100%;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
df = pickle.load(open("df.pkl", "rb"))
tfidf_matrix = pickle.load(open("tidf_matrix.pkl", "rb"))
indices = pickle.load(open("movie_indices.pkl", "rb"))

# ------------------------------------------------
# SAFE INDEX
# ------------------------------------------------
def _get_single_index(idx):
    if isinstance(idx, (list, tuple, np.ndarray, pd.Series)):
        return int(idx[0])
    return int(idx)

# ------------------------------------------------
# RECOMMEND FUNCTION
# ------------------------------------------------
def recommend(title, n=9):
    if title not in indices:
        return []

    idx = _get_single_index(indices[title])

    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    sorted_idx = np.argsort(sim_scores)[::-1]
    sorted_idx = sorted_idx[sorted_idx != idx]
    sorted_idx = sorted_idx[:n]

    results = []
    for i in sorted_idx:
        movie_title = df['title'].iloc[i]
        score = round(sim_scores[i] * 100, 2)
        results.append((movie_title, score))

    return results

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.markdown('<div class="brand-title">🎬 Aurora Recommender AI</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">NLP-based Movie Recommendation Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-author">Built by Omkar Salunke</div>', unsafe_allow_html=True)

# ------------------------------------------------
# SEARCH
# ------------------------------------------------
col1, col2 = st.columns([4,1])

with col1:
    selected_movie = st.selectbox(
        "Search your favorite movie",
        df['title'].values
    )

with col2:
    recommend_btn = st.button("Discover")

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------
# RESULTS
# ------------------------------------------------
if recommend_btn:
    with st.spinner("Finding similar movies... 🎥"):
        results = recommend(selected_movie)

    st.markdown("### 🎯 Recommendations")
    st.markdown("<br>", unsafe_allow_html=True)

    if results:
        rows = [results[i:i+3] for i in range(0, len(results), 3)]

        for row in rows:
            cols = st.columns(3, gap="large")
            for col, (movie, score) in zip(cols, row):
                with col:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h4>{movie}</h4>
                            <div class="similarity">
                                {score}% Similar
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    else:
        st.warning("Movie not found in dataset.")
