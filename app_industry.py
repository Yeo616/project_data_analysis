import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def run_industry():
    st.subheader("데이터 애널리스트 모집 산업/섹터 Top")
    st.text('')

    df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
    df = df.astype({'Founded':'int'})
    df = df.astype({'Rating':'int'})

    chosen_menu = st.selectbox('산업/섹터',['산업별','섹터별'])

    if chosen_menu == '산업별':

        col1, col2 = st.columns([1, 3])
        
        top_list = ['Top10','Top30','Top50']
        top = col1.radio('Top 보기',top_list)

        industry = df['Industry'].value_counts()
        industry = industry.to_frame()
        industry.columns = ['counts']

        if top == top_list[0]:
            top = 10 
        elif top == top_list[1]:
            top = 20
        elif top == top_list[2]:
            top = 30  

        col2.text('\n\n')

        with col2.expander('데이터 애널리스트 모집 공고 산업별 Top{}'.format(top)):
            st.dataframe(industry.head(top))
        # col2.text('데이터 애널리스트 모집 공고 산업별 Top{}'.format(top))
        # col2.dataframe(industry.head(top))

        st.markdown("****")
        st.text('산업별 모집공고 Top{} 그래프'.format(top))

        fig1 = px.bar(industry.head(top))
        st.plotly_chart(fig1)

        top_pie_name = industry.head(top).index

        st.markdown("****")
        fig2 = px.pie(industry.head(top),names= top_pie_name,
                    values = 'counts', title= '산업별 Top 분표도')
        st.plotly_chart(fig2)


    if chosen_menu =='섹터별':
        col1, col2 = st.columns([1, 3])
        
        top_list = ['Top10','Top30','Top50']
        top = col1.radio('Top 보기',top_list)

        sector = df['Sector'].value_counts()
        sector = sector.to_frame()
        sector.columns = ['counts']

        if top == top_list[0]:
            top = 10 
        elif top == top_list[1]:
            top = 20
        elif top == top_list[2]:
            top = 30  

        col2.text('\n\n')

        st.markdown("****")
        with col2.expander('데이터 애널리스트 모집 공고 섹터별 Top{}'.format(top)):
            st.dataframe(sector.head(top))

  
        st.text('섹터별 모집공고 Top{} 그래프'.format(top))

        fig1 = px.bar(sector.head(top))
        st.plotly_chart(fig1)

        top_pie_name = sector.head(top).index
        
        st.markdown("****")
        fig2 = px.pie(sector.head(top),names= top_pie_name,
                    values = 'counts', title= '섹터별 Top 분표도')
        fig2.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
        # fig2.update_layout(legend=dict(title_font_family="Times New Roman",
        #                       font=dict(size= 20)
        #     ))
        st.plotly_chart(fig2)


