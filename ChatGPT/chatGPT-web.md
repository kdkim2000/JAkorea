# 파이썬으로 웹 프로그램 만들기
웹 개발을 집을 짓는 것에 비유하면 이해하기 쉽습니다.

**백엔드(Backend)** 는 집의 기반이나 구조를 만드는 것과 같습니다. 이는 사용자가 보지 못하는 부분이지만, 실제로 웹사이트의 핵심 기능을 담당하고 있습니다. 백엔드에서는 데이터베이스 관리, 서버 설정, 사용자 인증 등의 작업을 수행합니다. 이러한 작업은 웹사이트가 제대로 작동하게 만드는 핵심적인 역할을 합니다.

백엔드에서 사용되는 주요 프로그래밍 언어로는 Python, Java, PHP, Node.js 등이 있습니다.

**프론트엔드(Frontend)** 는 집의 외관이나 인테리어 디자인과 같습니다. 사용자가 직접 보고 상호작용하는 부분입니다. 프론트엔드에서는 웹사이트의 디자인, 레이아웃, 사용자 인터페이스 등을 만듭니다. 이는 사용자의 경험을 직접적으로 영향을 미치며, 사용자가 웹사이트를 쉽고 효과적으로 사용할 수 있도록 돕습니다.

프론트엔드에서는 HTML, CSS, JavaScript 등의 언어를 사용하며, React.js, Angular.js, Vue.js 등의 프레임워크를 활용하여 더 효율적으로 개발할 수 있습니다.

따라서, 백엔드와 프론트엔드는 웹사이트를 만드는 데 있어서 모두 중요하며, 서로 다른 역할을 수행합니다. 두 영역 모두를 다루는 개발자를 '풀스택(Full Stack) 개발자'라고 합니다.

## 파이썬 백엔드 프로그램
웹 개발에서 백엔드(Backend)는 사용자에게 직접적으로 보이지 않지만, 웹사이트의 핵심 기능을 구현하는 부분을 말합니다. 예를 들어, 데이터베이스와의 연동, 사용자 인증, 서버 설정 등의 작업이 백엔드 개발에 해당합니다.

파이썬(Python)은 이러한 백엔드 개발에 널리 사용되는 언어 중 하나입니다. 그 이유는 다음과 같습니다:

| 이유 | 설명 |
| :---: | :--- |
| 읽기 쉬운 문법 | 파이썬의 문법은 간결하고 명확하며, 영어 문장과 비슷하여 읽기 쉽습니다. 이로 인해 코드의 가독성이 좋고, 디버깅이 용이합니다. |
| 풍부한 라이브러리 | 파이썬은 웹 개발, 데이터 분석, 인공지능 등 다양한 분야에서 사용할 수 있는 라이브러리를 제공합니다. |
| 프레임워크의 다양성 | Django, Flask, FastAPI 등 다양한 웹 프레임워크를 선택할 수 있습니다. 이들 프레임워크는 웹 개발을 더 효율적으로 할 수 있게 도와줍니다. |


## 파이썬 프레임워크

웹 개발을 할 때, 모든 것을 처음부터 만들기는 매우 어렵고 시간이 많이 걸립니다. 그래서 개발자들은 이미 잘 만들어진 도구들을 사용해서 웹 사이트를 만드는데, 이런 도구들을 '프레임워크'라고 부릅니다.

파이썬의 프레임워크는 이런 도구 중 하나인데요, Django나 Flask와 같은 프레임워크를 사용하면 웹 사이트를 더 쉽고 빠르게 만들 수 있습니다. 이러한 프레임워크는 웹 사이트를 만드는 데 필요한 여러 기능들을 이미 준비해두고 있기 때문입니다.

예를 들어, 웹 사이트에서는 보통 사용자의 정보를 관리하는 기능이 필요한데, 이런 기능을 '인증'이라고 합니다. Django 같은 프레임워크를 사용하면, 이런 인증 기능을 직접 만들지 않아도 됩니다. Django가 이미 이런 기능을 잘 만들어놓았기 때문이죠.

그래서 파이썬의 프레임워크를 사용하면, 웹 개발을 처음 시작하는 초보자도 복잡한 웹 사이트를 비교적 쉽게 만들 수 있습니다. 물론, 이렇게 만든 웹 사이트를 잘 관리하고, 원하는 대로 기능을 추가하려면 파이썬과 프레임워크에 대해 계속 공부해야 합니다.

