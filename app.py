from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")


#def index():
#    return render_template("index.html")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)