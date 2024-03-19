import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Define the path for the CSV file
data_file = 'data/expenses.csv'

# Load existing data if available
if os.path.exists(data_file):
    expenses = pd.read_csv(data_file)
    
else:
    expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
    
def display_Table(df):
    # 5 columns: NO, Date, Category, Amount, Description
    # TODO
    pass
    
        
# Function to save data to CSV
def save_data(frame):
    frame.to_csv(data_file, index=False)

def display_Report():
    st.write('Expenses Recorded:')
    # Display table
    # TODO
    # Expander
    # TODO
        

    
def display_Chart():
    # Display pie chart of expenses by category
    pass


# Streamlit UI
st.title('Expense Tracker')

# Input form
with st.form('expense_form', clear_on_submit=True):
    date = st.date_input('Date')
    category = st.selectbox('Category', ['🍱Food', '🚗Transport', '🧽Utilities', '🎳Entertainment', '🎈Others'])
    amount = st.number_input('Amount', min_value=0.0, format='%f')
    description = st.text_area('Description')
    submitted = st.form_submit_button('Submit')
    if description == '':
        description = '-'

    if submitted:
        # Append new expense
        new_expense = pd.DataFrame([[date, category, amount, description]], columns=['Date', 'Category', 'Amount', 'Description'])
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
        save_data(expenses)
        st.success('Expense added successfully!')

# Show data table
table, chart = st.tabs(['Table', 'Chart'])
with table:
    display_Report()
with chart:
    display_Chart()