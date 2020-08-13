# Load the Libraries
import streamlit as st
import pandas as pd
import numpy as np
import io
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

# Remove Warnings
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)

showWarningOnDirectExecution = False

@st.cache(suppress_st_warning=True)
def homepage():
    # Title of the App
    st.title("🎄 Explorer 🎄")

    # What can you do?
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        </style>
        Hi there! 👋  This is an interactive data analysis and model building tool.
        
        **Key Features:**
        - Generate interative plots 📊 📉 📺
        - Statsitical analysis of the Data 📝 🗜 🛠
        - Wide range Metrics to understand the model 🔎 📈 ⚙️
        - Ensemble different models for better predictions. ⛓ ⚖️
        
        A lot more to come.
        
        **NOTE:** Only supports files with **size < 200MB**
        
        **Recommendations:** If you have a large file create a small version of it and play around to get faster results.
        
        
        ### If you want run this locally:
        
        ```Shell
        pip install streamlit
        streamlit run https://raw.githubusercontent.com/Prudhvi0001/RandomForestDashboard/master/app.py
        ```
        
        
        ### **`FootNotes:`**
        
        - Authour: [Prudhvi Vajja](https://github.com/Prudhvi0001)
        - Source Code: [Explorer](https://github.com/Prudhvi0001/RandomForestDashboard)
        - LINCENSE: **FREE TO USE**
        """, unsafe_allow_html=True)


def statistics(data):
    st.title("Get ready to become a Statistician 👨‍🏫")
    st.sidebar.header('Stats of the Data')
    if st.sidebar.checkbox("Get the stats"):
        st.write("Top 5 Rows:", data.head(5))
        st.write('Data Shape:', data.shape)
        st.write('Description of data:', data.describe())
        st.write('Data Info:', data.dtypes)
        st.write('Count of Null or Missing values in the Data Frame:', data.isnull().sum()) 


def visualize(data):
    # Histogram Plot
    st.sidebar.header('Visualize Data:')
    if st.sidebar.checkbox('Plot Histograms of each column:'):
        column = st.selectbox('hist_column', data.columns)
        color_var = st.selectbox('Color_variable_hist', [None]+list(data.columns))
        bins = st.slider('No:Of Bins', min_value=1, max_value=50, value=10, step=1)
        fig = px.histogram(data, x = column, nbins = bins, color = color_var)
        st.plotly_chart(fig, )

    if st.sidebar.checkbox("Scatter plot:"):
        column1 = st.selectbox('X-axis_scatter', data.columns)
        column2 = st.selectbox('Y-axis_scatter', data.columns)
        color_var = st.selectbox('Color_variable_scat', [None]+list(data.columns))
        fig = px.scatter(data, x=column1, y=column2, color=color_var)
        st.plotly_chart(fig)
    
    if st.sidebar.checkbox("Feature Correlation Plot:"):
        corr = data.corr()
        fig = px.imshow(corr)
        st.plotly_chart(fig)
    

def model(data):
    # st.sidebar.header("Cool! let's Build a model.")
    target_column = st.sidebar.selectbox('target_column', data.columns)
    target_data = data[target_column]
    data = data.drop(columns = [target_column], axis = 0)
    if st.sidebar.checkbox("Shuffle Data:"):
        data = data.sample(frac=1).reset_index(drop=True)

    if st.sidebar.checkbox("Split Stratified Test Data"):
        test_size = st.sidebar.slider("test_size", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        xtrain,xtest,ytrain,ytest = train_test_split(data, target_data, test_size = test_size, random_state = 42, stratify = target_data)

    model = st.sidebar.selectbox("Select the model", ['RandomForestClassifier', 'RandomForestRegressor'])

    if model == 'RandomForestClassifier':
        m = RandomForestClassifier()
    elif model == 'RandomForestRegressor':
        m = RandomForestRegressor()
    if st.sidebar.button('RUN'):
        m.fit(xtrain,ytrain)
        st.write("R2 Score:", m.score(xtrain,ytrain))
        st.balloons()


homepage()


# File Upload widget
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is None:
    homepage()


if uploaded_file is not None:
    # uploaded_file = io.TextIOWrapper(uploaded_file)
    data = pd.read_csv(uploaded_file)
    statistics(data)
    visualize(data)
    st.sidebar.header("Cool! Let's Build a model.")
    if st.sidebar.checkbox("Run Model Analysis:"):
        model(data)