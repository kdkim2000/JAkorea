| 목차 | 내용 |
| --- | --- |
| [연산](#연산)  |[사칙연산](#사칙연산) <br> [거듭제곱](#거듭제곱) <br> [몫과나머지](#몫과나머지) <br> [지수](#지수) <br> [진수](#진수) <br> [논리연산](#논리연산) <br> [비교연산](#비교연산) |
| [변수](#변수)       |
| [자료형](#자료형)    |[문자열](#문자열) <br> [리스트](#리스트) <br> [세트](#세트) <br>[타입변환](#타입변환) <br> [딕셔너리](#딕셔너리) |
| [제어문](#제어문) | [조건문(if)](#조건문(if)) <br> [반복문(for)](#반복문(for)) <br> [반복문(while)](#반복문(while))
| [입력 과 출력](#입력-과-출력) | [화면출력](#화면출력) <br> [키보드입력](#키보드-입력) <br> [파일 읽고 쓰기](#파일-읽고-쓰기)
| [함수](#함수) | 
| [객체와 클래스](#객체와-클래스) | 
| [문자열과 텍스트](#문자열과-텍스트) | 
| [모듈](#모듈) | 


# 기본문법
## 연산
| 연산자 | 설명 |
| --- | --- |
| + | 더하기
| - | 빼기
| * | 곱하기
| / | 나누기
| ** | 더하기
| // | 몫
| % | 나머지

### 사칙연산
```python
print(3+2)
print(3-2)
print(3*2)
print(3/2)
```
```text
5
1
6
1.5
```
### 거듭제곱
```python
print(3**2)
print(2.5**2)
print(2**(1/2))
```
```text
9
6.25
1.4142135623730951
```
### 몫과나머지
```python
print(11//2)
print(11%2)
```
```text
5
1
```
### 지수
```python
print(1e16)
print(1e15)
print(1e-4)
print(1e-5)
```
```text
1e+16
1000000000000000.0
0.0001
1e-05
```
### 진수
```python
print(bin(17))
print(oct(17))
print(hex(17))

print(0b10001)
print(0o21)
print(0x11)
```
```text
0b10001
0o21
0x11
17
17
17
```
### 논리연산
```python
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)
```
```text
True
False
True
True
False
True
```
### 비교연산
```python
print(4<3)
print(4>3)
print(4<=3)
print(4>=3)
print(4==3)
print(4!=3)
```
```text
False
True
False
True
False
True
```
## 변수
- 자료형의 값을 저장하는 공간
- 변수명 = 값
### 변수 생성시 주의사항
- 변수명은 문자, 수자, 밑줄기호(_) 를 이용하여 생성
- 숫자로 시작할 수 없음(3e)
- 대.소문자 구분
- 특수문자 사용불가 (no@, no#1)
- 예약어를 사용할 수 없음(True, False, and, or, not 등)
- 변수명에 공백을 포함 할 수 없음 (no 1)

## 자료형
### 문자열
```python
print("'\"'를 활용한 String 형식")
print('\'를 활용한 String 형식')
str="String 형식입니다."
print(str)
```
```text
'"'를 활용한 String 형식
'를 활용한 String 형식
String 형식입니다.
```
```python
str2='''여러 행으로 문자를 표현할 수 있습니다.
'애국가'
작사 : "미상"
동해물과 백두산이 마르고 닳도록
'''
print(str2)
```
```text
여러 행으로 문자를 표현할 수 있습니다.
'애국가'
작사 : "미상"
동해물과 백두산이 마르고 닳도록
```
```python
str3 = "파이션은 매우 좋은 언어입니다."
str4 = "!!!"
print(str3 + str4)
print(str3 + str4 * 3)
```
```text
파이션은 매우 좋은 언어입니다.!!!
파이션은 매우 좋은 언어입니다.!!!!!!!!!
```
### 리스트
- 리스트는 [] 를 이용하여 생성
- 리스트 내용은 숫자, 문자열, bool, 리스트, 튜플, 세트 등 가능
- 리스내 데이터 타입이 달라도 생성 가능
```python
list1 = [1,2,3,4,5,6,7]
print(list1)
type(list1)
```
```text
[1, 2, 3, 4, 5, 6, 7]
list
```
- 각 항목에 대해 [i] 형식으로 지정할 수 있다
```python
list2 = [10,"String",30.6,True,'50',6,7]
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print(list2[-1])
print(list2[-2])
```
```text
10
String
30.6
True
50
7
6
```
- list 내 항목 변경
```python
list3 = [10,"String",30.6,40,50,6,7]
print(list3)
list3[0] = "데이터를 변경합니다."
print(list3)
```
```text
[10, 'String', 30.6, 40, 50, 6, 7]
['데이터를 변경합니다.', 'String', 30.6, 40, 50, 6, 7]
```
- list 연산
```python
list4 = [1,True,'String']
list5 = [2,3,4]
print(list4+list5)
print(list4*3)
```
```text
[1, True, 'String', 2, 3, 4]
[1, True, 'String', 1, True, 'String', 1, True, 'String']
```
- list 데이터 추출하기
- [start : end : step]
```python
list6=[1,2,3,4,5,6,7,8,9,10]
print(list6)
print(list6[::])
print(list6[3:5:])
print(list6[1:4:2])
print(list6[::-1])
print(list6[0:3])
print(list6[3:10])
print(list6[:3])
print(list6[3:])
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[4, 5]
[2, 4]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
```
- list 값 삭제
```python
list7=[1,2,3,4,5,6,7,8,9,10]
print(list7)
del list7[3]
print(list7)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 5, 6, 7, 8, 9, 10]
```
- list 값 존재 여부
```python
list8=[1,2,3,4,5,6,7,8,9,10]
print(list8)
print(4 in list8)
print(14 in list8)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
True
False
```
- list 함수

| 리스트 함수 | 설명 |
| --- | --- |
|append (object) | 목록 끝에 요소 추가
|insert (index,object) | 정의 된 색인에 항목을 삽입
|extend (iterable) | 리스트의 모든 요소를 ​​다른리스트에 추가
|remove (value) | 목록에서 항목을 제거합니다
|pop (index) | 주어진 인덱스에서 요소를 제거하고 반환
|index (value) | 첫 번째 일치 항목의 인덱스를 반환
|count (value) | 인수로 전달 된 항목 수의 개수를 반환합니다.
|sort () | 목록의 항목을 오름차순으로 정렬
|reverse () | 목록의 항목 순서를 반대로 바꿉니다.
|clear () | 목록에서 모든 항목을 제거합니다
```python
list9=["손흥민","조규성","황의조","김승규"]
print(list9)
list9.append("이강인")
print(list9)
list9.insert(3,"이강인")
print(list9)
list9.extend(["김영권","황인범"])
print(list9)
list9.remove("손흥민")
print(list9)
member=list9.pop()
print(member)
print(list9)
print(list9.index("이강인"))
print(list9.count("이강인"))
list9.sort()
print(list9)
list9.reverse()
print(list9)
list9.clear()
print(list9)
```
```text
['손흥민', '조규성', '황의조', '김승규']
['손흥민', '조규성', '황의조', '김승규', '이강인']
['손흥민', '조규성', '황의조', '이강인', '김승규', '이강인']
['손흥민', '조규성', '황의조', '이강인', '김승규', '이강인', '김영권', '황인범']
['조규성', '황의조', '이강인', '김승규', '이강인', '김영권', '황인범']
황인범
['조규성', '황의조', '이강인', '김승규', '이강인', '김영권']
2
2
['김승규', '김영권', '이강인', '이강인', '조규성', '황의조']
['황의조', '조규성', '이강인', '이강인', '김영권', '김승규']
[]
```
```python
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
print(solarsys)
del solarsys[-1]
print(solarsys)

solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
del solarsys[1:7]
print(solarsys)
```
```text
['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '명왕성']
['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
['태양', '천왕성', '해왕성', '명왕성']
```
```python
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
moon = solarsys.index('지구')
solarsys.insert(moon,'달')
print(solarsys)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
solarsys.extend('헬리혜성')
print(solarsys)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
solarsys.extend(['헬리혜성'])
print(solarsys)
```
```text
['태양', '수성', '금성', '달', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '명왕성']
['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '명왕성', '헬', '리', '혜', '성']
['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '명왕성', '헬리혜성']
```
### 튜플
- 튜플은 () 를 이용하여 생성
- 튜플은 생선된 요소를 변경하거나 삭제가 불가함
```python
tuple1 = (1,2,3,4,5,6,7)
print(tuple1)
type(tuple1)
```
```text
(1, 2, 3, 4, 5, 6, 7)
tuple
```
- 튜플은 () 가 없어도 튜플로 인식
```python
tuple2 = 1,2,3,4,5,6,7
print(tuple2)
type(tuple2)
```
```text
(1, 2, 3, 4, 5, 6, 7)
tuple
```
- 인덱스 위치
```python
tuple3 = 1,2,3,4,5,6,7
print(tuple3[3])
```
```text
4
```
- 인자가 하나만 있더라도 마지막에 , 사용
```python
tuple4 = 1,
print(tuple4)
print(type(tuple4))
tuple5 = (2,)
print(tuple5)
```
```text
(1,)
<class 'tuple'>
(2,)
```
- 튜플 함수
```python
tuplue5 = 1,2,3,4,5,6,7,8,9,10,3,4,3,5
print(tuplue5.index(3))
print(tuplue5.index(3,4))
print(tuplue5.count(4))
```
```text
2
10
2
```

### 세트
- 수학의 집합 개념으로 데이터의 순서가 없고 중복하여 사용할 수 없음
- 교집합, 합집합, 차집합 사용가능
- 세트는 {} 를 사용함

```python
set1={1,2,3,4}
set2={1,2,2,2,3,4,5}
print(set1)
print(set2)
print(type(set1))
```
```text
{1, 2, 3, 4}
{1, 2, 3, 4, 5}
<class 'set'>
```
- 세트 연산자

| 연산 | 연산자 | 예 |
| --- | --- | --- |
| 교집합 | & | A.intersection(B) |
| 합집합 | \| | A.union(B) |
| 차집합 | - | A.difference(B) |
```python
set1={1,2,3,4}
set2={2,2,2,3,4,5}

print(set1&set2)
print(set1|set2)
print(set1-set2)
print(set2-set1)

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.intersection(set2))
```
```text
{2, 3, 4}
{1, 2, 3, 4, 5}
{1}
{5}
{2, 3, 4}
{1, 2, 3, 4, 5}
{2, 3, 4}
```
```python
BEST2018= set(["MESSI","ROLALDO","MBAPPE","HAZARD","KANTE","MODRIC","MARCELO","RAMOS","VARANE","ALVES","DEGEA"])
BEST2017= set(["MESSI","SUAREZ","ROLALDO","INIESTA","KROOS","MODRIC","MARCELO","RAMOS","PIQUE","ALVES","NEUER"])
print(BEST2018 & BEST2018)
print(BEST2018 - BEST2017)
print(BEST2018 | BEST2017)
```
```text
{'RAMOS', 'ALVES', 'ROLALDO', 'KANTE', 'MODRIC', 'VARANE', 'DEGEA', 'MESSI', 'MARCELO', 'HAZARD', 'MBAPPE'}
{'KANTE', 'VARANE', 'DEGEA', 'HAZARD', 'MBAPPE'}
{'RAMOS', 'ALVES', 'ROLALDO', 'SUAREZ', 'MODRIC', 'MESSI', 'KROOS', 'MARCELO', 'HAZARD', 'NEUER', 'MBAPPE', 'PIQUE', 'KANTE', 'VARANE', 'DEGEA', 'INIESTA'}
```
### 타입변환
- list()
- tuple()
- set()
```python
list10 = [1,2,3]
print(list10)
print(type(list10))

tuple10=tuple(list10)
print(tuple10)
print(type(tuple10))

set10=set(tuple10)
print(set10)
print(type(set10))

set11=list(set10)
print(set11)
print(type(set11))
```
```text
[1, 2, 3]
<class 'list'>
(1, 2, 3)
<class 'tuple'>
{1, 2, 3}
<class 'set'>
[1, 2, 3]
<class 'list'>
```
### 딕셔너리
- key : value 
```python
dict1={"성별":"남자","나이":20,"취미":["파이선","AI"]}
print(dict1)
print(type(dict1))
```
```text
{'성별': '남자', '나이': 20, '취미': ['파이선', 'AI']}
<class 'dict'>
```
- 값 가져오기
```python
print(dict1["성별"])
print(dict1["나이"])
print(dict1["취미"])
```
```text
남자
20
['파이선', 'AI']
```
- 값 수정하기
```python
dict1["나이"] = 21
print(dict1)
```
```text
{'성별': '남자', '나이': 21, '취미': ['파이선', 'AI']}
```
- 카 삭제하기
```python
dict1["나이"] = 21
print(dict1)
```
```text
{'성별': '남자', '취미': ['파이선', 'AI']}
```
- 딕셔너리 함수

| 함수 | 내용 |
| --- | --- |
|keys () | 키 전체 리스트 반환
|values () | 값 전체 리스트 반환
|items () | 키와 값을 튜플 평태로 반환
|update (dict) | 딕셔너리 데이터를 추가
|clear () | 목록에서 모든 항목을 제거합니다

```python
dic2={"성별":"남자","나이":20,"취미":["파이선","AI"]}
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())
dic2.update({"희망대학":"MIT"})
print(dic2)
dic2.clear()
print(dic2)
```
```text
{'성별': '남자', '나이': 20, '취미': ['파이선', 'AI']}
dict_keys(['성별', '나이', '취미'])
dict_values(['남자', 20, ['파이선', 'AI']])
dict_items([('성별', '남자'), ('나이', 20), ('취미', ['파이선', 'AI'])])
{'성별': '남자', '나이': 20, '취미': ['파이선', 'AI'], '희망대학': 'MIT'}
{}
```

## 제어문

### 조건문(if)

- 비교연산자

| 비교연산자 | 의미 |
| --- | --- |
| < | 작다
| > | 크다
| <= | 작거나 같다
| >= | 크거나 같다
| == | 같다
| != | 같지 않다

- 논리연산자

| 논리연산자 | 활용예 | 내용 |
| --- | --- | --- |
| 논리곱(and) | A and B | A와 B 둘다 참일 떄만 참
| 논리합(or) | A or B | A와 B 중 한 개발도 참일 경우 참
| 논리부정(not) | not A | A가 참이면 거짓, 거짓이면 참

```python
if <조건문>:
    <코드블록1>
elif <조건문2>:
    <코드블록2>
else:
    <코드블록3>
```
```python
score = int(input("점수를 입력하세요:"))
if score >= 60:
    print("통과")
else:
     print("과락")
```
```text
점수를 입력하세요:70
통과
점수를 입력하세요:50
과락
```
### 반복문(for)
```python
for <반복변수> in < 반복범위>:
    <코드블록>
```
- range(start, stop, step)
```python
for <반복변수> in < 반복범위>:
    <코드블록>
```
```python
for i in range(10):
    print("i=",i)
```
```text
i= 0
i= 1
i= 2
i= 3
i= 4
i= 5
i= 6
i= 7
i= 8
i= 9
```
```python
for i in range(2,10):
    print("i=",i)
```
```text
i= 2
i= 3
i= 4
i= 5
i= 6
i= 7
i= 8
i= 9
```
```python
for i in range(2,10,2):
    print("i=",i)
```
```text
i= 2
i= 4
i= 6
i= 8
```
```python
list=[1,2,4,5,8]
for i in list:
    print("i=",i)
```
```text
i= 1
i= 2
i= 4
i= 5
i= 8
```
```python
print(list(range(10)))
```
```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
print(list(range(0,20,5)))
```
```text
[0, 5, 10, 15]
```
```python
print(list(range(-10,0, 2)))
```
```text
[-10, -8, -6, -4, -2]
```
```python
x_list=['x1','x2']
y_list=['y2','y2']
print("X,Y")
for x in x_list:
    for y in y_list:
        print(x,y)
```
```text
X,Y
x1 y2
x1 y2
x2 y2
x2 y2
```
```python
x=0
y=0
print("x,y")
while(y<20):
    x+=1
    y+=x
    print(x,y)
```
```text
x,y
1 1
2 3
3 6
4 10
5 15
6 21
```

### 반복문(while)
```python
a=0
while True:
    a+=1
    if(a>5):
        break
    print(a)
```
```text
1
2
3
4
5
```
```python
i=0
while(i<4):
    print(" "*i,"*"*(7-i*2))
    i += 1
```
```text
 *******
  *****
   ***
    *
```
### 반복문제어
- break
- continue

### 간단한 한줄 for 문
```python
[<반복 실행문> for <반복변수> in <반복범위>]
```
```python
[<반복 실행문> for <반복변수> in <반복범위> if<조건문>]
```

```python
n=[1,3,5,7,9]
s=[]
for i in n:
    s.append(i**2)
    print(s)
```
```text
[1]
[1, 9]
[1, 9, 25]
[1, 9, 25, 49]
[1, 9, 25, 49, 81]
```
```python
n=[1,3,5,7,9]
s=[i**2 for i in n if i>=5]
print(s)
```
```text
[25, 49, 81]
```
## 입력 과 출력

### 화면출력

- 형식지정

```python
N=4
print("{0:4d}".format(N))
print("{0:04d}".format(N))
N=12
print("{0:>4d}".format(N))
N=0.123456
print("{0:.4f}".format(N))
N=123456000
print("{0:,}".format(N))
N=0.4789
print("{0:.2%}".format(N))
N=95700000000
print("{0:.3e}".format(N))
N=17
print("{0:#x}".format(N))
print("{0:#o}".format(N))
print("{0:#b}".format(N))
```
```text
   4
0004
  12
0.1235
123,456,000
47.89%
9.570e+10
0x11
0o21
0b10001
```
```python
print("Best","python","course", sep="**")
```
```text
Best**python**course
```
```python
name="Jun"
tall = 185
print("Name:",name +", Tall:",tall)
```
```text
Name: Jun, Tall: 185
```
```python
print("Jun is my friend.")
print("He is smart")
```
```text
Jun is my friend.
He is smart
```
```python
print("Jun is my friend.", end="")
print("He is smart")
```
```text
Jun is my friend.He is smart
```
```python
print("%d"%10)
print("%d %s"%(10, " 정수 형태 입니다."))
print("{0} {1} {2}".format(1, 2, 3))
```
```text
10
10  정수 형태 입니다.
1 2 3
```
```python
r=5
pi=3.141592
print("반지름:%d, 원주율:%f" %(r, pi))
```
```text
반지름:5, 원주율:3.141592
```
```python
cellphone_0="test1"
cellphone_1="test2"
cellphone_2="test3"

print("cellphone : {0}". format(cellphone_0))
print("cellphone : {0} {1} {2}". format(cellphone_0, cellphone_1, cellphone_2))
print("cellphone : {2} {1} {2}". format(cellphone_0, cellphone_1, cellphone_2))
print("cellphone : {} {} {}". format(cellphone_0, cellphone_1, cellphone_2))
```
```text
cellphone : test1
cellphone : test1 test2 test3
cellphone : test3 test2 test3
cellphone : test1 test2 test3
```
```python
a=1.1223123128731923891829
print("{0:.2f}, {0:.5f}".format(a))
```
```text
1.12, 1.12231
```
- 형식출력 방법 4
```python
#방법1
print("나는 %d살 입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s 색을 좋아해요" % ("파란","빨간"))
```
```text
나는 20살 입니다.
나는 파이썬를 좋아해요
Apple 은 A로 시작해요
나는 20살 입니다.
나는 파란색과 빨간 색을 좋아해요
```
```python
#방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {} 색을 좋아해요" .format("파란","빨간"))
print("나는 {0}색과 {1} 색을 좋아해요" .format("파란","빨간"))
print("나는 {1}색과 {0} 색을 좋아해요" .format("파란","빨간"))
```
```text
나는 20살 입니다.
나는 파란색과 빨간 색을 좋아해요
나는 파란색과 빨간 색을 좋아해요
나는 빨간색과 파란 색을 좋아해요
```
```python
#방법3
print("나는 {age}살이며, {color} 색을 좋아해요".format(age=20, color="빨간"))
```
```text
나는 20살이며, 빨간 색을 좋아해요
```
```python
#방법4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color} 색을 좋아해요")
```
```text
나는 20살이며, 빨간 색을 좋아해요
```
```python
#\n \" 
print("백문의 불여일견\n백견이 불여일타")
print("저도 \"나도코딩\" 입니다.")
print("저도 \'나도코딩\' 입니다.")
print('저도 "나도코딩" 입니다.')
#\\
print("C:\\김경덕\\Python")
print("C:\김경덕\Python")
#\r
print("Red Apple\rPine")
#\b
print("Red Apple\bPine")
#\t
print("Red Apple\tPine")
```
```text
백문의 불여일견
백견이 불여일타
저도 "나도코딩" 입니다.
저도 '나도코딩' 입니다.
저도 "나도코딩" 입니다.
C:\김경덕\Python
C:\김경덕\Python
PineApple
Red ApplPine
Red Apple	Pine
```

### 키보드 입력
```python
data=input("문자열")
```
```python
num=input("1-100 사이 숫자를 입력하세요")
print("당신이 입력한 숫자는 {} 입니다.".format(num))
```
```text
당신이 입력한 숫자는 10 입니다.
```
```python
num=input("1-100 사이 숫자를 입력하세요")
area=int(num)**2
print("당신이 입력한 숫자의 제곱은 {} 입니다.".format(area))
```
```text
당신이 입력한 숫자의 제곱은 100 입니다.
```
### 파일 읽고 쓰기
| mode | 내용 |
| --- | --- |
| r | 읽기, default |
| w | 쓰기 같은 파일 내용을 지우고 덮어쓰기|
| x | 쓰기, 같은 파일 존재시 오류 발생 |
| a | 쓰기, 같은 파일 존재시 추가, 없으면 쓰기 |
| b | 바이러리 파일 모드 |
| t | 텍스트 파일 모드 |

```python
f=open('file_name','mode')
```
```python
f=open('file_name','w')
f.write(str)
f.close()
```
```python
f=open('file_name','r')
data=f.read()
f.close()
```
```python
f=open("file.txt","w")
f.write("This is my first time")
f.close()
```
```python
!type file.txt
```
```text
This is my first time
```
```python
f=open("file.txt","r")
file_text=f.read()
f.close()
print(file_text)
```
```text
This is my first time
```
```python
f=open("file2.txt","w")
for num in range(6):
    format_string="2x{0}={1}\n".format(num, num*2)
    f.write(format_string)
f.close()
```
```python
!type file2.txt
```
```text
2x0=0
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
```
```python
f=open("file2.txt")
line=f.readline()
while line:
    print(line, end="")
    line=f.readline()
f.close()
```
```text
2x0=0
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
```
```python
f=open("file2.txt")
lines=f.readlines()
f.close()
print(lines)
```
```text
['2x0=0\n', '2x1=2\n', '2x2=4\n', '2x3=6\n', '2x4=8\n', '2x5=10\n']
```
```python
f=open("file2.txt")
lines=f.readlines()
f.close()
for line in lines:
    print(line,end="")
```
```text
2x0=0
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
```
```python
f=open("file2.txt")
for line in f.readlines():
    print(line,end="")
f.close()
```
```text
2x0=0
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
```
### with를 이용한 파일 읽고 쓰기
```python
with open('file_name','mode') as f:
    <코드블록>
```
```python
with open('file_name','w') as f:
    f.write(str)
```
```python
with open('file_name','r') as f:
    data=f.read()
```

## 함수

### 함수의 구조
```python
def 함수이름([인자1, 인자2, ....,인자n]):
    <코드블록>
    [return <반환 값>]
```
### 람다(lambda) 함수
```python
lambda<인자> : <인자 활용 수행 코드>
```

## 객체와 클래스
### 클래스 선언과 객체 생성
```python
class 클래스명():
    [변수1]
    [변수2]
    ...
    def 함수1(self[,인자1, 인자2, ...,안자n]):
        <코드블록>
        ...
    def 함수2(self[,인자1, 인자2, ...,안자n]):
        <코드블록>
        ...
```
### 클래스 상속
```python
class 자식클래스명(부모 클래스 이름):
    <코드블록>
        ...
```

## 문자열과 텍스트
### 문자열 분리
```python
str.split([sep,] maxsplit=숫자)
```
```python
str="에스프레소 아메리카노 카페라데 카푸치노"
print(str.split())
print(str.split(" ",2))
```
```text
['에스프레소', '아메리카노', '카페라데', '카푸치노']
['에스프레소', '아메리카노', '카페라데 카푸치노']
```
### 공백제거
```python
str="[  에스프레소  아메리카노  카페라데 카푸치노]  "
print(str.strip())
```
```text
[  에스프레소  아메리카노  카페라데 카푸치노]
```
### 문자열 합치기
```python
str_list=["부산광역시","남구","용소로","14번길10"]
print(" ".join(str_list))
print("-".join(str_list))
```
```text
부산광역시 남구 용소로 14번길10
부산광역시-남구-용소로-14번길10
```
### 문자열 함수
```python
str="Hello python a python python python"
search_str="python"
prefix="python"
print(str.find(search_str, 10))
print(str.count(search_str))
print(str.startswith(prefix,0))
print(str.startswith("Hello",0))
print(str.endswith(prefix,0))
print(str.replace(search_str,"java",2))
```
```text
15
4
False
True
True
Hello java a java python python
```
## 모듈
### 모듈이란
### 모듈 사용법
```python
import 모듈명
from 모듈명 import 변수명
from 모듈명 import 함수명
from 모듈명 import 클래스명
from 모듈명 import *
import 모듈명 as 별명
from 모듈명 import 변수명 as 별명
from 모듈명 import 함수명 as 별명
from 모듈명 import 클래스명 as 별명
```
### 내장모듈
- random
```python
import random
print(random.random())
print(random.randint(1,6))
print(random.randrange(0,10,2))
print(random.choice([1,2,3]))
print(random.choice(["사과","배","복숭아"]))
print(random.sample(["사과","배","복숭아","포도"],2))
print(random.sample(range(1,10),2))
```
```text
0.9857213195381337
2
2
2
사과
['사과', '포도']
[9, 6]
```
- datetime
```python
import datetime
print(datetime.timedelta(days=5, hours=17, minutes=30))
print(datetime.date.today())
print(datetime.date(2019, 12, 25))
```
```text
5 days, 17:30:00
2023-09-05
2019-12-25
```
- calendar
```python
import calendar
print(calendar.calendar(2023))
```
```text
                                  2023

      January                   February                   March
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
...
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31
```

```python
print(calendar.month(2023,9))
print(calendar.monthrange(2023,9))
print(calendar.firstweekday())
calendar.setfirstweekday(5)
print(calendar.firstweekday())
print(calendar.weekday(2023,9,5))
print(calendar.isleap(2023))
print(calendar.isleap(2024))
print(calendar.isleap(2025))
print(calendar.isleap(2026))
```
```text
September 2023
Sa Su Mo Tu We Th Fr
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

(4, 30)
5
5
1
False
True
False
False
```