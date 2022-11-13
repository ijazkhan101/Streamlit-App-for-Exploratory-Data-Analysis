import streamlit as st               
import seaborn as sns
import pandas as pd
import numpy as np 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report 

# Webapp Title
st.markdown('' 
'# ** Exploratory Data Analysis   ** ' '')
st.markdown('Web Application')


# how to upload a file from PC

with st.sidebar.header("Upload your dataset(.csv) file"):
    upload_file = st.sidebar.file_uploader("Upload your file",type=['csv'])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")


    # profiling report for pandas

    if upload_file is not None:
        @st.cache
        def load_csv():
            csv=pd.read_csv(upload_file)
            return csv

        df = load_csv()
        pr = ProfileReport(df,explorative=True)
        st.header("** input DF **")
        st.write(df)
        st.write('--------')
        st.header('******Profiling report with pandas ***')
        st_profile_report(pr)
    else:
        st.info('Awaiting for CSV file ')
        if st.button('Press to use Example data'):
            def load_data():
                a = pd.DataFrame( np.random.rand(100,5),
                                columns=['age','banana','codanics','new','Ear'])
                return a
            
            df=load_data()
            pr = ProfileReport(df,explorative=True)
            pr = ProfileReport(df,explorative=True)
            st.header("** input DF **")
            st.write(df)
            st.write('--------')
            st.header('******Profiling report with pandas ***')
            st_profile_report(pr)

