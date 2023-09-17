# Markdown 배우기

![](https://openai.com/favicon.ico) 
```
초보자에게 Markdown 언어를 배울 수 있는 교재의 목차를 알려 줘
```
---
# 목차
|  장  |         제목         |       부제목        |
|:----|:-------------------|:------------------|
| 서론  |                     |                    |
|      | 1.1 Markdown 이란?  |                    |
|      | 1.2 Markdown의 용도 |                    |
|      | 1.3 Markdown의 장점과 단점   |            |
| 기본 문법   |                     |                    |
|      |    2.1 헤더 (Headers)       |            |
|      |    2.2 단락 (Paragraphs)     || 
|      |2.3 줄바꿈 (Line Breaks)|
||   	2.4 강조 (Emphasis)|- 볼드체<br>- 이탤릭체<br>- 취소선|
||   	2.5 목록 (Lists)|- 순서 있는 목록 <br>- 순서 없는 목록|
||   	2.6 링크 (Links)|- 인라인 링크 <br>- 참조 링크|
||   	2.7 이미지 추가하기 (Images)||
| 고급 문법||
||3.1 블록 인용문(Blockquotes)|
||3.2 코드(Code)<br> - 인라인 코드<br> - 코드 블럭|
||3.3 표(Tables)|
||3.4 체크 박스(Checkboxes)|
|Markdown 응용||
||- GitHub Flavored Markdown(GFM)<br> - 다른 도구와 함께 사용하기(예: Jekyll, Hugo 등)|
|실전 예제||
||* README 파일 작성하기
||부록: 유용한 리소스 및 도구들|


# 서론
## 1.1 Markdown 이란?
Markdown은 텍스트를 HTML로 변환하는 경량 마크업 언어입니다. 2004년에 존 그루버(John Gruber)와 아론 스워츠(Aaron Swartz)가 만들었습니다.

Markdown은 문법이 간단하고 배우기 쉬워서, 개발자뿐만 아니라 많은 사람들이 웹 콘텐츠를 작성하는 데 사용합니다. README 파일, 위키, 포럼, 블로그 포스트 등 다양한 곳에서 활용됩니다.

주요 특징은 다음과 같습니다
|     주요 특징    |                             설명                            |
|:---------------:|:----------------------------------------------------------|
| 간결함          | Markdown의 문법은 간단하고 직관적입니다.                      |
| 변환 용이성    | Markdown으로 작성된 텍스트는 쉽게 HTML로 변환할 수 있습니다.   |
| 읽기 쉬움      | Markdown 문서는 일반 텍스트 파일이므로 별도의 도구 없이도 읽을 수 있습니다. |
| 호환성         | 거의 모든 텍스트 에디터와 웹 기반 도구에서 사용할 수 있습니다.   |
| 다양한 변형    | GitHub Flavored Markdown(GFM) 등과 같은 다양한 변형 버전이 있어서 활용 범위가 넓습니다.  |

마크다운 문법을 사용하면 복잡한 HTML 태그 없이도 깔끔하게 서식 있는 텍스트를 작성할 수 있으며, 이렇게 작성된 마크다운 파일은 웹 브라우저에서 바로 확인할 수 있습니다.

## 1.2 Markdown의 용도
Markdown의 주요 사용처를 표로 정리하면 다음과 같습니다:

|     주요 사용처    |                             설명                            |
|:------------------|:----------------------------------------------------------|
| 문서 작성         | 개발자들은 코드와 함께 문서를 작성하는 데 Markdown을 많이 사용합니다. 특히 README 파일, API 문서, 개발자 가이드 등에 이용됩니다. |
| 블로그 포스팅     | 많은 블로그 플랫폼과 정적 사이트 생성기(Jekyll, Hugo 등)가 Markdown을 지원합니다. 따라서 사용자는 복잡한 HTML 대신 Markdown을 이용해 콘텐츠를 쉽게 작성하고 관리할 수 있습니다. |
| 노트 작성         | Notion, Typora 등의 노트 앱에서는 Markdown 형식으로 노트를 작성할 수 있습니다. |
| 위키 및 지식베이스 생성  | GitHub 위키 같은 곳에서는 페이지를 만들거나 편집할 때 Markdown을 사용합니다. |
| 온라인 커뮤니케이션   | StackOverflow, Reddit, Discourse 등의 플랫폼에서는 게시글이나 댓글을 작성할 때 Markdown 형식을 이용합니다. |

Markdown은 그 간결함과 유연함으로 인해 다양한 분야에서 활용되며 그 용도가 계속 확장되고 있습니다.

## 1.3 Markdown의 장점과 단점
Markdown은 여러 가지 장점을 가지고 있지만, 동시에 일부 단점도 존재합니다. 다음은 그 중 몇 가지를 정리한 것입니다:

|     분류    |                             내용                            |
|:-----------------:|:----------------------------------------------------------|
| 간결함| Markdown의 문법은 간단하고 직관적이며, HTML보다 훨씬 적은 태그를 사용합니다. |
| 읽기 쉬움| Markdown 문서는 일반 텍스트 파일이므로 별도의 도구 없이도 읽을 수 있습니다. |
| 호환성 | 거의 모든 텍스트 에디터와 웹 기반 도구에서 사용할 수 있습니다. |
| 포맷 변환 용이성| Markdown으로 작성된 문서는 HTML 뿐만 아니라 PDF, MS Word 등 다양한 형식으로 변환할 수 있습니다. |

---

|     분류    |                             내용                            |
|:-----------------:|:----------------------------------------------------------|
| 표준화 부재 | 많은 변형 버전(GitHub Flavored Markdown 등)이 존재하므로, 어떤 버전을 사용해야 할 지 혼란스러울 수 있습니다. |
| 복잡한 서식 제한 | 복잡한 서식(테이블, 각주 등)을 만드는 데 한계가 있다는 비판도 있습니다. |
| 비 개발자 친화적인 면모 | 비 개발자들에게는 처음에 약간 낯설 수 있는 면모가 있다는 점입니다. |



# Markdown 기본 문법
## 2.1 헤더 (Headers)
```
Markdown에서 헤더(Headers)는 문서의 제목이나 부제목을 나타내는 데 사용되며, HTML의 <h1>부터 <h6>까지의 태그에 해당합니다.
```

Markdown에서 헤더를 작성하는 방법은 두 가지가 있습니다:

### 해시(#) 기호를 이용한 방법
```
해시(#) 기호를 이용하여 <h1>부터 <h6>까지의 헤더를 나타낼 수 있습니다. #의 개수가 많아질수록 글자 크기는 작아집니다.
```
```markdown
# h1
## h2
### h3
#### h4
##### h5
###### h6
```
# h1
## h2
### h3
#### h4
##### h5
###### h6

위 코드는 아래와 같이 변환됩니다:

```html
<h1>h1</h1>
<h2>h2</h2>
<h3>h3</h3>
<h4>h4</h4>
<h5>h5</h5>
<h6>h6</h6>
```

### 밑줄을 이용한 방법
```
텍스트 아래에 = 혹은 -을 사용하면 각각 <H1>과 <H2>에 해당합니다.
```
```markdown
H1 Header 
===

H2 Header 
---
```
H1 Header 
===
H2 Header 
---
위 코드는 아래와 같이 변환됩니다:

```html
<h1>H1 Header </hi>
<h2>H2 Header </hi>
```

해시(#) 기호를 이용한 방식은 6개 까지의 서로 다른 크기로 표현할 수 있어서 더 유연하지만, 밑줄을 사용하는 방식은 보다 명확하게 제목과 내용을 구분할 수 있다는 장점이 있습니다.


## 2.2 단락 (Paragraphs)

Markdown에서 단락(Paragraphs)은 매우 간단하게 생성할 수 있습니다. 일반적으로, 단락은 하나 이상의 연속된 텍스트 줄입니다. 단락을 분리하려면 하나 이상의 빈 줄을 사용합니다.

예를 들어, 다음과 같이 Markdown을 작성하면

```markdown
This is a paragraph. It has two sentences.

This is another paragraph. It also has two sentences.
```
다음과 같이 HTML로 변환됩니다:

```html
<p>This is a paragraph. It has two sentences.</p>

<p>This is another paragraph. It also has two sentences.</p>
```
Markdown에서는 단락 내부에 있는 개행(newline)은 그대로 개행으로 처리되지 않습니다. 

즉, Markdown에서 줄 바꿈을 위해선 실제로 두 번의 개행(엔터 키 두 번)이 필요합니다.

만약 한 줄 바꿈만으로도 실제 출력 결과에 반영하고 싶다면, 문장 끝에 공백(space) 두 개를 추가하면 됩니다:

```markdown
This is a line.
And this line will be right below the previous one.
```
위 코드는 아래와 같이 변환됩니다:

```html
<p>This is a line.<br>
And this line will be right below the previous one.</p>
```

## 2.3 줄바꿈 (Line Breaks)
Markdown에서 줄바꿈(Line Breaks)을 생성하는 방법은 두 가지입니다:

### 두 개의 공백
문장의 끝에 공백(space) 두 개를 추가하면 그 다음에 오는 텍스트는 새로운 줄에서 시작됩니다.

예시:

```markdown
This is the first line.  
And this is the second line.
``````
위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<p>This is the first line.<br>
And this is the second line.</p>
```
### 빈 줄을 사용
빈 줄(empty line)을 사용하여 새 단락(paragraph)을 생성하면, 그 결과는 시각적으로 새 줄에서 시작하는 텍스트와 비슷합니다.

예시:

```markdown
This is the first paragraph.

And this is the second paragraph.
```
위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<p>This is the first paragraph.</p>

<p>And this is the second paragraph.</p>
```

```
이렇게 보면, Markdown에서의 "줄 바꿈"은 실제로 HTML의 <br> 태그를 생성하거나 새 <p>(단락)를 시작하는 방법 중 하나라고 볼 수 있습니다.
```

## 2.4 강조 (Emphasis)
Markdown에서는 텍스트를 강조하기 위해 별표(*) 또는 언더스코어(_)를 사용합니다. 이 기호들을 사용하여 텍스트를 이탤릭체로 만들거나 굵게 할 수 있습니다.

### 이탤릭체
텍스트 앞뒤에 별표(*) 또는 언더스코어(_) 한 개를 넣으면 해당 텍스트는 이탤릭체로 변환됩니다.
```markdown
*This text will be italic*
_This will also be italic_
```
*This text will be italic*<br>
_This will also be italic_

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<em>This text will be italic</em>
<em>This will also be italic</em>
```
### 굵은 글씨
텍스트 앞뒤에 별표(*) 또는 언더스코어(_) 두 개를 넣으면 해당 텍스트는 굵은 글씨로 변환됩니다.
```markdown
**This text will be bold**
__This will also be bold__
```
**This text will be bold** <br>
__This will also be bold__

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<strong>This text will be bold</strong>
<strong>This will also be bold</strong>
```
### 굵은 이탤릭체
```
텍스트 앞뒤에 별표(*) 세 개 또는 언더스코어(_) 세 개를 넣으면 해당 텍스트는 굵은 이탤릭체로 변환됩니다.
```
```markdown
***This text will be bold and italic***
___This will also be bold and italic___
```
***This text will be bold and italic***<br>
___This will also be bold and italic___

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<strong><em>This text will be bold and italic</em></strong>
<strong><em>This will also be bold and italic</em></strong>
```
각각의 방법을 적절하게 혼합하여 사용할 수 있으며, 강조할 부분만 정확하게 감싸주면 됩니다.

## 2.5 목록 (Lists)
Markdown에서는 순서 있는 목록과 순서 없는 목록을 모두 생성할 수 있습니다.

### 순서 있는 목록 (Ordered Lists)
숫자와 점(.)을 사용하여 순서 있는 목록을 만듭니다.
```markdown
1. First item
2. Second item
3. Third item
```
1. First item
2. Second item
3. Third item

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```
### 순서 없는 목록 (Unordered Lists)
별표(*), 더하기(+), 또는 하이픈(-)을 사용하여 순서 없는 목록을 만듭니다.
```markdown
* Item 1
* Item 2
* Item 3

or

- Item 1
- Item 2
- Item 3

or 

+ Item 1 
+ Item 2 
+ Item 3 
```
위 코드들은 모두 아래와 같이 HTML로 변환됩니다:

```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

or 

<ul>
    <li>Item A </i></ul></i></ul></i></ul><i><ul><i><ul><i><ul>
```

### 중첩된 목록
공백(스페이스 또는 탭)으로 들여쓰기를 하면 중첩된(nested) 리스트를 생성할 수 있습니다.

```markdown
1. First item:
   - Subitem a 
   - Subitem b  
     - Sub-subitem i  
     - Sub-subitem ii  
2. Second item:
   * Subitem c  
   * Subitem d  
```
1. First item:
   - Subitem a 
   - Subitem b  
     - Sub-subitem i  
     - Sub-subitem ii  
2. Second item:
   * Subitem c  
   * Subitem d 

위 코드들은 아래와 같이 HTML로 변환됩니다

```html
<ol>
    <li>First item:
        <ul>
            <li>Subitem a </li>
            <li>Subitem b </li>
            <ul>
                <li>Sub-subitem i </li>
                <li>Sub-subitem ii </li>
            </ul>
        </ul>
    <li >Second item :
        <ul >
            <li>Sub item c</li>
            <li>Sub item d</li> 
        </ul>
    </li>
</ol> 

```
<ol>
    <li>First item:
        <ul>
            <li>Subitem a </li>
            <li>Subitem b </li>
            <ul>
                <li>Sub-subitem i </li>
                <li>Sub-subitem ii </li>
            </ul>
        </ul>
    <li >Second item :
        <ul >
            <li>Sub item c</li>
            <li>Sub item d</li> 
        </ul>
    </li>
</ol>

## 2.6 링크 (Links)

Markdown에서는 링크를 생성하는 데 두 가지 주요 방법이 있습니다: 인라인 링크와 참조 링크입니다.

### 인라인 링크 (Inline Links)
인라인 링크는 URL을 직접 문서에 포함시키는 방식입니다. 다음과 같은 형식을 사용합니다:
```markdown
[Google](https://www.google.com)
```
[Google](https://www.google.com)

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<a href="https://www.google.com">Google</a>
```
### 참조 링크 (Reference Links)
참조 링크는 페이지의 다른 부분에 정의된 링크를 재사용하는 방식입니다. 이렇게 하면 동일한 URL을 여러 번 사용해야 하는 경우 유용하며, 문서가 깔끔하게 유지됩니다.
```markdown
[Google][1]

[1]: https://www.google.com
```
위 코드도 마찬가지로 아래와 같이 HTML로 변환됩니다

[Google][1]

[1]: https://www.google.com

```html
<a href="https://www.google.com">Google</a>
```
추가적으로, Markdown에서는 URL이나 이메일 주소를 감싸고 있는 < 와 >를 통해 자동으로 클릭 가능한 링크를 생성할 수 있습니다.

예시:

```markdown
<http://www.example.com>
<example@example.com>
```
위 코드들은 간단하게 아래와 같이 HTML로 변환됩니다.

<http://www.example.com>

<example@example.com>


```html
<a href="http://www.example.com">http://www.example.com</a>
<a href="mailto:example@example.com">example@exampl
```

## 2.7 이미지 추가하기 (Images)

Markdown에서는 이미지를 쉽게 추가할 수 있습니다. 링크와 비슷한 구조를 가지고 있지만, 앞에 느낌표(!)가 붙습니다.

### 인라인 이미지 (Inline Images)
다음과 같은 형식을 사용하여 인라인 이미지를 추가합니다:

```markdown
![Alt Text](url)
```
여기서 Alt Text는 이미지가 로드되지 않을 때 대신 표시되는 텍스트이며, url은 실제 이미지의 URL입니다. 예를 들면,

```markdown
![OpenAI Logo](https://openai.com/favicon.ico)
```
![OpenAI Logo](https://openai.com/favicon.ico)

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<img src="https://openai.com/favicon.ico" alt="OpenAI Logo">
```
### 참조 이미지 (Reference Images)
참조 링크와 유사하게, 참조 이미지도 가능합니다. 이렇게 하면 동일한 URL을 여러 번 사용해야 하는 경우 문서를 깔끔하게 유지할 수 있습니다.

```markdown
![OpenAI Logo][1]

[1]: https://openai.com/favicon.ico
```

![OpenAI Logo][1]

[1]:https://openai.com/favicon.ico

위 코드도 마찬가지로 아래와 같이 HTML로 변환됩니다:

```html
<img src="https://openai.com/favicon.ico" alt="OpenAI Logo">
```

# Markdown 고급 문법
##	3.1 블록 인용문(Blockquotes) 
Markdown에서는 블록 인용문(blockquotes)을 생성하기 위해 > 문자를 사용합니다. 이 기호를 문장이나 단락의 시작 부분에 넣으면, 해당 내용은 블록 인용문으로 처리됩니다.

예시:

```markdown
> This is a blockquote.
```
> This is a blockquote.

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<blockquote>
  <p>This is a blockquote.</p>
</blockquote>
```
블록 인용문은 중첩될 수 있습니다. 즉, > 문자를 여러 개 연속해서 사용하면 더 깊은 레벨의 인용문을 생성할 수 있습니다.

예시:

```markdown
> This is a blockquote.
>> This is a nested blockquote.
>>> And this is a nested-nested blockquote.
```
> This is a blockquote.
>> This is a nested blockquote.
>>> And this is a nested-nested blockquote.

위 코드는 아래와 같이 HTML로 변환됩니다:

```html
<blockquote>
  <p>This is a blockquote.</p>
  <blockquote>
    <p>This is a nested blockquote.</p>
    <blockquote>
      <p>And this is a nested-nested blockquote.</p>
    </blockquote>
  </blockquote>
</blockquote>
```
블록 인용문 안에 다른 Markdown 요소(제목, 목록, 코드 등)를 포함할 수도 있습니다. 이렇게 하려면 각 줄에서 적절한 Markdown 구문을 사용하면 됩니다.

 ##	3.2 코드(Code) 
 Markdown에서는 코드를 표현하는 데 두 가지 주요 방법이 있습니다: 인라인 코드와 코드 블록입니다.

### 인라인 코드 (Inline Code)
인라인 코드는 백틱(  `) 문자로 감싸서 표현합니다. 이 방식은 문장 중간에 짧은 코드나 변수 이름 등을 표시할 때 사용합니다.
```markdown
Here is some inline `code`.
```
Here is some inline `code`.

위의 마크다운은 아래와 같이 HTML로 변환됩니다:

```html
<p>Here is some inline <code>code</code>.</p>
```
### 코드 블록 (Code Blocks)
여러 줄의 코드를 표시하려면, 세 개의 백틱으로 감싼 형태를 사용합니다.
```java
function helloWorld() {
    console.log("Hello, world!");
}
```

위의 마크다운은 아래와 같이 HTML로 변환됩니다:

```html
<pre><code>function helloWorld() {
  console.log("Hello, world!");
}</code></pre>
```
언어 지정된 구문 강조 (Syntax Highlighting): Markdown에서는 세 개의 백틱 다음에 프로그래밍 언어 이름을 명시함으로써 해당 언어에 맞는 구문 강조(syntax highlighting) 기능을 사용할 수 있습니다. 이 기능은 Markdown 처리기가 이를 지원해야 합니다.

예시(Python):

<pre>
```python
def hello_world():
    print("Hello, world!")
```
</pre>
```python
def hello_world():
    print("Hello, world!")
```
위의 마크다운 예제는 Python 구문에 따라 적절하게 강조되며 HTML로 변환될 때도 동일한 형태를 유지합니다.

 ##	3.3 표(Tables)  
 Markdown에서는 간단한 표를 만들 수 있습니다. 각 열은 파이프(|)로 구분하며, 헤더와 본문은 대시(-)와 파이프로 구분합니다.

다음과 같은 형식을 사용합니다:

```markdown
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Column 2 | Column 3 |
| Row 2    | Column 2 | Column 3 |
```
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Column 2 | Column 3 |
| Row 2    | Column 2 | Column 3 |

위의 마크다운 코드는 아래와 같이 HTML로 변환됩니다:

```html
<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1</td>
            <td>Column 2</td>
            <td>Column 3</td>
        </tr>
        <tr>
            <td>Row2 </td>
            <td>Column2 </td >
            <td>Column3 </ td >
        </tr>
    </tbody>
</table>
```
또한, 콜론(:)을 사용하여 열의 정렬 방향을 지정할 수 있습니다. 왼쪽에 콜론을 두면 왼쪽 정렬, 오른쪽에 두면 오른쪽 정렬, 양쪽에 두면 가운데 정렬됩니다.

예시:

```markdown
| Left-aligned   | Center-aligned   | Right-aligned   |
| :------------- | :--------------: | --------------: |
| Cell           | Cell             | Cell            |
```
| Left-aligned   | Center-aligned   | Right-aligned   |
| :------------- | :--------------: | --------------: |
| Cell           | Cell             | Cell            |

위의 마크다운 코드는 아래와 같이 HTML로 변환되며, 각 열은 지정된 방향으로 정렬됩니다.



```html
<table>
    <thead >
        <tr >
            <th style="text-align:left" >Left -aligned </th>
            <th style="text-align:center" >Center -aligned </th>
            <th style="text-align:right" >Right -aligned </th>
        </tr>
    </thead >
    <tbody >
        <tr>
            <td style="text-align:left" >Cell </td >
            <td style="text-align:center" >Cell </td >
            <td style="text-align:right" >Cell </td >
        </tr>
    </tbody>
</table>
```
## 3.4 체크박스(Checkboxes)

Markdown에서는 체크박스를 만드는 것도 가능합니다. 이 기능은 주로 할 일 목록(to-do list) 등을 만들 때 사용됩니다. 대괄호([ ])를 사용하여 체크박스를 표시하며, 대괄호 안에 x 문자를 넣으면 체크된 상태로 표시됩니다.

다음과 같은 형식을 사용합니다:

```markdown
- [ ] Item 1
- [x] Item 2
```
- [ ] Item 1
- [x] Item 2

위의 마크다운 코드는 아래와 같이 HTML로 변환됩니다:

```html
<ul>
    <li><input type="checkbox"> Item 1</li>
    <li><input type="checkbox" checked> Item 2</li>
</ul>
```
위의 예제에서 보듯이, Markdown 처리기가 이러한 형식의 체크박스를 지원해야 합니다. 일부 처리기(예: GitHub Flavored Markdown)에서는 이러한 형식의 체크박스가 지원되지만, 모든 처리기에서 지원되지 않습니다.

참고로, HTML 변환 결과에서 실제 `<input>` 태그가 생성되지만, 이것은 단순히 예시일 뿐 실제로 브라우저에 그려질 때는 다르게 보일 수 있습니다.

# Markdown 응용	
GitHub Flavored Markdown(GFM)은 GitHub에서 사용하는 Markdown의 변형 버전입니다. 기본적인 Markdown 문법에 추가로 몇 가지 기능이 더해져 있습니다.

GFM의 주요 특징은 다음과 같습니다:

URL 자동 링크: GFM에서는 URL을 자동으로 링크로 변환합니다. 이 기능은 일반적인 Markdown에서는 지원되지 않습니다.

### 체크박스
위에서 설명한 것처럼, GFM에서는 체크리스트를 만들 수 있습니다.
```markdown
- [ ] unchecked item
- [x] checked item
```
- [ ] unchecked item
- [x] checked item

### 표(Table)
GFM에서는 간단한 표를 만드는 것이 가능합니다.
```markdown
| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |
```
| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |

### 코드 강조(Syntax Highlighting)
GFM에서는 코드 블록에 프로그래밍 언어를 명시하여 해당 언어에 맞게 구문 강조가 적용됩니다.

<pre>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
</pre>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

### 줄바꿈(Line Breaks): 
일반적인 Markdown과 달리, GFM은 줄의 끝에 있는 공백 문자 없이도 자동으로 줄 바꿈을 인식합니다.

### 스트라이크스루(Strike Through)
`~~` 텍스트 `~~` 형식을 사용하여 취소선(strike through)을 추가할 수 있습니다.

```markdown
~~strikethrough text~~
```
~~strikethrough text~~

# 실전 예제
* README 파일 작성하기 
README 파일은 프로젝트의 첫 페이지로, 프로젝트에 대한 중요한 정보를 제공하는 문서입니다. README 파일은 보통 다음과 같은 내용을 포함합니다:

프로젝트의 이름 및 간단한 설명
설치 방법
사용 방법
기여 방법
라이센스 정보
아래는 이러한 요소들을 포함하는 간단한 README.md 파일 작성 예제입니다:

<pre>
# Project Name

This is a simple description of the project. It explains what the project does and why it is useful.

## Installation

Describe how to install the project/library/software. It could be as simple as:

```python
pip install yourproject
```

## Usage 

Explain how to use the project. Provide some examples.

```python
import yourproject

yourproject.do_something()
```
## Contributing
Explain how to contribute to your project. For example:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Include information about the license. If you're using a standard license such as MIT or GPL, you might simply write:

MIT
</pre>

위의 예제는 매우 기본적인 형태이며 실제 README 파일에서는 더 많은 섹션과 복잡성

# 부록: 유용한 리소스 및 도구들

Markdown을 사용하면서 도움이 될 수 있는 몇 가지 유용한 리소스와 도구들을 소개합니다:

1. **[Markdown Guide](https://www.markdownguide.org/)**: Markdown 문법에 대한 기본적인 내용부터 고급 기능까지 다루고 있습니다.

2. **[GitHub Flavored Markdown Spec](https://github.github.com/gfm/)**: GitHub에서 사용하는 Markdown의 변형 버전인 GFM에 대한 자세한 사양입니다.

3. **[Dillinger](https://dillinger.io/)**: 온라인 상에서 Markdown 문서를 작성하고 미리보기를 할 수 있는 편집기입니다.

4. **[StackEdit](https://stackedit.io/app#)**: 온라인 상의 Markdown 편집기로, Google Drive나 Dropbox와 같은 클라우드 저장소와 연동하여 사용할 수 있습니다.

5. **[Typora](https://typora.io/)**: 매우 강력하고 아름다운 UI를 가진 데스크톱용 Markdown 편집기입니다.

6. **VS Code**: Visual Studio Code는 코드 편집기이지만, 확장 프로그램을 설치함으로써 다양한 언어를 지원합니다. 그 중에도 "Markdown All in One" 확장 프로그램을 설치하면 VS Code에서도 간편하게 Markdown 문서를 작성할 수 있습니다.

7. **[Pandoc](https://pandoc.org/)**: "유니버설 문서 변환 도구"로, 여러가지 마크업 언어간에 변환을 할 수 있으며 이 중에서도 마크다운(Markdown)을 HTML, PDF, Word 등으로 변환하는데 유용합니다.
   
이 외에도 여러가지 마크다운 관련 도구들이 존재합니다만 위의 목록들은 가장 널리 알려져있고 사용되는 리소스 및 도구들입니다.
