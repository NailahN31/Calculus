import streamlit as st

st.set_page_config(
    page_title="Calculus Animations",
    layout="wide",
    page_icon="📐"
)

st.markdown("<h1 style='text-align:center; color:#FFD580;'>📐 Welcome to Calculus Animations</h1>", unsafe_allow_html=True)

# Animasi kalkulus GIF
calc_gif_url = "https://media.giphy.com/media/l0HlQ7LRalF7wLZgA/giphy.gif"
st.markdown(f"""
<div style='display:flex; justify-content:center;'>
    <img src="{calc_gif_url}" style='width:60%; border-radius:12px; box-shadow:0 0 15px rgba(0,0,0,0.4);'/>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; color:#FFFFFF; font-size:18px;'>
Explore the fascinating world of calculus! Switch to Page 2 to visualize functions and their derivatives interactively.
</p>
""", unsafe_allow_html=True)
