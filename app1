import streamlit as st
from sympy import symbols, Eq, solve

x = symbols('x')

st.title("حل المعادلات")

equation = st.text_input("أدخل المعادلة (مثال: 2*x + 3 - 7)")

if equation:
    try:
        expr = eval(equation)
        solution = solve(expr, x)
        st.write("الحل هو:", solution)
    except:
        st.write("تحقق من الإدخال")
