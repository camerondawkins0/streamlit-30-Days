import streamlit as st
import pandas as pd
from data import df_peng, df_iris

df_peng.dropna(inplace=True)

dataset_selection = st.selectbox('Select Dataset to View',
             ('Iris', 'Penguin'))

if dataset_selection == 'Iris':
    setosa = pd.DataFrame(df_iris.loc[df_iris['species'] == 'setosa'],
                          columns=['sepal_length', 'sepal_width'])
    versicolor = pd.DataFrame(df_iris.loc[df_iris['species'] == 'versicolor'],
                              columns=['sepal_length', 'sepal_width'])
    virginica = pd.DataFrame(df_iris.loc[df_iris['species'] == 'virginica'],
                             columns=['sepal_length', 'sepal_width'])

    add_selectbox = st.sidebar.selectbox(
        "Which species would you like to view?",
        ("Setosa", "Versicolor", "Virginica")
    )

    st.header(add_selectbox)

    if add_selectbox == 'Setosa':
        st.dataframe(setosa, width=700)
        st.line_chart(setosa)
    if add_selectbox == 'Versicolor':
        st.dataframe(versicolor, width=700)
        st.line_chart(versicolor)
    if add_selectbox == 'Virginica':
        st.dataframe(virginica, width=700)
        st.line_chart(virginica)

if dataset_selection == 'Penguin':
    M = pd.DataFrame(df_peng.loc[df_peng['sex'] == 'Male'],
                     columns=['flipper_length_mm', 'bill_length_mm'])
    F = pd.DataFrame(df_peng.loc[df_peng['sex'] == 'Female'],
                     columns=['flipper_length_mm', 'bill_length_mm'])
    
    add_selectbox = st.sidebar.selectbox(
        "Which sex would you like to view?",
        ("Male", "Female")
    )

    st.header(add_selectbox)
    
    if add_selectbox == "Male":
        st.dataframe(M)
        st.line_chart(M)
    if add_selectbox == "Female":
        st.dataframe(F)
        st.line_chart(F)