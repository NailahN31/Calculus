import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

# --- Page config ---
st.set_page_config(
    page_title="Function & Derivative Plotter",
    layout="wide",
    page_icon="📈"
)

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    function_text = st.text_inpu
