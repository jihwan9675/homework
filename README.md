# homework
### 디렉토리 구조
homework
 - data
   - concept.csv
   - condition_occurrence.csv
   - death.csv
   - drug_exposure.csv
   - person.csv
   - visit_occurrence.csv
 - modules
   - createDB.py
   - Databases.py
   - getdata.py
 - run.py

### 실행방법
1. postgreSQL에서 tests DB를 생성한다.
2. modules.Databases.py에 init 함수에서 psycopg2.connect의 password를 설정한다.
3. modules.createDB를 실행한다.
4. run.py를 실행한다.

### REST API
총 10개의 get 메서드가 있다.
1. /person
    - 총 환자 수
    - modules.getdata.person_count()로 구현    
2. /person/death
    - 사망자 수
    - modules.getdata.death_count()로 구현
3. /person/ethnicity
    - 민족별 환자 수
    - modules.getdata.person_ethnicity()로 구현
4. /person/gender
    - 성별별 환자 수
    - modules.getdata.person_gender()로 구현
5. /person/race
    - 인종별 환자 수
    - modules.getdata.person_race()로 구현
6. /visitation/age
    - 연령대 별 방문자 수
    - modules.getdata.visit_age()로 구현
7. /visitation/concept
    - 방문자 유형별 방문자 수
    - modules.getdata.visit_concept()로 구현
8. /visitation/ethnicity
    - 민족별 방문자 수
    - modules.getdata.visit_ethnicity()로 구현
9. /visitation/gender
    - 성별별 방문자 수
    - modules.getdata.visit_gender()로 구현
10. /visitation/race
    - 인종별 방문자 수
    - modules.getdata.visit_race()로 구현
