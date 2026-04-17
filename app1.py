import streamlit as st
from sympy import symbols, Eq, solve, sympify, solveset, S

# -----------------------------
# CONFIGURATION
# -----------------------------
st.set_page_config(page_title="Solveur Mathématique", page_icon="📘", layout="centered")

x = symbols('x')

st.title("📘 Application éducative : Équations & Inéquations")
st.write("Outil interactif pour aider les élèves à comprendre la résolution.")

# -----------------------------
# CHOIX TYPE
# -----------------------------
choice = st.radio("Choisir le type :", ["Équation", "Inéquation"])

# -----------------------------
# INPUT
# -----------------------------
expr_input = st.text_input("✍️ Entrer l'expression (ex: 2*x + 3 - 7)")

# -----------------------------
# FONCTION EXPLICATION SIMPLE
# -----------------------------
def explain_equation(expr):
    st.subheader("🧠 Explication (simplifiée)")
    st.write("On cherche à isoler x dans l'équation.")

# -----------------------------
# CAS ÉQUATION
# -----------------------------
if choice == "Équation" and expr_input:
    try:
        expr = sympify(expr_input)
        solution = solve(expr, x)

        st.success("✔️ Équation résolue")

        explain_equation(expr)

        st.subheader("📌 Solution")
        st.write(solution)

    except:
        st.error("❌ Vérifie la syntaxe de ton équation")

# -----------------------------
# CAS INÉQUATION
# -----------------------------
elif choice == "Inéquation" and expr_input:
    try:
        expr = sympify(expr_input)

        solution = solveset(expr, x, domain=S.Reals)

        st.success("✔️ Inéquation résolue")

        st.subheader("🧠 Remarque importante")
        st.write("Pour les inéquations, le signe peut changer lorsqu'on multiplie/divise par un nombre négatif.")

        st.subheader("📌 Solution")
        st.write(solution)

    except:
        st.error("❌ Vérifie la syntaxe de ton inéquation")

# -----------------------------
# FOOTER PEDAGOGIQUE
# -----------------------------
st.markdown("---")
st.caption("Application pédagogique - Enseignement des mathématiques avec technologie éducative")
