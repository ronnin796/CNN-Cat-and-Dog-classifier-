import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image  # For high-quality image handling

# Load model
model = load_model('cat_dog_classifier.keras')

# App title
st.title("🐱🐶 Cat vs Dog Classifier")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display original image (not resized)
    original_img = Image.open(uploaded_file)
    st.image(original_img, caption="Uploaded Image", use_container_width=True)

    # Resize copy for prediction
    img = original_img.resize((128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # Predict
    prediction = model.predict(x)
    confidence = float(prediction[0][0])

    # Determine label
    label = "Dog 🐶" if confidence > 0.5 else "Cat 🐱"
    display_confidence = confidence if confidence > 0.5 else 1 - confidence

    # Show prediction and confidence
    st.subheader(f"Prediction: {label}")
    st.progress(display_confidence)  # visual bar
    st.caption(f"Confidence: {display_confidence*100:.2f}%")
    st.balloons()  # celebration effect