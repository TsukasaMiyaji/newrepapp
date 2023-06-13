#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
from numpy import percentile
from io import StringIO
from pandas.api.types import is_numeric_dtype
import seaborn as sns
import seaborn as sb
import matplotlib.pyplot as plt


st.title('Streamlit Application')


st.write("""
            # Upload your CSV file
            You can drag and drop your own csv file below.
            """)




uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    bytes_data = uploaded_file.getvalue()
    

    
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    

    
    string_data = stringio.read()
    

    
    dataframe = pd.read_csv(uploaded_file)
    dataframe = dataframe.dropna()
    dataframe = dataframe[list(dataframe.columns[~dataframe.columns.duplicated()])]
    dataframe
    
    
    st.write("The number of rows is: ",len(dataframe.index))
    st.write("The number of column is: ",len(dataframe.columns))
    st.write("The column types in this dataset: ",dataframe.dtypes)
    
    
    option = st.selectbox(
    'Your selected columns',list(dataframe.columns.values))

    st.write('You selected:', option)
    
    group_labels = ['Density Graph']

    
    if is_numeric_dtype(dataframe[option]) == True:
        st.write("Here is five numbers summery below: ")
        st.write(dataframe[option].describe())
        
        
        fig, ax = plt.subplots()
        ax.hist(dataframe[option], bins=30)

        st.pyplot(fig)
    else:
        val_count = dataframe[option].value_counts()
        val_count

        fig = plt.figure(figsize=(10, 4))
        sns.countplot(x=option, data=dataframe)

        st.pyplot(fig)
        
        
        
        
        
        
        
        
        
        
        
        
        
        