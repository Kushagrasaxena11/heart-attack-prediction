import streamlit as st
import numpy as np
import string
import pickle
# Loading the model from the storage to the code
with open('logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)


def main():
  st.sidebar.header("Heart Stroke Risk Prediction")
  st.sidebar.text("This a Web app that tells you the predicted wether you will have a stoke or not.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The Logistic regression Classifier was used.")


 
  gender = st.selectbox("Sex", ["Male","Female"])
  age = st.slider("Input Your age", 0, 100)
  hypertension = st.slider("Input your if you have hypertension with 0 for no and 1 for yes",0,1)
  heartdisease = st.slider("Input your if you have heartdisease with 0 for no and 1 for yes",0 ,1)
  evermarried = st.slider("input your if you have married with 0 for no and 1 for yes",0,1)
  glucoselevel = st.slider("Put your average glucose level",150.0, 300.000)
  smokingstatus = st.selectbox("smoking status",["formerely smoked","never smokes","smokes"])
  bmi = st.slider("Input your BMI",0.0,70.0)

  inputs = [[gender,age,hypertension,heartdisease,evermarried,glucoselevel,smokingstatus,bmi]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
       st.write("Not very Proabable you will have a stoke soon but still take good care of yourself regardless")
    else:
       st.write("It is Probable you might have a stroke soon therfore you should take better care of yourself")
   


if __name__ =='__main__':
  main()
