
# 💳 Credit Card Fraud Detection

A Machine Learning web application that detects whether a credit card transaction is **Legitimate** or **Fraudulent** using **Logistic Regression**. The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

## 🚀 Live Demo

🔗 **Try the App Here:**

https://detecting-credit-card-fraud-vgwrhrds5kvclfbghrt6gu.streamlit.app

---

## 📌 Features

- Detects fraudulent credit card transactions
- User-friendly Streamlit web interface
- Logistic Regression classification model
- Balanced dataset using random under-sampling
- Real-time prediction from user input
- Fast and lightweight application

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📂 Dataset

This project uses the **Credit Card Fraud Detection Dataset** containing anonymized credit card transactions.

### Dataset Information

- **Total Transactions:** 284,807
- **Fraudulent Transactions:** 492
- **Legitimate Transactions:** 284,315

Because the dataset is highly imbalanced, random under-sampling is used to create a balanced training dataset.

---

## ⚙️ Machine Learning Workflow

1. Load the dataset
2. Explore the data
3. Handle class imbalance using random under-sampling
4. Split data into training and testing sets
5. Train Logistic Regression model
6. Evaluate model accuracy
7. Predict whether a transaction is fraudulent
8. Deploy using Streamlit

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── app.py
├── creditcard.csv.zip
├── requirements.txt
├── README.md
└── screenshots/
    ├── homepage.png
    └── prediction.png
```

---

## 📊 Model

**Algorithm Used**

- Logistic Regression

The model is trained using Scikit-learn's Logistic Regression classifier.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
```

Move into the project directory

```bash
cd Credit-Card-Fraud-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 Usage

Enter all **30 feature values** separated by commas and click **Submit**.

Example:

```
0,-1.359807134,-0.072781173,2.536346738,...
```

The application predicts whether the transaction is:

- ✅ Legitimate Transaction
- 🚨 Fraudulent Transaction

---

## 📈 Results

The model is evaluated using:

- Training Accuracy
- Testing Accuracy

Performance is measured using **Accuracy Score**.

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## 🔮 Future Improvements

- Save trained model using Pickle
- Add probability/confidence score
- Improve UI with individual input fields
- Deploy on Streamlit Community Cloud
- Experiment with Random Forest and XGBoost
- Add ROC Curve and Confusion Matrix

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Prakriti Bhandari**

- GitHub: https://github.com/Prakritibhandari07
- LinkedIn: https://linkedin.com/in/prakriti-bhandari-18pp

If you found this project helpful, don't forget to ⭐ the repository.
