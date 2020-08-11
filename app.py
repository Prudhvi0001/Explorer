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

# Title of the App
st.title("Random Forest Explorer")

# Description about the app using markdown format
st.markdown(
    """
    Hi there! this a tool where you can upload a dataset and fine tune a random forest model and 
    check the results in a interactive way let me known if this helpful or check my [github](https://github.com/Prudhvi0001) 
    to create your own machine learning model explorer with a few tweaks

    **If Your file size is too high Create a small version of your data file and check how Random Forest works on your Data**
    """
    )



def statistics(data):
    st.sidebar.header('Stats of the Data')
    if st.sidebar.checkbox("Get the stats"):
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

        
# File Upload widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # uploaded_file = io.TextIOWrapper(uploaded_file)
    data = pd.read_csv(uploaded_file)
    st.write("Top 5 Rows:", data.head(5))
    statistics(data)
    visualize(data)
    st.sidebar.header("Cool! Let's Build a model.")
    if st.sidebar.checkbox("Run Model Analysis:"):
        model(data)
    # st.balloons()


# # statistics(data)
# import time
# progress_bar = st.progress(0)
# status_text = st.empty()
# chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     # Update progress bar.
#     progress_bar.progress(i + 1)

#     new_rows = np.random.randn(10, 2)

#     # Update status text.
#     status_text.text(
#         'The latest random number is: %s' % new_rows[-1, 1])

#     # Append data to the chart.
#     chart.add_rows(new_rows)

#     # Pretend we're doing some computation that takes time.
#     time.sleep(0.1)

# status_text.text('Done!')
# st.balloons()

# int maxArithmeticLength(vector<int> a, vector<int> b) {
#     unordered_set<int> diffs;
#     unordered_set<int> m;
#     for (auto x : b) m.insert(x);
#     diffs.insert(a[1] - a[0]);
#     for (auto x : b) if (x - a[0] > 0) diffs.insert(x - a[0]);
#     int rtnVal = -1;
#     for (auto diff : diffs) {
#         int i = 0;
#         int curr = a[0];
#         int ans = 0;
#         // handle if b[i] < a[0]
#         int c = a[0];
#         while (m.count(c - diff)) {
#             c -= diff;
#             ans++;
#         }
#         while (i < a.size()) {
#             if (m.count(curr + diff)) {
#                 curr = curr + diff;
#             } else if (i < a.size() - 1 && curr + diff == a[i + 1]) {
#                 curr = a[++i];
#                 continue;
#             } else {
#                 break;
#             }
#             ans++;
#         }
#         if (i == a.size() - 1)
#             rtnVal = max(rtnVal, ans + (int)a.size());
#     }
#     return rtnVal;
# }