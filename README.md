

![header](https://capsule-render.vercel.app/api?type=waving&text=DataAnalyst&animation=fadeIn&color=timeGradient&fontSize=50&height=180 )

</br>

##  📝 개요

</br>

- Python 언어와 분석의 학습 과정 중에, 지식과 기술을 이용한 현업에서는 구체적으로 어떤 역할을 수행하고, 어떠한 업계에서 일을 하는지 이해 및 동기부여를 주고자 작업하였습니다.

- 하기 분류에 따라 데이터를 분석 및 정리하였고, 유저가 직접 검색을 하여 더 상세한 정보를 참고할 수 있도록 검색 기능도 탑재하였습니다.
	- 각 회사 유형
	- 급여
	- 산업/섹터
	- 평점

- **머신 러닝 이용: Naive Bayes**
	- 1점과 5점을 받은 회사의 Job Description 컬럼에서, 키워드를 입력 후에 버튼 클릭, 정확도는 78.26%입니다. 

- 데이터 셋의 출처는:
	- 미국의 익명 직장 및 상사 평가 사이트인 글래스도어이며, Data Analyst에 관련한 모집공고의 데이터입니다. 
	- https://www.kaggle.com/datasets/ashishjangra27/ted-talks?select=data.csv

- 결과물: www.ec2-3-34-129-145.ap-northeast-2.compute.amazonaws.com:8503/

 </br>

참고사항: 영문로 된 데이터셋의 가공이므로, 도출 자료는 모두 영문입니다.
</br>
</br>

##  📝 항목 및 테이블 설명

</br>

###  > 좌측 사이드바 각 항목 설명

</br>

![enter image description here](https://user-images.githubusercontent.com/102447800/190915198-b1f913f0-2a7b-4b5c-b47a-13ec6e9a1ca8.gif)

- **Home**
	- 프로젝트의 개요입니다.

- **회사/회사 유형별**
	- 모집공고를 낸 회사명 검색할 수 있습니다.
	- 회사 유형(사기업, 공기업, 비영리 단체 등)으로 모집공고 분류 가능케 하였습니다.

- **급여별**
	- 최저 급여가 높은 직무: 별점순/설립연도별로 정리하였습니다. 
	- 산업별로 급여 차이 테이블/그래프로 정리하였습니다.
	- 급여 분포도로, 데이터 애널리스트의 다양한 직무 연봉 범위를 그래프로 확인 할 수 있습니다.

- **산업/섹터별**
	-  데이터 애널리스트를 가장 많이 모집하는 산업/섹터를 각 Top10/20/30 으로 확인 할 수 있습니다.

- **평점별**
	-  평점별로, 직무/회사 확인 가능토록 slidebar로 평점을 선택하면, 해당 데이터가 출력됩니다.
	- 평점별로, 산업별로 급여/회사규모의 평균이 테이블/그래프로 확인할 수 있습니다.

- **설립연도별**
	- 설립연도의 범위를 슬라이드바로 설정할 수 있습니다. 
	- 시작범위가 끝나는 범위보다 클 경우에, '시작<끝 수치'의 예외처리를 하였습니다.
	- 회사가 오래되었을 수록, 회사 규모가 회사 연식과 비례하여 큰지 여부를 체크할수 있으며, 그와 관련해서 직무 내용이 더 자세하게 기술되어있는지 확인이 가능합니다. (분업이 더 상세하게 되어있는지 확인 할 수 있습니다.)

- **긍정/부정 예측**
	- 평점 1점과 5점의 데이터를 가지고, Job Description을 분석하여, 평가를 좋게 받은 회사/나쁘게 받은 회사의 모집 공고에는 어떤 키워드를 주로 사용하는지에 대한 판단하는 기능입니다.

- **검색**
	- 상세한 데이터를 알고 싶으면, Job Title, Job Description,회사명으로 직접 영문으로 검색할 수 있습니다.

---
### > 테이블 

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

</br>
</br>

##  📝 프로젝트 수행 과정

### > 사전 데이터 가공 

- 가공 전 데이터: (2257 x 15)
- 급여/회사규모는 범위로 한 컬럼으로 묶여있어, 분리하여 가공하였습니다.
-  '회사 최대 규모' 컬럼을 제외한 Nan 값은 제거하였습니다.
- 가공 후 데이터: (1810 x 17)

</br>

### > 머신러닝

![enter image description here](https://user-images.githubusercontent.com/102447800/190916491-aea4fd02-287d-4c97-b56e-2299576a2f50.gif)

- Naive Bayse의 머신러닝 기능을 이용했습니다. 학습 데이터는 113개입니다.
- 현재 정확도는 78.26%입니다. 

</br>

###  > 이슈

![image](https://user-images.githubusercontent.com/102447800/172653266-296f8527-67dd-455a-bb4f-671b14c3221e.png)

</br>

(1) 
WordCloud의 기능을 사용하여, 단어를 정리하였으나, 여러 WordCloud의 사용으로 로딩이 과부하 되는 것을 방지하여, 사전에 Jupyter Notebook으로 처리하고, 해당 코드는 주석 처리를 하였습니다. 해당 프로젝트에서는 이미지로 표시하였습니다. 

</br>

> (평점 5점의 WordCloud)
> 
![df5](https://user-images.githubusercontent.com/102447800/172653661-46c1e81e-ef14-4103-8208-149b4010d768.png)

</br>

> (평점 1점의 WordCloud)

![df1](https://user-images.githubusercontent.com/102447800/172654778-270c1ca1-b9f8-4f5f-898e-fe6e4213f9db.png)

</br>

(2)
WordCloud의 기능을 사용하여, 평점별의 Job Description 키워드입니다. 평점 5점의 키워드에 Job Description의 키워드가 있어서 제거하려고 했으나, 평점1점의 키워드와 비교해봤을 때, 평점 5점의 회사는 구인 포맷이 따로 존재하는 것으로 판단(=체계적인 시스템 존재)되어, Job Description 키워드는 제거하지 않기로 하였습니다. 

</br>

(3) 
"최저/최고 급여 분포"의 그래프 표현 할 때, 하기 이미지와 같은 경고창이 나타납니다.

</br>

![image](https://user-images.githubusercontent.com/102447800/172659545-447d67e8-7659-4d61-98c6-ac8bd656c6e9.png)

</br>
해당 이슈는 하기 코드를 넣어주면, 경고창은 뜨지 않게 됩니다. 

```
st.set_option('deprecation.showPyplotGlobalUse', False)
```
</br>

###  > 작업 환경
**언어:** 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  

</br>

**개발환경:**
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

</br>

**라이브러리:**
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

</br>
</br>

## 📝 결과물

![enter image description here](https://user-images.githubusercontent.com/102447800/190917272-e0c4f328-5a29-4eb1-8b56-295edcf9927d.gif)

</br>

----

</br>

>### 추후 보충사항
- location 위치 지도 추가
- 컬럼이름 간결하게 수정
- 항목 이름도 고급스럽게 수정

</br>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=100&section=footer)
