import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout = "wide") #Wide layout


def data_stats(data): # Function to display the relevant statistics
    st.write("**# of Rows:**", data.shape[0]) #Shows number of rows
    st.write("**# of Columns:**", data.shape[1]) # Shows number of columns
    st.write("**Data Types:**") # Shows the Data Types
    st.write(data.dtypes.value_counts()) #Shows the value counts for the data types

def column_stats(data, column): #Function to show the column stats
    st.write("**Column:**", column) # Shows what column
    st.write("**Data Type:**", data[column].dtype) # Shows the data type of the column

    if data[column].dtype == 'object': #If the data type is categorical 
        st.write("**Proportion of Categories:**") #Shows the proportion of the categories in this categorical variable
        st.write(data[column].value_counts(normalize=True))

        plt.figure(figsize=(14, 6)) #Create barplot and change color of barplot
        data[column].value_counts().plot(kind='bar', color = 'red', edgecolor = 'black') 
        plt.xticks(rotation=45)
        plt.xlabel(column)
        plt.ylabel("Count")
        st.pyplot(plt)

    elif data[column].dtype in ['int64', 'float64']: #If Numerical Column
        st.write("**Five Number Summary:**")
        st.write(data[column].describe()) #Show the five number summary

        # Create a distribution plot
        plt.figure(figsize=(10, 6)) # Create a histogram using matplotlib to show the distribution of the numeric variable
        plt.hist(data[column], bins='auto', color = 'purple', edgecolor = 'orange')
        plt.xlabel(column)
        plt.ylabel("Count")
        st.pyplot(plt)

# Main Streamlit application
def main():
    st.title("EDA Discussion Stats 21") #Title of project
    file_chosen = st.file_uploader("Choose a CSV file", type="csv") # CSV Picker

    if file_chosen is not None:
        data = pd.read_csv(file_chosen) 
        st.subheader("Data Stats") #Use above function to find stats
        data_stats(data)

        selected_column = st.radio("Choose a Column", data.columns)
        st.subheader("Column Stats")
        column_stats(data, selected_column)


if __name__ == "__main__":
    main()


