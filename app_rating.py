import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import plotly.graph_objects as go


df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})

df['Rating'] = round(df['Rating'],1)
# pd.options.display.float_format ='{:1f}'.format

df = df[['Rating','Job Title', 'Job Description','Company Name','Location','Headquarters','Founded','Type of ownership','Industry','Sector','Revenue','Competitors', 'Easy Apply', 'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Size_From(employees)','Size_To(employees)']]


def run_rating():
    
    col1,col2 = st.columns([1,3])

    rating = st.slider('별점 선택', 1.0,5.0,1.0,0.1 )

    df_rating = df.loc[df['Rating'] == rating, 
        ['Rating','Job Title','Company Name','Industry',
        'Sector','Revenue','Salary_Estimate_From_(K)','Salary_Estimate_To_(K)',
        'Size_From(employees)','Size_To(employees)']]
    st.dataframe(df_rating)
    
    if st.checkbox('산업별로 묶어 급여 평균 보기'):
        group_df_rating = round(df_rating.groupby(['Rating','Industry'])[['Salary_Estimate_From_(K)','Salary_Estimate_To_(K)']].mean())
        st.dataframe(group_df_rating)
    else:
        pass

    if st.checkbox('산업별로 묶어 회사규모 평균 보기'):
        st.text('"<NA>"로 표시된 부분은 그 이상이라는 뜻')
        group_df_rating = round(df_rating.groupby(['Rating','Industry'])[['Size_From(employees)','Size_To(employees)']].mean())
        st.dataframe(group_df_rating)
    else:
        pass

    st.markdown("****")
    # 급여 분포도그래프
    st.write(' ')
    st.write('해당 별점 범위에 해당하는 급여 범위 산점그래프')
    fig = px.scatter(df_rating, 'Salary_Estimate_From_(K)', 
        'Salary_Estimate_To_(K)', )
    
    st.plotly_chart(fig)
    
    st.markdown("****")
    # 회사 규모
    st.text('해당 별점 범위에 해당하는 회사규모 산점 그래프')
    fig1 = px.scatter(df_rating, 'Size_From(employees)', 'Size_To(employees)')
    st.plotly_chart(fig1)
    # 버블로 만들고 싶드아아아아아아아ㅏ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# checkbox를 이용해서, groupby에 누굴 포함할지 여부 결정.