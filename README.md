## 📝 DataAnalyst


###  개요
>Python 분석과 언어의 학습 과정 중에, 지식과 기술을 이용한 현업에서는 구체적으로 어떤 역할을 수행하고, 어떠한 업계에서 일을 하는지 이해 및 동기부여를 주고자 작업하였다.

>자료 출처: 미국의 익명 직장 및 상사 평가 사이트인 글래스도어이며, Data Analyst에 관련한 모집공고의 데이터이다. 

> 참고사항: 영문로 된 데이터셋의 가공이므로, 데이터는 모두 영문

- 데이터셋: 
>https://www.kaggle.com/datasets/ashishjangra27/ted-talks?select=data.csv
- 결과물: 
> www.ec2-3-34-129-145.ap-northeast-2.compute.amazonaws.com:8503/

---
###  작업 환경
언어: 

```
Python
```

개발환경:
```
Anaconda Jupyter Notebook, Google Colab, VSCode, AWS 
```


라이브러리:
```
$ pip install pandas
```
```
$ pip install streamlit
```
```
$ pip install image
$ pip install pillow
```
```
$ pip install nltk
```
```
$ pip install matplotlib
```
```
$ pip install plotly
```

---
## 📋 페이지 분류
**1.Home**
- 전체적인 개요 설명
 
**2.회사/회사 유형별**
- 모집공고를 낸 회사명 검색, 회사 유형(사기업, 공기업, 비영리 단체 등)으로 모집공고 분류 가능

**3.급여별**
- 최저 급여가 높은 직무: 별점순/설립연도별로 정리
산업별로 급여 차이 테이블/그래프로 정리
- 급여 분포도로, 많은 직무들이 어떠한 연봉 범위에 있는 지 확인

**4.산업/섹터별**
- 데이터 애널리스트를 가장 많이 모집하는 산업/섹터 Top 순위로 정리

**5.평별**
- 평점별로, 직무/회사 확인 가능토록 slidebar로 평점 확인
- 해당 산업별로 급여/회사규모의 평균이 어떤지 테이블/그래프로 정리

**6.설립연도별**
- 회사가 오래되었을 수록, 회사 규모 체크, 직무 내용이 더 상세하게 되는지, 역할은 더 구체적인지 확인

**7.긍정/부정 예측**
- 평점 1점과 5점의 데이터를 가지고, Job Description으로 어떤 역할이 직무/회사에 대해 안좋은 영향을 끼쳤는지 판단하는 기능.
- 현재 정확도는 78.26%이다.

**8.검색**
- 상세한 데이터를 알고 싶으면, Job Title, Job Description,회사명으로 직접 영문으로 검색
