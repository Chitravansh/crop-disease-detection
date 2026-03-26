# 🌿 ArogyaFasal — AI-Powered Crop Health Platform

ArogyaFasal is a **full-stack AI-driven agricultural platform** that helps farmers detect crop diseases, get intelligent recommendations, access expert guidance, and monitor weather conditions — all in one place.

---

# 🚀 Key Features

## 🌱 AI Crop Disease Detection

- Upload leaf images using drag & drop
- CNN-based deep learning model (TensorFlow/Keras)
- Predicts:
  - Crop type
  - Disease name
  - Confidence score

---

## 🤖 AI Assistant (Chatbot)

- Powered by **Groq API**
- Provides:
  - Disease explanation
  - Treatment suggestions
  - Fertilizer advice
  - Prevention methods

- Features:
  - Multilingual responses
  - Markdown formatting
  - Context-aware responses
  - Typing animation
  - Conversation history
  - Floating widget UI
  - Integrated CNN → Chatbot context sharing

---

## 👨‍⚕️ Expert System

- Find agricultural experts easily

### Local Experts

- Based on user location
- Includes:
  - Name
  - Expertise
  - Contact details
  - Organization

### Global Experts

- Agricultural universities
- Research institutes
- Helplines

---

## 🌦 Weather Intelligence Module

- Real-time weather insights for farmers based on Geo-location

Includes:

- Temperature
- Humidity
- Rain probability
- Wind speed
- 7-day forecast

---

## 🌍 Multilingual Support

- Powered by Flask-Babel
- Supported languages:
  - English
  - Hindi
  - Marathi
  - Punjabi

---

## Geo-Location Based Personalization

- Integrated browser-based geolocation
  -Used across:
  - Weather module
  - Expert recommendations

---

## 🔐 Authentication System

- Register / Login / Logout
- Secure password hashing (bcrypt)
- Session-based authentication
- Protected routes

---

# 🧠 Tech Stack

## Backend

- Python (Flask)
- MongoDB (PyMongo)

## Frontend

- HTML, CSS, Bootstrap
- JavaScript, jQuery

## AI / ML

- TensorFlow 2.3
- CNN Model for image classification
- Groq API for chatbot

## Others

- Flask-Babel (i18n)
- Git + GitHub

---

# 📁 Project Structure

```bash
project/

app/
│
├── __init__.py
│
├── routes/
│   ├── auth_routes.py
│   ├── prediction_routes.py
│   ├── chatbot_routes.py
│   ├── experts_routes.py
│   ├── weather_routes.py
│
├── services/
│   ├── prediction_service.py
│   ├── chatbot_service.py
│   ├── expert_service.py
│   ├── weather_service.py
│
├── models/
│   ├── user_model.py
│   ├── expert_model.py
│
├── database/
│   └── mongo.py
│
├── scripts/
│   └── seed_experts.py
│
├── utils/
│   ├── auth_decorator.py
│   ├── password_utils.py
│
├── templates/
├── static/
│   ├── css/
│   ├── js/
│
├── data/
│   └── disease_labels.py
│
translations/

config.py
app.py
requirements.txt
babel.cfg
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Chitravansh/crop-disease-detection.git
cd project
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in root directory:

```env
SECRET_KEY=your_secret_key
MONGO_URI=your_mongodb_connection_string
DB_NAME=your_database_name
GROQ_API_KEY=your_groq_api_key
```

---

## 5️⃣ Ensure Upload Folder Exists

```bash
mkdir uploads
```

---

## 6️⃣ Seed experts

```bash
python -m app.scripts.seed_experts
```

## 7️⃣ Run the Application

```bash
flask run
```

App will run at:

```bash
http://127.0.0.1:5000/
```

---

# 🧪 Sample Workflow

1. Login/Register
2. Upload crop leaf image
3. Get disease prediction
4. Open AI Assistant
5. Ask for treatment advice
6. Check weather conditions
7. Contact agricultural experts

---

# ⚠️ Important Notes

- Python version must be:

```bash
python==3.8.5
```

- TensorFlow version must be:

```bash
tensorflow==2.3.0
numpy==1.18.5
h5py==2.10.0
keras==2.4.3
```

---

# 📌 Assumptions

- Model works only on trained crops
- Limited disease classes
- Requires clear leaf images

---

# 📈 Advantages

- Fast disease detection
- AI-powered agricultural guidance
- Multilingual accessibility
- Integrated expert + weather system
- Scalable architecture

---

# 🔮 Future Enhancements

- 📞 Expert booking system
- 📊 Farmer dashboard
- 📱 Mobile app version
- 🧠 Personalized crop recommendations

---

# 🧾 Dataset

- Plant Disease Dataset (Kaggle / Google Dataset Search)

---

# 👨‍💻 Contributors

- **Chitravansh Mohan**
- **Divya Rai**
- **Deependra Bhatt**

---

# 🏁 Conclusion

ArogyaFasal transforms traditional farming into **AI-assisted agriculture** by combining:

- Deep Learning
- Conversational AI
- Real-time Weather
- Expert Systems

This platform helps farmers make **faster, smarter, and data-driven decisions**.

---
