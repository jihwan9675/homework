from flask import Flask
from flask_restplus import Api, Resource, fields
from modules.getdata import getdata

app = Flask(__name__)
api = Api(app, version='1.0', title='환자 정보 조회', description='기술과제')
getdata = getdata() # 쿼리문 구현 클래스, 요구사항의 메소드 구현


@api.route('/person') # 환자 수
class Person(Resource):
    def get(self):
        return getdata.person_count()

@api.route('/person/gender') # 환자 수 기준 남,여 환자 수
class person_gender(Resource):
    def get(self):
        return getdata.person_gender()

@api.route('/person/race') # 환자 수 기준 인종별 환자 수
class person_gender(Resource):
    def get(self):
        return getdata.person_race()

@api.route('/person/ethnicity') # 환자 수 기준 민족별 환자 수
class person_gender(Resource):
    def get(self):
        return getdata.person_ethnicity()

@api.route('/person/death') # 사망자 수
class person_gender(Resource):
    def get(self):
        return getdata.death_count()

@api.route('/visitaion/concept') # 방문자 수 기준 방문 유형별 방문자 수
class person_gender(Resource):
    def get(self):
        return getdata.visit_concept()

@api.route('/visitaion/age') # 방문자 수 기준 나이별 방문자 수
class person_gender(Resource):
    def get(self):
        return getdata.visit_age() 

@api.route('/visitaion/ethnicity') # 방문자 수 기준 민족별 방문자 수
class person_gender(Resource):
    def get(self):
        return getdata.visit_ethnicity() 

@api.route('/visitaion/gender') # 방문자 수 기준 성별별 방문자 수
class person_gender(Resource):
    def get(self):
        return getdata.visit_gender()

@api.route('/visitaion/race') # 방문자 수 기준 인종 별 방문자 수
class person_gender(Resource):
    def get(self):
        return getdata.visit_race()



if __name__ == '__main__':
    app.run(debug=True)
