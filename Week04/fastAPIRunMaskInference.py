# Go to http://localhost:8000/docs to see the api docs
# Call the api using the terminal with: curl -X 'GET' 'http://localhost:8000/' -H 'accept: application/json' 
# Run inference on a new image file :  http://localhost:8000/docs#/default/predict_predict_get
# curl -X 'GET' \
#   'http://localhost:8000/predict?imageFile=%2FUsers%2Fpgmenon%2FDocuments%2FCMU%2FPGSS%2FPGSS2022%2Fgitcheckout%2FCMU_PGSS_2022%2FWeek04%2FtestImage.jpg' \
#   -H 'accept: application/json'
# Make a prediction on an image from tnhe internet: http://localhost:8000/docs#/default/predict_predict_get
# curl -X 'GET' \
#   'http://localhost:8000/predict?imageFile=data%3Aimage%2Fjpeg%3Bbase64%2C%2F9j%2F4AAQSkZJRgABAQAAAQABAAD%2F2wCEAAkGBxIPEhUQEhIVFhAVEBIVFRAXFRUVFRAQFRUWFhUWFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGhAQGi0lHyUrLSstLS0tKy0tLS0tLS0tLS0tLS0tNS0tLS0tLS8tLS0tLSstLS0tLS0tLS0tKy0tLf%2FAABEIALsBDQMBIgACEQEDEQH%2FxAAcAAEAAgMBAQEAAAAAAAAAAAAAAQYDBAUHAgj%2FxABBEAACAQMCAwUEBgYJBQAAAAAAAQIDBBEFIQYSMRNBUWFxIoGRoQcyQrHR8BRSYnLB4RYjMzRDgqKy8RUkRGOS%2F8QAGgEBAAMBAQEAAAAAAAAAAAAAAAEDBAIFBv%2FEACYRAAIDAAIBBAICAwAAAAAAAAABAgMREiExBBMiQVHwkbEygaH%2F2gAMAwEAAhEDEQA%2FAPbgASgAACAACCQAAAARKWE34Jv4AHhH056z2l5C3TThQppNb7VqntS6fs9mecUN5ZXj0Zl1vUXdVqleXWrUnUfk5Tk8Z8unwOholnGTy02vBHDeI2Qj9HZ0Wi2%2BV80VLqo%2BHju39xZI8LxjKFSnnK65wnju3S9e41dLpSe1KHIl1ljf44%2B4t%2BmWc8Y3Ue%2FfMpPzl1MsrDV7Zh03hempdoo8rfWOzTz12LHb6Wo%2Bnnv8cmxZW6itkb8InK1lEnhoPTovu%2Fl6GSna8vTf8DoRgfSgd8Ct2GjKGN0t%2FExTjlNtL89TpSpmGcA00E0ytapp1Ksk2um6Xg%2FIp%2Bq8HwmnJSjFbYXRJeGe49AvLdr6u%2Ffg4F9SbXMm16Nrbw8jlTwuUN8FDuOH6dBZ%2Btno10wVvW5weIxg4tPfJ6BqFvBr2pPyzuil65bwT2S%2FPiXwlpzKGFv%2BiHVeyu4UPs1KcotftPM0%2FwDTj3ntx%2BZ%2BCq%2FY1v0mT%2Fsnzesvspeiy%2FQ%2FS1KaklJdGk16PcuRltXen0SGCSoAjBIAIJAAYIJAPkAEkMAAgkAAkMAAgA1tUulQo1azWVTo1JteKhFy%2FgbJwuPZ8unXb6f9rVWfJxafybDJXbPyt2eXFbbJJl64ZtefCS28f5%2FgU63o5qf5nn4npPCtFbYWy%2BZntfR6NS70t%2BlWMYLzO7QpGjaI6tvEx%2BWWTZs0omeMTFA2IF8EZZmSMT7wfMT7NCM7PhmKojKzHM5kdRNOrDJy720i3nHqdaqaVzEyT6NlbZVNV0eM03nG7ePwPO9e0xx3W66c3j5NdzPW68Sh8R0ZQk3Fvll1X4%2BJ1VLstmtRSbKty%2Bx59O7Hp8Pgj9K8KXnb2lGo%2BvJyv1g3B%2F7T81VHyz2W7xl%2BC%2FP3H6J%2Bj6k42FFN7vtJP1lUk%2F4m6Jgu8FjAB0ZyACQAgQAAAACAASAACAAAAAAADicc0HU068hH6zs6%2BF4vs28HbPmtSU4yg%2BkouL9GsMMlPGflbRaPPLPeek8OWvJhvqyncM2bhXnQn9anKUX6xk4s9BoNU1zSaUYrd9MJGO1tvD1a8USx2sTqUSi3Gu3j%2Fu9q%2BzX%2BJU2cvSHcvXc06XH1ei8XFs0ls2sp%2Bqzt8DmNZxPWenQMsSkWH0jWNTaVR034TTXzLFp2t0LhZpVoT9JJ%2FItSwzyiztRPvJqQqmbnO1JFTifbMcj4nUOTqPEFC3Tc6sVjuzlnLaOowb8HSmjVrpFLu%2FpIpN8tGEpvOM7LPourMH%2FVNUuHmnTUY9VlJc3l7TK5Q0vimizXcdira5bZXNjK3T8n3P8Ah7zbp67Vi%2ByvKLpyeEqq3puT6Jvu9ehuVaHMmmtmmsFKXFmldo8ou7bFTptlYXy2P0DwUkrKhjpyPHpzSPDtWotVZU84cXs%2FBM964bt%2BytaEPCjD7kbq3vZh9Qs6OmQMklhlBBIADIJYAIJyCACAASgAAQAAAAACSAY7m4jTXNJ4WceO5kOFxvzqzqVKf16eJrPls%2Fk2cTfGLaLaYe5ZGH5eHl1S1jHVa7i1KFR1asZLzqSUk%2FBqSexYKcYqS5t0nlLz7it6Dipd1KqWFODljwbkuZfHJaL%2BylJc0euDG5a9PUdbrfCXlGS54ht6C5qlSMV6mhV4qtbj2FSnUzth0mk%2FTnSyUHim3rKceWDhJvl7VvPJlreCS2l55ysrGMmnr3BtxbQp1YzqYnz%2B3JuMnPCaTX2crme%2B5fXSpR5Nmey1RkoxXk7PEel2j9tUa1Hv5%2BSXZruy5LKijX03Sp0JRq05rCeVUX53PvgDSr24uHHtJU4woJNtuoocuIrPNviT53jzfgWaz0t06%2FYzhGnXlnMI7UbqPXmp90Z%2BMe%2Fr4kzrxbF9Fld2vjJdl30XVFVisPPQ7amUnR9PdvXwm3TksrPd5F27P2clMdKroxTWFe4ru5qk40%2Frt46427zzmPCVSpLnuayhBtbLdv3%2BPkem%2FobnNyazjocOnTrXdWSo%2FwBXGLlF3LW%2B22KK8P2ts9zwdQi2zrmoRMGl6ZZ2K540Jyl31JxUX7u05dvQ6a4ttotRlzU98Lng4xb8FL6r6Pozx%2FV7K%2BnUqU6lWW0926nKoOPMnzRS9p%2FVfM30XmdiXCd3a2tK4hUknOEXUoy9qEt9nKEuuU1s8%2BhaqU97OJWY1yXnweqzuaVaONpRa6dU0YpUVFJLolj3HF4TjUnSjJ04R2W8Pq58o9xY50WluZpddFi8lBvNP7TUo0%2BnPGK%2FP57z2S3qQX9XF%2FVitl0UVtseVahKNPUqM5vlh2MpTk%2F1IqUmvki48GV6txOrczWKc0uyh%2BrDL%2BbwXQnjUTi2lyg7H4X9stYBJoMADAABBJABJBJABAAJQAADAABAAAJIBr6lQVSlUpvpKnNfFM2CTlrVh1F49R4rw5TUa84r7FFR9faW%2FwB5f7OCkig6dPk1G5pYxiE174Tj%2FMu2mV9jAvHZ7fq03Ny%2FOM0NW4WjWkqmfbWWn9lY6LBo0bO5hTdKceeD25JRVSm13Lll3bfMu9KWTOoJlsU14Zjdv1JaVrTKc6XsU6UacHhtQpqHM%2Bjbw92dVWakk5wTaaay28SXRrPRnRdNHxPodNvO2Vck30sOTVp%2B2n5nXk%2FZOdcLdepvyfsHEfs6n4Rhto5Xqn8zXr0J096a6LCWW1t02Zt2hu8uTuPgrlLGUu6hOc1OdvSlUX%2BI6Sc9umGya2kVruUXVzyd6eMPDeMR7uq%2BBceRESRL5PyzpWpeInNsNPhQjyxSS8F0F41g2K9TByrurl4K5Z4O4Jyesr%2Bs6Sri7pQa9nsk5fuqUmy%2F6NRUKaSWFhJLwSX%2FACV%2Bgo%2FpEm%2BsaKj6Z3efii1W0cQivJHdS%2BbZPqZtVxj%2FAL%2Ff%2BGUAg0mAlkAAEogkgAkgkgAgAAAAAAAEohgAAAkgkgk824t05W99GusJVZpvzzGUJr3Nxl7xY3PJLlfcy58SaLG9oum9pp81Of6s%2FwAGUPUaUqVTE1ieE5LwljcxWwcW%2FwAHr0Wq2CT8pZ%2FHgtdpcJnRp1CqafcbHboVyIzK7asOspmKozFCZNWWE2%2BiTfuR23qKOOM5k5NzXhzHXmsQyee6pxrbUVF8zaeGnFOWz%2FdR0NT4xp0aHaOW23TMm%2FDCXU4UsNM6JvCz2VbuOpGZReG%2BKKF4oODfM5Yw008%2BjLhznUJFF1eM2JVDXqVTHOoa1WrsdOZzGs%2BLqsc%2BhLnqJeZjva5l0SDbbSzLDwvNLJXF7I0yXGGmbSabqzm%2BV4lWk%2BZvqo%2BzHbwSii3pYOfo1h2MEpbz5Um10XkjoI01Q4rsw32KUuvCJIJBaUEAE4ABAAAJIABAAAAAAAAJIAAIJBJBIAKVx5b4qQn4xx703%2BJdSv8AGlvz0FLvjL5P8ortWxZf6aXGxFPspYO1bTZw7Q7FsefvZ60zsW8zZlhpp7pppryZyoVcEVNXp00%2BaS27s7lkZGR1tvormo%2FRxbybdGUqbf2c80fg%2Bhh0j6OJRkldVe0pR%2BrTWUm%2F2vwOvLiiPNiLWPibb4mjjuz7%2FwATtJGlx9Tn7pn03hm0t5qdOjFTWcPfbOzwuiOxM4tvr0X9bbzOjGvGSymmTqRlshYn8z5rTwaVeZsVpmlXZU2WQRz7iWWWHhml3%2BC%2B84Eo5Zb9Bo8tPPiW0LWceqlkMOmgAbDzQSQACQAACCQAMEAAEAAAAAAAAkgAAgkEkEoAGG8t1VhKm%2BkotengzMAxudnllSnKjUdOW0lJr5nXs6qaN3juwi1CrHao24%2Fv4WV79ir2F73PqeZbHjLD2q5e7WpFiq0lOLj4lWueB6c5uX6VWUH9lqEsS%2Fe8CzUKudzW1OpOmu0hHmX2od780TXPi9JrlKLxPCuy%2BjZNc1K6qqS6ZUZR8PqpI1%2F6B37n%2FeoJdMqDb%2Bfedi34vt479oovvi3jD95tUeMqLeVcRflzGrmmaeV66X7%2FAAcb%2BgV3H%2Fz1jvzR6%2B9TRvaNoF3RlmV3GVNZ2UJNz8t3t8zbuOIaUn%2FaZb2UYvLfob9lUbWWsLuj3peZVbOOYVzlYo%2FJm4m0t2a9xNEXVbBzKtw%2Bi%2FLKNM8Ym%2FaU%2BeaS72XihT5IqK7kcbhzTHTiqk%2FrNbLwO4b6YcUef6izlLF9AAFpnBJBIBAJIAAJGAAQAAQACQAAQAAAQCSACQSQSAQSQSAUz6U58trD9bt1h%2BGIy3PN7HWVUliW1b4Kr5rwl4r4eBd%2FpbuPZo0%2FKc38kvukeMag2nn85Mdq5TaPa9GsqTPYNIvOZYLBSpJni%2BgcVum1Gq%2FSp4fvLv8AU9M03iCEkstbpb52fozO48X2d2Vt9xOrdcJ2Vw%2BarbwlLveHFv1ccZNet9G2lyW1vh%2BKqVE%2F9x0LfUotZyZ1qK8S6M4pGR%2B8vEmcqx4UtbT%2BxppP9Ztyl8XuZatPHebVe%2Bj4nD1DVI4bckoRWZTbSjFebKZ430Ww5vuR831cxabWhGvCnL2q8msU%2BvZxe%2FNPweOi9H060bW%2BNuZuNrnw%2FSJLfH%2Fri%2Bnq%2Fcu86f0bLNV1JNuWHJyby34tt97ZZCGNaWTXwZ7kgYrafNCMvGKMp6B4gAAAAAAJIJQAIJIAAAAIAAAAAAAAAAAAAAAJRB8VqqhGU30jFt%2BiWQDyP6SLztLqaXSCUF7lv88nnF9EvGqU3WlKb6ylKT97yVLU7dxZgUtlp9DXHjBRK7Vibem6tUo7J%2Bz%2Bq%2Bn8vcYK6NcuxNdnPJxZcbfiprq5L%2FUvxNr%2BlyX23%2F8ALKOpEykVeyi12FsuuM39lSb%2FAGmor5Zf3Fe1HVq1y12kvZTyoLaEX4pd783lmgZaNNtlkYRj4KnNyM1vHc9E4Nl2UJz7%2BX%2FgqOnaXJ4bRbrKn2cOXxwcOS0Sjqw9d4Vue0toPvSwzrFO%2Bj24xCVN%2BOUXE1VvYpni3R4zaAAOyoAAAEkAAkgAAEgAHyAAAACQAAQAAAAAACTj8UXHLRcF1nt%2Fl7%2F4L3nWqTUU23hIq2o1nWm5Pp0S8EU3T4xz7LqIcpb9Iq0rZbvBwNVsFL1LrVtsnIv7TB52tHsVzWnlOsWLpvPcchnp2raSqsNkef6jps6Taa95qqs1YdTjvaNJEsJE4LTjsiMS38L6Jz%2B3JHE0bTpVppJbZ3PW9KsFSppY7kUXTzpHX%2BKOX%2BgqHcZadvzM3qkcywbun2m%2BcGeLZEpYjd0SLpSjJflF2pzUkmujKtGlhHW0u6x7L6GyiefFnm%2Bojy%2BR1QAazGAAACSAASQSAAMggAgAAAAEgAAgAAAA17q9hS6v2v1V1%2Fka%2BtV5QiuV4y8FdTy8sz23cOkaaaOa1%2BDfur2VV77R7omKED4p9TapmXXJ6zS0orEfKtkcy%2Fte7B2zFVRMo9HEZtMqVO2w8PofN9w5Cst0dq9ppNYRv2MVgqjH5YaZWtLkjyfUuCGm%2BVM0Lfg%2Bbe57RVpLwNWVGKfRFmyS8nS9Rv0V3hvhqNFZxude9hhYOzRikvccy6WZHE10VxscpazRtrfO7OzY25gowXgdS1R1XE4tm2fMoHy443RsVTGy1opTN2yvfsyOgnkrMnhnSsKr8S6q3emVW1Z2jqAA0GcAAAEkAAkBkoA%2F%2F9k%3D' \
#   -H 'accept: application/json'
 
from fastapi import FastAPI
import uvicorn 

from keras.models import load_model
from PIL import Image, ImageOps  #pip install Pillow
import numpy as np
import pandas as pd
import sys
import cv2

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


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

"""Create a new fastapi endpoint for the /predict endpoint that takes an input of the image file and returns the predicted label"""
@app.get("/predict")
async def predict(imageFile='testImage.jpg'):
    # Run the inference function
    myPredictions = ModelInference_Keras(labelFile='../Week03-L5/teachableMachine_ImageBasedMaskClassifier/labels.txt', modelFile='../Week03-L5/teachableMachine_ImageBasedMaskClassifier/keras_model.h5', imageFile='testImage.jpg')
    return {"Prediction": myPredictions}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)