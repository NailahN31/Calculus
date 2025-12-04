import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.set_page_config(
    page_title="Function & Derivative Visualizer",
    layout="wide",
    page_icon="📈"
)

# =======================
# Sidebar
# =======================
st.sidebar.header("Settings")
function_text = st.sidebar.text_input("Enter function f(x):", value="x**3 - 3*x")
range_min = st.sidebar.number_input("Range Minimum (x)", value=-5)
range_max = st.sidebar.number_input("Range Maximum (x)", value=5)
num_points = st.sidebar.slider("Number of points", 200, 2000, 500)
plot_mode = st.sidebar.radio("Plot Mode:", ["2D", "3D"])

# GIF kucing di bawah sidebar
st.sidebar.markdown(
    """
    <div style="margin-top: 50px; text-align:center;">
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" 
        style="width:150px; border-radius:12px; box-shadow:0 0 12px rgba(255,255,255,0.6);" 
        alt="Cat GIF">
    </div>
    """, unsafe_allow_html=True
)

# =======================
# Main background + title
# =======================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #5F9EA0;
    color: #FFFFFF;
}
.sub-box {
    background: rgba(219,112,147,0.8);
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(219,112,147,0.9);
}
.big-title {
    font-size: 36px !important;
    font-weight: 700;
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

# =======================
# Symbolic Math
# =======================
x = sp.symbols("x")
try:
    func = sp.sympify(function_text)
    derivative = sp.diff(func, x)
    second_derivative = sp.diff(derivative, x)

    st.markdown("### Step-by-step derivative f'(x)")
    st.latex(sp.latex(derivative))

    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    # --------------------------
    # 2D plotting
    # --------------------------
    if plot_mode == "2D":
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f(x)")
            fig1, ax1 = plt.subplots()
            ax1.plot(x_vals, y_vals, color="#FFD580", linewidth=3, alpha=0.8)
            ax1.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color="#FF9AA2", linewidth=3, alpha=0.8)
            ax2.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------
    # 3D plotting
    # --------------------------
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("3D Interactive Curve f(x) & f'(x)")
        z_vals = np.zeros_like(x_vals)
        z_vals2 = np.ones_like(x_vals)

        fig3d = go.Figure()
        fig3d.add_trace(go.Scatter3d(x=x_vals, y=y_vals, z=z_vals, mode='lines',
                                     line=dict(color='lightblue', width=5), name='f(x)'))
        fig3d.add_trace(go.Scatter3d(x=x_vals, y=dy_vals, z=z_vals2, mode='lines',
                                     line=dict(color='pink', width=5), name="f'(x)"))
        fig3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='Curve ID',
                                       bgcolor='rgba(0,0,0,0)'),
                            margin=dict(l=0, r=0, b=0, t=0), height=600)
        st.plotly_chart(fig3d, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error("Error processing the function.")
    st.error(str(e))
