# Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches

In this project, I have developed the strawberry plant disease prediction  and classification application. This Application is very helpful for the farmers. By  using this application farmer can upload images of diseased plants and get the  prediction of the diseases of the main 5 strawberry plant diseases that I have implemented. After the user has uploaded the image the disease description and cure methods. The Web application has a simple UI with four primary pages: home, expert, pesticide, and contact us.

## Designing of the Deep Learning Model

The project implementation contains two stages, the First stage is the training and designing of the Deep Learning Model and the second stage is the Development of the Web application using the designed DL Model.
In this project, firstly I trained and designed the DL Model. The Project dataset contains 2,750 images used to train and validate the model. I collected 310 separate images for testing the web application for disease prediction. The dataset contains 5 diseases of the strawberry plant. and 1 healthy leaf. The diseases which I included in the dataset are Angular Leafspot, Blossom Blight, Gray Mold, Leaf Spot, and Powdery Mildew Leaf. In this project, I created a novel ensemble model using a Iighted ensemble average. For creating the Ensemble model, I selected three pre-trained CNN models. The selected CNN models are Xception, Densenet169, and MobileNet. 

![image](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/84635081-6ad7-4dd4-88ba-3411875c4357)

##  Web Application

After training the model, I save the model file with the .h5 extension.  So, the second stage of the project is the implementation of the b application to predict strawberry plant diseases. 
I have used Html, CSS, JavaScript, and Bootstrap for the front end of the Website. I have used Flask and Python for the backend of the Website. I have written the code in the spyder IDE. After running the app.py file in the project one URL will be generated. By pasting that URL in the browser the strawberry plant diseases detection and classification application will be started.
The main features of the Web application
1)	Home Page
2)	Upload image
3)	Gallery 
4)	Experts Page
5)	Pesticides Page
6)	Contact Us Page
7)	Disease Description and Cure Page
 
## Home Page

![Screenshot (8267)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/dda02447-fe33-4269-aa25-082ed723dc34)

![Screenshot (8272)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/7c07664f-71a5-4e64-99d9-e83b242a3bcb)

![Screenshot (8273)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/0a2d2180-ee0e-4bbc-83db-76dc39de17a2)


The above images are the home page. The Home page contains a navigation bar with options such as Experts, Pesticides, and Contact us.
## Upload Image

![Screenshot (8266)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/55c5595d-c8a2-4dbc-98e3-ea0d60d804c2)

In the above image, the user must select and upload the image of the diseased plant leaf/floIr/fruit. The user must click on the Predict button to get the prediction of the image that was uploaded.
## Gallery

![Screenshot (8269)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/321351a0-4a3c-4462-80c3-0ae98cc19afe)

The above image shows the gallery of strawberry farming by the farmers. 
## Experts Page	
 
![Screenshot (8275)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/1ec1e03e-e29e-4c9b-9eef-47c4caa625db)

![Screenshot (8276)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/9e89fda4-409f-4087-a7a1-90833b68fa87)

The above images shows the experts contact page. After the farmers got the prediction of the disease, description and the cure methods of the diseases if still the farmers have doubts and want to contact the experts such as botanists, horticulturists, agronomists, plant pathologists, and plant geneticists. So that farmers can contact those experienced people to get suggestions for prediction and cure of strawberry diseases. This page contains the scientists/ expert’s image, Professional, Contact number and email.
## Pesticides page
 
![Screenshot (8270)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/0af9f28c-a8c7-426a-8c4f-86f82cfd478e)

![Screenshot (8274)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/f140eb39-6728-4538-9193-475689891bbc)

![Screenshot (8271)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/92e919d1-cb73-420b-b1e7-1735964c0a9f)

The above images shows the pesticides page of the Website. After the farmers got the prediction of the disease, description, and the cure methods of the diseases if the farmers want to know about the different pesticides that cure of the predicted diseases. So, the farmers can visit this page and check the information of different pesticides for the different types of strawberry diseases.
## Contact Us 
 
![Screenshot (8277)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/e9312f1d-c715-49f0-b0af-f0bf07445985)

The above images shows the Contact Us page. This page contains the contact information of the Website admin. It contains the mobile number, email, LinkedIn, and more. By using this page, the farmers/users can contact the admin of the Website if they encounter any problem.
## Disease Description and Cure Page

![Screenshot (8279)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/3466ef25-eaba-4fdf-9f0d-5d2f28db41e1)

![Screenshot (8280)](https://github.com/gslprasanna/Prediction-of-Strawberry-Plant-Diseases-using-Deep-Learning-Approaches/assets/63353137/0ec3de80-fb7b-4cea-991f-292d04217082)

The above images is the disease description and cure page of all diseases. After the user has uploaded the image to the Web application, the model will predict the disease and gives the disease description and cure methods of the predicted angular leaf spot disease. The Website shows the description and the cure methods in three different languages English, Hindi, and Telegu.
