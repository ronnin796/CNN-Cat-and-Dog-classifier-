# 🐱🐶 Cats vs Dogs Classifier using CNN (Jupyter Notebook)

This project is a **binary image classifier** built using a **Convolutional Neural Network (CNN)** in a Jupyter Notebook. It classifies images of cats and dogs and demonstrates my learning journey from a simple CNN to a more robust model.

🚀 **[Live Demo](https://catdogclassifier23.streamlit.app/)**  
---

## 🎯 Project Overview

- **Goal:** Classify images into cat or dog.
    
- **Training Images:** ~8000
    
- **Test Images:** ~2000
    
- **Libraries:** TensorFlow, Keras, NumPy, Matplotlib
    

---



### 1️⃣ First Attempt – Simple CNN

- **Architecture:** 2 Conv2D layers, 32 filters, 64×64 images
    
- **Problem:** Poor accuracy (~50–60% on cats)
    
- **Lesson Learned:** Small input size and shallow network couldn’t capture enough features
    

---

### 2️⃣ Improved Model – Enhanced CNN

- **Changes Made:**
    
    - Increased **input size** to 128×128
        
    - Added **3rd Conv2D layer** (128 filters)
        
    - Stronger **data augmentation**: rotation, zoom, brightness, horizontal flip
        
    - Added **Dropout (0.5)** for regularization
        
    - Trained for **50+ epochs** with **EarlyStopping**
        

- **Results:**
    
    - Accuracy: ~85–90%
        
    - Cats and dogs predicted reliably
        
    - Learned importance of **depth, input size, and augmentation**
        

---

## 🔧 How to Run in Jupyter Notebook

1. Install dependencies:
    

`pip install tensorflow numpy matplotlib jupyter`

2. Open the notebook:
    

`jupyter notebook`

3. Open the provided notebook file (e.g., `cats_vs_dogs_cnn.ipynb`) and run all cells step by step.
    
4. Make predictions on new images directly within the notebook:
    

`predict_image('path_to_image.jpg')`


## ✨ Key Concepts Learned

- **Convolutional Layers:** Learn patterns in images (edges, textures, shapes)
    
- **Pooling Layers:** Reduce spatial size, control overfitting
    
- **Flatten + Dense Layers:** Map convolutional features to output
    
- **Dropout:** Prevents overfitting
    
- **Data Augmentation:** Makes the model robust to variations
    

