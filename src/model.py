import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


def main(data):
    st.title("Get ready to become a Data Scientist 🕵️‍♂️")
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        </style>
        > “A data scientist is a unique blend of skills that can both unlock the insights of data and tell a fantastic story via the data”
        **-DJ Patil**
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
    if st.checkbox("Shuffle Data (Once shuffled data will remain shuffled)"):
        data = data.sample(frac=1).reset_index(drop=True)
    
    target_column = st.selectbox('target_column', data.columns)
    target_data = data[target_column]
    data = data.drop(columns = [target_column], axis = 0)
    
    test_size = st.slider("test_size", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
    try:
        xtrain,xtest,ytrain,ytest = train_test_split(data, target_data, test_size = test_size, random_state = 42, stratify = target_data)
    except:
        st.markdown("""
                    **Error:** Choose the target column correctly
                    """)
    model = st.selectbox("Select the model", ['RandomForestClassifier', 'RandomForestRegressor'])

    if st.checkbox("FineTune your model:"):
        # model_tuner(model)
        st.write("Yet to build, For now sklearns default parameters are intialized.")
    
    if model == 'RandomForestClassifier':
        m = RandomForestClassifier()
    elif model == 'RandomForestRegressor':
        m = RandomForestRegressor()
        
    if st.button('RUN THE MODEL'):
        m.fit(xtrain,ytrain)
        st.write("R2 Score:", m.score(xtest,ytest))
        st.balloons()
        # if st.checkbox("R2 Score"): 
        # metrics = ['R2 Score', 'confusion_matrix', 'RMSE']
        # # Emetrics = st.multiselect("Select the metric for your model:", metrics)
        # for metric in Emetrics:
        #     st.write(f"{metric}:", score_of_the_model(m, metric))

    # st.write("R2 Score:", m.score(xtest,ytest))
    # st.balloons()
  
    

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

    