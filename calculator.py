import streamlit as st

# ==============================
# Calculator Functions (Modular)
# ==============================
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate(a, b, op):
    """Perform calculation based on operation symbol."""
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Invalid operation!"


# ==============================
# Streamlit App
# ==============================
st.title("🧮 Modular  Calculator")

# Session state to handle restart/quit
if "restart" not in st.session_state:
    st.session_state.restart = True
if "quit" not in st.session_state:
    st.session_state.quit = False

# Main calculator logic
if st.session_state.restart and not st.session_state.quit:
    st.subheader("Enter Your Calculation")

    # 1. Accept two numbers
    num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
    num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

    # 2. Accept operation
    operation = st.selectbox("Choose Operation", ["+", "-", "*", "/"])

    # 3. Perform calculation
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result}")

        # 5. Ask user to Quit or Restart
        choice = st.radio("Do you want to quit?", ["No", "Yes"], index=0)
        if choice == "Yes":
            st.session_state.quit = True
        else:
            st.session_state.restart = True

elif st.session_state.quit:
    st.warning("Calculator program terminated. ✅")
    if st.button("Restart"):
        st.session_state.quit = False
        st.session_state.restart = True
