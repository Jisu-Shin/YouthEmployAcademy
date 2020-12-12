#  Week1 :: 20.07.27 - 07.31

1. [파이썬기초 - basic+IO](#파이썬기초---basicio)
2. [파이썬기초 - Function,Object,Class](#파이썬기초---functionobjectclass)
3. [크롤링](#크롤링)
4. [Pandas](#pandas)
5. [datetime 모듈](#datetime-모듈)
6. [네이버 기사 댓글 가져오기](#네이버-기사-댓글-가져오기)


- - -


## 파이썬기초 - basic+IO

a,b,c = 80,90,100 // unpack 가능

### 문자열

```python
  quote ="""안녕하세요
  저는 신지수입니다"""  # 엔터쳐서 입력가능 따옴표 3개
  quote = "\"신지수\""  # 따옴표를 입력하고 싶을 때

  print("영어점수는 %.2f , 수학점수는 %.1f 입니다", %(en,ma))
  print("영어점수는 {}, 수학점수는{} 입니다".format(en,ma))
  # input_val.lower() / input_val.upper()

  list1.reverse() # 리스트 역행
  list1.sort(reverse=True) # 리스트 내림차순
```



### ★중요★

```python
  import copy

  list1 = [[1,2,3],[4,5,6],[7,8,9]]

  # 2차원 이상 list는 deepcopy를 사용해야한다
  #list1.copy()는 원본에도 영향이 가기 때문
	list2 = copy.deepcopy(list1)

```



### Dictionary

```python
  'name' in profile  # 프로필 사전에 name이라는 키가 있는지 검사
  profile.setdefault('score',0) # score 값이 없을 경우 기본으로 0이다

    # 한번에 두개의 값을 바꾸고 싶을 때
    profile.update({  
          'score' : 50,
          'height':176
          })

    key_li=profile.keys()
    val_li=profile.values()
    new_dict={
      key_li[i]:val_li[i] for i in range(len(key_li))
    }
    new_dict = dict(zip(key_li,val_li))
    profile.items() # 전체(key, val) 다 나옴
```



###  리스트 컴프리핸션

```python
    list1= list(range(10,50,10))
    list2 = [i for i in list1 if i%2==0]
```





###  Random

```python
    import random

    random.random()
    random.randint(1,10)  #1부터 10까지 숫자중 랜덤
```





###  IO

```python
    file = open("sample.txt","wt+")
    file.write("Heeeeeello")
    file.seek(0) # 커서의 위치를 바꿔준다
    file.close() # 꼭해줘야함

    # file.close()의 불상사를 막기 위해 사용하는 방법
    with open("sample.txt","rt+") as f:
        content = f.read()
        print(content)
```



[목차](#week1--200727---0731)


- - -


## 파이썬기초 - Function,Object,Class

###  lambda

```python
    (lambda x,y : (x+y , x-y))(3,4)

    calc = lambda x,y : (x+y , x-y)
    calc(3,4) # => 결과값 (7,-1)

    li1 = [1,2,3,1,4,2,1,]
    list(map(str,li1)) # li1을 string 타입으로 저장
    list(map(lambda x : x**2,li1)) # li1을 제곱해서 저장
```





###  가변인수 *args

```python
    def func1(*args):
        print(args)
        return sum(args)

    li1 = [1,2,3,4,5]

    func(li1,6)
    #출력> error

    func(*li2,6,7,8)
    #출력> (1,2,3,4,5,6,7)
    #      28
```





###  default parameter

```python
    #입력을 안해도 기본값으로 50점이 들어간다
    def set_profile(name, score=50):
        print("이름: ",name)
        print("점수: ",score)

    set_profile("신지수")
    #출력> 신지수
    #      50
```





###  Class

```python

  # Dog = Dog()=Dog(Object)
  class Dog():
        # 생성자 self는 모든 메소드에 들어가야한다
        def __init__(self, name,color):
          self.__hungry=0 // private 변수이다
          self.name = name
          self.color = color

        # 메소드를 부를시 eat() 괄호 안이 빈칸이지만 만들시에 꼭 **self** 적어주기
        def eat(self):
          self.__hungry+=10
          print("밥 먹음",self.__hungry) // private변수는 모두 다 이렇게 써줘야 한다

        # print(choco) 를 하면 아래 메소드 출력
        def __str__(self):
          return str({
              'name':self.name,
              'color':self.color
          })

    ----------------------------------------------------------

    # Animal 클래스(=부모)를 상속받음    
      class Dog(Animal):
          pass
```



[목차](#week1--200727---0731)



- - -


## 크롤링

### BeautifulSoup

```python
      import requests
      from bs4 import BeautifulSoup

      resp =requests.get(url,params = params, header= header)
      soup = BeautifulSoup(resp.text)
      # soup = BeautifulSoup(resp.text,"lxml") lxml 오류 날 때 
      div_tag=soup.div.attrs # div의 속성 알고 싶을때
      div_tag.get('id')

```



###  select, find, find_all

```python
      soup.select('div.group_nav > ul.list_nav a.nav')

      # 가장 첫번째 한개만 가져옴
      soup.find('div',class_='group_nav')

      # iframe 속성중 name이 day 인 것 <iframe name="day" >
      soup.find('iframe',attrs={'name':'day'})

      #여러개 가져옴 , 자식 태그의 div 까지만 가져옴
      #recursive는 find_all만 
      soup.find_all('div',class_='group_nav',recursive=False)

      # 그 중에 하나 가져오기
      soup.find_all('div',class_='group_nav')[2]
```





###  Beautifulsoup - 이미지 저장

```python

  url = '이미지링크'
  resp = requests.get(url)

	# 이미지 파일이기 때문에 binary 형태이다
	resp.content

	with open("temp.jpg","wb") as f:
		f.write(resp.content)
```





###  Selenium

```python

  from selenium import webdriver

  driver = webdriver.Chrome() # 파일 같은 폴더에 저장해야함
  driver.maximize_window() # 전체 창으로 만들어야 크롤링하기 쉬워짐
  driver.get('https://www.naver.com')
  driver. title   
```



###  Selenium  - 이미지 저장

```python
	driver = webdriver.Chrome()
	driver.get("링크")
	driver.save_screenshot('사진이름.png')
```

```python
	screenshot = driver.get_screenshot_as_png()
	with open('사진이름.png','wb') as f:
		f.write(screenshot)
```





###  Json

```python
	import json

	month_candle = json.loads(resp.text)
	month_candle[0]['lowPrice']
```



[목차](#week1--200727---0731)


- - -


## Pandas

```python
      import pandas as pd

      sise = get_day_sise('005930',5)
      sise_df = pd.DataFrame(sise)

      #DataFrame 을 csv로 저장함
      sise_df.to_csv("my_sise.csv",encoding='cp949')
      #csv를 DataFrame으로 불러옴
      #index까지 csv로 들어갔기 때문에 index_col로 지정해줌
      pd.read_csv("my_sise.csv",encoding='cp949',index_col=0)

      # DataFrame 을 excel로 저장함
      sise_df.to_excel("my_second_sise.xlsx",encoding='cp949')
      # excel을 불러옴
      pd.read_excel("my_second_sise.xlsx",encoding='cp949',index_col=0)
```



[목차](#week1--200727---0731)





## datetime 모듈

```python
    import datetime

    # 현재시간 출력
    now = datetime.datetime.now()
    # 출력> datetime.datetime(2020, 8, 4, 15, 28, 36, 555245)

    # 이전 시간으로 이동하기 위해 datetime.timedelta 사용
    past = now - datetime.timedelta(days=30,minutes=50,weeks=4)

    # 문자열로 변경하기
    now.strftime('%Y%m%d')
    # 출력> '20200804'

```



[목차](#week1--200727---0731)



## 네이버 기사 댓글 가져오기



- 네이버 기사 댓글 `더보기∨` 클릭

- `크롬 개발자 도구` -> `Network` -> Name 이 `web_naber_list_jsonp.js.`. 클릭

- `Headers`  ->  `▼General`  -> `Request URL` 을 보면

  `https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?` 뒤로 파라미터를 넣는다

  `ticket=news&templateId=default_world&pool=cbox5&_callback=jQuery11240046997381188230936_1597388193599&lang=ko&country=KR&objectId=news001%2C0011785467&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=2&refresh=false&sort=FAVORITE&current=2199946622&prev=2199886612&includeAllStatus=true&_=1597388193601`





```python
  import urllib
  # URL Decoding 함수.
  urllib.parse.unquote('news001%2C0011785467')
  #출력> news001,0011785467
```



```python
  base_url = 'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json'
  params={
      'ticket':'news',
      'templateld':'default_world',
      'pool':'cbox5',
      #'_callback':'jQuery112408231101889070349_1596430477773',
      'lang':'ko',
      'country':'KR',

      # 중요 %2c -> , 로 바꿔줘야 댓글 개수가 보인다
      'objectId':'news001,0011785467',
      'categoryId': None,

      # 댓글을 몇개 가져오고 싶은지 지정할 수 있다
      'pageSize':20,
      'indexSize':10,
      'groupId': None,
      'listType': 'OBJECT',
      'pageType':'more',

      # page:1로 할경우 첫댓글 부터 가져오게 된다
      'page':2,
      'refresh':'false',
      'sort':'FAVORITE',
  #     'current':'2199946622',
  #     'prev':'2199886612',
  #     'includeAllStatus':'true',
  #     '_':'1596444823308'
  }
```


- `Headers`  ->  `▼ Request Headers` 를 보면
- `referer` 와 `user-agent` 값을 header에 넣어준다


```python
  headers = {
      'referer':'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LS2D&mid=shm&sid1=105&sid2=731&oid=001&aid=0011785467',
      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
  }
```



```python
  import json

  # " 부터 시작해야 되기 때문에 slicing 꼭 해줘야 한다 안그러면 에러남
  data = json.loads(resp.text[10:-2])
  result = data.get('result')
  result.keys()
  #출력> dict_keys(['commentList', 'pageModel', 'exposureConfig', 'count', 'listStatus', 'sort', 'bestList'])

  #댓글들을 모아놓음
  comments = result['commentList']

```

본문과 댓글의 관계는 직접 확인해보기



[목차](#week1--200727---0731)
