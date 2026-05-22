import streamlit as st
import pickle

with open('review_model.pkl', 'rb') as f:
    model = pickle.load(f)

text = st.text_input('Enter Review')

if st.button('Predict'):
    result = model.predict([text])

    if result[0] == 'positive':
        st.success('Positive Review✔️✔️')
    else:
        st.error('Negative Review ❌❌')

