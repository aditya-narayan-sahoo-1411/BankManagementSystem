import streamlit as st  # type: ignore[reportMissingImports]
from bank import Bank

user = Bank()

st.title("🏦 Bank Management System")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

# CREATE ACCOUNT
if option == "Create Account":

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN")

    if st.button("Create Account"):
        result = user.Createaccount(name, age, email, pin)

        if result["success"]:
            st.success(result["message"])
            st.write("Account Number:", result["accountNo."])
        else:
            st.error(result["message"])


# DEPOSIT
elif option == "Deposit Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        result = user.depositmoney(acc, pin, amount)

        if result["success"]:
            st.success(result["message"])
            st.write("Balance:", result["balance"])
        else:
            st.error(result["message"])


# WITHDRAW
elif option == "Withdraw Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        result = user.withdrawmoney(acc, pin, amount)

        if result["success"]:
            st.success(result["message"])
            st.write("Balance:", result["balance"])
        else:
            st.error(result["message"])


# SHOW DETAILS
elif option == "Show Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Show"):
        result = user.showdetails(acc, pin)

        if result["success"]:
            st.json(result["data"])
        else:
            st.error(result["message"])


# UPDATE DETAILS
elif option == "Update Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN")

    if st.button("Update"):
        result = user.updatedetails(
            acc,
            pin,
            new_name,
            new_email,
            new_pin
        )

        if result["success"]:
            st.success(result["message"])
        else:
            st.error(result["message"])


# DELETE ACCOUNT
elif option == "Delete Account":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Delete"):
        result = user.Delete(acc, pin)

        if result["success"]:
            st.success(result["message"])
        else:
            st.error(result["message"])