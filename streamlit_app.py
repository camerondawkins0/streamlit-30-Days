import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('./iris')
df_peng = pd.read_csv('./penguin')
df_peng.dropna(inplace=True)

iris_col = ['sepal_length',
            'sepal_width',
            'petal_length',
            'petal_width']

peng_col = ['bill_length_mm',
            'bill_depth_mm',
            'flipper_length_mm',
            'body_mass_g']

dataset_selection = st.sidebar.selectbox('Select Dataset to View',
                                 ('Iris', 'Penguin'))

if dataset_selection == 'Iris':
    
    select_metric = st.sidebar.selectbox(
        "Metric",
        iris_col
    )
    
    setosa = pd.DataFrame(df_iris.loc[df_iris['species'] == 'setosa'],
                          columns=[select_metric])
    versicolor = pd.DataFrame(df_iris.loc[df_iris['species'] == 'versicolor'],
                              columns=[select_metric])
    virginica = pd.DataFrame(df_iris.loc[df_iris['species'] == 'virginica'],
                             columns=[select_metric])
    
    d = {'Setosa': setosa,
         'Versicolor': versicolor,
         'Virginica': virginica}

    add_selectbox = st.sidebar.selectbox(
        "Which species would you like to view?",
        ("Setosa", "Versicolor", "Virginica", "All")
    )

    st.header(add_selectbox)
    
    fig = plt.figure(figsize=(8,4))
    if add_selectbox != 'All':
        st.dataframe(d[add_selectbox], width=700)
        plt.plot(d[add_selectbox][select_metric],
                 marker='o',
                 label=select_metric,
                )
        st.pyplot(fig)
    if add_selectbox == 'All':
        st.dataframe(pd.concat([setosa, versicolor, virginica],
                               ignore_index=True,
                               names=[select_metric, 'species']),
                               use_container_width=True
                     )
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
        plt.figure(figsize=(8,4))
        d_axes = [ax1, ax2, ax3]
        dfs = [setosa, versicolor, virginica]
        
        for ax in d_axes:
            for df in dfs:
                ax.plot(df[select_metric])
                dfs.copy().pop(0)
        st.pyplot(fig)

    fig.legend()        

if dataset_selection == 'Penguin':

    add_selectbox = st.sidebar.selectbox(
        "Which sex would you like to view?",
        ("Male", "Female")
    )

    select_metric = st.sidebar.selectbox(
        "First column",
        peng_col
    )

    ind = peng_col.index(select_metric)
    peng_col = peng_col.copy()
    peng_col.pop(ind)

    select_col2 = st.sidebar.selectbox(
        "Second Column",
        peng_col
    )
 
    M = pd.DataFrame(df_peng.loc[df_peng['sex'] == 'Male'],
                    columns=[select_metric, select_col2])
    F = pd.DataFrame(df_peng.loc[df_peng['sex'] == 'Female'],
                    columns=[select_metric, select_col2])

    st.header(add_selectbox)

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    plt.figure(figsize=(5,5))

    if add_selectbox == "Male":
        st.dataframe(M, use_container_width=True)
        ax1.plot(M[select_metric], label=select_metric)
        ax2.plot(M[select_col2], label=select_col2, color='orange')
    if add_selectbox == "Female":
        st.dataframe(F, use_container_width=True)
        ax1.plot(F[select_metric], label=select_metric)
        ax2.plot(F[select_col2], label=select_col2, color='orange')

    fig.legend()
    st.pyplot(fig)
