import streamlit as st
import os

st.title("TIFF File Hosting")

file_name = "F8 Test.tif"
file_path = os.path.join("static", file_name)

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        st.download_button(
            "Download TIFF File",
            f,
            file_name=file_name,
            mime="image/tiff"
        )
else:
    st.error("File not found in static folder.")




































# import streamlit as st
# import pandas as pd
# df=pd.read_excel('app.xlsx')


# st.write("## Contact Info")


# # Create multiselect options for filtering by columns
# filter_column = st.selectbox('Select column to filter', df.columns)

# # Dropdown filter: Select one or more unique values from the column
# selected_values = st.multiselect(f'Select {filter_column} value(s)', df[filter_column].unique())

# # Text-based search input: Provide additional refinement through case-insensitive search
# search_value = st.text_input(f'Enter value to search in {filter_column} (case-insensitive)')

# # Apply both dropdown and text-based filters
# filtered_df = df.copy()

# # Apply dropdown filter if values are selected
# if selected_values:
#     filtered_df = filtered_df[filtered_df[filter_column].isin(selected_values)]

# # Apply text-based search filter if a search term is provided
# if search_value:
#     filtered_df = filtered_df[filtered_df[filter_column].str.contains(search_value, case=False, na=False)]

# # Show filtered dataframe
# st.write('Filtered Data:', filtered_df)

# # Prepare email list for download
# if not filtered_df.empty:
#     email_list = filtered_df['Email ID'].to_list()
#     email_str = "\n".join(email_list)

#     # Button to download email list as a .txt file
#     st.download_button(
#         label="Download Emails",
#         data=email_str,
#         file_name="filtered_emails.txt",
#         mime="text/plain"
#     )
# else:
#     st.write("No data to display or download.")
