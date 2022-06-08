import streamlit as st
from PIL import Image
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')

import joblib
import numpy as np

def run_ml():
    st.write('- Job Description을 입력 및 버튼 클릭, 긍정 부정 예측.')
    st.write('- 머신러닝 데이터 113개')
    st.write('- 정확도: 78.26%')
    st.markdown("****")
  

    
    sentence = st.text_input('Job Description안의 영문 키워드 입력후 버튼클릭')

    # 유저가 버튼을 누르면, 예측하도록 만든다.
    if st.button('예측 실행') :

        classifier = joblib.load('data/classifier.pkl')
        vec = joblib.load('data/vec.pkl')
        new_data = np.array([sentence])
        X_new = vec.transform(new_data)
        X_new = X_new.toarray()
        y_pred = classifier.predict(X_new)
       
        if y_pred[0] == 5:
            st.text('입력하신 문장은 긍정입니다.')
        else :
            st.text('입력하신 문장은 부정입니다.')

        st.write(y_pred)
    st.markdown("****")
    with st.expander('키워드 참고'):
 
        st.write('##### * 평점 1점의 Job Description 키워드')
        img = Image.open('data/df1.png')
        st.image(img, use_column_width= True)
        # # df 1점
        # from wordcloud import WordCloud,STOPWORDS
        # df_1 = df.loc[df['Rating'] == 1,]
        # job_title=df_1['Job Description'][~pd.isnull(df_1['Job Description'])]
        # wordCloud = WordCloud(width=450,height= 300,background_color= 'white').generate(' '.join(job_title))
        # plt.figure(figsize=(19,9))
        # plt.axis('off')
        # plt.imshow(wordCloud)
        # plt.show()
        st.markdown('****')

        st.write('##### * 평점 5점의 Job Description 키워드')
        img = Image.open('data/df5.png')
        st.image(img, use_column_width= True)
        # # df 5점
        # from wordcloud import WordCloud,STOPWORDS\
        # df_5 = df.loc[df['Rating'] == 5,]
        # job_title=df_5['Job Description'][~pd.isnull(df_5['Job Description'])]
        # wordCloud = WordCloud(width=450,height= 300,background_color= 'white').generate(' '.join(job_title))
        # plt.figure(figsize=(19,9))
        # plt.axis('off')
        # plt.imshow(wordCloud)
        # plt.show()
        st.markdown('****')

        st.write('##### * 평점 1점과 5점의 Job Description 키워드')
        img = Image.open('data/df1_5.png')
        st.image(img, use_column_width= True)
        # 평점 1점과 5점
        # from wordcloud import WordCloud,STOPWORDS
        # df_1_5 = df.loc[(df['Rating'] == 1) | (df['Rating'] == 5),]
        # job_title=df_1_5 ['Job Description'][~pd.isnull(df_1_5 ['Job Description'])]
        # my_stopwords = STOPWORDS
        # my_stopwords.add('Job Description')
        # wordCloud = WordCloud(width=450,height= 300,background_color= 'white',stopwords=my_stopwords).generate(' '.join(job_title))
        # plt.figure(figsize=(19,9))
        # plt.axis('off')
        # plt.title(df_1_5 ['Job Description'].name,fontsize=20)
        # plt.imshow(wordCloud)
        # plt.show()
        st.markdown('****')

        st.write('##### * 전체 Job Description 키워드')
        img = Image.open('data/df_description.png')
        st.image(img, use_column_width= True)


       



