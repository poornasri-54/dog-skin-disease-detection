# dog-skin-disease-detection
A deep learning model using CNN (XceptionV3) for detecting dog skin diseases

🐶 Dog Skin Disease Detection Using Deep Learning
📌 Overview
This project is a Flask-based web application that detects four common dog skin diseases using a deep learning model (Xception CNN). Users can upload an image of a dog's skin, and the model will predict the disease along with medications and precautions.

🚀 Features
✅ Deep Learning Model: Uses Xception CNN for high-accuracy classification
✅ Image Classification: Detects Flea Allergy, Hotspot, Mange, and Ringworm
✅ Medicine & Precautions: Provides treatment suggestions and preventive measures
✅ User-Friendly Web App: Simple UI for easy image upload and prediction
✅ Flask API: Handles image processing and model inference

📂 Project Structure
graphql
Copy
Edit
📁 dog-skin-disease-detection
 ├── 📂 templates/        # HTML files for frontend
 ├── 📂 static/           # CSS, JS, images
 ├── 📂 model/            # Trained model files (model.json, model.h5)
 ├── app.py              # Flask backend
 ├── requirements.txt    # Dependencies
 ├── README.md           # Project documentation (this file)
🛠 Technologies Used
🔹 Python
🔹 Flask
🔹 TensorFlow & Keras
🔹 OpenCV
🔹 NumPy, PIL

🎯 How It Works
1️⃣ User Uploads Image → Upload a dog's skin image via the web UI
2️⃣ Model Predicts Disease → The trained model classifies the disease
3️⃣ Provides Medication & Precautions → Displays treatments & preventive tips

🏗 Installation & Setup
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/dog-skin-disease-detection.git
cd dog-skin-disease-detection
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Flask app:

bash
Copy
Edit
python app.py
4️⃣ Open in browser:

bash
Copy
Edit
http://127.0.0.1:3000
Upload an image to get the disease prediction, accuracy, medications, and precautions!

📈 Model Training
Dataset: 400+ images of dog skin diseases
Model: Xception CNN trained for classification
Accuracy: 96% 
