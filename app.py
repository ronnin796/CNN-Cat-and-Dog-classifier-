import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import time

# ---------------------------
# Load model
# ---------------------------
model = load_model('cat_dog_classifier.keras')
st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐾", layout="centered")

# ---------------------------
# Sidebar Model Info
# ---------------------------
st.sidebar.markdown("## 🧠 Model Info")
st.sidebar.text("Model: cat_dog_classifier.keras")
st.sidebar.text("Validation Accuracy: 92.3%")  # update with your real accuracy
st.sidebar.text(f"Parameters: {model.count_params():,}")

# ---------------------------
# Title
# ---------------------------
st.title("🐱🐶 Cat vs Dog Classifier")

# ---------------------------
# Image Upload
# ---------------------------
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display original image
    original_img = Image.open(uploaded_file).convert("RGB")
    st.image(original_img, caption="Uploaded Image", width=400)

    # Prepare image for model
    img = original_img.resize((128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # ---------------------------
    # Predict
    # ---------------------------
    start_time = time.time()
    prediction = model.predict(x)
    end_time = time.time()
    inference_time = (end_time - start_time) * 1000  # ms

    confidence = float(prediction[0][0])
    label = "Dog 🐶" if confidence > 0.5 else "Cat 🐱"
    display_confidence = confidence if confidence > 0.5 else 1 - confidence
    dog_prob = confidence * 100
    cat_prob = (1 - confidence) * 100

    # ---------------------------
    # Celebrate high confidence
    # ---------------------------
    if display_confidence > 0.8:
        st.balloons()
        st.toast(f"🎉 Yay! It's a {label.split()[0]}!", icon="🎉")

    # ---------------------------
    # Prediction Card
    # ---------------------------
    card_color = "#1E3A8A" if label.startswith("Dog") else "#7E22CE"
    bar_gradient = (
        "linear-gradient(90deg, #60A5FA, #2563EB)" if label.startswith("Dog")
        else "linear-gradient(90deg, #C084FC, #9333EA)"
    )
    st.markdown("---")
    st.markdown(
        f"""
        <div style="
            text-align:center;
            background-color: {card_color};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.3);
        ">
            <h2 style="margin-bottom: 0.5rem;">Prediction: {label}</h2>
            <div style="height: 22px; background-color: #333; border-radius: 12px; overflow: hidden;">
                <div style="
                    width: {display_confidence * 100}%;
                    height: 100%;
                    background: {bar_gradient};
                    transition: width 1s ease;">
                </div>
            </div>
            <p style="margin-top: 1rem; font-size: 1.1rem;">
                Confidence: <b>{display_confidence * 100:.2f}%</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------
    # Insights
    # ---------------------------
    st.markdown("## 🔍 Model Insights")
    st.write(f"🐶 Dog Probability: {dog_prob:.2f}%")
    st.write(f"🐱 Cat Probability: {cat_prob:.2f}%")
    st.write(f"🕒 Inference Time: {inference_time:.2f} ms")

    # Confidence messages
    if display_confidence > 0.9:
        st.success("💯 Super confident prediction!")
    elif display_confidence > 0.7:
        st.warning("🤔 Fairly confident, could go either way.")
    else:
        st.error("😅 Low confidence, tricky image!")

    st.markdown("🐾 Try another image to see the model in action again!")
else:
    st.info("👆 Upload a cat or dog photo to get started!")
