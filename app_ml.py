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
        img = Image.open('data/wc_jobdescription.png')
        st.image(img, use_column_width= True)
