import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title('Football dashboard')

results = pd.read_csv('./data/results.csv')
scorers = pd.read_csv('./data/goalscorers.csv')


results_checkbox = st.sidebar.checkbox("Results")
scorers_checkbox = st.sidebar.checkbox("Scorers")



if results_checkbox:


    column_names = results.columns.tolist()

    selected_column = st.selectbox("Choose an option:", column_names)

    options = results[str(selected_column)].unique().tolist()

    selected_options = st.multiselect(
        "Select one or more options:",
        options,
        default=None  # You can set default selected options if needed
    )

    results2 = results[results[str(selected_column)].isin(selected_options)]

    score_counts2 = results2[str(selected_column)].value_counts().to_dict()

    keys_list2 = list(score_counts2.keys())
    values_list2 = list(score_counts2.values())

    fig2, ax2 = plt.subplots()
    ax2.pie(values_list2, labels = keys_list2, shadow=True, startangle=90)

    col1, col2 = st.columns(2)

    with col1: 
        st.write(results)
    with col2:
        st.pyplot(fig2)



if scorers_checkbox :

    column_names = scorers.columns.tolist()

    selected_column = st.selectbox("Choose an option:", column_names)

    options = scorers[str(selected_column)].unique().tolist()

    selected_options = st.multiselect(
        "Select one or more options:",
        options,
        default=None  # You can set default selected options if needed
    )

    results2 = scorers[scorers[str(selected_column)].isin(selected_options)]

    score_counts2 = results2[str(selected_column)].value_counts().to_dict()

    keys_list2 = list(score_counts2.keys())
    values_list2 = list(score_counts2.values())

    fig2, ax2 = plt.subplots()
    ax2.pie(values_list2, labels = keys_list2, shadow=True, startangle=90)

    col1, col2 = st.columns(2)

    with col1: 
        st.write(scorers)
    with col2:
        st.pyplot(fig2)
