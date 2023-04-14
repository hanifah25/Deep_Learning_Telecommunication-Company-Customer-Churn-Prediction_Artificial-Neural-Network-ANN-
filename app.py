import streamlit as st
import joblib
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import  load_model


st.title('Churn prediction')

# Load The Models
with open('full_pipeline.pkl', 'rb') as file_1:
  model_pipeline = joblib.load(file_1)

model_ann = load_model('model_func_tune.h5')


membership_category = st.selectbox('membership_category', ('Gold Membership','Silver Membership','Premium Membership','No Membership','Basic Membership'))

feedback = st.selectbox('feedback', ('Too many ads','Poor Product Quality','Poor Customer Service','Poor Product Quality','Poor Website'))

points_in_wallet = st.number_input('jumlah poin: ', step=1)
st.write('jumlah poin di dompet anda Anda:', points_in_wallet)

avg_transaction_value =st.number_input('Rata-rata Transaksi: ', step=1)
st.write('Rata-rata Transaksi Anda:', avg_transaction_value)

#Dataframe random
data = pd.DataFrame({'membership_category' : [membership_category],
        'feedback' : [feedback],
        'points_in_wallet' : [points_in_wallet],
        'avg_transaction_value'	: [avg_transaction_value]})

model_full_pipeline= model_pipeline.transform(data[['membership_category','feedback','points_in_wallet','avg_transaction_value']])

if st.button('Predict'): 
    final_result_ada = model_ann.predict(model_full_pipeline)
    st.write('Hasil Prediksi: ')
    if final_result_ada == 1:
        st.subheader('Churn')
    else:
        st.subheader('Not Churn')


