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

# --- SIDEBAR ---
with st.sidebar:
    st.header("Settings")
    mode = st.radio("Theme:", ["Light", "Dark"])
    function_text = st.text_input("Enter function f(x):", value="x**2")
    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)
    num_points = st.slider("Number of points", 200, 2000, 500)
    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

# --- Set CSS berdasarkan mode ---
if mode == "Light":
    bg_color = "#E0FFFF"  # beige
    text_color = "#333333"
    box_bg = "rgba(255, 255, 255, 0.6)"
    grid_color = "gray"
else:  # Dark mode
    bg_color = "#191970"
    text_color = "#f0f0f0"
    box_bg = "rgba(40, 40, 60, 0.6)"
    grid_color = "white"

st.markdown(f"""
<style>
body {{
    background-color: {bg_color} !important;
}}
.main {{
    background: transparent;
}}
.big-title {{
    font-size: 36px !important;
    font-weight: 700;
    text-align: center;
    color: {text_color};
    margin-bottom: 20px;
}}
.sub-box {{
    background: {box_bg};
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(200, 200, 200, 0.4);
}}
[data-testid="stSidebar"] {{
    background-color: #fff !important;
    padding: 15px;
    border-radius: 8px;
}}
</style>
""", unsafe_allow_html=True)

# --- Judul ---
st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

# --- Simbolik dan numerik ---
x = sp.symbols("x")

try:
    func = sp.sympify(function_text)
    derivative = sp.diff(func, x)

    # Tampilkan turunan simbolik
    st.markdown("### Symbolic derivative f'(x)")
    st.latex(sp.latex(derivative))

    # Fungsi numerik
    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    # --- Warna plot berdasarkan mode ---
    color_func = "#4FC3F7" if mode == "Light" else "#00ffff"
    color_deriv = "#FF8A65" if mode == "Light" else "#ff6f61"

    # --- Plot 2D ---
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

    # --- Plot 3D ---
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

