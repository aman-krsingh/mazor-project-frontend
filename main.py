import streamlit as st
from stock import render_dashboard_page
from home import render_homepage

logo_path = './logo.png'
logo_width = 150

# logo
st.sidebar.image('./logo.png', width=logo_width)

st.sidebar.title('StockSage')
selection = st.sidebar.radio("Go to", ['Home', 'Dashboard', 'Contact us'])

if selection == 'Home':
    render_homepage()


elif selection == 'Dashboard':
    render_dashboard_page()

elif selection == 'Contact us':
    st.title('we are:')
    st.write('Aakriti Vijay')
    st.write('Aman Kumar Singh')    
    st.write('Hardik Badhoriya')
    st.write('Mukul Dev Arya')
    st.write('Send us an email at 2003013001@ipec.org.in')

