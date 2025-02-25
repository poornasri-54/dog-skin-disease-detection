from flask import render_template, jsonify, Flask, redirect, url_for, request, make_response
import os
import io
import numpy as np
from PIL import Image
import keras.utils as image
from keras.models import model_from_json

app = Flask(__name__)

SKIN_CLASSES = {
    0: 'Flea Allergy',
    1: 'Hotspot',
    2: 'Mange',
    3: 'Ringworm'

}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

def findMedicine(pred):
    if pred == 0:
        return "Corticosteroids (e.g., prednisone) for inflammation.\n Antihistamines (e.g., diphenhydramine) for itching.\n Flea control products (e.g., topical treatments, oral medications like NexGard)."
    elif pred == 1:
        return "Topical antibiotics or corticosteroids to reduce inflammation and infection.\n Oral antibiotics if the infection is severe.\n Antihistamines for itching."
    elif pred == 2:
        return "Topical or oral acaricides (e.g., ivermectin, selamectin).\n Corticosteroids to reduce inflammation (for demodectic mange).\n Antihistamines for itching."
    elif pred == 3:
        return "Antifungal medications (e.g., griseofulvin, terbinafine) for systemic treatment.\n Topical antifungal treatments (e.g., clotrimazole, miconazole)."


def findPrecaution(pred):
    if pred == 0:
        return "1. Regularly use flea prevention products.\n 2. Keep the environment clean; vacuum carpets and wash pet bedding frequently.\n 3. Monitor pets for signs of fleas and treat promptly."
    elif pred == 1:
        return "1. Keep the affected area clean and dry.\n 2. Prevent pets from licking or biting the area (use an Elizabethan collar if necessary).\n 3. Identify and address the underlying cause (e.g., allergies, parasites)."
    elif pred == 2:
        return "1. Isolate infected pets to prevent transmission.\n 2. Regularly clean and disinfect the living area.\n 3. Follow up with the veterinarian for treatment monitoring."
    elif pred == 3:
        return "1. Maintain good hygiene and clean the environment frequently.\n 2. Isolate infected animals to prevent spreading.\n 3. Treat all pets in the household if one is infected, as ringworm is contagious."
        
@app.route('/detect', methods=['GET', 'POST'])
def detect():
    json_response = {}
    if request.method == 'POST':
        try:
            file = request.files['file']
        except KeyError:
            return make_response(jsonify({
                'error': 'No file part in the request',
                'code': 'FILE',
                'message': 'file is not valid'
            }), 400)

        imagePil = Image.open(io.BytesIO(file.read()))
        # Save the image to a BytesIO object
        imageBytesIO = io.BytesIO()
        imagePil.save(imageBytesIO, format='JPEG')
        imageBytesIO.seek(0)
        print("detected ")
        path = imageBytesIO
        j_file = open('model.json', 'r')
        loaded_json_model = j_file.read()
        j_file.close()
        model = model_from_json(loaded_json_model)
        model.load_weights('model.h5')
        img = image.load_img(path, target_size=(224, 224))
        img = np.array(img)
        img = img.reshape((1, 224, 224, 3))
        img = img/255
        prediction = model.predict(img)
        pred = np.argmax(prediction)
        disease = SKIN_CLASSES[pred]
        accuracy = prediction[0][pred]
        accuracy = round(accuracy*100, 2)
        medicine=findMedicine(pred)
        precaution=findPrecaution(pred)
        
        print(f"Prediction: {pred}, Disease: {disease}, Medicine: {medicine}, Precaution: {precaution}")


        json_response = {
            "detected": False if pred == 2 else True,
            "disease": disease,
            "accuracy": accuracy,
            "medicine" : medicine,
            "img_path": file.filename,
            "precaution": precaution,

        }

        return make_response(jsonify(json_response), 200)

    else:
        return render_template('detect.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
