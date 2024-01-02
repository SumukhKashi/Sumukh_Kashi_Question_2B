# from flask import Flask

# app = Flask(_name_)

# @app.route('/')
# def index():
#     return 'Hello, your_name (your_usn)!'

# if _name_ == '_main_':
#     app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home_page(name=None):
    return render_template("index.html",name=name)


if __name__ == '_main_':
    app.run(host='0.0.0.0',port=5000)
