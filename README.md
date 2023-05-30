# 삼성 주니어 SW 아카데미 온라인 IT 멘토링 학습

### 그룹 정보 
- 그룹 명 : 소스 (소정의 스터디) 
- 그룹원 (멘토) 김경덕 (멘티) 강소정 
### 멘토링 목표 
- 목표 : 프로그램에 대한 기본적인 이해를 바탕으로 응용할 수 있는 역량을 키운다 
- 진행방법 : 실습을 통해 일단 하고 나중에 이론적 배경을 이해한다 
- 최종산출물 : Java로 구현한 게시판 프로그램 
### 멘토링 운영 계획
| 주차 |	활동 내용 |
|--|--|
|1주차 |	멘토링 방향 수립 및 교재 선정               |
|2주차 |	[프로그램 설치 및 Hello Java 출력](#프로그램-설치-및-Hello-Java-출력)  | 
|3주차 |	[Database 기초 (SQL)](#Database-기초-SQL) | 
|4주차 |	[Github로 소스 관리](#Github로-소스-관리)   | 
|5주차 |	[Backend 구현/실행(1)](#Backend-구현) |
|6주차 |	[Backend 구현/실행(2)](#swagger-알아보기)  |
|7주차 |	[게시판 만들기(1)](#게시판-구현) |
|8주차 |	[게시판 만들기(2)](#Thymeleaf-를-이용하여-View-와-Controller-연결)  |

## 프로그램 설치 및 Hello Java 출력
### 프로그램 설치
#### 1. Intelij
- https://www.jetbrains.com/ko-kr/idea/
- [X] Community Edition
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/f1c4bb55-e80d-4067-a5eb-0cd4b4774ef9)

#### 2. Java
- https://www.azul.com/downloads/?package=jdk#zulu
- [X] 11.0.19+7 Azul Zulu: 11.64.19 Windows x86 64-bit JDK
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/22999e84-237a-4108-8111-4a9824ebec22)

#### 3. Git
- https://git-scm.com/download/win
- [X] 2.40.1 64-bit version of Git for Windows
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/0fc9e269-e05f-4eba-a617-ca6ce28b2bfa)

#### 4. Postman
- https://www.postman.com/downloads/
- [X] Windows 64-bit
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/8f65a692-04ad-4fdb-a3db-0647ab2227ea)

### Spring Boot 초기화
1. Spring boot : https://start.spring.io/
- [X] Gradle - Groovy
- [X] Java
- [X] 2.7.12
- [X] Project Metadata
- Group : com.samsung.sds
- Artifact : study
- Name : JAKorea
- Description : JAKorea SpringBoot study
- Package name : com.samsung.sds.study
- [X] Jar
- [X] 11
- [X] Spring Web
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/29f8fde2-4aaa-472a-b376-6d4ba1a09823)
- [https://start.spring.io/#!type=gradle...](https://start.spring.io/#!type=gradle-project&language=java&platformVersion=2.7.12&packaging=jar&jvmVersion=11&groupId=com.samsung.sds&artifactId=study&name=JAKorea&description=JAKorea%20SpringBoot%20study&packageName=com.samsung.sds.study&dependencies=web)


2. 다운로드 받아서 풀기
3. Intelij 로 열기
- src/main/java/com/samsung/sds/study/StudyApplication.java
```java
package com.samsung.sds.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class StudyApplication {

	public static void main(String[] args) {
		SpringApplication.run(StudyApplication.class, args);
	}

}
```

### 실행하기
```
오후 9:17:26: Executing ':StudyApplication.main()'...

> Task :compileJava
> Task :processResources
> Task :classes

> Task :StudyApplication.main()

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::               (v2.7.12)

2023-05-19 21:17:29.927  INFO 31072 --- [           main] com.samsung.sds.study.StudyApplication   : Starting StudyApplication using Java 11.0.19 on DESKTOP-2R6AV3M with PID 31072 (C:\JAKorea\study\build\classes\java\main started by kdkim in C:\JAKorea\study)
2023-05-19 21:17:29.934  INFO 31072 --- [           main] com.samsung.sds.study.StudyApplication   : No active profile set, falling back to 1 default profile: "default"
2023-05-19 21:17:31.719  INFO 31072 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2023-05-19 21:17:31.732  INFO 31072 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-05-19 21:17:31.732  INFO 31072 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.75]
2023-05-19 21:17:31.889  INFO 31072 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-05-19 21:17:31.889  INFO 31072 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1874 ms
2023-05-19 21:17:32.369  INFO 31072 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2023-05-19 21:17:32.380  INFO 31072 --- [           main] com.samsung.sds.study.StudyApplication   : Started StudyApplication in 3.005 seconds (JVM running for 3.561)
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
- [http://localhost:8080/](http://localhost:8080/)
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/71262e49-7913-4494-9a85-2569f679dff2)

## Database 기초 (SQL)
### DBMS 종류
- 출처 : https://velog.io/@98kimjh/Database-NoSQL-Concept
- ![image](https://velog.velcdn.com/images%2F98kimjh%2Fpost%2Fd8f6888a-ddc4-43be-9815-960418436691%2Fimage.png)

### RDB 종류
- 출처 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=goottceo&logNo=221404636153
- ![image](https://mblogthumb-phinf.pstatic.net/MjAxODExMjNfMTU1/MDAxNTQyOTUzMzYzMzI5.Yran0cXpkY6RxKFej-5bXdapA4ccRIrJMYADV8y3WCsg.Stcnr_lTiRqEKvV0-PedDFjjpQNPZhtTuIp7rdN2FDcg.JPEG.goottceo/DB%EC%A2%85%EB%A5%98.JPG?type=w800)

### Database 설치하기
- build.gradle
- [x] **pring Data JPA** : Persist data in SQL stores with Java Persistence API using Spring Data and Hibernate.
- [x] **H2 Database** : Provides a fast in-memory database that supports JDBC API and R2DBC access, with a small (2mb) footprint. Supports embedded and server modes as well as a browser based console application.
- [x] **Lombok** : Java annotation library which helps to reduce boilerplate code.
```groovy
plugins {
	id 'java'
	id 'org.springframework.boot' version '2.7.12'
	id 'io.spring.dependency-management' version '1.0.15.RELEASE'
}

group = 'com.samsung.sds'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
	mavenCentral()
}

dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-web'
	implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
	runtimeOnly 'com.h2database:h2'
	compileOnly 'org.projectlombok:lombok'
	annotationProcessor 'org.projectlombok:lombok'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

tasks.named('test') {
	useJUnitPlatform()
}


```
- /src/main/resources/application.properties
```groovy
#h2 console
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

#h2 db
spring.datasource.url=jdbc:h2:~/test;
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.H2Dialect

#hibernate
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.hibernate.ddl-auto=create
```
### Lombok Plungins 설치
- File > settings (Ctrl + Alt + S)
- plugins > Marketplace 에서 "lombok" 검색
- "Lombok Builder Helper" Install 
- 설치후 다시실행하기
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/89c70a7e-0252-4b24-87d0-2d5c00e12a3b)

### Entity 설계
- package 만들기 : com.samsung.sds.study.member
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/7513cfa4-2329-4d99-bc45-97e8cb4bd3bb)
- Class 만들기 : Member
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/11d3cd5a-cecf-4c61-b468-3cad40ccf60d)

```java
package com.samsung.sds.study.member;

import javax.persistence.*;

@Entity
@Setter
@Getter
public class Member {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Long id;
    @Column
    private String name;
    @Column
    private String email;
}
```
### SpringBoot 다시 실행하기
```bash
오후 9:50:06: Executing 'bootRun'...

> Task :compileJava UP-TO-DATE
> Task :processResources UP-TO-DATE
> Task :classes UP-TO-DATE
> Task :bootRunMainClassName UP-TO-DATE

> Task :bootRun

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::               (v2.7.12)

2023-05-19 21:50:08.486  INFO 39324 --- [           main] com.samsung.sds.study.StudyApplication   : Starting StudyApplication using Java 11.0.19 on DESKTOP-2R6AV3M with PID 39324 (C:\JAKorea\study\build\classes\java\main started by kdkim in C:\JAKorea\study)
2023-05-19 21:50:08.489  INFO 39324 --- [           main] com.samsung.sds.study.StudyApplication   : No active profile set, falling back to 1 default profile: "default"
2023-05-19 21:50:08.802  INFO 39324 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2023-05-19 21:50:08.813  INFO 39324 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 3 ms. Found 0 JPA repository interfaces.
2023-05-19 21:50:09.087  INFO 39324 --- [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2023-05-19 21:50:09.130  INFO 39324 --- [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 5.6.15.Final
2023-05-19 21:50:09.240  INFO 39324 --- [           main] o.hibernate.annotations.common.Version   : HCANN000001: Hibernate Commons Annotations {5.1.2.Final}
2023-05-19 21:50:09.954  INFO 39324 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2023-05-19 21:50:10.092  INFO 39324 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2023-05-19 21:50:10.103  INFO 39324 --- [           main] org.hibernate.dialect.Dialect            : HHH000400: Using dialect: org.hibernate.dialect.H2Dialect
Hibernate: 
    
    drop table if exists member CASCADE 
Hibernate: 
    
    create table member (
       id bigint generated by default as identity,
        email varchar(255),
        name varchar(255),
        primary key (id)
    )
2023-05-19 21:50:10.468  INFO 39324 --- [           main] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000490: Using JtaPlatform implementation: [org.hibernate.engine.transaction.jta.platform.internal.NoJtaPlatform]
2023-05-19 21:50:10.476  INFO 39324 --- [           main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2023-05-19 21:50:10.528  INFO 39324 --- [           main] com.samsung.sds.study.StudyApplication   : Started StudyApplication in 2.378 seconds (JVM running for 2.747)
2023-05-19 21:50:10.543  INFO 39324 --- [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2023-05-19 21:50:10.547  INFO 39324 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2023-05-19 21:50:10.551  INFO 39324 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.

BUILD SUCCESSFUL in 4s
4 actionable tasks: 1 executed, 3 up-to-date
오후 9:50:11: Execution finished 'bootRun'.
```
### H2 DataBase 접속하기
- http://localhost:8080/h2-console
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/106c2228-79ae-4217-9302-67f4d7388f69)
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/e3b5c9dd-c098-49c6-a6d1-0f274278489a)
- SQL 기초
```SQL
INSERT INTO MEMBER (NAME, EMAIL) VALUES ('홍길동','gildong@gmail.com');
SELECT * FROM MEMBER WHERE NAME='홍길동';

UPDATE MEMBER SET NAME = '허준' WHERE NAME='홍길동';
SELECT * FROM MEMBER;

DELETE MEMBER WHERE NAME='허준';
SELECT * FROM MEMBER;
```
### SpringBoot 시작시 기초 데이터 입력
- /src/main/resources/import.sql
```SQL
INSERT INTO MEMBER (NAME, EMAIL) VALUES ('홍길동','gildong@gmail.com');
INSERT INTO MEMBER (NAME, EMAIL) VALUES ('허준','jun@gmail.com');
```
- SpringBoot 재기동
```
...
Hibernate: 
    INSERT INTO MEMBER (NAME, EMAIL) VALUES ('?��길동','gildong@gmail.com')
Hibernate: 
    INSERT INTO MEMBER (NAME, EMAIL) VALUES ('?���?','jun@gmail.com')
...
```
#### ❓실행시 한글 꺠짐 해결
- Help > Edit Custom VM Options... 
- -Dfile.encoding=UTF-8 추가 후 저장, InteliJ 재기동 
```
-Xmx2007m
-Dfile.encoding=UTF-8
```
## Github로 소스 관리

### Github Repository 만들기
- https://github.com/new
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/14b65f09-27ba-485a-8c2f-8998f57d7a10)

### Git 설치
- [Git 다운로드](https://git-scm.com/downloads)
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/9623166e-1325-4f4f-9175-b9c687e53b45)

### git 환경설정
- Gitbash 실행 (Shift + F10)
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/df05815d-7198-427a-86d3-860f74bce757)
```bash
git config --global user.name "사용자 이름"
git config --global user.email "사용자 이메일"
git config --global credential.helper store   
```

### .gitignore 설정
```git
HELP.md
.gradle
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache
bin/
!**/src/main/**/bin/
!**/src/test/**/bin/

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr
out/
!**/src/main/**/out/
!**/src/test/**/out/

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

### VS Code ###
.vscode/

```
### 로컬 소스와 Github 소스 동기화
- 로컬 PC의 소스 폴더
- Gitbash 실행 (Shift + F10)
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin  <url>
git push -u origin main
```
### 로컬 소스를 Github 에 올리기
```bash
git status
git add .
git commit -m <msg>
#add + commit
git commit -am <msg>
#push
git push
```

## Backend 구현
### JPA 를 활용한 CRUD
- src/main/java/com/samsung/sds/study/member/MemberRepository.java
```java
package com.samsung.sds.study.member;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member, Long> {
}
```
### REST API Design Guide
- URI는 정보의 자원를 표현해야 한다.
- resource는 동사보다는 명사를, 대문자보다는 소문자를 사용한다.
- 자원에 대한 행위는 HTTP Method (GET, POST, PUT, DELETE)로 표현한다.
- URI에 HTTP Method가 들어가면 안된다.
- URI에 행위에 대한 동사 표현이 들어가면 안된다.
- 경로 부분 중 변하는 부분은 유일한 값으로 대체한다.
- 슬래시 구분자(/ )는 계층 관계를 나타내는데 사용한다.
- URI 마지막 문자로 슬래시(/ )를 포함하지 않는다.
- URI에 포함되는 모든 글자는 리소스의 유일한 식별자로 사용되어야 하며 URI가 다르다는 것은 리소스가 다르다는 것이고, 역으로 리소스가 다르면 URI도 달라져야 한다.
- 하이픈(- )은 URI 가독성을 높이는데 사용할 수 있다.
- 밑줄( _ )은 URI에 사용하지 않는다.
- URI 경로에는 소문자가 적합하다.
- URI 경로에 대문자 사용은 피하도록 한다.
- 파일 확장자는 URI에 포함하지 않는다.

### REST API HTTP Methods

| Method | 설명 |
| --- |--- |
| GET | 읽어 오기 |
| POST | 입력 하기 |
| PUT | 변경 하기 |
| DELETE | 삭제하기 |

### Controller
- src/main/java/com/samsung/sds/study/member/MemberRestController.java
```java
package com.samsung.sds.study.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/member")
public class MemberRestController {
    @Autowired
    MemberRepository memberRepository;

    @GetMapping
    public List<Member>  getMembers(){
        return memberRepository.findAll();
    }
    @GetMapping("/{id}")
    public Optional<Member> getMember(@PathVariable Long  id){
        return memberRepository.findById(id);
    }
    @DeleteMapping("/{id}")
    public void deleteMember(@PathVariable Long  id){
        memberRepository.deleteById(id);
    }

    @DeleteMapping
    public void deleteMemberAll(){
        memberRepository.deleteAll();
    }

    @PutMapping("/{id}/name")
    public Member updateMemberName(@PathVariable Long  id,
                                   @RequestParam String name){
        Member member = memberRepository.findById(id).get();
        member.setName(name);
        return memberRepository.save(member);
    }

    @PutMapping("/{id}/email")
    public Member updateMemberEmail(@PathVariable Long  id,
                                    @RequestParam String email){
        Member member = memberRepository.findById(id).get();
        member.setEmail(email);
        return memberRepository.save(member);
    }
    @PutMapping("/{id}")
    public Member updateMember(@PathVariable Long  id,
                               @RequestParam String name,
                               @RequestParam String email){
        Member member = memberRepository.findById(id).get();
        member.setEmail(email);
        member.setName(name);
        return memberRepository.save(member);
    }
    @PostMapping("/member")
    public Member setMember(@RequestParam String name,
                            @RequestParam String email){
        Member member = new Member();
        member.setEmail(email);
        member.setName(name);
        return memberRepository.save(member);
    }
    @PostMapping
    public List <Member>  setMembers(@RequestBody List<Map<String,Object>>members){
        List <Member> newMembers = new ArrayList<>();
        for(Map map:members){
            Member member = new Member();
            member.setEmail(map.get("email").toString());
            member.setName(map.get("name").toString());
            newMembers.add(memberRepository.save(member));
        }
        return newMembers;
    }
}

```

## RestApi 시행하기

### Postman 실행
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/5a6613e1-04a4-4440-b531-54c22b70c775)

### Swagger 추가
- build.gradle
```groovy
...
	//swagger
	implementation 'io.springfox:springfox-boot-starter:3.0.0'
	implementation 'io.springfox:springfox-swagger-ui:3.0.0'
...
```
- src/main/java/com/samsung/sds/study/config/SwaggerConfig.java
```java
package com.samsung.sds.study.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

@Configuration
@EnableWebMvc
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.OAS_30)
                .useDefaultResponseMessages(false)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.samsung.sds.study"))
                .paths(PathSelectors.any())
                .build()
                .apiInfo(apiInfo());
    }
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("소스 Swagger")
                .description("SS swagger config")
                .version("1.0")
                .build();
    }
}
```
### Swagger 접속하기
- http://localhost:8080/swagger-ui/index.html#
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/3e4648b2-a964-4280-a6f6-bcaa72689aad)


## 게시판 구현
### 게시판 구현을 위한 아키텍처
![image](https://github.com/kdkim2000/JAkorea/assets/26553219/43b47590-d88c-498d-954f-6b94c26ef73d)

### Thymeleaf 추가
- build.gradle
```groovy
...
	implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
	developmentOnly 'org.springframework.boot:spring-boot-devtools'
...
```
- src/main/resources/application.properties
```bash
spring.thymeleaf.cache=false
spring.thymeleaf.enabled=true
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html
```
### html page 만들기 
- src/main/resources/templates/index.html
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<H2 th:text="'안녕하세요? '+ ${name} +'님 반갑습니다.'">안녕하세요? 홍길동 님 반갑습니다.</H2>
</body>
</html>
```
### html page 주소 연결하기
- src/main/java/com/samsung/sds/study/controller/HomeController.java
```java
package com.samsung.sds.study.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping
    public String init(Model model) {
        model.addAttribute("name","허준");
        return "index";
    }
}
```

### Board Entity 추가
- src/main/java/com/samsung/sds/study/board/Board.java
```java
package com.samsung.sds.study.board;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
public class Board {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Long id;
    @Column
    private String title;
    @Column(length = 2000)
    private String contents;
}
```

### 서버 시작시 초기값 입력
- src/main/resources/import.sql
```sql
...
INSERT INTO BOARD (TITLE, CONTENTS ) VALUES ('소스의 오늘 작업','오늘은 SpringBoot를 학습하였습니다.');
INSERT INTO BOARD (TITLE, CONTENTS ) VALUES ('소스의 내일 작업','내일도 SpringBoot를 학습하겠습니다..');
```

### Board Repository 추가
- src/main/java/com/samsung/sds/study/board/BoardRepository.java
```java
package com.samsung.sds.study.board;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BoardRepository extends JpaRepository<Board, Long> {
}
```

### Board 를 위한 화면 추가
- 화면 Design 을 위해 BootStrap 활용
- https://getbootstrap.com/
- src/main/resources/templates/boardList.html
```html
<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>Bootstrap Example</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body class="p-3 m-0 border-0 bd-example">
<H2>Board</H2>
<p class="fw-medium">총 건수 : <span>1</span></p>
<table class="table">
    <thead class="table-dark">
    <tr>
        <th scope="col">#</th>
        <th scope="col">title</th>
        <th scope="col">contents</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th>1</th>
        <td><a href="form.html">title</a></td>
        <td>contents</td>
    </tr>
    </tbody>
</table>
<div class="text-end">
    <a type="button" class="btn btn-outline-primary" href="form.html">쓰기</a>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>
```

- src/main/resources/templates/boardForm.html
```html
<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>Bootstrap Example</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body class="p-3 m-0 border-0 bd-example">
<H2>Board</H2>
<form>
    <input type="hidden">
    <div class="mb-3">
        <input type="text" class="form-control" id="inputTitle" placeholder="Title">
    </div>
    <div class="mb-3">
        <textarea class="form-control" id="intpuContent" rows="10" placeholder="Contents"></textarea>
    </div>
    <div class="text-end">
        <a type="button" class="btn btn-outline-primary" href="list.html">취소</a>
        <button type="submit" class="btn btn-outline-primary">확인</button>
    </div>
</form>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>
```

### Board Controller 추가
- src/main/java/com/samsung/sds/study/board/BoardController.java
```java
package com.samsung.sds.study.board;

import com.samsung.sds.study.member.Member;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@Controller
@RequestMapping("/board")
public class BoardController {
    @Autowired
    BoardRepository boardRepository;

    @GetMapping
    public String index() {
        return "redirect:/board/list";
    }
    @GetMapping("/list")
    public String getBoards(Model model) {
        List<Board> boards = boardRepository.findAll();
        model.addAttribute("boards", boards);
        return "boardList.html";
    }
    @GetMapping("/form")
    public String getBoard(Model model,
                           @RequestParam(required = false) Long id) {
        Board board;
        if(id == null){
            board = new Board();
        }else{
            board = boardRepository.findById(id).orElse(null);
        }
        model.addAttribute("board", board);
        return "boardForm.html";
    }
    @PostMapping("/form")
    public String boardSubmit(@ModelAttribute Board board, Model model) {
        boardRepository.save(board);
        return "redirect:/board/list";
    }
}
```

### Thymeleaf 를 이용하여 View 와 Controller 연결
- Thymeleaf 알아보기
- https://www.thymeleaf.org/documentation.html

###Thymeleaf 문법
| 표현 | 항목 | 예제 |
| --- |--- |--- |
| ${...} | 변수 | th:text="${board.id}" |
| th:each | 반복처리 | th:each="board: ${boards}" |
| @{...} | 링크URL | th:href="@{/board/form}" |
| @{...} | 링크URL with param | th:href="@{/board/form(id=${board.id})}" |
| @{...} | form summit | action="#" th:action="@{/board/form}" th:object="${board}" method="post" |
| *{...} | field 연동 | th:field="\*{title}\" |

- src/main/resources/templates/boardList.html
```html
<!DOCTYPE html>

<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>Bootstrap Example</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body class="p-3 m-0 border-0 bd-example">
<H2>Board</H2>
<p class="fw-medium">총 건수 : <span th:text="${#lists.size(boards)}">1</span></p>
<table class="table">
    <thead class="table-dark">
    <tr>
        <th scope="col">#</th>
        <th scope="col">title</th>
        <th scope="col">contents</th>
    </tr>
    </thead>
    <tbody>
    <tr th:each="board: ${boards}">
        <th th:text="${board.id}">1</th>
        <td><a th:text="${board.title}" th:href="@{/board/form(id=${board.id})}">title</a></td>
        <td th:text="${board.contents}">contents</td>
    </tr>
    </tbody>
</table>
<div class="text-end">
<a type="button" class="btn btn-outline-primary" th:href="@{/board/form}">쓰기</a>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>
```
- src/main/resources/templates/boardForm.html
```html
<!DOCTYPE html>

<html xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
  <title>Bootstrap Example</title>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body class="p-3 m-0 border-0 bd-example">
<H2>Board</H2>
<form action="#" th:action="@{/board/form}" th:object="${board}" method="post">
  <input type="hidden" th:field="*{id}">
  <div class="mb-3">
    <input type="text" class="form-control" id="inputTitle" placeholder="Title" th:field="*{title}">
  </div>
  <div class="mb-3">
    <textarea class="form-control" id="intpuContent" rows="10" placeholder="Contents" th:field="*{contents}"></textarea>
  </div>
  <div class="text-end">
    <a type="button" class="btn btn-outline-primary" th:href="@{/board/list}">취소</a>
    <button type="submit" class="btn btn-outline-primary">확인</button>
  </div>
</form>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>
```

### 최종기능 테스트

- 게시판 조회 : http://localhost:8080/board/list
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/76a95391-5a99-4eca-9990-126b7ce9a578)
- 새 게시글 쓰기 : "쓰기" 버튼 클릭
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/90d7c4a9-f5b4-412e-b40c-d06843effe8b)
- 기존 게시글 수정 : "title" 링크 클릭
- ![image](https://github.com/kdkim2000/JAkorea/assets/26553219/41d0ed2a-5d47-4019-860a-acabf0c9403d)

### 이후 해야 할 일
- [ ] 로그인 관리
- [ ] 권한 관리
- [ ] 예외 처리
- [ ] Page 처리
- [ ] backend 와 frontend 분리 (React, Vuejs, Angular)
- [ ] 어플리케이션 빌드 및 서버 배포하기
- [ ] CI/CD 구현하기
- [ ] 모니터링 툴 적용
- [ ] Dockerizing
- [ ] k8s 구현하기

## SW 개발/운영 
- [X] SW 기획자 : 어떤 SW를 만들 것인가?
- [X] SW 구조 설계자 : 어떤 SW Architecture 를 사용할 것인가?
- [X] DBAdmin : 데이터를 어떻게 설계하고 관리할 것인가?
- [X] SW backend 개발자 : 로직을 어떻게 구현할 것인가?
- [X] SW frontend 개발자  : 어떻게 화면을 구현할 것인가?
- [X] Web Designer : 어떤 UX를 활용하여 설계할 것인가?
- [X] SW 운영자 : 운영을 위해 어떤 프로세스로 관리할 것인가?
- [X] 클라우드 운영자 : 클라우드 환경에서 SW를 어떻게 운용할 것인가?
- [X] 알고리즘 개발자 : 어떤 알고리즘으로 로직을 구현할 것인가?
- [X] 빅데이터 전문가 : 어떤 데이터에 의미를 부여하고 분석할 것인가?

