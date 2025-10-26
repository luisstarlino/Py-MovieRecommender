import streamlit as st
import pandas as pd
from src.recommender import HybridRecommender

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.title("🎥 Sistema de Recomendação de Filmes (Híbrido)")
st.markdown("Escolha suas preferências e veja recomendações personalizadas!")

genre = st.selectbox("Selecione o gênero preferido:", 
                     ["Action", "Comedy", "Drama", "Romance", "Thriller", "Sci-Fi", "Horror", "Animation"])

age_group = st.selectbox("Faixa etária:", 
                         ["18-25", "26-35", "36-50", "50+"])

popularity = st.slider("Popularidade mínima", 0, 100, 50)

if st.button("Gerar Recomendações"):
    st.info("🔄 Gerando recomendações...")

    recommender = HybridRecommender()
    recommendations = recommender.get_recommendations(genre, popularity)

    st.success("✅ Recomendações geradas com sucesso!")
    for _, row in recommendations.iterrows():
        st.markdown(f"**🎬 {row['title']}** — ⭐ {row['score']:.2f}")
