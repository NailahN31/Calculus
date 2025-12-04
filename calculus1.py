import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Function & Derivative Plotter",
    layout="wide",
    page_icon="📈",
)

st.markdown("""
<style>
    .big-title {
        font-size: 40px !important;
        font-weight: 700;
        text-align: center;
        color: #4FC3F7;
    }
    .sub-box {
        background: rgba(255,255,255,0.07);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)
st.write("Enter a mathematical function, then view the graph of the function and its derivative directly!")

with st.sidebar:
    st.header("⚙ Settings")
    function_text = st.text_input(
        "Put the function f(x):",
        value="x**2",
        help="Contoh: sin(x), exp(x), x**3 - 2*x"
    )

    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)

    num_points = st.slider("Jumlah titik (resolusi)", 200, 2000, 500)

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

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("📘 Graph Function f(x)")
        fig1, ax1 = plt.subplots()
        ax1.plot(x_vals, y_vals, label="f(x)")
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        st.pyplot(fig1)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("📕 Graph Derivative f'(x)")
        fig2, ax2 = plt.subplots()
        ax2.plot(x_vals, dy_vals, label="f'(x)")
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        st.pyplot(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error("⚠ Terjadi kesalahan saat memproses fungsi. Periksa kembali input Anda.")
    st.error(str(e))
