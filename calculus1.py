import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from matplotlib.colors import LinearSegmentedColormap

st.set_page_config(
    page_title="Enhanced Function & Derivative Visualizer",
    layout="wide",
    page_icon="📈"
)

sidebar_bg = "#4682B4"
text_color = "#FFFFFF"
box_bg_rgba = "rgba(219, 112, 147, 0.8)"  # #DB7093 with opacity
border_color_rgba = "rgba(219, 112, 147, 0.9)"
grid_color = "#E0E0E0"

gif_kucing_url = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"

# Sidebar input
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; height:100%;">
        <div>
            <h2 style="color:{text_color};">Settings</h2>
            Function: <br>
            <input type="text" value="x**3 - 3*x" id="func_input" style="width:100%; margin-bottom:10px;">
            Range Min: <input type="number" value="-5" id="range_min" style="width:100%; margin-bottom:10px;"><br>
            Range Max: <input type="number" value="5" id="range_max" style="width:100%; margin-bottom:10px;"><br>
            Number of points: <input type="range" min="200" max="2000" value="500" style="width:100%; margin-bottom:10px;"><br>
            Plot Mode: <select style="width:100%; margin-bottom:10px;">
                <option>2D</option>
                <option>3D</option>
            </select>
        </div>
        <div style="margin-top:auto; text-align:center;">
            <img src="{gif_kucing_url}" style="width:150px; border-radius:12px; box-shadow:0 0 12px rgba(255,255,255,0.6);" alt="Cat GIF">
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main background style
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://i.ibb.co/3yq9p0Y/pastel-flower.jpg"),
                      url("https://i.ibb.co/TMbJghC/pastel-stars.png");
    background-size: cover, contain;
    background-position: center, top right;
    background-repeat: no-repeat, repeat;
    background-attachment: fixed;
    background-color: rgba(95, 158, 160, 0.7);
    background-blend-mode: overlay;
    color: {text_color};
}}
.sub-box {{
    background: {box_bg_rgba};
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid {border_color_rgba};
}}
.big-title {{
    font-size: 36px !important;
    font-weight: 700;
    text-align: center;
    color: {text_color};
    margin-bottom: 20px;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📈 Enhanced Function & Derivative Visualizer</div>", unsafe_allow_html=True)

# --- Fungsi Matematika ---
x = sp.symbols("x")
function_text = "x**3 - 3*x"
range_min = -5
range_max = 5
num_points = 500
plot_mode = "2D"

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

    critical_points = sp.solve(derivative, x)
    critical_points = [p.evalf() for p in critical_points if p.is_real]
    max_points, min_points = [], []
    for p in critical_points:
        sd = second_derivative.subs(x, p)
        if sd < 0:
            max_points.append(p)
        elif sd > 0:
            min_points.append(p)

    if plot_mode == "2D":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f(x) with Critical Points")
            fig1, ax1 = plt.subplots()
            ax1.plot(x_vals, y_vals, color="#FFD580", linewidth=3, alpha=0.8)
            ax1.scatter([float(p) for p in max_points], [f_num(float(p)) for p in max_points],
                        color='red', label='Maxima', zorder=5)
            ax1.scatter([float(p) for p in min_points], [f_num(float(p)) for p in min_points],
                        color='green', label='Minima', zorder=5)
            ax1.grid(True, color=grid_color, alpha=0.5, linestyle="--")
            ax1.legend()
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
