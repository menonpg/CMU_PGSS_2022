""" Streamlit app that consumes the fastAPI endpoint in fastAPIRunMaskInference.py """
# Run command: streamlit run consumeFastAPIinStreamlit.py --server.port=8501     # --server.address=
# This does the equivalent of the following curl command wihtout the need to install curl or use the terminal 
# curl -X 'GET' \
#   'http://localhost:8000/predict?imageFile=%2FUsers%2Fpgmenon%2FDocuments%2FCMU%2FPGSS%2FPGSS2022%2Fgitcheckout%2FCMU_PGSS_2022%2FWeek04%2FtestImage.jpg' \
#   -H 'accept: application/json'

import requests
import json
import sys 
from PIL import Image, ImageOps  #pip install Pillow
import streamlit as st
# Allows you to run the streamlit app by running the script directly:
from streamlit import cli as stcli
import cv2
    
#"""Make get request to fastAPI endpoint """
def getFastAPI(url):
    # Make the API call
    response = requests.get(url)
    # Convert the response to a Python dictionary
    data = response.json()
    return data

def main():
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
        myPredictions = getFastAPI( url='http://localhost:8000/predict?imageFile='+'testImage.jpg')

        # Display the image
        st.image(Image.fromarray(frame))

        with st.expander("Prediction"):
            # Display the prediction
            # st.write("Prediction:", myPredictions)
            st.write("Prediction:", myPredictions.get('Prediction'))

    
if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
        
    else:
        sys.argv = ["streamlit", "run", sys.argv[0], "--server.port=8501", "--server.address=0.0.0.0"]
        sys.exit(stcli.main())