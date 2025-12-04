import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # penting untuk 3D

# --- Konfigurasi halaman ---
st.set_page_config(
    page_title="Function & Derivative Plotter",
    layout="wide",
    page_icon="📈"
)

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    mode = st.radio("Theme:", ["Light", "Dark"])
    function_text = st.text_input("Enter function f(x):", value="x**2")
    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)
    num_points = st.slider("Number of points", 200, 2000, 500)
    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

# --- Warna dan style berdasarkan mode ---
if mode == "Light":
    bg_color = "#f5f5dc"  # beige
    text_color = "#333333"
    box_bg = "rgba(255, 255, 255, 0.6)"
    gr
