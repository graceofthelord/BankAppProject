import streamlit as st
from savings_account import SavingsAccount


st.set_page_config(page_title='BANK APP', layout='centered')

savings = SavingsAccount(200000)

with st.form('savings_form'):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox('Deposit or Withdraw', ("deposit","withdraw", 'transfer'))
    submit = st.form_submit_button('submit')


if  submit and operations == 'withdraw':
    with st.spinner(' Processing... '):
        if amount <= 10000 :
            savings.withdraw(amount)
            st.write(f"your balance is {savings.balance}")
        elif amount > savings.balance:
            st.write('Insufficient funds')

        else:
            st.write("sorry, you've exceeded your limit.")



if  submit and operations == 'deposit':
    with st.spinner(' Processing... '):
            savings.deposit(amount)
            st.write(f"your balance is {savings.balance}")
