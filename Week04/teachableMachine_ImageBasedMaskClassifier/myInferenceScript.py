from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import pandas as pd

# Load labels.txt
labels = pd.read_csv('labels.txt', header=None, delimiter=' ')
labels.columns= ['Prediction', 'Label']

# Load the model
model = load_model('keras_model.h5')

# Load the data and transform it:
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('/content/gdrive/MyDrive/PGSS2022/L5--7-15-2022/MaskData/with_mask/106-with-mask.jpg')
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
print(PredictionLabel)

