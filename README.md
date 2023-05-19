# 삼성 주니어 SW 아카데미 온라인 IT 멘토링 학습

### ■ 그룹 정보 
- 그룹 명 : 소스 (소정의 스터디) 
- 그룹원 (멘토) 김경덕 (멘티) 강소정 
### ■ 멘토링 목표 
- 목표 : 프로그램에 대한 기본적인 이해를 바탕으로 응용할 수 있는 역량을 키운다 
- 진행방법 : 실습을 통해 일단 하고 나중에 이론적 배경을 이해한다 
- 최종산출물 : Java로 구현한 게시판 프로그램 
### ■ 멘토링 운영 계획 
| 주차 |	활동 내용 |
|--|--|
|1주차 |	멘토링 방향 수립 및 교재 선정               |
|2주차 |	[프로그램 설치 및 Hello Java 출력](#1-프로그램-설치-및-Hello-Java-출력)  | 
|3주차 |	Database 기초 (SQL) + Java 기초문법      | 
|4주차 |	웹 프로그램 구조 이해 + Java 클래스 이론      | 
|5주차 |	Swagger 알아보기                       |
|6주차 |	backend 구현                          |
|7주차 |	Github 를 활용한 소스 관리                | 
|8주차 |	Frontend 구현                         |

## 1.프로그램 설치 및 Hello Java 출력
### 프로그램 설치
1. Intelij : https://www.jetbrains.com/ko-kr/idea/
- [X] Community Edition
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/f1c4bb55-e80d-4067-a5eb-0cd4b4774ef9)


2. Java : https://www.azul.com/downloads/?package=jdk#zulu
- [X]  11.0.19+7 Azul Zulu: 11.64.19 Windows x86 64-bit JDK
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/22999e84-237a-4108-8111-4a9824ebec22)

### Spring Boot 초기화
1. Spring boot : https://start.spring.io/
- [X] Gradle - Groovy
- [X] Java
- [X] 2.7.12
- [X] Jar
- [X] 11
- [X] Spring Web
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/79432eba-59eb-4473-b28c-bea11a2b1cf3)

2. 다운로드 받아서 풀기
3. Intelij 로 열기
- src/main/java/com/example/demo/DemoApplication.java
```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

}
```
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/c6f72cf8-34d3-45c4-b626-5550c2bbf43b)

### 실행하기
```
> Task :compileJava
> Task :processResources
> Task :classes

> Task :DemoApplication.main()

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::               (v2.7.12)

2023-05-19 12:38:18.683  INFO 23568 --- [           main] com.example.demo.DemoApplication         : Starting DemoApplication using Java 11.0.19 on DESKTOP-2R6AV3M with PID 23568 (C:\JAKorea\demo (1)\demo\build\classes\java\main started by kdkim in C:\JAKorea\demo (1)\demo)
2023-05-19 12:38:18.687  INFO 23568 --- [           main] com.example.demo.DemoApplication         : No active profile set, falling back to 1 default profile: "default"
2023-05-19 12:38:20.655  INFO 23568 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2023-05-19 12:38:20.671  INFO 23568 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-05-19 12:38:20.672  INFO 23568 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.75]
2023-05-19 12:38:20.835  INFO 23568 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-05-19 12:38:20.836  INFO 23568 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 2066 ms
2023-05-19 12:38:21.319  INFO 23568 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2023-05-19 12:38:21.329  INFO 23568 --- [           main] com.example.demo.DemoApplication         : Started DemoApplication in 3.397 seconds (JVM running for 3.987)
```
### 접속하기 
- [http://localhost:8080/](http://localhost:8080/)
```
Whitelabel Error Page
This application has no explicit mapping for /error, so you are seeing this as a fallback.

Fri May 19 12:41:18 KST 2023
There was an unexpected error (type=Not Found, status=404).
```
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/28c9913a-88cb-4083-8c34-4a321f0a152b)

### index.html 만들기
- src/main/resources/static/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1> Hello Java!!</h1>
</body>
</html>
```
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/cfef66db-68bf-4663-8fef-e9d725ce329e)

### 재실행 하여 다시 접속하기
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/a35c6ef5-e649-4420-9097-0fee2ce4a191)
- [http://localhost:8080/](http://localhost:8080/)
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/71262e49-7913-4494-9a85-2569f679dff2)




