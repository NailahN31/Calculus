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
    function_text = st.text_input("Enter function f(x):", value="x**2")  # <-- perbaikan typo
    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)
    num_points = st.slider("Number of points", 200, 2000, 500)
    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

# --- Colors ---
sidebar_bg = "#4682B4"
text_color = "#FFFFFF"
box_bg = "rgba(40, 40, 60, 0.6)"
grid_color = "#E0E0E0"

# Pastel gradient colors
cmap_func = LinearSegmentedColormap.from_list("pastel_func", ["#FFD580", "#FFE4B2"])
cmap_deriv = LinearSegmentedColormap.from_list("pastel_deriv", ["#FF9AA2", "#FFB3C1"])

# --- CSS for dark theme + flower bg + pattern overlay ---
st.markdown(f"""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {{
    background-image: 
        url("https://i.ibb.co/3yq9p0Y/pastel-flower.jpg"), /* main bunga */
        url("https://i.ibb.co/TMbJghC/pastel-stars.png");  /* pattern overlay */
    background-size: cover, contain;
    background-position: center, top right;
    background-repeat: no-repeat, repeat;
    background-attachment: fixed;
    background-color: rgba(95, 158, 160, 0.7); /* overlay semi-transparent */
    background-blend-mode: overlay;
    color: {text_color};
}}

/* Sidebar background dan teks */
[data-testid="stSidebar"] > div:first-child {{
    background-color: {sidebar_bg};
    color: {text_color};
    padding: 15px;
}}
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
            ax1.plot(x_vals, y_vals, color="#FFD580", linewidth=3, alpha=0.8)
            ax1.grid(True, color=grid_color, alpha=0.5, linestyle="--")
            ax1.set_facecolor('none')
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color="#FF9AA2", linewidth=3, alpha=0.8)
            ax2.grid(True, color=grid_color, alpha=0.5, linestyle="--")
            ax2.set_facecolor('none')
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("3D Plot of f(x) & f'(x)")

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Gradient pastel line for f(x)
        for i in range(len(x_vals)-1):
            ax.plot3D(x_vals[i:i+2], y_vals[i:i+2], [0,0],
                      color=cmap_func(i/len(x_vals)), linewidth=3, alpha=0.8)
        # Gradient pastel line for f'(x)
        for i in range(len(x_vals)-1):
            ax.plot3D(x_vals[i:i+2], dy_vals[i:i+2], [1,1],
                      color=cmap_deriv(i/len(x_vals)), linewidth=3, alpha=0.8)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("curve id")
        ax.view_init(elev=25, azim=45)
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error("Error processing the function.")
    st.error(str(e))
