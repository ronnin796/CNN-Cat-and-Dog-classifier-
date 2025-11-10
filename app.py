import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

model = load_model('cat_dog_classifier.keras')

st.title("🐱🐶 Cat vs Dog Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the original image (high quality)
    original_img = Image.open(uploaded_file)
    st.image(original_img, caption="Uploaded Image", use_container_width=True)

    # Resize a copy for model input
    img_resized = original_img.resize((128, 128))
    x = image.img_to_array(img_resized)
    x = np.expand_dims(x, axis=0) / 255.0

    # Predict
    prediction = model.predict(x)
    label = "Dog 🐶" if prediction[0][0] > 0.5 else "Cat 🐱"
    st.subheader(f"Prediction: {label}")
