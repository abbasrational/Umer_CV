import streamlit as st
import pandas as pd

# Load the existing data from the Excel file
df = pd.read_excel('app.xlsx')

# Delete the 'Timestamp' column if it exists
if 'Timestamp' in df.columns:
    del df['Timestamp']

st.write("## Contact Info")

# Create multiselect options for filtering by columns
filter_column = st.selectbox('Select column to filter', df.columns)

# Dropdown filter: Select one or more unique values from the column
selected_values = st.multiselect(f'Select {filter_column} value(s)', df[filter_column].unique())

# Text-based search input: Provide additional refinement through case-insensitive search
search_value = st.text_input(f'Enter value to search in {filter_column} (case-insensitive)')

# Apply both dropdown and text-based filters
filtered_df = df.copy()

# Apply dropdown filter if values are selected
if selected_values:
    filtered_df = filtered_df[filtered_df[filter_column].isin(selected_values)]

# Apply text-based search filter if a search term is provided
if search_value:
    filtered_df = filtered_df[filtered_df[filter_column].str.contains(search_value, case=False, na=False)]

# Show filtered dataframe
st.write('Filtered Data:', filtered_df)

# Prepare email list for download
if not filtered_df.empty:
    email_list = filtered_df['Email ID'].to_list()
    email_str = "\n".join(email_list)

    # Button to download email list as a .txt file
    st.download_button(
        label="Download Emails",
        data=email_str,
        file_name="filtered_emails.txt",
        mime="text/plain"
    )
else:
    st.write("No data to display or download.")

# Section to add new contact info
st.write("## Add New Contact Info")

# Create input fields for new contact information
new_name = st.text_input("Name")
new_email = st.text_input("Email ID")
new_phone = st.text_input("Phone Number")
new_organization = st.text_input("Organization")  
new_designation = st.text_input("Designation")   

# Button to submit new contact info
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

# Reload the DataFrame to reflect the new data
df = pd.read_excel('app.xlsx')

# Section to delete a contact
st.write("## Delete Contact Info")

# Display the filtered DataFrame with delete options
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        col1, col2 = st.columns([4, 1])
        col1.write(f"{row['Name']} - {row['Email ID']} - {row['Phone Number']} - {row['Organization']} - {row['Designation']}")
        if col2.button("Delete", key=index):
            # Delete the selected row
            df = df.drop(index)
            df.to_excel('app.xlsx', index=False)
            st.success(f"Contact '{row['Name']}' deleted successfully!")
            # Reload the DataFrame to reflect the changes
            df = pd.read_excel('app.xlsx')
            # Refresh the filtered DataFrame
            filtered_df = df.copy()
else:
    st.write("No contacts available to delete.")
