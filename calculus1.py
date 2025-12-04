import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # penting untuk 3D



plt.style.use("dark_background")

COLOR_FUNC = "#4FC3F7"    # neon blue
COLOR_DERIV = "#FF8A65"   # neon orange

st.set_page_config(
    page_title="Function & Derivative Plotter",
    layout="wide",
    page_icon="📈",
)

# ==== CUSTOM BACKGROUND + GLASSMORPHISM (LIGHT BLUE) ====
st.markdown("""
<style>

/* 🌤 BACKGROUND BIRU MUDA */
body {
    background: linear-gradient(135deg, #b3e5fc, #e1f5fe, #bbdefb) !important;
}

/* Transparan untuk container utama */
.main {
    background: transparent;
}

/* Judul */
.big-title {
    font-size: 42px !important;
    font-weight: 800;
    text-align: center;
    color: #0a2a43; /* biru gelap */
    padding-top: 10px;
    text-shadow: 0px 0px 12px rgba(255,255,255,0.7);
}

/* Glass effect boxes */
.sub-box {
    background: rgba(255,255,255,0.35);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.50);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 0 25px rgba(0,0,0,0.15);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.40) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.6);
    box-shadow: 4px 0 25px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

body {
    background: linear-gradient(145deg, #0f2027, #203a43, #2c5364) !important;
}
.main {
    background: transparent;
}
.big-title {
    font-size: 42px !important;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    padding-top: 10px;
    text-shadow: 0px 0px 15px rgba(0,0,0,0.6);
}
.sub-box {
    background: rgba(255,255,255,0.10);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.25);
    backdrop-filter: blur(14px);
    box-shadow: 0 0 25px rgba(0,0,0,0.25);
}
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.10) !important;
    backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255,255,255,0.2);
    box-shadow: 4px 0 25px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙ Settings")
    function_text = st.text_input("Put the function f(x):", value="x**2")

    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)

    num_points = st.slider("Number of points", 200, 2000, 500)

    plot_mode = st.radio("Plot Mode:", ["2D", "3D"])

x = sp.symbols("x")

try:
    func = sp.sympify(function_text)
    derivative = sp.diff(func, x)

    st.markdown("### 🧮 Symbolic derivative f'(x)")
    st.latex(sp.latex(derivative))

    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    # -------------------------
    #        MODE 2D
    # -------------------------
    if plot_mode == "2D":
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("📘 Graph Function f(x)")
            fig1, ax1 = plt.subplots()
            ax1.plot(x_vals, y_vals, color=COLOR_FUNC, linewidth=2.5)
            ax1.grid(True, alpha=0.3)
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("📕 Graph Derivative f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color=COLOR_DERIV, linewidth=2.5)
            ax2.grid(True, alpha=0.3)
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------
    #        MODE 3D
    # -------------------------
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("🌐 3D Plot of f(x) & f'(x)")

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        # 3D curves
        ax.plot3D(x_vals, y_vals, np.zeros_like(x_vals), color=COLOR_FUNC, linewidth=2.5, label="f(x)")
        ax.plot3D(x_vals, dy_vals, np.ones_like(x_vals), color=COLOR_DERIV, linewidth=2.5, label="f'(x)")

        # Labeling
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("curve id")

        ax.view_init(elev=25, azim=45)  # sudut kamera 3D
        ax.legend()

        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error("⚠ Error processing the function.")
    st.error(str(e))



