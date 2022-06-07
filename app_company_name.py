from matplotlib.pyplot import scatter
from numpy import character
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})
df = df.astype({'Rating':'int'})
df = df[['Company Name','Job Title', 'Job Description','Rating','Location','Headquarters','Founded','Type of ownership','Industry','Sector','Revenue','Competitors', 'Easy Apply', 'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Size_From(employees)','Size_To(employees)']]

def search_company(name):
    result = df.loc[df['Company Name'].str.lower().str.contains(name.lower()), ]
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

def run_company_type ():
    
    col1,col2 = st.columns([2,3])

    ownership = df['Type of ownership'].value_counts()
    ownership = ownership.to_frame()
    ownership.columns = ['counts']

    st.markdown("****")
    with st.expander('회사 유형 총 정리 테이블'):
        st.dataframe(ownership)

    chart_type = col1.radio('회사 유형 차트 확인',['그래프 닫기','원형 그래프','막대 그래프'])
    if chart_type == '원형 그래프':
        fig1 = px.pie(ownership,names = ownership.index, values='counts')
        st.plotly_chart(fig1)

    elif chart_type == '막대 그래프':
        fig2 = px.bar(ownership)
        st.plotly_chart(fig2)
    else:
        pass
    
    company_type = st.selectbox('회사 유형 선택',ownership.index)
    
    data = df.loc[df['Type of ownership'] == company_type,['Type of ownership','Job Title','Sector','Company Name','Founded','Industry']]
    st.dataframe(data)
    st.text('* 더 상세한 정보(연봉, 회사 규모 등)는 회사명 검색')




