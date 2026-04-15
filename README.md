# portfolio_website
Dit is mijn portfolio website gemaakt voor de cursus Webtechnologie bij HBO-ICT bij de Hanze Hogeschool Groningen. 
Deze website zal ik ook uitbreiden en persoonlijk gebruiken.

---
## Vereisten:
- Website heeft vormgeving en een koppeling met een database
- Op de site ingevulde data komt via SQLAlchemy terecht in een SQLite-database
- Website maakt gebruik van verschillende views
- Geregistreerde bezoekers kunnen op de site inloggen   

### Libraries & modules:
`Requirements.txt`
```
bcrypt==4.2.1
email_validator==2.2.0
Flask==3.1.0
Flask-Email==1.4.4
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
Jinja2==3.1.5
SQLAlchemy==2.0.38
WTForms==3.2.1
markdown==3.10.2
python-frontmatter==1.1.0
```
---

# Features
- **Home/About me pagina**  
Een korte beschrijving van mij, mijn skills en wat voorbeelden van mijn werk.
- **Portfolio pagina**  
Bevat een galerij aan portfolio-items met een thumbnail, en een knop om de portfolio-item te bekijken. Dit gaat via een database.
- **Blog pagina**  
Een lijst van blog-posts met een knop om de blog-post te bekijken. Dit gaat via een database.
- **Resume pagina**  
Mijn CV.
- **Tech pagina**  
Overview van mijn tech-stack, zoals de software die ik gebruik en de hardware die ik heb.
- **Writing pagina**  
Voor als ik ooit iets leuks wil schrijven, zoals tutorials in de toekomst bijvoorbeeld.

---

# Database design

```
    BLOGS {
        int id PK
        string title
        date date
        string description
        string content
    }

    PORTFOLIO_ITEMS {
        int id PK
        string title
        date date
        string description
        string content
    }

    IMAGES {
        int id PK
        int portfolio_item_id FK
        int blog_id FK
        string alt_text
        string file_path
    }
```

**Database table 1: Blog**  <br>
Een blog is een simpelere object om een database-table voor te maken.
`.md` bestanden kunnen in de browser gerenderd worden via `from flask import render_template`. 

Requirements:
- Title
- Date
- Description
- Contents markdown file

```python
class Blog(db.Model):
	__tablename__ = 'blogs'
	# ID: db.Integer
	# TITLE: db.Text
	# DATE: db.Date
	# DESCRIPTION: db.Text
	# CONTENT: db.Text (Markdown)
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.Text)
	date = db.Column(db.Date)
	description = db.Column(db.Text)
	content = db.Column(db.Text)
	
	# Class Constructor
	def __init__(self,title,date,description,content):
	self.title = title
	self.date = date
	self.description = description
	self.content = content

```
**Database table 2: Portfolio**  <br>
Deze database-table is iets ingewikkelder. Het liefst kunnen de image-gallery en de text-markdown door elkaar heen. Een portfolio-item bevat ook een galerij van beelden, dit kan er maar 1 zijn, of 25. Uiteindelijk kan het zelfs een embed of video bevatten, maar dit kan op dezelfde manier geïmplementeerd worden als beelden als de database-structuur slim aan wordt gepakt. Zie database 3.

Requirements:
- Title
- Date
- Description
- Thumbnail
- Image gallery
- Text markdown

```python
class PortfolioItem(db.Model):
	__tablename__ = 'portfolio_items'
	# ID: db.Integer
	# TITLE: db.Text
	# DATE: db.Date
	# DESCRIPTION: db.Text
	# CONTENT: db.Text (Markdown)
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.Text)
	date = db.Column(db.Date)
	description = db.Column(db.Text)
	content = db.Column(db.Text)
	
	# Class Constructor
	def __init__(self,title,date,description,content):
	self.title = title
	self.date = date
	self.description = description
	self.content = content

```

**Database table 3: Images**  <br>
Deze database-table is een subtable van de portfolio-item table.
Deze database-table zou in de toekomst ook videos of embeds kunnen ondersteunen.

Requirements:
- Foreign-Key om te linken met portfolio_item table
- Alt-Text wat ook eventueel als mini-omschrijving kan worden gebruikt.
- File-Path 

```python
class Image(db.Model):
	__tablename__ = 'portfolio_items'
	# ID: db.Integer (PK)
	# PORTFOLIO_ITEM_ID: db.Text (FK)
	# ALT_TEXT: db.Text
	# FILE_PATH: db.Text
	id = db.Column(db.Integer, primary_key=True)
    portfolio_item_id = db.Column(db.Integer, db.ForeignKey('portfolio_item.ID'))
    alt_text = db.Column(db.Text)
    file_path = db.Column(db.Text)
	
	# Class Constructor
	    def __init__(self, portfolio_item_id, alt_text, file_path):
        self.portfolio_item_id = portfolio_item_id
        self.altText = alt_text
        self.filePath = file_path

```

---

