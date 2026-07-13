import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import pickle

# credited_card_df=pd.read_csv(r'C:/Users/LENOVO/Desktop/Detecting Credit Card Fraud/creditcard.csv.zip')

# legit=credited_card_df[credited_card_df.Class==0]
# fraud=credited_card_df[credited_card_df.Class==1]

# legit_sample=legit.sample(n=len(fraud),random_state=2)
# credited_card_df=pd.concat([legit_sample,fraud],axis=0)

# X=credited_card_df.drop('Class',axis=1)
# Y=credited_card_df['Class']
# X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y, random_state=2)
# model = LogisticRegression(
#     solver='liblinear',
#     max_iter=1000,
#     random_state=42
# )


# model.fit(X_train, Y_train)

# #evaluate model performance
# train_acc=accuracy_score(model.predict(X_train),Y_train)
# test_acc=accuracy_score(model.predict(X_test),Y_test)

model = pickle.load(open("model.pkl", "rb"))

#web app
st.title("Credit Card Fraud Detection Model")
input_df=st.text_input('Enter all Required features Values')
input_df_splited=input_df.split(',')

submit=st.button("Submit")

if submit:
    features=np_df=np.asarray(input_df_splited,dtype=np.float64)
    prediction=model.predict(features.reshape(1,-1))


    if prediction[0]==0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fradulant Transaction")    
