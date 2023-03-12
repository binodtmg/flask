from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask App"

@app.route('/test')
def test():
    return "<h1>Hello World</h1>"

@app.route("/data")
def data():
    newdata = "hello world"
    return newdata

@app.route('/jsondata')
def mydata():
    name="Rajendra"
    age=28
    myjson={
        "Name":name,
        "Age":age,
        "phones":[
            {
                "phoneName":"Samsung",
                "phoneNumber":11111
            },
            {
                "phoneName":"Redmi",
                "phoneNumber":1234567
            }
        ]
    }

    return jsonify(myjson)

if __name__ == "__main__":
    app.run(debug=True)
