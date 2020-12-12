#  Week2 :: 20.08.03 - 08.08

1. [Numpy](#numpy)
2. [Pandas](#pandas)
3. [Ecommerce Purchase](#ecommerce-purchase)
5. [Matplotlib](#matplotlib)
6. [REST API](#rest-api)
7. [크롤링(팀플)](#크롤링팀플)





## Numpy

파이썬은 연속적인 메모리 배치를 갖지 않아서 numpy를 사용한다



```python
import numpy as np

arr1 = np.array([1,2,'a','b',0.1,0.2])
#출력 > array(['1', '2', 'a', 'b', '0.1', '0.2'], dtype='<U11')

arr2 = np.array([1,2,0.3,0.4])
#출력 > array([1. , 2. , 0.3, 0.4])

arr2.dtype
#출력 > float64

arr2=arr2.astype(int)
#출력 > array([1, 2, 0, 0])
```

np.array 안은 같은 데이터타입으로 저장된다



```python
arr3 = np.arange(36)

arr3.shape
#출력 > (36,)

arr3 = arr3.reshape(3,4,3)
#출력 > array([[[ 0.,  1.,  2.],
#        [ 3.,  4.,  5.],
#        [ 6.,  7.,  8.],
#        [ 9., 10., 11.]],

#       [[12., 13., 14.],
#        [15., 16., 17.],
#        [18., 19., 20.],
#        [21., 22., 23.]],

#       [[24., 25., 26.],
#        [27., 28., 29.],
#        [30., 31., 32.],
#        [33., 34., 35.]]])

arr3.ndim # 몇차원인지 알 수 있다
#출력 3

arr3 = arr3.reshape(-1,3)
arr3.shape
#출력 > (12,3)

arr3[arr3>23]
#출력 > array([24, 25, 26, ...33, 34, 35])

arr4 = np.arange(0,5,0.5)
#출력> array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])

arr5 = np.linspace(0,5,10) 
#출력> array([0.        , 0.55555556, 1.11111111, 1.66666667, 2.22222222, 
#		2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.        ])

```



arange(start,stop,step)는 stop숫자를 포함하지 않은채 step만큼 이동한다

linspace(start,stop,num)는 stop을 포함한채 num개가 일정한 step만큼 이동한다 



```python
np.random.seed(0)
# random 값이 변하지 않게 된다

np.random.rand(5)
#출력 > array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

np.random.rand(4,3,2) #z,x,y

np.random.randint(-5,3,(3,3))
# -5부터 3까지 3행 3열의 배열이다

np.random.randn(2,5)
# 가우시안 정규분포 랜덤

arr = np.array([1,2,3, np.nan, np.inf, -np.inf])
#출력>(array[ 1, 2, 3, nan, inf, -inf])

np.zeros((3,3)) #0행렬
np.ones(5) #1행렬
np.identity(2) #단위행렬
np.eye(2)#단위행렬
#출력 > array([[1 ,0 ])
#			[0 ,1	]])
```



**통계를 위한 연산**

```python
arr = np.arange(1,11).reshape(5,2)

arr.sum(axis=0) #column 별로 합산
#출력> array([25, 30])

arr.sum(axis=1) #row 별로 합산
#출력> array([3, 7, 11, 15, 19])

arr.mean() #평균
arr.var() #분산
arr.std() #표준편차
arr.min(), arr.max() #최소 최대
arr.cumsum() #누적합
arr.cumprod #누적곱

arr1 @ arr2 #행렬곱
arr.dot(arr2) #행렬곱
np.matmul(arr1,arr2) #행렬곱

arr.transpose #전치
arr.T #전치

#아래 출력결과와 같다
np.vstack([arr1,arr2])
np.concatenate((arr1,arr2),axis=0) 
# 출력 > array([[ 0,  1],
#	  	      [ 2,  3],
#   		  [ 0, 10],
#       	  [20, 30]])

#아래 출력결과와 같다
np.c_[arr1,arr2] 
np.hstack([arr1,arr2]) 
np.concatenate((arr1,arr2),axis=1)
# 출력> array([[ 0,  1,  0, 10],
#	          [ 2,  3, 20, 30]])

np.tile(arr1,2)
#출력 > array([[0, 1, 0, 1],
#			  2, 3, 2, 3,]])

```

np.tile(arr1,(3,2)) 도 가능하다

[목차](#week2--200803---0808)



## Pandas



```python
import numpy as np
import pandas as pd

s1 = pd.Series([1., 3., np.nan, np.inf, -1.], index=['a','b','c','d','e'])
#출력>  a    1.0
#	    b    3.0
#		c    NaN
#		d    inf
#		e   -1.0
#		dtype: float64

dict_data={
    '국어':100,
    '영어':85,
    '수학':95
}
s2 = pd.Series(dict_data)

pd.date_range('2019-07-27','2020-09-24',freq='Y')
# 출력> DatetimeIndex(['2019-12-31'], dtype='datetime64[ns]', freq='A-DEC')
# freq: 주기 (default='D','M','Y')
# 매 달(년)의 마지막 날짜가 나온다
```

pandas는 numpy, pandas 패키지 모두 import 해야한다

Series 끼리 연산이 가능하다



```python
english_score = np.random.randint(70,100,5)
kor_score = np.random.randint(50,100,5)
math_score = np.random.randint(0,100,5)

score_df=pd.DataFrame({
    'english':english_score,
    'korean':kor_score,
    'math':math_score
})

score_df.index = range(1,6) #(행) 수정 
score_df.columns = ['eng','kor','math'] #(열) 수정
```

pd.Series()와 pd.DataFrame() 의 차이

시리즈는 1차원 자료구조이다, 리스트와의 다른 점은 index 설정이 가능하다는 점이다

데이터프레임은 2차원 자료구조이다



```python
ktx_df = pd.read_csv('ktx_data.csv',encoding='cp949')
ktx_df = ktx_df.set_index(np.arange(2011,2018)) #위의 index방법과 결과는 동일
ktx_df[['경부선 KTX','전라선 KTX']] # [] 하나에 여러 열을 넣으면 에러가 난다

ktx_df.loc[index,column] # 인덱스 기준 슬라이싱
ktx_df.iloc[num_index, num_column] #행열 숫자로 값 가져오기
```

loc와 iloc 구분해서 잘 사용하기



```python
#새로운 행 추가
new_df = pd.DataFrame(
    [
        [5000,35000,7000,7000,8000]
    ],
    index=[0], #[ktx_df.index[-1]+1]
    columns=ktx_df.columns #넣을 df의 columns 넣어주기
)
ktx_df.append(new_df,ignore_index=True) #원래 인덱스 사라지고 0부터 시작한다

#새로운 열 추가
data = np.random(1000,100000,(7,1))
air_df = pd.DataFrame(data,columns=['항공편',index=np.arange(2011,2018)])
ktx_df.join(air_df) 
ktx_df['항공편'] = air_df['항공편'] #위와 같은 명령

#행열제거
ktx_df.drop(2017,axis=0,inplace=True) #inplace: 원본도 바뀌는지
```

새로운 데이터 추가



```python
ktx_df['rank'] = 'A'
ktx_df.loc[:2013,'rank']='B'
ktx_df.loc[[2014,2016],'rank']='c'

rank_df = pd.DataFrame({
    'rank':['A','B','C','D'],
    'price':[1000,100,10,1]
})

ktx_df.merge(rank_df,on='rank',how='left') #rank의 기준으로 rank_df와 합쳐진다
```

merge 이지만 DB에서 join과 개념 비슷

how = outer /left /right 들어갈 수 있다

```python
ktx_df['rank'].value_counts()
ktx_df.sort_values('경부선 KTX',ascending=False) #내림차순
```

상관관계 ..등 더 필요한 때가 생기면 그때 추가하자

[목차](#week2--200803---0808)



## Ecommerce Purchase



```python
import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')

ecom.info() # column값, non-null값 개수, dtype
ecom.describe() #연산 관련 ecom.describe(include='all') 가능

ecom.max()['Purchase Price'] == ecom['Purchase Price'].max()
ecom[].unique() #고유 값만
ecom[].value_counts() #고유 값 + 값에 대한 총 갯수

len(ecom.loc[ecom['Language']=='en','Credit Card'].unique())
len(ecom[ecom['Job']=='Lawyer'])

# 직업개수별로 상위 하위 알아보기
ecom['Job'].value_counts().head()
ecom['Job'].value_counts().tail()

# and, or 사용 가능
len(ecom[(ecom['CC Provider']=='American') && (ecom['Purchase Price']>95) ])

# apply , lambda
len(ecom[ecom['CC Exp Date'].apply(
    lambda x: (x.split('/')[1]=='25')
	)])

ecom['Email Provider']=ecom['Email'].apply(lambda email: email.split('@')[1])
ecom['Email Provider'].value_counts().head()
```

[목차](#week2--200803---0808)



## Matplotlib



```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4.5,5,0.5)

y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10

#plt.plot(x,y1,x,y2,x,y3) 가능
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()
```

matplotlib 기본



```python
x = np.linspace(-4,4,100)
y1 = x**3
y2 = 10*x**2-2

plt.figure(1,figsize=(10,3)) #새로운 창이 나타난다
plt.plot(x,y1)

plt.figure(2)
plt.plot(x,y1)

plt.figure(1)
plt.plot(x,y2)

plt.figure(2)
plt.clf() #clear figure 초기화
plt.plot(x,y1,x,y2)
plt.xlim(-1,1) #x축 확대
plt.ylim(-3,3) #y축 확대
plt.grid()
plt.show()
```

plt.figure() 로 각 창마다 그래프 그릴 수 있음

plt.xlim(), plt.ylim() 으로 특정 부분 그래프 확대하기



```python
# 맷플롯립 한글 폰트 지정
import platform
from matplotlib import font_manager, rc

# 한글 설정시 마이너스 부호 깨지는 것 방지
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    # mac
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    # windows
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
```

한글 설정



```python
plt.plot(df['DIS'],y,'^g',label='Corr of DIS&Price',alpha = 0.3)
plt.plot(df['RM'],y,'vr',label='Corr of RM&Price',alpha = 0.3) #alpah는 투명도
```

label 이름을 각 그래프마다 작성함



```python
plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')

plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'], loc = 'best') #best : 최적의 위치를 찾아준다
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.title('그래프 제목')
plt.text(2,2,"여긴 2,2 입니다")
plt.grid(True)
```

plt.legend()를 사용해서 순서대로 label을 지정해줌

plt.text()를 사용해서 그래프 특정 위치에 글씨를 쓸 수 있음



- 산점도 : plt.scatter()

- 막대그래프 : plt.bar()

- 히스토그램 : plt.hist()   

- 파이그래프 : plt.pie()



[목차](#week2--200803---0808)



## REST API

**메소드** : 요청의 종류를 서버에 알리기 위해서 사용하는 것, 게시판 기능 (CRUD, REST API)을 만들 때 사용

**HTTP 메소드 종류** 

1. POST : 정보를 입력하기 위해 사용 (Create)
2. GET : 정보를 요청하기 위해 사용 (Read)
3. PUT : 정보를 업데이트 하기 위해 사용 (Update)
4. DELETE : 정보를 삭제하기 위해 사용 (Delete)



**REST란 ?**

- URI를 이용한 접근 : 모든 개체를 리소스로 보고, 리소스에 고유번호를 부여
- URI 디자인 원칙 : 자원에 대한 처리를 주소에 나타내지 않는다 , 어떤 자원인지 주소에 명확하게 나타냄
- URI에서는 '_'(언더바) 보다는 '-' (하이픈)을 권장한다
- URI에 파일 확장자는 포함시키지 않는다
- HTTP 메소드를 사용한다 (자원에 대한 행위 표현)
- 클라이언트가 요청할 때마다 필요한 정보를 주기 때문에 서버에서는 세션정보를 보관할 필요가 없다 그렇기때문에 서비스에 자유도가 높아지고 유연한 아키텍처 적응이 가능하다
- 무상태성 (Stateless) 성격을 갖고 있다 작업을 위한 상태정보를 따로 저장하고 관리하지 않다
- 캐시가능 (Cacheable) : REST는 HTTP라는 기존 웹표준을 그대로 사용하기 때문에, 웹에서 사용하는 기존 인프라를 그대로 활용이 가능하다 



**REST의 장점**

* 언어와 플랫폼에 독립적이다
* SOAP(다른통신방식) 보다 개발이 쉽고 단순하다
* REST가 지원하는 프레임워크나 언어등 도구들이 없어도 구현이 가능하다
* 기존 웹 인프라를 사용 가능하다 HTTP를 그대로 사용하기 때문에 그런 것이다



**REST의 단점**

* HTTP 프로토콜만 사용이 가능하다
* p2p 통신 모델을 가정했기 때문에 둘 이상을 대상으로 하는 분산환경엔 유용하지 않다
* 보안, 정책 등에 대한 표준이 없기 때문에 관리가 어렵고 이러한 부분까지 고려해서 구현 할 경우 설계나 구현에서 좀 더 어려움을 갖는다
* 기존 웹 인프라를 사용 가능하다 HTTP를 그대로 사용하기 때문에 그런 것이다





```python
import requests
from bs4 import BeautifulSoup
import urllib

key = '(서비스 키)'
servicekey = urllib.parse.unquote(key) #퍼센트 인코딩된 시퀀스를 유니코드 문자로 decoding
params = { #문서에 맞게 작성
    'serviceKey' : key,
    'numOfRows' : 10,
    'PageNo': 1,
    'startCreateDt' : 20200310,
    'endCreateDt':20200505'
} 

resp = requests.get(url,params=params)
resp.text
```

실제로 해봤는데 안됐다.. 주말이라그런가 ㅠㅠ



**json**

```python
import datetime
now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
url = ''
params = {
    'edDt' : today,
    '_type':'json'
}
resp = requests.get(url,params=params)
data = resp.json()
```



**네이버 POST 요청**

```python
import json

url=
headers={}
params={}

data = json.dumps(params)
resp = requests.post(url,headers=headers,data=data)
result = resp.json()
```

한글 설정



```python
plt.plot(df['DIS'],y,'^g',label='Corr of DIS&Price',alpha = 0.3)
plt.plot(df['RM'],y,'vr',label='Corr of RM&Price',alpha = 0.3) #alpah는 투명도
```

label 이름을 각 그래프마다 작성함



[목차](#week2--200803---0808)



## 크롤링(팀플)



```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4.5,5,0.5)

y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10

#plt.plot(x,y1,x,y2,x,y3) 가능
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()
```

matplotlib 기본



```python
x = np.linspace(-4,4,100)
y1 = x**3
y2 = 10*x**2-2

plt.figure(1,figsize=(10,3)) #새로운 창이 나타난다
plt.plot(x,y1)

plt.figure(2)
plt.plot(x,y1)

plt.figure(1)
plt.plot(x,y2)

plt.figure(2)
plt.clf() #clear figure 초기화
plt.plot(x,y1,x,y2)
plt.xlim(-1,1) #x축 확대
plt.ylim(-3,3) #y축 확대
plt.grid()
plt.show()
```

plt.figure() 로 각 창마다 그래프 그릴 수 있음

plt.xlim(), plt.ylim() 으로 특정 부분 그래프 확대하기



```python
# 맷플롯립 한글 폰트 지정
import platform
from matplotlib import font_manager, rc

# 한글 설정시 마이너스 부호 깨지는 것 방지
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    # mac
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    # windows
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
```

한글 설정



```python
plt.plot(df['DIS'],y,'^g',label='Corr of DIS&Price',alpha = 0.3)
plt.plot(df['RM'],y,'vr',label='Corr of RM&Price',alpha = 0.3) #alpah는 투명도
```

label 이름을 각 그래프마다 작성함



[목차](#week2--200803---0808)

