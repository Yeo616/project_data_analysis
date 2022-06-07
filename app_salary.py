import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import plotly.graph_objects as go


df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})
df = df.astype({'Rating':'int'})
df = df.astype({'Salary_Estimate_From_(K)':'int'})
df = df.astype({'Salary_Estimate_To_(K)':'int'})

# df = df[['Job Title', 'Job Description','Company Name','Rating','Location','Headquarters','Founded','Type of ownership','Industry','Sector','Revenue','Competitors', 'Easy Apply', 'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Size_From(employees)','Size_To(employees)']]


def run_salary():

    df_from_max = df.loc[df['Salary_Estimate_From_(K)'] == df['Salary_Estimate_From_(K)'].max(),
        ['Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Job Title','Company Name','Rating','Founded','Type of ownership','Industry','Sector']]
  
    sorting = st.radio('',['정렬 기준 없음','별점순 정렬','설립연도별 정렬'])
    if sorting == '정렬 기준 없음':
        sorting = 'Job Title'
    elif sorting == '별점순 정렬':
        sorting = 'Rating'
    elif sorting == '설립연도별 정렬':
        sorting = 'Founded'


    df_from_max =  df_from_max.sort_values(sorting,ascending=False)
    
    group_df = round(df.groupby('Industry')[['Salary_Estimate_From_(K)','Salary_Estimate_To_(K)']].mean())

    with st.expander('최저급여 제일 높은 테이블: 별점순/설립연도별 정렬 '):
   
        st.dataframe(df_from_max)

    with st.expander('산업별 급여 테이블 '):
   
        st.dataframe(group_df)
   
    group_df['sum'] = group_df['Salary_Estimate_From_(K)'] + group_df['Salary_Estimate_To_(K)']


    # 급여 받는 그래프
    group_df= group_df.sort_values('sum',ascending = False)
    group_df = group_df.drop('sum',axis =1)

    st.text('')
    st.text('평균적으로 높은 급여를 받는 산업순 그래프')
    fig2 = px.bar(group_df)
    st.plotly_chart(fig2)

    st.markdown("****")
    st.text('')
    st.text('급여 분포도')
    fig = px.scatter(group_df,'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)')
    st.plotly_chart(fig)
    # 안예쁨. 
    # 버블버블버블!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

