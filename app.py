#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from keras_preprocessing.image.utils import img_to_array
from keras.models import load_model

#load model
model =load_model("model/final_wsensemble1.h5")

print('@@ Model loaded')

def pred_straw_dieas(str_plant):
  test_image = load_img(str_plant, target_size=(224,224)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value

  if pred == 0:
    return "Angular Leaf Spot", 'AngularLeafSpot.html' # if index 0 angular
  elif pred == 1:
    
      return 'Blossom Blight', 'BlossomBlight.html' # # if index 1 blossom
  elif pred == 2:
      return 'Gray mold', 'GreyMold.html'  # if index 2  graymold
  elif pred == 3:
    return 'Healthy Leaf','healty.html'
  elif pred == 4:
    return 'Leaf Spot','LeafSpot.html'      
    
  else:
    return "Powdery Mildew Leaf", 'PowderyMildew.html' 


    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
@app.route("/exp", methods=['GET', 'POST'])
def exp():
        return render_template('exp.html')
@app.route("/cure", methods=['GET', 'POST'])
def cure():
        return render_template('cure.html') 
@app.route("/contact", methods=['GET', 'POST'])
def contact():
        return render_template('contact.html') 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_straw_dieas(str_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,) 
    
    
