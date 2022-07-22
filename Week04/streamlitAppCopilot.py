""" Streamlit app based on ../Week03-L5/teachableMachine_ImageBasedMaskClassifier/InferenceFunctionWithArguments.py """
# Run command: streamlit run streamlitAppCopilot.py --server.port=8501     # --server.address=0.0.0.0
from keras.models import load_model
from PIL import Image, ImageOps  #pip install Pillow
import numpy as np
import pandas as pd
import sys
import cv2
import streamlit as st

def ModelInference_Keras(labelFile='labels.txt', modelFile='keras_model.h5', imageFile='testImage.jpg'):
  # Load labels.txt
  labels = pd.read_csv(labelFile, header=None, delimiter=' ')
  labels.columns= ['Prediction', 'Label']

  # Load the model
  model = load_model(modelFile)

  # Load the data and transform it:
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  # Replace this with the path to your image
  image = Image.open(imageFile)
  #resize the image to a 224x224 with the same strategy as in TM2:
  #resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)
  #turn the image into a numpy array
  image_array = np.asarray(image)
  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  # Load the image into the array
  data[0] = normalized_image_array

  # Run the inference / prediction on the loaded data
  prediction = model.predict(data)
  predictedClass = np.argmax(prediction, axis=1)

  PredictionLabel = labels.loc[labels['Prediction'].isin(predictedClass)]['Label'].values[0]
  
  return(PredictionLabel)


if __name__ == "__main__":
    # Load the image from the webcam
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    #Create a run button in streamlit
    st.title("Mask Detector")
    run = st.sidebar.checkbox('Run')

    if run:
        # Convert to PIL image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imwrite('testImage.jpg', frame)

        # Run the inference function
        myPredictions = ModelInference_Keras(labelFile='../Week03-L5/teachableMachine_ImageBasedMaskClassifier/labels.txt', modelFile='../Week03-L5/teachableMachine_ImageBasedMaskClassifier/keras_model.h5', imageFile='testImage.jpg')

        # Display the image
        st.image(Image.fromarray(frame))

        with st.expander("Prediction"):
            # Display the prediction
            st.write("Prediction:", myPredictions)