import streamlit as st
import pandas as pd

import src.home
import src.stats
import src.plot
import src.model

# Remove Warnings
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
showWarningOnDirectExecution = False


# Model pipeline setup
pipeline = {
    "Home": src.home,
    "Data Exploration": src.stats,
    "Data Visualization": src.plot,
    "Data Modeling": src.model
}

def main():
    st.sidebar.title("Pipeline")
    selection = st.sidebar.radio("Go to:", list(pipeline.keys()))
    
    # Uploader Widget
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    data = 0
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
    page = pipeline[selection]
    with st.spinner(f"Loading {selection} ...."):
        page.main(data)
    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This is fun project created to help beginners to explore the possibilites of machine learning "
        " in an interactive way. If you have any suggestions or requests,"
        "Feel free to raise an [issue](https://github.com/Prudhvi0001/Explorer/issues)"
        ""
    )
    st.sidebar.title("Footnotes")
    st.sidebar.markdown(
    """
    - Authour: [Prudhvi Vajja](https://github.com/Prudhvi0001)
    - Source Code: [Explorer](https://github.com/Prudhvi0001/RandomForestDashboard)
    - Create with: [Streamlit](https://docs.streamlit.io/en/stable/index.html)
    - LINCENSE: **FREE TO USE**
    """
    )

if __name__ == "__main__":
    main()