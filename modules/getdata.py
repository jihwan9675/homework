from Databases import Databases
from datetime import datetime

class getdata(Databases):
    def person_count(self):
        ls=[]
        ls.append(self.execute("""select count(*) from person;""")[0][0])
        return ls
    def person_ethinicity(self):
        ls=[]
        ls.append(self.execute("""select count(*) from person where person.ethnicity_concept_id='hispanic';""")[0][0])
        ls.append(self.execute("""select count(*) from person where person.ethnicity_concept_id='nonhispanic';""")[0][0])
        return ls

    def person_race(self):
        ls=[]
        items = ["other","native","black","white","asian"]
        for item in items:
            ls.append(self.execute("""select count(*) from person where person.race_source_value='{item}';""".format(item=item))[0][0])
        return ls

    def person_gender(self):
        ls=[]
        ls.append(self.execute("""select count(*) from person where person.gender_source_value='M';""")[0][0])
        ls.append(self.execute("""select count(*) from person where person.gender_source_value='F';""")[0][0])
        return ls

    def visit_concept(self):
        ls = []
        ls.append(self.execute("""select count(*) from visitation where visit_concept_id=9201;""")[0][0])
        ls.append(self.execute("""select count(*) from visitation where visit_concept_id=9202;""")[0][0])
        ls.append(self.execute("""select count(*) from visitation where visit_concept_id=9203;""")[0][0])
        return ls

    def visit_ethnicity(self):
        ls = []
        ls.append(self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='nonhispanic';""")[0][0])
        ls.append(self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.ethnicity_concept_id='hispanic';""")[0][0])
        return ls

    def visit_gender(self):
        ls = []
        ls.append(self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='M';""")[0][0])
        ls.append(self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.gender_source_value='F';""")[0][0])
        return ls

    def visit_race(self):
        ls=[]
        items = ["other","native","black","white","asian"]
        for item in items:
            ls.append(self.execute("""select count(*) from visitation, person where visitation.person_id = person.person_id and person.race_source_value='{item}';""".format(item=item))[0][0])
        return ls

    def visit_age(self):
        ls=[]
        for i in range(10):
            ls.append(self.execute("""select count(*) from person where {year} - year_of_birth>{start} and {year} - year_of_birth <{end};""".format(year=datetime.today().year, start = i*10,end =i*10+10))[0][0])
        return ls
        
    def death_count(self):
        ls=[]
        ls.append(self.execute("""select count(*) from death;""")[0][0])
        return ls
        
if __name__=="__main__":
    s= getdata()
    print(s.visit_race())
    #k = s.getpersongender()
