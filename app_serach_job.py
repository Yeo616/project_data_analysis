import pandas as pd
import streamlit as st

df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})
df = df.astype({'Rating':'int'})
df = df[['Job Title', 'Job Description','Company Name','Rating','Location','Headquarters','Founded','Type of ownership','Industry','Sector','Revenue','Competitors', 'Easy Apply', 'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Size_From(employees)','Size_To(employees)']]

def search_jobtitle(name):
    result = df.loc[df['Job Title'].str.lower().str.contains(name.lower()), ]
    result.sort_values('Rating')
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

