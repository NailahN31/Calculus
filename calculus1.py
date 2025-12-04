import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.markdown("""
<style>

/* ===== LIGHT BLUE BACKGROUND ===== */
body {
    background: linear-gradient(135deg, #b3e5fc, #e1f5fe, #bbdefb) !important;
}

/* Main container transparan */
.main {
    background: transparent;
}

/* Title style */
.big-title {
    font-size: 42px !important;
    font-weight: 800;
    text-align: center;
    color: #0a2a43;  /* dark blue untuk kontras */
    padding-top: 10px;
    text-shadow: 0px 0px 10px rgba(255,255,255,0.6);
}

/* Glassmorphism box */
.sub-box {
    background: rgba(255,255,255,0.35);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.45);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 0 25px rgba(0,0,0,0.15);
}

/* Sidebar glass */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.40) !important;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,0.6);
    box-shadow: 4px 0 25px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)


