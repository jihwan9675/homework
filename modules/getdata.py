from Databases import Databases
from datetime import datetime

class getdata(Databases):
    def person_count(self):
        dic=dict()
        dic["person_count"]=self.execute("""select count(*) from person;""")[0][0]
        
        return dic
        
    def person_ethinicity(self):
        dic = dict()
        dic["hispanic"]=self.execute("""select count(*) from person where person.ethnicity_concept_id='hispanic';""")[0][0]
        dic["nonhispanic"]=self.execute("""select count(*) from person where person.ethnicity_concept_id='nonhispanic';""")[0][0]
        
        return dic

    def person_race(self):
        dic = dict()
        items = ["other","native","black","white","asian"]
        for item in items:
            dic[item]=self.execute("""select count(*) from person where person.race_source_value='{item}';""".format(item=item))[0][0]

        return dic

    def person_gender(self):
        dic = dict()
        dic["male"]=self.execute("""select count(*) from person where person.gender_source_value='M';""")[0][0]
        dic["female"]=self.execute("""select count(*) from person where person.gender_source_value='F';""")[0][0]

        return ls

    def visit_concept(self):
        dic = dict()
        dic["입원"]=self.execute("""select count(*) from visitation where visit_concept_id=9201;""")[0][0]
        dic["외래"]=self.execute("""select count(*) from visitation where visit_concept_id=9202;""")[0][0]
        dic["응급"]=self.execute("""select count(*) from visitation where visit_concept_id=9203;""")[0][0]

        return dic

    def visit_ethnicity(self):
        dic = dict()
        dic["visit_nonhispanic"] = self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='nonhispanic';""")[0][0]
        dic["visit_hispanic"] = self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='hispanic';""")[0][0]
    
        return dic

    def visit_gender(self):
        dic = dict()
        dic["male"]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='M';""")[0][0]
        dic["female"]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='F';""")[0][0]
        return dic

    def visit_race(self):
        dic=dict()
        items = ["other","native","black","white","asian"]
        for item in items:
            dic[item]=self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.race_source_value='{item}';""".format(item=item))[0][0]
            
        return dic

    def visit_age(self):
        dic=dict()
        for i in range(10):
            dic[str(i*10)+"대"]=self.execute("""select count(*) from person where {year} - year_of_birth>{start} and {year} - year_of_birth <{end};""".format(year=datetime.today().year, start = i*10,end =i*10+10))[0][0]
        return dic

    def death_count(self):
        dic=dict()
        dic[death]=self.execute("""select count(*) from death;""")[0][0]
        return dic
        
if __name__=="__main__":
    s= getdata()
    print(s.visit_age())
    #k = s.getpersongender()