간단히 말해서, 파이썬의 프레임워크는 웹 사이트를 만드는 데 필요한 여러 도구와 기능을 미리 준비해둔 도구 세트입니다. 이를 사용하면 웹 개발을 더 쉽고 빠르게 할 수 있습니다.

### 파이썬 프레임 웍 종류

| 프레임워크 | 설명 |
|------------|------|
| Django | 강력하고 다양한 기능을 제공하는 풀스택 프레임워크입니다. |
| Flask | 가벼운 마이크로 프레임워크로, 필요한 기능만 선택적으로 추가하여 사용할 수 있습니다. |
| Pyramid | 유연성과 확장성을 중점으로 두는 프레임워크입니다. |
| Tornado | 비동기 네트워킹 라이브러리를 내장한 웹 프레임워크로, 실시간 웹 서비스를 구축하는 데 유용합니다. |
| Bottle | 단일 파일로 구성된 마이크로 웹-프레임워크로, 간단한 웹 애플리케이션을 빠르게 개발하는 데 적합합니다. |
| FastAPI | 빠르고 쉬운 API 개발을 위한 현대적인 프레임워크로, 비동기 처리를 지원하며 타입 체킹과 자동 문서화 기능을 제공합니다. |


### Django

| 기능 | 설명 |
|------|------|
| 관리자 인터페이스 | 사용자, 그룹, 권한 등을 쉽게 관리할 수 있는 관리자 페이지를 제공합니다. |
| 데이터베이스 인터페이스 | SQL 없이도 데이터베이스를 쉽게 조작할 수 있도록 도와줍니다. |
| 인증 및 권한 | 사용자 인증, 권한 관리, 비밀번호 변경 등의 기능을 제공합니다. |
| URL 라우팅 | URL을 특정 함수와 매핑해주는 기능을 제공합니다. |
| 템플릿 엔진 | HTML 코드 안에 파이썬 코드를 넣어 동적인 웹 페이지를 만들 수 있도록 도와줍니다. |
| 폼 | HTML 폼을 쉽게 다룰 수 있게 해줍니다. 검증(Validation) 기능도 포함되어 있습니다. |
| 세션 및 쿠키 | 사용자 세션과 쿠키를 쉽게 다룰 수 있게 해줍니다. |
| RSS 및 Atom 피드 | RSS 및 Atom 피드를 쉽게 만들 수 있게 해줍니다. |
| 캐싱 | 웹 사이트의 속도를 높이기 위한 다양한 캐싱 기능을 제공합니다. |

### Flask
| 기능 | 설명 |
|------|------|
| 라우팅 | URL을 특정 함수와 연결해주는 기능을 제공합니다. |
| 템플릿 엔진 | HTML 코드 안에 파이썬 코드를 넣어 동적인 웹 페이지를 만들 수 있도록 도와줍니다. |
| 요청 처리 | 웹 요청을 쉽게 처리할 수 있도록 도와줍니다. |
| 세션 | 사용자 세션을 쉽게 다룰 수 있게 해줍니다. |
| 쿠키 | 쿠키를 쉽게 설정하고 읽을 수 있게 해줍니다. |
| 메시지 플래싱 | 사용자에게 알림 메시지를 보여주는 기능을 제공합니다. |


### Flask 사용법

#### 설치
- 먼저 Flask를 설치합니다. 터미널에서 아래의 명령어를 실행하세요.
```bash
pip install flask
```
- Flask 애플리케이션을 작성합니다. app.py라는 파일을 만들고 아래의 코드를 입력합니다.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

이 코드는 루트 URL('/')에 접속하면 'Hello, World!'라는 텍스트를 반환하는 간단한 웹 서버를 만듭니다. @app.route('/') 부분이 URL 라우팅을 담당하며, def hello_world(): 함수가 해당 URL에 대한 요청을 처리합니다.

- 애플리케이션을 실행합니다. 터미널에서 아래의 명령어를 실행하세요.
```bash
python app.py
```
이후 브라우저에서 http://localhost:5000에 접속하면 'Hello, World!'라는 텍스트를 볼 수 있습니다

## Swagger

Swagger는 API를 설계, 빌드, 문서화, 그리고 사용할 수 있도록 돕는 오픈소스 프레임워크입니다. API에 대한 명세를 정의한 후, 이 명세에 따라 API를 구현하고 테스트하며 문서화할 수 있습니다.

