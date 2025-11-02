import streamlit as st
import pandas as pd
import io
import logging
from src.recommender import HybridRecommender

# =======================
# Configurações iniciais
# =======================
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.title("🎥 Sistema de Recomendação de Filmes (Híbrido)")
st.markdown("Escolha suas preferências e veja recomendações personalizadas!")

# =======================
# Captura de logs em tempo real
# =======================
log_stream = io.StringIO()
handler = logging.StreamHandler(log_stream)
handler.setLevel(logging.DEBUG)

for h in logging.root.handlers[:]:
    logging.root.removeHandler(h)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[handler],
)

# =======================
# Entradas do usuário
# =======================
genre = st.selectbox(
    "🎭 Selecione o gênero preferido:",
    ["Action", "Comedy", "Drama", "Romance", "Thriller", "Sci-Fi", "Horror", "Animation"]
)

rating_min = st.slider("⭐ Nota mínima média (0 a 5)", 0.0, 5.0, 3.5, 0.1)
popularity = st.slider("🔥 Popularidade mínima (número de avaliações)", 0, 500, 50)

# =======================
# Painel lateral de logs
# =======================
st.sidebar.header("🧾 Logs do Sistema")
log_box = st.sidebar.empty()

# =======================
# Estado do botão e resultados
# =======================
if "processing" not in st.session_state:
    st.session_state.processing = False
if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

button_placeholder = st.empty()  # Placeholder para botão/spinner

# =======================
# Função para gerar recomendações
# =======================
def generate_recommendations():
    st.session_state.processing = True
    button_placeholder.button("🔄 Gerando...", disabled=True)
    
    try:
        recommender = HybridRecommender()
        recommendations = recommender.get_recommendations(genre, popularity, rating_min)
        st.session_state.recommendations = recommendations

        # Atualiza logs
        log_box.text(log_stream.getvalue())

    except Exception as e:
        logging.exception("Erro ao gerar recomendações:")
        log_box.text(log_stream.getvalue())
        st.error(f"❌ Ocorreu um erro: {e}")

    finally:
        st.session_state.processing = False

# =======================
# Botão com efeito de spinner
# =======================
if st.session_state.processing:
    button_placeholder.button("🔄 Gerando...", disabled=True)
else:
    if button_placeholder.button("Gerar Recomendações"):
        generate_recommendations()

# =======================
# Mostra recomendações se existirem
# =======================
if st.session_state.recommendations is not None:
    recommendations = st.session_state.recommendations
    if recommendations.empty:
        st.warning("⚠️ Nenhum filme encontrado com os filtros selecionados.")
    else:
        st.success("✅ Recomendações geradas com sucesso!")
        for _, row in recommendations.iterrows():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(f"**🎬 {row['title']}**")
            with cols[1]:
                st.markdown(f"⭐ {row['score']:.2f}")

# =======================
# Atualiza logs no sidebar sempre
# =======================
log_box.text(log_stream.getvalue())
