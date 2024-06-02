import streamlit as st

# Set the theme configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="auto"
)

from stock import render_dashboard_page
from home import render_homepage

# Apply custom CSS for additional styling
st.markdown(
    """
    <style>
    /* Primary accent for interactive elements */
    .css-1avcm0n {
        background-color: #E0E0E0;
    }

    /* Background color for the main content area */
    .css-18e3th9 {
        background-color: #74512D;
    }

    /* Background color for sidebar and most interactive widgets */
    .css-1d391kg {
        background-color: #543310;
    }

    /* Color used for almost all text */
    .css-1cpxqw2, .css-1i8bgfe, .css-1n1u3lz, .css-8uashd {
        color: #FBF8F1;
    }

    /* Font family for all text in the app, except code blocks */
    body {
        font-family: "sans serif";
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* News section */
    .news-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: space-between;
    }

    .news-card {
        background-color: #543310;
        padding: 20px;
        border-radius: 5px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 40px;
        flex: 1 1 calc(33.333% - 20px);
    }

    .news-title {
        font-size: 14px;
        font-weight: bold;
        text-align: center;
    }

    /* Dashboard fonts */
    .big2-font {
        font-size: 25px;
        text-align: center;
        margin-bottom: 20px;
    }

    .big3-font {
        font-size: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

logo_path = './logo.png'
logo_width = 150

# logo
st.sidebar.image(logo_path, width=logo_width)

st.sidebar.title('StockSage')
selection = st.sidebar.radio("Go to", ['Home', 'Dashboard', 'Contact us'])

if selection == 'Home':
    render_homepage()
elif selection == 'Dashboard':
    render_dashboard_page()
elif selection == 'Contact us':
    st.title('We are:')
    st.write('Aakriti Vijay')
    st.write('Aman Kumar Singh')
    st.write('Hardik Badhoriya')
    st.write('Mukul Dev Arya')
    st.write('Send us an email at 2003013001@ipec.org.in')