Python에서는 Flask-RESTX와 같은 라이브러리를 이용하여 Swagger를 사용할 수 있습니다. Flask-RESTX는 Flask를 이용한 RESTful API를 구현하면서 동시에 Swagger를 이용한 API 문서를 자동으로 생성하도록 돕는 확장 모듈입니다.

간단한 예제로는 다음과 같은 코드가 있습니다.
- swagger.py
```python
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
```
```bash
pip install flask-restx
python swagger.py
```
```bash
 * Serving Flask app 'swagger'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```
## restAPI
REST API는 웹 서비스에서 데이터를 주고받는 방식 중 하나입니다. REST는 Representational State Transfer의 약자로, 웹의 장점을 최대한 활용할 수 있는 네트워크 기반의 아키텍처 스타일입니다. API는 Application Programming Interface의 약자로, 애플리케이션 간의 상호작용을 가능하게 하는 인터페이스를 의미합니다.

REST API는 HTTP 메서드를 사용해 특정 URL에 접근함으로써 데이터를 주고받습니다. 주로 사용되는 HTTP 메서드는 다음과 같습니다:

| HTTP 메서드 | 설명 |
| :--------: | :--- |
| GET | 데이터를 조회합니다. |
| POST | 데이터를 생성합니다. |
| PUT | 데이터를 수정합니다. |
| DELETE | 데이터를 삭제합니다. |

파이썬에서는 다양한 웹 프레임워크를 사용해 REST API를 구현할 수 있습니다. 그 중에서도 Flask는 간단하면서도 강력한 웹 개발 도구로 많이 사용됩니다.

