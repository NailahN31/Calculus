import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Title
st.title("Matrix Application: Function & Derivative Plotter")

# User input
function_text = st.text_input(
    "Enter a function of x (examples: x**2, sin(x), exp(x))",
    value="x**2"
)

# Symbolic variable
x = sp.symbols("x")

try:
    # Convert text to symbolic expression
    func = sp.sympify(function_text)

    # Derivative
    derivative = sp.diff(func, x)

    # Show symbolic derivative
    st.subheader("Symbolic derivative f'(x)")
    st.latex(sp.latex(derivative))

    # Prepare numeric functions
    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    # Plot range
    x_vals = np.linspace(-10, 10, 500)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    # Plot function
    st.subheader("Function Plot")
    fig1, ax1 = plt.subplots()
    ax1.plot(x_vals, y_vals, color="blue", label="f(x)")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

    # Plot derivative
    st.subheader("Derivative Plot")
    fig2, ax2 = plt.subplots()
    ax2.plot(x_vals, dy_vals, color="red", label="f'(x)")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

except Exception as e:
    st.error(f"Error: {e}")
