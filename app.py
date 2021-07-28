from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#this is using get method inside class
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

#Below we are implementing only method
@app.route("/LeapYearOrNot/<int:year>")
def leapYearOrNot(year):
    if ((year%4)==0):
        if ((year%100)==0):
            if ((year%400)==0):
                dictResult = {
                    'Input Number is' : year,
                    'Year is leap or not' : 'It is leap year'
                }
            else:
                dictResult = {
                    'Input Number is' : year,
                    'Year is leap or not' : 'It is not leap year'
                }
        else:
            dictResult = {
                    'Input Number is' : year,
                    'Year is leap or not' : 'It is leap year'
                }
    else:
        dictResult = {
                    'Input Number is' : year,
                    'Year is leap or not' : 'It is not leap year'
                }

    return dictResult

if __name__ == '__main__':
    app.run(debug=True)