```python
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

tasks = []

task = api.model('Task', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

class TaskList(Resource):
    @api.doc('list_tasks')
    @api.marshal_list_with(task)
    def get(self):
        '''List all tasks'''
        return tasks

    @api.doc('create_task')
    @api.expect(task)
    @api.marshal_with(task, code=201)
    def post(self):
        '''Create a new task'''
        new_task = api.payload
        new_task['id'] = len(tasks) + 1
        tasks.append(new_task)
        return new_task, 201

class Task(Resource):
    @api.doc('get_task')
    @api.marshal_with(task)
    def get(self, task_id):
        '''Fetch a task given its identifier'''
        for task in tasks:
            if task['id'] == task_id:
                return task
        api.abort(404)

    @api.doc('update_task')
    @api.expect(task)
    @api.marshal_with(task)
    def put(self, task_id):
        '''Update a task given its identifier'''
        for task in tasks:
            if task['id'] == task_id:
                task.update(api.payload)
                return task
        api.abort(404)

    @api.doc('delete_task')
    @api.response(204, 'Task deleted')
    def delete(self, task_id):
        '''Delete a task given its identifier'''
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return '', 204

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

### CORS

CORS(Cross-Origin Resource Sharing)는 웹 페이지가 다른 도메인의 리소스에 접근하려 할 때 보안을 위해 브라우저가 제한을 거는 정책입니다. 이는 웹 사이트의 보안을 위한 중요한 방법으로, 악의적인 스크립트가 사용자의 데이터를 다른 사이트로 전송하는 것을 방지합니다.

예를 들어, http://mywebsite.com의 웹 페이지에서 http://yourwebsite.com의 API를 호출하려고 하면 브라우저는 이를 다른 도메인 간의 요청으로 보고 CORS 정책에 따라 이를 제한합니다.

이 문제를 해결하기 위해 서버 측에서는 'Access-Control-Allow-Origin'이라는 특별한 헤더를 응답에 포함시켜, 특정 도메인 혹은 모든 도메인에서의 요청을 허용하도록 설정할 수 있습니다.

예를 들어, Python의 Flask를 사용하는 서버에서는 Flask-CORS라는 라이브러리를 사용하여 이를 쉽게 설정할 수 있습니다. 먼저 Flask-CORS를 설치하고, Flask 앱에 CORS를 적용하면 됩니다.
- 설치 
```bash
pip install -U flask-cors
```
- 수정
```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 이 부분이 CORS를 적용하는 부분입니다.
```

이렇게 하면 Flask 서버는 모든 도메인에서의 요청을 허용하게 됩니다. 이는 개발 과정에서 테스트를 위해 사용할 수 있지만, 실제 서비스에서는 특정 도메인만 요청을 허용하도록 설정하는 것이 좋습니다. 이를 위해서는 CORS() 함수에 허용할 도메인을 인자로 전달하면 됩니다.

CORS는 웹의 핵심 보안 메커니즘이며, 이를 이해하고 올바르게 설정하는 것은 웹 개발에서 중요한 부분입니다.

---
## 프론트엔드 프로그램

### 프론트엔트 프레임워크
| 프레임워크 | 장점 | 단점 |
|---|---|---|
| React.js | 1. 페이스북이 지원하고 있어서 안정적이며, 큰 커뮤니티와 풍부한 자료가 있습니다. <br> 2. 가상 DOM을 사용하여 빠른 렌더링을 제공합니다. <br> 3. 재사용 가능한 컴포넌트를 사용하여 개발 효율성이 높습니다. | 1. 배우기 어려울 수 있습니다. <br> 2. 프레임워크가 아닌 라이브러리이므로, 라우팅, 상태 관리 등의 기능을 위해 추가 라이브러리를 사용해야 합니다. |
| Angular.js | 1. 구글이 지원하고 있어서 안정적입니다.<br> 2. MVC 패턴을 사용하여 구조적인 개발이 가능합니다.<br> 3. TypeScript를 기반으로 하므로, 타입 체크가 가능하여 안정적인 개발이 가능합니다. | 1. 러닝 커브가 높습니다.<br> 2. 초기 로딩 속도가 느릴 수 있습니다.<br> 3. 무거운 프레임워크입니다. |
| Vue.js | 1. 쉬운 러닝 커브를 가지고 있습니다.<br> 2. 가볍고 빠른 프레임워크입니다.<br> 3. 단일 파일 컴포넌트를 지원합니다.<br> 4. React와 Angular의 장점을 결합한 프레임워크입니다. | 1. 비교적 작은 커뮤니티와 자료를 가지고 있습니다.<br> 2. 대규모 프로젝트에는 적합하지 않을 수 있습니다. |

### Vue.js
Vue.js는 웹 애플리케이션의 사용자 인터페이스를 구축하는데 사용되는 자바스크립트 프레임워크입니다. HTML, CSS, JavaScript를 기반으로 하며, 컴포넌트 기반의 구조를 가지고 있어 재사용이 가능한 코드를 작성할 수 있습니다. 이는 개발자가 효율적으로 코드를 작성하고 관리할 수 있도록 돕습니다.

Vue.js를 배우기 쉽다는 것이 큰 장점 중 하나입니다. 이는 Vue.js의 API가 간결하고 직관적이며, 문서도 잘 정리되어 있기 때문입니다. 그래서 자바스크립트에 익숙하지 않은 초보자도 비교적 쉽게 배울 수 있습니다.

간단한 Vue.js 예제를 살펴보겠습니다.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue.js 예제</title>
    <!-- Vue.js 라이브러리를 불러옵니다 -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <!-- Vue.js 앱의 범위를 정의합니다 -->
    <div id="app">
        <h1>{{ message }}</h1>
    </div>

    <script>
      // Vue.js 앱을 생성하고 초기화합니다
      var app = new Vue({
        el: '#app',
        data: {
          message: '안녕하세요, Vue.js!'
        }
      });
    </script>
</body>
</html>
```

위 예제에서 {{ message }}는 Vue.js의 데이터 바인딩 문법으로, message라는 데이터를 HTML에 바인딩합니다. 즉, message의 값이 변하면 HTML에 자동으로 업데이트됩니다. 이처럼 Vue.js는 웹 애플리케이션의 상태를 관리하는 데 유용하며, 동적인 웹 애플리케이션을 쉽게 구축할 수 있게 돕습니다.

### Vue.js 라이브러리
| 라이브러리 | 설명 | 특징 |
| --- | --- | --- |
| Vuetify | Material Design 스펙을 따르는 Vue.js UI 라이브러리입니다. | 80개 이상의 컴포넌트를 제공하며, 그룹화 된 디스플레이, 그리드 시스템, 폼 유효성 검사 등과 같은 고급 기능을 지원합니다. |
| BootstrapVue | Bootstrap을 Vue.js에 맞게 재구성한 라이브러리입니다. | 반응형 레이아웃과 다양한 UI 컴포넌트를 제공하며, Bootstrap의 모든 CSS, 컴포넌트, 그리드 시스템을 Vue.js에서 사용할 수 있습니다. |
| Element UI | Vue 2.0을 위한 데스크탑 UI 툴킷입니다. | 풍부한 컴포넌트와 인터내셔널라이제이션(i18n) 기능을 제공하며, 데스크탑 중심의 프로젝트에 적합합니다. |

