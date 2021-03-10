from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='환자 정보 조회', description='기술과제')

@api.route('/person/<id>')
@api.doc(params={'id': 'An ID'})
class Person(Resource):
    def get(self, id):
        return {id:1}



if __name__ == '__main__':
    app.run(debug=True)
