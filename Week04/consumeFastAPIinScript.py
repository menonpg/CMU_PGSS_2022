""" Python script that consumes the fastAPI endpoint in fastAPIRunMaskInference.py """
# Run command: streamlit run consumeFastAPIinStreamlit.py --server.port=8501     # --server.address=
# This does the equivalent of the following curl command wihtout the need to install curl or use the terminal 
# curl -X 'GET' \
#   'http://localhost:8000/predict?imageFile=%2FUsers%2Fpgmenon%2FDocuments%2FCMU%2FPGSS%2FPGSS2022%2Fgitcheckout%2FCMU_PGSS_2022%2FWeek04%2FtestImage.jpg' \
#   -H 'accept: application/json'

""" Make api call to fastAPI endpoint """
import requests
import json
import sys 
    
"""Make get request to fastAPI endpoint """
def getFastAPI(url):
    # Make the API call
    response = requests.get(url)
    # Convert the response to a Python dictionary
    data = response.json()
    return data

if __name__ == "__main__":
    # makeAPIcall( url='http://localhost:8000/predict', data={'imageFile': sys.argv[0]} )
    data = getFastAPI( url='http://localhost:8000/predict?imageFile='+sys.argv[0])
    print(data)