import streamlit as st
import pandas as pd
df = pd.read_excel('app.xlsx')
if 'Timestamp' in df.columns:
    del df['Timestamp']
st.write("## Contact Info")
filter_column = st.selectbox('Select column to filter', df.columns)
selected_values = st.multiselect(f'Select {filter_column} value(s)', df[filter_column].unique())
search_value = st.text_input(f'Enter value to search in {filter_column} (case-insensitive)')
filtered_df = df.copy()
if selected_values:
    filtered_df = filtered_df[filtered_df[filter_column].isin(selected_values)]
if search_value:
    filtered_df = filtered_df[filtered_df[filter_column].str.contains(search_value, case=False, na=False)]
st.write('Filtered Data:', filtered_df)
if not filtered_df.empty:
    email_list = filtered_df['Email ID'].to_list()
    email_str = "\n".join(email_list)
    st.download_button(
        label="Download Emails",
        data=email_str,
        file_name="filtered_emails.txt",
        mime="text/plain"
    )
else:
    st.write("No data to display or download.")
st.write("## Add New Contact Info")
new_name = st.text_input("Name")
new_email = st.text_input("Email ID")
new_phone = st.text_input("Phone Number")
new_organization = st.text_input("Organization")  
new_designation = st.text_input("Designation")   
if st.button("Add Contact"):
    new_entry = pd.DataFrame({
        'Name': [new_name],
        'Email ID': [new_email],
        'Phone Number': [new_phone],
        'Organization': [new_organization], 
        'Designation': [new_designation]     
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_excel('app.xlsx', index=False)
    st.success("New contact added successfully!")
df = pd.read_excel('app.xlsx')
