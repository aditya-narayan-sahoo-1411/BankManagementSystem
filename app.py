
import streamlit as st
from bank import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)

st.markdown(
"""
<style>
div.stButton > button{
    width:100%;
    border-radius:10px;
}
</style>
""",
unsafe_allow_html=True
)

user = Bank()

st.title("🏦 Bank Management System")

option = st.sidebar.selectbox(
    "Choose Option",
    [
        "➕ Create Account",
        "💰 Deposit Money",
        "💸 Withdraw Money",
        "👤 Show Details",
        "✏️ Update Details",
        "🗑 Delete Account"
    ]
)

if option == "➕ Create Account":

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=18,
        value=None,
        placeholder="Enter age"
    )

    email = st.text_input("Email")

    pin = st.text_input(
        "4-digit PIN",
        type="password"
    )

    if st.button("Create Account"):

        result = user.Createaccount(
            name,
            age,
            email,
            pin
        )

        if result["success"]:
            st.success(result["message"])
            st.info(
                f'Account Number: {result["accountNo."]}'
            )
        else:
            st.error(result["message"])


elif option == "💰 Deposit Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):

        result = user.depositmoney(acc, pin, amount)

        if result["success"]:
            st.success(result["message"])
            st.metric("Balance", f'₹{result["balance"]}')
        else:
            st.error(result["message"])


elif option == "💸 Withdraw Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):

        result = user.withdrawmoney(acc, pin, amount)

        if result["success"]:
            st.success(result["message"])
            st.metric("Balance", f'₹{result["balance"]}')
        else:
            st.error(result["message"])


elif option == "👤 Show Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        result = user.showdetails(acc, pin)

        if result["success"]:

            data = result["data"]

            st.subheader("Account Details")

            st.write("👤 Name :", data["name"])
            st.write("📧 Email :", data["email"])
            st.write("🎂 Age :", data["age"])
            st.write("🏦 Account No :", data["accountNo."])

            st.metric(
                "Current Balance",
                f'₹{data["balance"]}'
            )

        else:
            st.error(result["message"])


elif option == "✏️ Update Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN", type="password")

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


elif option == "🗑 Delete Account":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):

        result = user.Delete(acc, pin)

        if result["success"]:
            st.success(result["message"])
        else:
            st.error(result["message"])

