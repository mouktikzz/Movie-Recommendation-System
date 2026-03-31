import streamlit as st
from model import load_data, create_matrix, train_model, recommend_svd 

# Page config (wide layout like Netflix)
st.set_page_config(layout="wide")

st.title("🎬 Movie Recommendation System")
st.markdown("## 🍿 Your Personalized Picks")
st.divider()

# Load data and model
data = load_data()
user_item = create_matrix(data)
reconstructed = train_model(user_item)

# User input
user_id = st.number_input("Enter User ID", min_value=1, step=1)

# Button click
if st.button("Recommend"):

    # New user handling
    if user_id not in user_item.index:
        st.warning("New user detected! Showing trending movies 🔥")

        top_movies = (
            data.groupby('title')['rating']
            .mean()
            .sort_values(ascending=False)
            .head(5)
        )

        cols = st.columns(5)
        for i, movie in enumerate(top_movies.index):
            with cols[i]:
                st.markdown(f"### 🎬 {movie}")
                st.caption("🔥 Popular choice")
    
    else:
        # Get recommendations
        recs = recommend_svd(user_id, user_item, reconstructed)

        st.subheader("🔥 Top Recommendations")

        # Create Netflix-style horizontal layout
        cols = st.columns(len(recs))

        for i, movie in enumerate(recs):
            with cols[i]:
                st.markdown(f"### 🎬 {movie}")
                st.caption("⭐ Recommended for you")
                st.caption("💡 Based on your preferences")
