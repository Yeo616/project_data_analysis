from re import U
import streamlit as st
import pandas as pd
from app_founded import run_founded
from PIL import Image

from app_industry import run_industry
from app_ml import run_ml
from app_rating import run_rating
from app_salary import run_salary
from app_search import search_sector
from app_company_name import run_company_type, search_company
from app_serach_job import search_jobtitle
from app_search_industry import search_industry

import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')

def message_cleaning(sentence) : 
  #  1. 구두점 제거
  Test_punc_removed = [char for char in sentence if char not in string.punctuation]
  # 2. 각 글자들을 하나의 문자열로 합친다. 
  Test_punc_removed_join = ''.join(Test_punc_removed)
  # 3. 문자열에 불용어가 포함되어잇는지 확인해서, 불용어 제거한다.
  Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in my_stopwords]
  # 4. 결과로 남은 단어들만 리턴한다. 
  return Test_punc_removed_join_clean


def main():
    # 가로로 길게 보이도록 어케함?


    # st.set_page_config(layout="wide")
    st.sidebar.header('데이터 애널리스트 모집공고 분석')
    column_list = ['Home','회사/회사유형별','급여별','산업/섹터별','평가별','설립연도별','긍정/부정 예측','검색']
    
    choice = st.sidebar.radio(label= '분석 내용 선택',options = column_list)
    

           
    if choice == column_list[0]:
        st.header('데이터 애널리스트 모집 공고 분석')
        st.write('데이터 출처: Glassdoor')
        st.write('(글래스도어는 미국의 해당 회사 직원의 익명 리뷰에 기반한 직장 및 상사 평가 사이트이다.)')
        st.markdown("****")

        url = 'https://cdn-images-1.medium.com/max/1600/1*Hu4TWEt6o3iAWeqxqklbZg.jpeg'
        st.image(url)

    elif choice == column_list[1]:
        url = 'https://static.onecms.io/wp-content/uploads/sites/28/2021/02/19/new-york-city-evening-NYCTG0221.jpg'
        st.image(url)

        st.subheader('회사/회사 유형별 정리')
        st.markdown("****")
        name2 = st.text_input('회사명 검색',max_chars = 35)
        if len(name2)>0:
            search_company(name2)
        run_company_type()

    elif choice == column_list[2]:
        url = 'https://cdn.searchenginejournal.com/wp-content/uploads/2021/07/seo-salary-report-60e4618f40216-sej-1520x800.png'
        st.image(url)    
        st.subheader('급여별 정리')
        run_salary()
   
    elif choice == column_list[3]:
        url = 'https://www.quantzig.com/wp-content/uploads/2017/09/predicting-data-analytics-trends-industry.jpg'
        st.image(url)        
        # st.subheader('산업/섹터별 정리')
        run_industry()

    elif choice == column_list[4]:
        url = 'https://img.freepik.com/free-vector/feedback-or-rating-scale-with-smiles-representing-various-emotions-arranged-into-horizontal-row-customer-s-review-and-evaluation-of-service-or-good-colorful-illustration-in-flat-style_198278-1988.jpg?w=2000'
        st.image(url)
        st.subheader('평가별로 데이터 정리')
        run_rating()

    elif choice == column_list[5]:
        url = 'https://image.shutterstock.com/image-vector/vector-horizontal-illustration-chinese-city-260nw-1369618772.jpg'
        st.image(url)
        st.subheader('설립연도별 정리')
        run_founded()

    elif choice == column_list[6]:
        url = 'https://apro-software.com/wp-content/uploads/2018/11/Artboard-1@2x.png'
        st.image(url)
        st.subheader('긍정/부정 예측')
        run_ml()

    elif choice == column_list[7]:
        url = 'https://www.1stformationsblog.co.uk/wp-content/uploads/2021/04/shutterstock_364134773.png'
        st.image(url)

        st.subheader('영문 키워드 검색')

        name = st.text_input('Job Title',max_chars = 35)
        if len(name)>0:
            search_jobtitle(name)

        name2 = st.text_input('회사명',max_chars = 35)
        if len(name2)>0:
            search_company(name2)

    # st.sidebar.snow()


if __name__ == '__main__':
    main()