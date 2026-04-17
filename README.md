# portfolio_website
Dit is mijn portfolio website gemaakt voor de cursus Webtechnologie bij HBO-ICT bij de Hanze Hogeschool Groningen. 
Deze website zal ik ook uitbreiden en persoonlijk gebruiken.

---
## Vereisten:
- ✅ Website heeft vormgeving en een koppeling met een database
- ✅ Op de site ingevulde data komt via SQLAlchemy terecht in een SQLite-database
- ✅ Website maakt gebruik van verschillende views
- ❌ Geregistreerde bezoekers kunnen op de site inloggen   

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
Flask-Login==0.6.3
Jinja2==3.1.5
SQLAlchemy==2.0.38
WTForms==3.2.1
markdown==3.10.2
python-frontmatter==1.1.0
```
---

# Features
- **Home/About me pagina**  
Een korte beschrijving van mij, mijn skills en wat voorbeelden van mijn werk en blogs die dynamisch worden geladen uit de database.
- **Portfolio pagina**  
Bevat een galerij aan portfolio-items met een thumbnail, en een knop om de portfolio-item te bekijken. Dit gaat via de database.
- **Blog pagina**  
Een lijst van blog-posts met een knop om de blog-post te bekijken. Dit gaat via de database.
- **Resume pagina**  
Simpele statische pagina met mijn CV.
- **Tech pagina**  
Overview van mijn tech-stack, zoals de software die ik gebruik en de hardware die ik heb.
- **~~Login~~**  
Niet aan toe gekomen.

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

    PROJECTS {
        int id PK
        string title
        date date
        string thumbnail
        string content
    }

    MEDIA_ITEMS {
        int id PK
        int portfolio_project_id FK
        string file_path
        string type
        string alt_text
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
  
**Database table 2: Project**  <br>
Deze database-table is iets ingewikkelder. Het liefst kunnen de image-gallery en de text-markdown door elkaar heen. Een portfolio-item bevat ook een galerij van beelden, dit kan er maar 1 zijn, of 25. Zie database 3.

Requirements:
- Title
- Date
- Description
- Thumbnail
- Image gallery
- Text markdown

**Database table 3: Media**  <br>
Deze database-table is een subtable van de project table.

Requirements:
- Foreign-Key om te linken met portfolio_item table
- Alt-Text wat ook eventueel als mini-omschrijving kan worden gebruikt.
- File-Path

---

## Scripts

Momenteel worden twee scripts gebruikt om de database te vullen. `/scripts/blog_markdown_to_db.py` en `/scripts/portfolio_markdown_to_db.py`
De data wordt uit markdown bestanden gehaald. 
Idealer is dat de user (ik als site-eigenaar) deze aan kan maken via een GUI.

---

