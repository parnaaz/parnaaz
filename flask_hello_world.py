from flask import Flask

# from flask import render_template
#
# @app.route('/')
# def index():
#     name = 'Parnaz'
#     return render_template('index.html', title='Welcome', username=name)
#
# app = Flask(__name__)

# creating an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the main page <h1>HELLO WORLD<h1>"

if __name__ == "__main__":
    app.run()


