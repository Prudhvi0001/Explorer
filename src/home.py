import streamlit as st

def main(data):
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
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()