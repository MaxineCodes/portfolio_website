import os
import sys
import frontmatter
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
# Add app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, db, PortfolioPost
# Get portfolioposts directory
script_dir = os.path.dirname(os.path.abspath(__file__))
portfolioposts_dir = os.path.join(script_dir, '..', 'portfolioposts')

# Process all .md files in portfolioposts directory
for filename in os.listdir(portfolioposts_dir):
    if filename.endswith('.md'):
        with open(os.path.join(portfolioposts_dir, filename), 'r') as f:
            post = frontmatter.load(f)

        # Extract metadata
        title = post['title']
        date_obj = post['date']
        thumbnail_path = post['thumbnail']

        # Convert content to HTML
        content_html = markdown.markdown(post.content, extensions=['fenced_code', 'tables', 'toc'])

        with app.app_context():
            # Check if port already exists
            existing_post = PortfolioPost.query.filter_by(title=title, date=date_obj).first()
            if not existing_post:
                # Create database entry
                post = PortfolioPost(title=title, date=date_obj, thumbnail=thumbnail_path, content=content_html)
                db.session.add(post)
                db.session.commit()
                print(f"Added: {title}")

            else:print(f"Skipped (already exists): {title}")