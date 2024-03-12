import streamlit as st
import pickle
import random

# Load model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# Set page title and favicon
st.set_page_config(page_title="Sentiment Analysis App", page_icon=":smiley:")

# Add custom CSS for background color and styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f0f2f6, #4c9faf); /* Set gradient background */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease 0s;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green background on hover */
    }
    .emoji-animation {
        position: fixed;
        font-size: 30px; /* Larger font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set app title
st.title('Sentiment Analysis Model 😊😔')

# Text input for review
review = st.text_input('Enter your review:')

# Button to trigger prediction
submit = st.button('Predict')

# Add some space for better layout
st.write('---')

# Perform prediction when button is clicked
if submit:
    if review.strip():  # Check if review is not empty
        # Make prediction
        prediction = model.predict([review])

        # Display prediction result with emojis and styled text
        if prediction[0] == 'positive':
            st.success('😊 Positive Review')
        else:
            st.error('😔 Negative Review')

        # Generate random number of emojis between 5 to 10
        num_emojis = random.randint(5, 10)

        # Add floating emojis based on prediction
        for _ in range(num_emojis):
            if prediction[0] == 'positive':
                st.markdown('<div class="emoji-animation" style="bottom: {}%; left: {}%;">😊</div>'.format(random.randint(0, 100), random.randint(0, 100)), unsafe_allow_html=True)
            else:
                st.markdown('<div class="emoji-animation" style="bottom: {}%; left: {}%;">😔</div>'.format(random.randint(0, 100), random.randint(0, 100)), unsafe_allow_html=True)
    else:
        # If no review is provided, predict neutral sentiment
        st.info('😐 Neutral Review')
