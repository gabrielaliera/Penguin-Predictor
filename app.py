#Import required libraries
import numpy as np
from flask import Flask, request, render_template
import pickle

#Create flask app
app = Flask(__name__)

#Load pickle model
model = pickle.load(open('model.pkl', 'rb'))

#Home page that renders template index.html from templates folders
@app.route('/')
def home():
    return render_template('index.html')


#Web page that renders after clicking predict button
@app.route('/predict',methods=['POST'])
def predict():
   
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text='Your peguin species is: {}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)