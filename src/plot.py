import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def main(data):
    st.title("Get ready to become a Painter 👨‍🎨")
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        </style>
        > “The greatest value of a picture is when it forces us to notice what we never expected to see.  ”
        **-John Tukey**
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
    
    if st.checkbox("Scatter Plot"):
        column1 = st.selectbox('X-axis_scatter', data.columns)
        column2 = st.selectbox('Y-axis_scatter', data.columns)
        color_var = st.selectbox('Color_variable_scat', [None]+list(data.columns))
        fig = px.scatter(data, x=column1, y=column2, color=color_var)
        st.plotly_chart(fig)
    
    if st.checkbox("Histograms"):
        column = st.selectbox('hist_column', data.columns)
        color_var = st.selectbox('Color_variable_hist', [None]+list(data.columns))
        bins = st.slider('No:Of Bins', min_value=1, max_value=50, value=10, step=1)
        fig = px.histogram(data, x = column, nbins = bins, color = color_var)
        st.plotly_chart(fig)
        
    if st.checkbox("Feature correlation plot"):
        corr = data.corr()
        fig = px.imshow(corr)
        st.plotly_chart(fig)
    



def visualize(data):
    # Histogram Plot
    st.sidebar.header('Visualize Data:')
    if st.sidebar.checkbox('Plot Histograms of each column:'):
        column = st.selectbox('hist_column', data.columns)
        color_var = st.selectbox('Color_variable_hist', [None]+list(data.columns))
        bins = st.slider('No:Of Bins', min_value=1, max_value=50, value=10, step=1)
        fig = px.histogram(data, x = column, nbins = bins, color = color_var)
        st.plotly_chart(fig)

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