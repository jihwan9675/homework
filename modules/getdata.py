from modules.Databases import Databases
from datetime import datetime

class getdata(Databases): # 요구사항 별 쿼리문
    def person_count(self): # 환자 수
        dic=dict()
        dic["person_count"]=self.execute("""select count(*) from person;""")[0][0]
        
        return dic

    def person_ethnicity(self): # 민족 별 환자 수
        dic = dict()
        dic["hispanic"]=self.execute("""select count(*) from person where person.ethnicity_concept_id='hispanic';""")[0][0]
        dic["nonhispanic"]=self.execute("""select count(*) from person where person.ethnicity_concept_id='nonhispanic';""")[0][0]
        
        return dic

    def person_race(self): # 인종 별 환자 수
        dic = dict()
        items = ["other","native","black","white","asian"]
        for item in items:
            dic[item]=self.execute("""select count(*) from person where person.race_source_value='{item}';""".format(item=item))[0][0]

        return dic

    def person_gender(self): # 성별 별 환자 수
        dic = dict()
        dic["male"]=self.execute("""select count(*) from person where person.gender_source_value='M';""")[0][0]
        dic["female"]=self.execute("""select count(*) from person where person.gender_source_value='F';""")[0][0]

        return dic

    def visit_concept(self): # 방문 유형별 방문자 수
        dic = dict()
        dic["입원"]=self.execute("""select count(*) from visitation where visit_concept_id=9201;""")[0][0]
        dic["외래"]=self.execute("""select count(*) from visitation where visit_concept_id=9202;""")[0][0]
        dic["응급"]=self.execute("""select count(*) from visitation where visit_concept_id=9203;""")[0][0]

        return dic

    def visit_ethnicity(self): # 민족 별 방문자 수
        dic = dict()
        dic["visit_nonhispanic"] = self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='nonhispanic';""")[0][0]
        dic["visit_hispanic"] = self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='hispanic';""")[0][0]
    
        return dic

    def visit_gender(self): # 성별 별 방문자 수
        dic = dict()
        dic["male"]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='M';""")[0][0]
        dic["female"]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='F';""")[0][0]
        return dic

    def visit_race(self): # 인종 별 방문자 수
        dic=dict()
        items = ["other","native","black","white","asian"]
        for item in items:
            dic[item]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.race_source_value='{item}';""".format(item=item))[0][0]
            
        return dic

    def visit_age(self): # 0대~90대까지 방문자 수
        dic=dict()
        for i in range(10):
            dic[str(i*10)+"대"]=self.execute("""select count(*) from person where {year} - year_of_birth>{start} and {year} - year_of_birth <{end};""".format(year=datetime.today().year, start = i*10,end =i*10+10))[0][0]
        
        return dic

    def death_count(self): # 사망자 수
        dic=dict()
        dic["death"]=self.execute("""select count(*) from death;""")[0][0]
        
        return dic
        
if __name__=="__main__":
    s= getdata()
    print(s.visit_age())
