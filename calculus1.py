import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Page config ---
st.set_page_config(
    page_title="Function & Derivative Plotter",
    layout="wide",
    page_icon="📈"
)

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    function_text = st.text_input("Enter function f(x):", value="x**2")
    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)
    num_points = st.slider("Number of points", 200, 2000, 500)
    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

# --- Colors ---
bg_color = "#5F9EA0"            # main background
sidebar_bg = "#4682B4"          # sidebar background
text_color = "#FFFFFF"           # teks putih
box_bg = "rgba(40, 40, 60, 0.6)" # box plot background
grid_color = "#E0E0E0"           # light gray grid
color_func = "#FFD580"           # pastel yellow
color_deriv = "#FF9AA2"          # pastel pink

# --- CSS for dark theme ---
st.markdown(f"""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {{
    background-color: {bg_color};
    color: {text_color};
}}

/* Sidebar background dan teks */
[data-testid="stSidebar"] > div:first-child {{
    background-color: {sidebar_bg};
    color: {text_color};
    padding: 15px;
}}

/* Semua teks sidebar */
[data-testid="stSidebar"] * {{
    color: {text_color} !important;
}}

/* Title */
.big-title {{
    font-size: 36px !important;
    font-weight: 700;
    text-align: center;
    color: {text_color};
    margin-bottom: 20px;
}}

/* Box plot */
.sub-box {{
    background: {box_bg};
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(200, 200, 200, 0.4);
}}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

# --- Symbolic & numeric calculations ---
x = sp.symbols("x")

try:
    func = sp.sympify(function_text)
    derivative = sp.diff(func, x)

    st.markdown("### Symbolic derivative f'(x)")
    st.latex(sp.latex(derivative))

    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    if plot_mode == "2D":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f(x)")
            fig1, ax1 = plt.subplots()
            ax1.plot(x_vals, y_vals, color=color_func, linewidth=3, alpha=0.8)
            ax1.grid(True, color=grid_color, alpha=0.5, linestyle="--")
            ax1.set_facecolor('none')
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color=color_deriv, linewidth=3, alpha=0.8)
            ax2.grid(True, color=grid_color, alpha=0.5, linestyle="--")
            ax2.set_facecolor('none')
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("3D Plot of f(x) & f'(x)")
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x_vals, y_vals, np.zeros_like(x_vals), color=color_func, linewidth=3, label="f(x)", alpha=0.8)
        ax.plot3D(x_vals, dy_vals, np.ones_like(x_vals), color=color_deriv, linewidth=3, label="f'(x)", alpha=0.8)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("curve id")
        ax.view_init(elev=25, azim=45)
        ax.legend()
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error("Error processing the function.")
    st.error(str(e))
