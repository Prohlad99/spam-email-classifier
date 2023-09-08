import streamlit as st
import pickle

cv = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Email Classifier")
input_sms = st.text_input("Enter The Message")

if st.button('Predict'):
    vector_input = cv.transform([input_sms])
    result = model.predict(vector_input)
    if result[0] == 1:
        st.header("This Is A Spam-Email")
    else:
        st.header("This Is Not A Spam-Email")