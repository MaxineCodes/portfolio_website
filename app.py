from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/tech")
def tech():
    return render_template("tech.html")
@app.route("/writing")
def writing():
    return render_template("writing.html")


#def index():
#    return render_template("index.html")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)