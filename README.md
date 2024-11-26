**Crop Recommendation System**
The Crop Recommendation System is a web-based application that helps farmers and agricultural professionals identify the most suitable crop to grow based on specific soil and environmental conditions. By leveraging a machine learning model and a user-friendly interface, the system provides accurate crop recommendations to improve agricultural productivity.

**Features** ✨
User-Friendly Interface: A simple and intuitive web form for entering soil and climate parameters.
Machine Learning Integration: Uses a pre-trained machine learning model to recommend crops based on input values.
Real-Time Predictions: Instantly returns the most suitable crop after submission.
Responsive Design: Clean and visually appealing interface, compatible with desktop and mobile devices.
**Technologies Used** 💻
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Machine Learning: Random Forest Classifier trained on agricultural datasets
Dataset: Contains soil compositions (Nitrogen, Phosphorus, Potassium), pH, rainfall, temperature, and humidity.
**Input Parameters** 
The system requires the following inputs:

Nitrogen (N): Amount of nitrogen in the soil.
Phosphorus (P): Amount of phosphorus in the soil.
Potassium (K): Amount of potassium in the soil.
Temperature (°C): Average temperature of the region.
Humidity (%): Humidity level of the region.
pH Value: pH level of the soil.
Rainfall (mm): Average annual rainfall in millimeters.
**How It Works** 
User Input: The user provides soil and climate parameters through the form.
**Backend Processing:**
The backend receives the input via a POST request.
The values are passed to the trained machine learning model.
Model Prediction: The model predicts the most suitable crop.
Output: The recommended crop is displayed to the user.
**Screenshots** 
Home Page:
![image](https://github.com/user-attachments/assets/9dcc9252-3720-4327-9c31-39728f49c156)

Recommendation Output:
![image](https://github.com/user-attachments/assets/18addf6b-e685-419c-bb4d-28a0d1ad20d5)


**Installation and Setup**
Follow these steps to run the project locally:

Clone this repository:


git clone https://github.com/your-username/crop-recommendation-system.git
cd crop-recommendation-system
Install the required dependencies:

pip install -r requirements.txt
Ensure the dataset (crop_data.csv) and trained model file (crop_recommendation_model.pkl) are in the same directory as app.py.

**Start the Flask server**:

python app.py
Open your browser and go to:

**Dataset**
The dataset includes information on soil and weather conditions and their relationship with different crops. Each row in the dataset represents:

Soil nutrients (N, P, K)
Environmental factors (temperature, humidity, rainfall)
Soil pH
Suitable crop for the conditions
**Future Improvements**
Add multi-language support for better accessibility.
Integrate real-time weather API for dynamic input values.
Deploy the project to a live server (e.g., Heroku, AWS, etc.).
Enhance UI/UX for a more interactive user experience.
**Contributing**
Contributions are welcome! Feel free to:

**Fork the repository**
Create a new branch for your feature/bug fix
Submit a pull request
**License**📄
This project is licensed under the MIT License. See the LICENSE file for details.

