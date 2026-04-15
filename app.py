# Imports
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
# Define app
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Define db (database)
db = SQLAlchemy(app)


##########################
#### Webpage routing #####
##########################
@app.route("/")
def index(): return render_template("index.html")
@app.route("/portfolio")
def portfolio(): return render_template("portfolio.html")
@app.route("/blog")
def blog(): return render_template("blog.html")
@app.route("/resume")
def resume(): return render_template("resume.html")
@app.route("/contact")
def contact(): return render_template("contact.html")
@app.route("/tech")
def tech(): return render_template("tech.html")
@app.route("/writing")
def writing(): return render_template("writing.html")

###########################
#### Define databases #####
###########################

# Blog
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    date = db.Column(db.Date)
    description = db.Column(db.Text)
    content = db.Column(db.Text) # markdown
    # Class Constructor
    def __init__(self, title, date, description, content):
        self.title = title
        self.date = date
        self.description = description
        self.content = content # markdown

# Portfolio item
class PortfolioItem(db.Model):
    __tablename__ = 'portfolio_items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    date = db.Column(db.Date)
    description = db.Column(db.Text)
    content = db.Column(db.Text) # markdown
    # Class Constructor
    def __init__(self, title, date, description, content):
        self.title = title
        self.date = date
        self.description = description
        self.content = content # markdown

# Gallery image
class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    portfolio_item_id = db.Column(db.Integer, db.ForeignKey('portfolio_item.ID'))
    alt_text = db.Column(db.Text)
    file_path = db.Column(db.Text)
    # Class Constructor
    def __init__(self, portfolio_item_id, alt_text, file_path):
        self.portfolio_item_id = portfolio_item_id
        self.altText = alt_text
        self.filePath = file_path

####################################
#### Put stuff in the database #####
####################################






if __name__ == "__main__":
    app.run(debug=True)