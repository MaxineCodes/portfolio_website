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
# STATIC routing
@app.route("/")
def index(): return render_template("index.html")
@app.route("/resume")
def resume(): return render_template("resume.html")
@app.route("/contact")
def contact(): return render_template("contact.html")
@app.route("/tech")
def tech(): return render_template("tech.html")
@app.route("/writing")
def writing(): return render_template("writing.html")

# DYNAMIC routing
@app.route('/portfolio')
def portfolio():
    recent_projects = PortfolioPost.query.order_by(PortfolioPost.date.desc()).all()
    print(recent_projects)
    return render_template('portfolio.html', projects=recent_projects)
@app.route('/portfolio/<int:portfolio_post_id>')
def portfolio_post(portfolio_post_id):
    project = PortfolioPost.query.get_or_404(portfolio_post_id)
    return render_template('portfolioPost.html', project=project)

@app.route('/blog')
def blog():
    recent_blogs = BlogPost.query.order_by(BlogPost.date.desc()).all()
    print(recent_blogs)
    return render_template('blog.html', blogs=recent_blogs)
@app.route('/blog/<int:blog_id>')
def blog_post(blog_id):
    blog = BlogPost.query.get_or_404(blog_id)
    return render_template('blogPost.html', blog=blog)


###########################
#### Define databases #####
###########################

# Blog
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
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
    def __repr__(self): return f"Blog Post [{self.id}]: {self.title}"

# Portfolio item
class PortfolioPost(db.Model):
    __tablename__ = 'portfolio_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    date = db.Column(db.Date)
    thumbnail = db.Column(db.Text) # path to image
    content = db.Column(db.Text) # markdown
    # Relationship to images
    images = db.relationship('Media', backref='portfolio_post', lazy=True)
    # Class Constructor
    def __init__(self, title, date, thumbnail, content):
        self.title = title
        self.date = date
        self.thumbnail = thumbnail
        self.content = content # markdown
    # Portfolio post representation
    def __repr__(self): return f"Portfolio post [{self.id}]: {self.title}"

# Media item
class Media(db.Model):
    __tablename__ = 'media_items'
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.Text)
    type = db.Column(db.Text)
    alt_text = db.Column(db.Text, nullable=True)
    portfolio_post_id = db.Column(db.Integer, db.ForeignKey('portfolio_posts.id'), nullable=True)
    # Class Constructor
    def __init__(self, file_path, media_type="image", alt_text=None, portfolio_post_id=None):
        self.file_path = file_path
        self.type = media_type
        self.alt_text = alt_text
        self.portfolio_post_id = portfolio_post_id
    # Media representation
    def __repr__(self): return f"Media [{self.id}]: {self.file_path}"

####################################
#### Put stuff in the database #####
####################################
with app.app_context():
    #db.session.delete(Blog.query.get(1))
    #db.create_all()
    #blog1 = BlogPost("My first blog", date(2000,1,1), "This is a blog post", "This is the content of the blog post")
    #db.session.add(blog1)
    #db.session.commit()
    #portfolioItem1 = PortfolioItem("Portfolio Item 1", date(2000,1,1), "This is a portfolio item", "This is the content of the portfolio item")
    #db.session.add(portfolioItem1)
    #db.session.commit()
    #image1 = Image(portfolioItem1.id, date(2000,1,1), "path/to/image1.jpg")
    #db.session.add(image1)
    #db.session.commit()

    all_blogs = BlogPost.query.all()
    print(*all_blogs , sep="\n")
    all_portfolio_posts = PortfolioPost.query.all()
    print(*all_portfolio_posts , sep="\n")
    all_media = Media.query.all()
    print(*all_media , sep="\n")






if __name__ == "__main__":
    app.run(debug=True)