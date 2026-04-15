import os
import sys
import frontmatter
import markdown
from datetime import datetime
# Add app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, db, BlogPost
# Get blogposts directory
script_dir = os.path.dirname(os.path.abspath(__file__))
blogposts_dir = os.path.join(script_dir, '..', 'blogposts')

# Process all .md files in blogposts directory
for filename in os.listdir(blogposts_dir):
    if filename.endswith('.md'):
        with open(os.path.join(blogposts_dir, filename), 'r') as f:
            post = frontmatter.load(f)

        # Extract metadata
        title = post['title']
        date_obj = post['date']
        description = post['description']

        # Convert content to HTML
        content_html = markdown.markdown(post.content)

        # Create database entry
        blog = BlogPost(title=title, date=date_obj, description=description, content=content_html)

        with app.app_context():
            db.session.add(blog)
            db.session.commit()
