import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('model.pkl', 'rb')
model = pickle.load(file1)
file1.close()

#

data = pd.read_csv("corona_tested_individuals.csv")
st.title("Covid19 Desease Diagnosis")

st.write('Test date:')
year = st.selectbox('Year', [2019, 2020, 2021, 2022, 2023])
month = st.selectbox('Month', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
day = st.selectbox('Day', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                           25, 26, 27, 28, 29, 30])

st.write('Analyzing symptoms:')
cough = st.selectbox('Do you have cough?', ['No', 'Yes'], key=1)
fever = st.selectbox('Do you have fever?', ['No', 'Yes'], key=2)
sore_throat = st.selectbox('Do you have sore throat?', ['No', 'Yes'], key=3)
head_ache = st.selectbox('Do you have head ache?', ['No', 'Yes'], key=4)

st.write('Related questions:')
age_60_and_above = st.selectbox('are you age 60 or above?', ['No', 'Yes'], key=5)
gender = st.selectbox('select your gender', ['male', 'female'])
test_indication = st.selectbox('select test indication', data['test_indication'].unique())

if st.button('Diagnose'):

    if cough == 'Yes':
        cough = 1
    else:
        cough = 0

    if fever == 'Yes':
        fever = 1
    else:
        fever = 0

    if sore_throat == 'Yes':
        sore_throat = 1
    else:
        sore_throat = 0

    if head_ache == 'Yes':
        head_ache = 1
    else:
        head_ache = 0

    if age_60_and_above == 'Yes':
        age_60_and_above = 1
    else:
        age_60_and_above = 0

    if gender == 'male':
        gender = 1
    else:
        gender = 0

    if test_indication == 'Contact with confirmed':
        test_indication = 0
    elif test_indication == 'Abroad':
        test_indication = 1
    else:
        test_indication = 2

    query = np.array([year, month, day, cough, fever, sore_throat,
                      head_ache, age_60_and_above, gender, test_indication])

    query = query.reshape(1, -1)

    st.write("Input Data:")

    st.write(query)

    # prediction using logistic regression
    prediction = model.predict(query)[0]
    if prediction == 1:
        st.title('The person tested positive')
    else:
        st.title('The person tested negative')
