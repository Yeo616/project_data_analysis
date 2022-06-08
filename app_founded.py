import streamlit as st
import pandas as pd

df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})
df = df.astype({'Rating':'int'})
# df = df.astype({'Size_To(employees)':'int'})
df = df.astype({'Size_From(employees)':'int'})
df = df[['Founded', 'Size_From(employees)','Size_To(employees)','Job Title', 'Job Description','Sector','Company Name','Headquarters','Industry','Rating','Type of ownership']
]

def run_founded():
    
    st.text('설립연도 범위 별로 테이블 보기')
    st.markdown("****")
    
    start_year = st.slider('연도 시작 범위 선택',1682,2018)

    end_year = st.slider('연도 끝 범위 선택',1698,2019)

    if start_year <= end_year:
        data = df.loc[(df['Founded']>= start_year) & (df['Founded'] <= end_year),]
    else:
        st.error('연도 시작 수치가 연도 끝 범위보다 작아야합니다.')

    st.dataframe(data)
