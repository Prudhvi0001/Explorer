import streamlit as st

import src.home as home

# Model pipeline setup
pipeline = {
    "Home": src.home,
    "Statistics": src.stats,
    "Visualization": src.plot,
    "Modeling": src.model
}

def main():
    st.sidebar.title("Pipeline")
    selection = st.sidebar.radio("Go to:", list(pipeline.keys()))
    
    page = pipeline[selection]
    with st.spinner(f"Loading {selection} ...."):
        page
    st.sidebar.title("Footnotes")
    st.sidebar.info(
        "This is fun project to help while learning, If you have any suggestions or requests "
        "feel free to raise an [issue]()"
    )

if __name__ == "__main__":
    main()