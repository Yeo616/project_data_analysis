### DataAnalyst


## 🏦 개요
- Python으로 데이터 가공/분석을 배웠다. 
- 해당 지식과 기술을 이용한 현업에서는 구체적으로 어떤 역할을 수행하고, 어떠한 업계에서 일을 하는지 이해 및 동기부여를 주고자 작업하였다.
- 자료 출처는 미국의 익명 직장 및 상사 평가 사이트인 글래스도어이며, Data Analyst에 관련한 모집공고의 데이터이다. 
- 참고사항: 영문로 된 데이터셋의 가공이므로, 데이터는 모두 영문

- Datatset: https://www.kaggle.com/datasets/ashishjangra27/ted-talks?select=data.csv
- Deployment: http://3.34.129.145:8502/

---
## 🚀 테이블 컬럼
- Job Title: 직무
- Job Description: 역할 
- Rating: 회사 평점
- Location: 위치
- Founded: 설립일
- Type of Ownership: 회사 유형
- Industry: 업계
- Sector: 섹터
- Revenue: 회사 이익
- Competitors: 경쟁사
- Salary_Estimate_To_(K): 최저 급여
- Salary_Estimate_To_(K): 최고 급여
- Size_From(employees): 회사 최소 규모
- Size_To(employees): 회사 최대 규모

- 기본적으로 직무/역할/회사 평점/ 설립일/ 최저급여/ 최고급여/ 회사 최소규모의 Nan 값은 제거하였음.
- 급여/회사규모는 한 컬럼으로 묶여있어, 분리하여 가공하였음

---
## 📝 실행 설명
- 실행파일 이름: app.py
- 실행 코드:

```
Streamlit run app.py
```

---
## 🎨 언어: 
python

---
## 🎨 설치해야할 패키지: 
pandas,
Streamlit,
PIL,
Nltk,
Matplotlib,
Plotly

Job Description을 분석하여 회사 평점에 대해 긍정/부정 기능을 가지고 있는 머신러닝 기능 탑재

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
