import streamlit as st
import pandas as pd

# Title of the App
def main(data):
    st.title("Get ready to become a Statistician 👨‍🏫")
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        </style>
        > “Facts are stubborn things, but statistics are pliable. ”
        **-Mark Twain**
        """, unsafe_allow_html=True)
    
    if st.checkbox("Tips"):
        st.markdown(
            """
            Tips to understand your Data.
            """)
    
    if not isinstance(data, pd.DataFrame):
        return st.markdown(
            """
            **Upload A Data file for futhuer exploration.**
            """)
    
    if st.checkbox("Head(Data):"):
        st.write(data.head())
        
    if st.checkbox("Basic stats of data:"):
        st.write(data.describe())
        
    if st.checkbox("Shape of the data:"):
        st.write(f"This dataset has {data.shape[0]} Rows and {data.shape[1]} Columns")
    
    if st.checkbox("Count of Missing values"):
        st.write(data.isnull().sum())
    
    if st.checkbox("Data Types"):
        st.write(data.dtypes)



def statistics(data):
    st.title("Get ready to become a Statistician 👨‍🏫")
    st.sidebar.header('Stats of the Data')
    if st.sidebar.checkbox("Get the stats"):
        st.write("Top 5 Rows:", data.head(5))
        st.write('Data Shape:', data.shape)
        st.write('Description of data:', data.describe())
        st.write('Data Info:', data.dtypes)
        st.write('Count of Null or Missing values in the Data Frame:', data.isnull().sum()) 