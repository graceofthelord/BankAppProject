import streamlit as st
from current_account import CurrentAccount


st.set_page_config(page_title='BANK APP', layout='centered')

current = CurrentAccount(200000)

with st.form('current_form'):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox('Deposit or Withdraw', ("deposit","withdraw", 'transfer'))
    submit = st.form_submit_button('submit')


if  submit and operations == 'withdraw':
    with st.spinner(' Processing... '):
        if amount > current.balance:
            st.write('Insufficient funds')
        else:
            current.withdraw(amount)
            st.write(f"your balance is {current.balance}")



if  submit and operations == 'deposit':
    with st.spinner(' Processing... '):
            current.deposit(amount)
            st.write(f"your balance is {current.balance}")


