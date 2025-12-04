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
    mode = st.radio("Theme:", ["Light", "Dark"])
    function_text = st.text_input("Enter function f(x):", value="x**2")
    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)
    num_points = st.slider("Number of points", 200, 2000, 500)
    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

# --- Warna dan style berdasarkan mode ---
if mode == "Light":
    bg_color = "#E0FFFF"       # light cyan
    sidebar_bg = "#F0FFFF"     # sedikit lebih terang dari main
    text_color = "#000000"     # teks gelap
    box_bg = "rgba(255, 255, 255, 0.7)"
    grid_color = "gray"
    color_func = "#0077b6"     # biru gelap
    color_deriv = "#d65f5f"    # merah gelap
else:
    bg_color = "#1e1e2f"
    sidebar_bg = "#2c2c44"
    text_color = "#f0f0f0"
    box_bg = "rgba(40, 40, 60, 0.6)"
    grid_color = "white"
    color_func = "#00ffff"
    color_deriv = "#ff6f61"

# --- CSS untuk background, sidebar, judul, box ---
st.markdown(f"""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {{
    background-color: {bg_color};
}}

/* Sidebar background */
[data-testid="stSidebar"] > div:first-child {{
    background-color: {sidebar_bg};
    padding: 15px;
    border-radius: 8px;
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

# --- Judul ---
st.markdown(f"<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

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
            ax1.plot(x_vals, y_vals, color=color_func, linewidth=2)
            ax1.grid(True, color=grid_color, alpha=0.3)
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color=color_deriv, linewidth=2)
            ax2.grid(True, color=grid_color, alpha=0.3)
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("3D Plot of f(x) & f'(x)")
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x_vals, y_vals, np.zeros_like(x_vals), color=color_func, linewidth=2, label="f(x)")
        ax.plot3D(x_vals, dy_vals, np.ones_like(x_vals), color=color_deriv, linewidth=2, label="f'(x)")
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
