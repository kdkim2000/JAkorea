| 목차 | 내용 |
| --- | --- |
| [연산](#연산)  |[사칙연산](#사칙연산) <br> [거듭제곱](#거듭제곱) <br> [몫과나머지](#몫과나머지) <br> [지수](#지수) <br> [진수](#진수) <br> [논리연산](#논리연산) <br> [비교연산](#비교연산) |
| [변수](#변수)       |
| [자료형](#자료형)    |[문자열](#문자열) <br> [리스트](#리스트) <br> [세트](#세트) <br>[타입변환](#타입변환) <br> [딕셔너리](#딕셔너리) |

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
{'성별': '남자', '취미': ['파이선', 'AI']}
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
```python
if <조건문>:
    <코드블록1>
elif <조건문2>:
    <코드블록2>
else:
    <코드블록3>
```
```python
```
```text
```
### 반복문(for)
```python
for <반복변수> in < 반복범위>:
    <코드블록>
range(start, stop, step)
```
```python
for <반복변수> in < 반복범위>:
    <코드블록>
range(start, stop, step)
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
### 반복문(while)
### 반복문제어