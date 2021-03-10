# 기술 과제 - 신지환

**목차**

---

## 시작하기 전

### 요구사항

---

1. 환자
    - 전체 환자 수
    - 성별 환자 수
    - 인종별 환자 수
    - 민족별 환자 수
    - 사망 환자수
2. 방문
    - 방문 유형(입원/외래/응급)별 방문 수
    - 성별 방문 수
    - 인종별 환자 수
    - 민족별 환자 수
    - 방문 시 연령대(10세 단위)별 환자 수

### 개발환경

---

- IDE : VSCode
- Python3.6
- Flask==1.1.2
- PostgreSQL==12.6
- Werkzeug==0.16.0
- psycopg2==2.8.6
### PostGreSQL(ver. 12.6) 설치

---

[Windows installers](https://www.postgresql.org/download/windows/)

먼저 위 링크에가서 자기에게 맞는 버전을 설치한다. 본인은 12.6 버전을 설치하였다. 

### Python과 연동

---

1. 모듈 설치

    ```python
    pip3 install psycopg2
    ```

![Untitled](https://user-images.githubusercontent.com/69146451/110596792-140e0100-81c3-11eb-8735-4c976e35fd12.png)

## 설계

### DB 설계

---

먼저 6개의 CSV 파일 중 필요 없는 컬럼을 삭제할 것이다. 요구 명세에 명시된 것이 아닌 불필요한 데이터를 줄여 DB의 성능을 올릴 것이다.

**person, visit_occurrence, death** 이 3가지 csv 파일만 사용할 것이고 사용할 컬럼은 다음과 같다.

1. person
    - person_id (PK, 전체 환자 수)
    - year_of_birth (연령대 확인)
    - race_source_value (인종)
    - gender_source_value (성별)
    - ethnicity_concept_id (민족)
2. visit
    - visit_occurrence_id (PK, 중복 체크)
    - visit_concept_id (방문 유형)
    - person_id (FK, 환자 조회)
3. death
    - person_id (PK, 사망자)

![Untitled 1](https://user-images.githubusercontent.com/69146451/110596795-153f2e00-81c3-11eb-8982-63e295eafba7.png)

### REST API 설계

---

- person
    1. 전체 환자 수 : /person/all
    2. 성별 환자 수 : /person/gender
        - /person/gender/male
        - /person/gender/female
    3. 인종별 환자 수 : /person/race
    4. 민족별 환자 수 : /person/ethnicity
    5. 사망 환자 수 : /person/death

- visitation
    1. 방문 유형(입원/외래/응급)별 방문 수 : /visitation/concept
    2. 성별 방문수 : /visitation/gender
    3. 인종별 방문 환자 수 : /visitation/race
    4. 민족별 방문 환자 수 : /visitation/ethnicity
    5. 방문 시 연령별 : /visitation/age 

## 코딩

### 오류

- Swagger를 사용할 것인데, Werkzeug 쪽에서 오류가 났다. 알아보니 다운그레이드 해야한다해서 Werkzeug==0.16.0으로 다운그레이드 하여 해결하였다.
