import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modelTraning = st.container()


st.write('ola,mundo')
with header:
    st.title("Welcome! This is my first project of Data Science.")
    st.text("In this project I look in to transactions of taxis yellows in NYC. ... ")

with dataset:
    st.header("NYC taxis dataset.")
    st.text("I foudn this dataset ou ....")
    taxi_data = pd.read_csv(r'C:\Users\Pichau\Downloads\cruso-streamlit\census.csv')
    st.write(taxi_data.head())
    st.write(taxi_data.describe())
    pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts())
    st.bar_chart(pulocation_dist)

with features:
    st.header("The features I created.")

with modelTraning:
    st.header("Time to train the model")
    st.text("Here you get to choose the hyperparameters of the model and see how the perfomance chenge.")
