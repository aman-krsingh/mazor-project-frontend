import streamlit as st

# Custom CSS for card size
st.markdown("""
    <style>
        .review-card {
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
            width: 70%;
            background-color: rgba(255, 255, 255, 0.6); /* White with 60% opacity */
            color: black; /* Text color */
        }
        .review-card:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

def render_homepage():
    st.title('Welcome to StockSage')
    st.write("  ")
    st.write('Your go-to web app for predicting stock prices over the next 30 days.')
    st.write("  ")
    st.write("Easy Four Step Tutorial:")
    st.write("1. Go to dashboard from navigation.")
    st.write("2. Select a company from dropdown option.")
    st.write("3. Hit the submit button.")
    st.write("4. Get instant, data-driven forecasts presented in clear graphs.")
    st.write("  ")
    st.write("  ")
    st.write("  ")

    # Prompt the user to enter a review
    st.header('Feel free to Write a Review')
    review = st.text_area('Enter your review here:', '')

    # Button to submit the review
    if st.button('Submit Review'):
        if review:
            st.success('Thank you for your review!')
            # Writing review
            with open('./reviews.txt', 'a') as f:
                f.write(review + '\n')
            review = '' 
        else:
            st.error('Please enter a review before submitting.')

    # Displaying previously submitted reviews
    st.header('Previous Reviews')
    # Reading reviews from the file
    try:
        with open('reviews.txt', 'r') as f:
            previous_reviews = f.readlines()
    except FileNotFoundError:
        previous_reviews = []
    
    # Displaying previous reviews in cards
    for idx, r in enumerate(previous_reviews):
        st.markdown(f'<div class="review-card">{r.strip()}</div>', unsafe_allow_html=True)
