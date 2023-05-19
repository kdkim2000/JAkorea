# JAkorea

## 프로그램 설치
1. Intelij : https://www.jetbrains.com/ko-kr/idea/
- [X] Community Edition
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/f1c4bb55-e80d-4067-a5eb-0cd4b4774ef9)


2. Java : https://www.azul.com/downloads/?package=jdk#zulu
- [X]  11.0.19+7 Azul Zulu: 11.64.19 Windows x86 64-bit JDK
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/22999e84-237a-4108-8111-4a9824ebec22)

## Spring Boot 초기화
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

![image](https://github.com/kdkim2000/JAkorea/assets/26553219/c6f72cf8-34d3-45c4-b626-5550c2bbf43b)
4. 실행하기

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

5. 접속하기 : [http://](http://localhost:8080/)
```
Whitelabel Error Page
This application has no explicit mapping for /error, so you are seeing this as a fallback.

Fri May 19 12:41:18 KST 2023
There was an unexpected error (type=Not Found, status=404).
```
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/28c9913a-88cb-4083-8c34-4a321f0a152b)