### Bootstrap
https://getbootstrap.com/
- sample
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Sample Page</title>
  <!-- Add Bootstrap CSS to the head of your HTML -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
</head>

<body>
  <div class="container">
    <!-- Navbar -->
    <nav class="navbar navbar-dark bg-dark">
      <a class="navbar-brand" href="#">My Simple Website</a>
    </nav>

    <!-- Main content -->
    <div class="mt-5">
      <h2>Welcome to My Simple Website</h2>
      <p>This is a simple website created using Bootstrap.</p>
      <button class="btn btn-primary">Click Me!</button>
    </div>
  </div>
</body>

</html>
```
### BootstrapVue
https://bootstrap-vue.org/

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BootstrapVue Template</title>
  <!-- Add Bootstrap and BootstrapVue CSS to the head of your HTML -->
  <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css" />
  <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.css" />
</head>

<body>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
      <b-navbar-brand href="#">My Website</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Home</b-nav-item>
          <b-nav-item href="#">About</b-nav-item>
          <b-nav-item href="#">Services</b-nav-item>
          <b-nav-item href="#">Contact</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-container class="mt-5">
      <b-row>
        <b-col cols="12" md="6">
          <h2>Welcome to My Website</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor tellus et aliquet.</p>
          <b-button variant="primary">Learn More</b-button>
        </b-col>
        <b-col cols="12" md="6">
          <img src="https://via.placeholder.com/400" alt="Placeholder Image" class="img-fluid">
        </b-col>
      </b-row>
    </b-container>

    <b-container class="mt-5">
      <h3>Our Services</h3>
      <b-card-group deck>
        <b-card title="Service 1" img-src="https://via.placeholder.com/300" img-alt="Service 1">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor tellus et aliquet.</p>
        </b-card>
        <b-card title="Service 2" img-src="https://via.placeholder.com/300" img-alt="Service 2">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor tellus et aliquet.</p>
        </b-card>
        <b-card title="Service 3" img-src="https://via.placeholder.com/300" img-alt="Service 3">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor tellus et aliquet.</p>
        </b-card>
      </b-card-group>
    </b-container>

    <b-container class="mt-5">
      <h3>Contact Us</h3>
      <b-form>
        <b-form-group label="Name">
          <b-form-input type="text"></b-form-input>
        </b-form-group>
        <b-form-group label="Email">
          <b-form-input type="email"></b-form-input>
        </b-form-group>
        <b-form-group label="Message">
          <b-form-textarea></b-form-textarea>
        </b-form-group>
        <b-button variant="primary">Submit</b-button>
      </b-form>
    </b-container>

    <b-footer align="center" class="mt-5">
      My Website &copy; 2023
    </b-footer>
  </div>

  <!-- Add Vue and BootstrapVue JS just before the closing </body> tag -->
  <script src="https://unpkg.com/vue@latest/dist/vue.min.js"></script>
  <script src="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.js"></script>

  <script>
    new Vue({
      el: '#app',
    })
  </script>
</body>

</html>
```

- sample.html
```html
<!DOCTYPE html>
<html>
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
  <div id="app" class="container">
    <h1 class="mt-5">Task List</h1>
    <div class="mb-3">
      <input class="form-control" v-model="newTask" @keyup.enter="addTask" placeholder="New task">
    </div>
    <ul class="list-group">
      <li class="list-group-item" v-for="(task, index) in tasks" :key="task.id">
        {{ task.task }}
        <button class="btn btn-danger btn-sm float-end" @click="deleteTask(task.id)">Delete</button>
      </li>
    </ul>
  </div>

  <script>
    new Vue({
      el: '#app',
      data: {
        tasks: [],
        newTask: ''
      },
      mounted() {
        axios.get('http://localhost:5000/tasks')
          .then(response => (this.tasks = response.data))
          .catch(error => console.log(error))
      },
      methods: {
        addTask() {
          axios.post('http://localhost:5000/tasks', { task: this.newTask })
            .then(response => {
              this.tasks.push(response.data);
              this.newTask = '';
            })
            .catch(error => console.log(error));
        },
        deleteTask(id) {
          axios.delete(`http://localhost:5000/tasks/${id}`)
            .then(response => {
              this.tasks = this.tasks.filter(task => task.id !== id);
            })
            .catch(error => console.log(error));
        }
      }
    })
  </script>
</body>
</html>
```