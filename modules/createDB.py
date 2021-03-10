import os
import csv
from Databases import Databases

# CSV 파일에서 데이터를 읽어 DB를 채우는 클래스
class createDB(Databases):
    def __init__(self):
        super().__init__()
        try:
            # person Table 생성
            self.cursor.execute("""CREATE TABLE person (
                    person_id INTEGER PRIMARY KEY,
                    year_of_birth INTEGER NOT NULL,
                    race_source_value VARCHAR(6) NOT NULL,
                    gender_source_value VARCHAR(1) NOT NULL,
                    ethnicity_concept_id VARCHAR(11) NOT NULL
                    );""")

            # visitation Table 생성
            self.cursor.execute("""CREATE TABLE visitation (
                        visit_occurrence_id INTEGER PRIMARY KEY,
                        visit_concept_id INTEGER NOT NULL,
                        person_id INTEGER NOT NULL
                    );""")
            
            # death Table 생성
            self.cursor.execute("""CREATE TABLE death (
                        person_id INTEGER PRIMARY KEY
                    );""")
            self.commit()
        except Exception as e :
            print(" Create Error ! ",e) 

    def fillDeathTable(self):
        with open('./data/death.csv','r') as death: # death.csv 읽고 db에 채우기
            lines = csv.reader(death)
            i=0
            # 컬럼 정보 스킵
            for line in lines:
                i+=1
                if i==1:
                    print(line[0])
                    continue
                try:
                    # index 0만 읽음.
                    # {0:person_id}
                    self.cursor.execute("INSERT INTO death (person_id) VALUES (%s)", (line[0],))
                except Exception as e :
                    print(" Insert Error !", e)
            self.commit()

    def fillPersonTable(self): # person.csv 읽고 db에 채우기
        with open('./data/person.csv','r') as person: 
            lines = csv.reader(person)
            i=0
            # 컬럼 정보 스킵
            for line in lines:
                i+=1
                if i==1:
                    print(line[0], line[2], line[14], line[12], line[16])
                    continue
                # index 0, 2, 14, 12, 16 만 읽음.
                # {0:person_id, 2:year_of_birth, 14:race_source_value, 12:gender_source_value, 16:ethnicity_conpcet_id}
                self.cursor.execute("""INSERT INTO person (person_id,
                                                        year_of_birth,
                                                        race_source_value,
                                                        gender_source_value,
                                                        ethnicity_concept_id) 
                                                        VALUES (%s, %s, %s, %s, %s)""", (line[0], line[2], line[14], line[12], line[16]))
            self.commit()

    def fillVisitationTable(self): # visit_occurrence.csv 읽고 db에 채우기
        with open('./data/visit_occurrence.csv','r') as visit: 
            lines = csv.reader(visit)
            i=0
            for line in lines:
                i+=1
                if i==1: # 컬럼 정보 스킵
                    continue
                print(line[0],line[1],line[2])
                # index 0, 1, 2 만 읽음.
                # {0:visit_occurrence_id, 1:person_id, 2:visit_conpcet_id}
                self.cursor.execute("""INSERT INTO visitation (visit_occurrence_id,
                                                            person_id, 
                                                            visit_concept_id)
                                                            VALUES (%s, %s, %s)""", (line[0],line[1],line[2]))
            self.commit()

if __name__=="__main__":
    db = createDB()
    db.fillDeathTable()
    db.fillPersonTable()
    db.fillVisitationTable()