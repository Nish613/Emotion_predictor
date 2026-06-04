import streamlit as st
import joblib

model = joblib.load("emotion_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

reverse_mapping = {
    0: 'sadness',
    1: 'anger',
    2: 'love',
    3: 'surprise',
    4: 'fear',
    5: 'joy'
}
st.title("Emotion Detection App")
st.write("Enter text to predict emotion")

text = st.text_area("Enter your text:")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        text_vector = tfidf.transform([text])
        prediction = model.predict(text_vector)[0]

        emotion = reverse_mapping[prediction]

        st.success(f"Predicted Emotion: {emotion}")