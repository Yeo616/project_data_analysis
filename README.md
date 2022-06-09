## 📝 DataAnalyst


###  개요
>Python 분석과 언어의 학습 과정 중에, 지식과 기술을 이용한 현업에서는 구체적으로 어떤 역할을 수행하고, 어떠한 업계에서 일을 하는지 이해 및 동기부여를 주고자 작업하였습니다.

>각 회사 유형별, 급여별, 산업/섹터별, 평점별, 설립연도별로 데이터를 분석 및 정리하였고, 직접 검색을 하여 더 상세한 정보를 참고할 수 있습니다.

> 1점과 5점을 받은 회사의 Job Description 컬럼을 Naive Bayes 머신러닝을 이용하여, Job Description의 키워드를 입력 후에, 정확도는 78.26%입니다. 

>자료 출처: 미국의 익명 직장 및 상사 평가 사이트인 글래스도어이며, Data Analyst에 관련한 모집공고의 데이터입니다. 

> 참고사항: 영문로 된 데이터셋의 가공이므로, 도출 자료는 모두 영문입니다.

- 데이터셋: 
>[https://www.kaggle.com/datasets/ashishjangra27/ted-talks?select=data.csv](https://www.kaggle.com/datasets/andrewmvd/data-analyst-jobs)
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
```
$ pip install seaborn
```
---
#### 데이터 구조

![image](https://user-images.githubusercontent.com/102447800/172677292-4b2ae25c-2259-4742-ab57-0cc342e54183.png)

---
### 각 항목 설명

Home

> 전체적인 개요 설명입니다.


회사/회사 유형별
> 모집공고를 낸 회사명 검색할 수 있습니다.

>회사 유형(사기업, 공기업, 비영리 단체 등)으로 모집공고 분류 가능케 하였습니다.

급여별
> 최저 급여가 높은 직무: 별점순/설립연도별로 정리하였습니다. 

> 산업별로 급여 차이 테이블/그래프로 정리하였습니다.

> 급여 분포도로, 데이터 애널리스트의 다양한 직무 연봉 범위를 그래프로 확인 할 수 있습니다.

산업/섹터별
> 데이터 애널리스트를 가장 많이 모집하는 산업/섹터를 각 Top10/20/30 으로 확인 할 수 있습니다.

평점별
> 평점별로, 직무/회사 확인 가능토록 slidebar로 평점을 선택하면, 해당 데이터가 출력됩니다.

> 평점별로, 산업별로 급여/회사규모의 평균이 테이블/그래프로 확인할 수 있습니다.

설립연도별
> 설립연도의 범위를 슬라이드바로 설정할 수 있습니다. 시작범위가 끝나는 범위보다 클 경우에, '시작<끝 수치'를 

> 회사가 오래되었을 수록, 회사 규모가 회사 연식과 비례하여 큰지 여부를 체크할수 있으며, 그와 관련해서 직무 내용이 더 자세하게 기술되어있는지 확인이 가능합니다. (분업이 더 상세하게 되어있는지 확인 할 수 있습니다.)

긍정/부정 예측
> 평점 1점과 5점의 데이터를 가지고, Job Description을 분석하여, 어떤 키워드가 직무/회사에 대해 안좋은 영향을 끼쳤는지 판단하는 기능입니다.

> Naive Bayse의 머신러닝 기능을 이용했습니다. 학습 데이터는 113개입니다.

>현재 정확도는 78.26%입니다. 

검색
> 상세한 데이터를 알고 싶으면, Job Title, Job Description,회사명으로 직접 영문으로 검색할 수 있습니다.

---
### 작업 순서

_ 가공 전 데이터: (2257 x 15)

_ 급여/회사규모는 범위로 한 컬럼으로 묶여있어, 분리하여 가공하였습니다.

_  '회사 최대 규모' 컬럼을 제외한 Nan 값은 제거하였습니다.

_ 가공 후 데이터: (1810 x 17)

---
### 테이블 

| 컬럼이름 | 의미 |
| --- | --- |
| Job Title | 직무 |
| Job Description | 역할 | 
| Rating | 회사 평점 | 
| Location | 위치 | 
| Founded | 설립일 | 
| Type of Ownership | 회사 유형 | 
| Industry | 업계 | 
| Sector | 섹터 | 
| Revenue | 회사 이익 | 
| Competitors | 경쟁사 | 
| Salary_Estimate_To_(K) | 최저 급여 | 
| Salary_Estimate_To_(K) | 최고급여 | 
| Size_From(employees) | 회사 최소 규모 | 
| Size_To(employees) | 회사 최대 규모 | 

---




---
###  이슈


![image](https://user-images.githubusercontent.com/102447800/172653266-296f8527-67dd-455a-bb4f-671b14c3221e.png)
(1) WordCloud의 기능을 사용하여, 단어를 정리하였으나, 여러 WordCloud의 사용으로 로딩이 과부하 되는 것을 방지하여, 사전에 Jupyter Notebook으로 처리하고, 해당 코드는 주석 처리를 하였습니다. 해당 프로젝트에서는 이미지로 표시하였습니다. 

![df5](https://user-images.githubusercontent.com/102447800/172653661-46c1e81e-ef14-4103-8208-149b4010d768.png)

![df1](https://user-images.githubusercontent.com/102447800/172654778-270c1ca1-b9f8-4f5f-898e-fe6e4213f9db.png)

> 첫번째 이미지: 평점 5점의 WordCloud

> 두번째 이미지: 평점 1점의 WordCloud

(2)WordCloud의 기능을 사용하여, 평점별의 Job Description 키워드입니다. 평점 5점의 키워드에 Job Description의 키워드가 있어서 제거하려고 했으나, 평점1점의 키워드와 비교해봤을 때, 평점 5점의 회사는 구인 포맷이 따로 존재하는 것으로 판단(=체계적인 시스템 존재)되어, Job Description 키워드는 제거하지 않기로 하였습니다. 

![image](https://user-images.githubusercontent.com/102447800/172659545-447d67e8-7659-4d61-98c6-ac8bd656c6e9.png)
(3) "최저/최고 급여 분포"의 그래프 표현 할 때, 상기 이미지와 같은 경고창이 나타났는데, 하기 코드를 넣어주면, 경고창은 뜨지 않게 됩니다. 


```
st.set_option('deprecation.showPyplotGlobalUse', False)
```

----
### 대시보드



----
>### 보충사항
_ location 위치 지도 추가

_ 컬럼이름 간결하게 수정

_ 항목 이름도 예쁘게 짓기

_ 리드미 파일 예쁘게 꾸미기
