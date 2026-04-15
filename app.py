# Imports
import os
from datetime import date
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
    # Blog representation
    def __repr__(self): return f"Blog [{self.id}]: {self.title}"

'''
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
    # Portfolio item representation
    def __repr__(self): return f"Portfolio item [{self.id}]: {self.title}"

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
    # Image representation
    def __repr__(self): return f"Image [{self.id}]: {self.filePath}"
'''

####################################
#### Put stuff in the database #####
####################################
with app.app_context():
    #db.session.delete(Blog.query.get(1))
    db.create_all()
    blog1 = Blog("My first blog", date(2000,1,1), "This is a blog post", "This is the content of the blog post")
    db.session.add(blog1)
    db.session.commit()
    #portfolioItem1 = PortfolioItem("Portfolio Item 1", "2000-01-01", "This is a portfolio item", "This is the content of the portfolio item")
    #db.session.add(portfolioItem1)
    #db.session.commit()
    #image1 = Image(portfolioItem1.id, "Alt text for image 1", "path/to/image1.jpg")
    #db.session.add(image1)
    #db.session.commit()

    all_blogs = Blog.query.all()
    print(all_blogs)






if __name__ == "__main__":
    app.run(debug=True)