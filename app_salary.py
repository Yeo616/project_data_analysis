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

def run_salary():


    sorting = st.radio('',['최저급여 정렬 기준 없음','최저급여 평점순 정렬','최저급여 설립연도별 정렬'])
    # 최저급여가 제일 높은 직무 중에서, 각 항목별로 정리

    if sorting == '최저급여 정렬 기준 없음':
        sorting = 'Job Title'
        df_from_max = df.loc[df['Salary_Estimate_From_(K)'] == df['Salary_Estimate_From_(K)'].max(),
        ['Job Title','Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Company Name','Rating','Founded','Type of ownership','Industry','Sector']]

        df_from_max =  df_from_max.sort_values('Job Title')

    elif sorting == '최저급여 평점순 정렬':
        df_from_max = df.loc[df['Salary_Estimate_From_(K)'] == df['Salary_Estimate_From_(K)'].max(),
        ['Rating','Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Job Title','Company Name','Founded','Type of ownership','Industry','Sector']]
 
        df_from_max =  df_from_max.sort_values('Rating',ascending=False)

    elif sorting == '최저급여 설립연도별 정렬':
        df_from_max = df.loc[df['Salary_Estimate_From_(K)'] == df['Salary_Estimate_From_(K)'].max(),
        ['Founded','Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Job Title','Company Name','Rating','Type of ownership','Industry','Sector']]
 
        df_from_max =  df_from_max.sort_values('Founded',ascending=False)

    
    group_df = round(df.groupby('Industry')[['Salary_Estimate_From_(K)','Salary_Estimate_To_(K)']].mean())
    # 산업별 급여 평균 테이블

    with st.expander('최저급여 제일 높은 테이블: 별점순/설립연도별 정렬 '):
        st.dataframe(df_from_max)

    with st.expander('산업별 급여 평균 테이블 '):
        st.dataframe(group_df)
   
    group_df['sum'] = group_df['Salary_Estimate_From_(K)'] + group_df['Salary_Estimate_To_(K)']
    # 전체적으로 그래프가 예쁘게 보이기 위해서, sum 컬럼을 만들어서, 정렬한 뒤 제거하였다.

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


