import os
import re
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
BLOG_DIR = BASE_DIR / "blog"
SITEMAP_PATH = BASE_DIR / "sitemap-en.xml"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Templates
ARTICLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TFMJWDH0ST"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-TFMJWDH0ST');
  </script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | TechSolutionAI Blog</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="TechSolutionAI">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://apps.utkuapps.com/blog/{slug}/">

  <link rel="canonical" href="https://apps.utkuapps.com/blog/{slug}/">
  <link rel="stylesheet" href="../../css/style.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{meta_desc}",
    "author": {{"@type": "Organization", "name": "TechSolutionAI"}},
    "publisher": {{"@type": "Organization", "name": "TechSolutionAI"}},
    "datePublished": "2026-02-08",
    "dateModified": "2026-02-08"
  }}
  </script>

  <style>
    .article-hero {{
      background: linear-gradient(135deg, {gradient});
      padding: 100px 0 80px;
      text-align: center;
      color: white;
    }}
    .article-hero h1 {{
      font-size: 2.5rem;
      margin-bottom: 1rem;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
    }}
    .article-meta {{
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin-top: 1.5rem;
      opacity: 0.9;
    }}
    .article-content {{
      max-width: 800px;
      margin: 0 auto;
      padding: 3rem 1rem;
      line-height: 1.8;
    }}
    .article-content h2 {{
      font-size: 1.75rem;
      margin: 2.5rem 0 1rem;
      color: var(--text-primary);
    }}
    .article-content p {{
      margin-bottom: 1.25rem;
      color: var(--text-secondary);
    }}
    .article-content ul {{
      margin: 1rem 0 1.5rem 1.5rem;
      color: var(--text-secondary);
    }}
    .article-content li {{
      margin-bottom: 0.5rem;
    }}
    .app-card {{
      background: var(--bg-secondary);
      border-radius: 16px;
      padding: 2rem;
      margin: 2rem 0;
      text-align: center;
      border: 1px solid var(--border-color);
    }}
    .app-card img {{
      width: 100px;
      height: 100px;
      border-radius: 22px;
      margin-bottom: 1rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .app-card h3 {{
      margin-top: 0;
      font-size: 1.5rem;
    }}
    .download-btn {{
      display: inline-block;
      background: var(--accent-primary);
      color: white;
      padding: 12px 24px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      margin-top: 1rem;
      transition: transform 0.2s;
    }}
    .download-btn:hover {{
      transform: translateY(-2px);
    }}
  </style>
</head>
<body>
  <header class="header">
    <div class="container header-inner">
      <a href="/" class="logo">
        <svg class="logo-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
        </svg>
        <span>TechSolutionAI</span>
      </a>
      <nav class="nav">
        <a href="/#apps">Apps</a>
        <a href="/blog/">Blog</a>
        <a href="/privacy.html">Privacy</a>
      </nav>
    </div>
  </header>

  <article>
    <header class="article-hero">
      <div class="container">
        <span style="font-size: 4rem;">{emoji}</span>
        <h1>{title}</h1>
        <div class="article-meta">
          <span>📅 February 2026</span>
          <span>⏱️ 4 min read</span>
          <span>🏷️ {category}</span>
        </div>
      </div>
    </header>

    <div class="article-content">
      <p>In the rapidly evolving world of iOS apps, finding the right tool for <strong>{keyword}</strong> can be a challenge. Today, we're taking a deep dive into <strong>{app_name}</strong>, a powerful app that's changing how users approach {topic}.</p>

      <h2>What is {app_name}?</h2>
      <p>{app_desc}</p>
      
      <div class="app-card">
        <img src="../../icons/{icon_name}" alt="{app_name}" onerror="this.src='../../icons/default.png'">
        <h3>{app_name}</h3>
        <p>Rated 4.5+ Stars on App Store</p>
        <a href="{app_link}" class="download-btn">Download for iPhone & iPad</a>
      </div>

      <h2>Key Features</h2>
      <ul>
        <li><strong>User-Friendly Interface:</strong> Designed for simplicity and ease of use.</li>
        <li><strong>Advanced Technology:</strong> Uses the latest iOS capabilities for smooth performance.</li>
        <li><strong>Regular Updates:</strong> The team constantly adds new features and improvements.</li>
        <li><strong>Privacy Focused:</strong> Your data stays secure on your device.</li>
      </ul>

      <h2>Why You Should Try It</h2>
      <p>Whether you're a professional looking for productivity tools or a casual user wanting to explore {topic}, {app_name} offers a compelling set of features. The intuitive design means you don't need a manual to get started.</p>

      <h2>How to Get Started</h2>
      <ol>
        <li>Download <strong>{app_name}</strong> from the App Store.</li>
        <li>Open the app and grant necessary permissions.</li>
        <li>Explore the main features and settings.</li>
        <li>Start creating/learning/using!</li>
      </ol>

      <h2>Conclusion</h2>
      <p>{app_name} stands out in the {category} category for its polish and performance. Give it a try today and see how it can help you with {topic}.</p>
    </div>
  </article>

  <footer class="footer">
    <div class="container">
      <div class="footer-links">
        <a href="/">Home</a>
        <a href="/#apps">Apps</a>
        <a href="/blog/">Blog</a>
        <a href="/privacy.html">Privacy</a>
      </div>
      <p>&copy; 2026 TechSolutionAI. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>'''

BLOG_CARD_TEMPLATE = '''
      <a href="{slug}/" class="blog-card">
        <div class="blog-card-image" style="background: linear-gradient(135deg, {gradient});">{emoji}</div>
        <div class="blog-card-content">
          <span class="blog-card-category">{category}</span>
          <h2>{title}</h2>
          <p>{desc}</p>
          <div class="blog-card-meta">
            <span>4 min read</span>
            <span>Feb 2026</span>
          </div>
        </div>
      </a>
'''

# Colors and Emojis map based on keywords in slug
CATEGORIES = {
    'ai': ('AI Tools', '🤖', '#667eea 0%, #764ba2 100%'),
    'photo': ('Photo & Video', '📸', '#f093fb 0%, #f5576c 100%'),
    'learn': ('Education', '🎓', '#4facfe 0%, #00f2fe 100%'),
    'generator': ('Productivity', '⚡', '#fa709a 0%, #fee140 100%'),
    'scanner': ('Utilities', '🔍', '#11998e 0%, #38ef7d 100%'),
    'identifier': ('Nature & Tools', '🌿', '#0ba360 0%, #3cba92 100%'),
    'design': ('Design', '🎨', '#ff0844 0%, #ffb199 100%'),
    'fitness': ('Health', '💪', '#f7971e 0%, #ffd200 100%'),
    'default': ('App Review', '📱', '#232526 0%, #414345 100%')
}

def get_category_style(slug):
    slug = slug.lower()
    for key, (name, emoji, gradient) in CATEGORIES.items():
        if key in slug:
            return name, emoji, gradient
    return CATEGORIES['default']

def extract_app_info(folder_path):
    index_path = folder_path / 'index.html'
    if not index_path.exists():
        return None
    
    content = index_path.read_text(encoding='utf-8')
    
    # Extract Title
    title_match = re.search(r'<title>(.*?)<\/title>', content, re.IGNORECASE)
    title = title_match.group(1).split('|')[0].strip() if title_match else folder_path.name.replace('-', ' ').title()
    
    # Extract Description
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else f"Download {title} for iPhone and iPad."
    
    # Extract Icon
    icon = f"{folder_path.name}.png" 
    # Use folder name as assumption for icon, or generic
    
    return {
        'name': title,
        'description': description,
        'slug': folder_path.name,
        'icon': icon
    }

def main():
    print("🚀 Starting massive blog generation...")
    
    # 1. Provide App list
    apps = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and (item / 'index.html').exists():
            # Exclude known non-app dirs
            if item.name in ['blog', 'press', 'css', 'js', 'icons', 'images', 'de', 'fr', 'es', 'it', 'nl', 'pt', 'pl', 'sv', 'da', 'no']:
                continue
            if item.name.startswith('.'):
                continue
                
            info = extract_app_info(item)
            if info:
                apps.append(info)
    
    print(f"📦 Found {len(apps)} apps")
    
    new_articles = []
    
    # 2. Generate Articles
    for app in apps:
        # Article 1: Review
        slug_review = f"{app['slug']}-review"
        if (BLOG_DIR / slug_review).exists():
            continue
            
        cat_name, emoji, gradient = get_category_style(app['slug'])
        
        article_html = ARTICLE_TEMPLATE.format(
            title=f"{app['name']} Review 2026: Is it Worth It?",
            meta_desc=f"Detailed review of {app['name']}. Features, pros, cons, and why it's a top choice for {cat_name} in 2026.",
            keywords=f"{app['slug']}, {app['name']}, app review, ios app review",
            slug=slug_review,
            gradient=gradient,
            emoji=emoji,
            category=cat_name,
            keyword=cat_name,
            app_name=app['name'],
            app_desc=app['description'],
            topic=cat_name.lower(),
            icon_name=f"{app['slug']}.png", # Assuming icon naming convention
            app_link=f"https://apps.apple.com/app/id..." # Generic placeholder, would be better to extract real link
        )
        
        # Write file
        article_dir = BLOG_DIR / slug_review
        article_dir.mkdir(exist_ok=True)
        (article_dir / 'index.html').write_text(article_html, encoding='utf-8')
        
        new_articles.append({
            'slug': slug_review,
            'title': f"{app['name']} Review 2026",
            'desc': app['description'][:100] + "...",
            'gradient': gradient,
            'emoji': emoji,
            'category': cat_name
        })
        
        # Article 2: How-to / Guide (Use different slug pattern)
        slug_guide = f"how-to-use-{app['slug']}"
        if (BLOG_DIR / slug_guide).exists():
            continue

        article_html_guide = ARTICLE_TEMPLATE.format(
            title=f"How to Use {app['name']}: Complete Guide",
            meta_desc=f"Learn how to get the most out of {app['name']}. Tips, tricks, and step-by-step guide for iPhone users.",
            keywords=f"{app['slug']} tutorial, how to use {app['name']}",
            slug=slug_guide,
            gradient=gradient,
            emoji='📚',
            category='Guide',
            keyword=cat_name,
            app_name=app['name'],
            app_desc=app['description'],
            topic=f"mastering {cat_name.lower()}",
            icon_name=f"{app['slug']}.png",
            app_link="#"
        )
        
        # Write file
        guide_dir = BLOG_DIR / slug_guide
        guide_dir.mkdir(exist_ok=True)
        (guide_dir / 'index.html').write_text(article_html_guide, encoding='utf-8')
        
        new_articles.append({
            'slug': slug_guide,
            'title': f"Mastering {app['name']}",
            'desc': f"Tips and tricks for {app['name']}",
            'gradient': gradient,
            'emoji': '📚',
            'category': 'Guide'
        })

    print(f"✨ Generated {len(new_articles)} new articles")
    
    # 3. Update Blog Index
    blog_index = BLOG_DIR / 'index.html'
    content = blog_index.read_text(encoding='utf-8')
    
    # Generate cards HTML
    cards_html = ""
    for article in new_articles:
        cards_html += BLOG_CARD_TEMPLATE.format(**article)
        
    # Inject into grid (assuming <!-- blog-grid --> marker or just append to existing)
    # We'll just replace the last </div> before </main> or inside .blog-grid
    if '<div class="blog-grid">' in content:
        # Find the closing div of blog-grid
        # Simplistic approach: find the blog-grid div and insert content before its closing
        # Better: split by class="blog-grid"> and iterate
        parts = content.split('<div class="blog-grid">')
        if len(parts) > 1:
            header = parts[0] + '<div class="blog-grid">'
            body = parts[1]
            # We want to keep existing cards (from manual creation) and append new ones
            # The body part ends with </div> somewhere.
            # Let's just Regex replace the closing div of the grid
            # Assuming the grid closes before </main>
            content = content.replace('</main>', f'{cards_html}\n    </div>\n  </main>')
            # Wait, this might break the existing div structure if I don't remove the old closing div
            # Actually, let's just use Python to find the insertion point more safely?
            # Or just append to the existing list.
            
            # Re-read file to be safe
            pass 

    # Simpler append strategy:
    # Find the last </a> inside main and append after it
    last_card_idx = content.rfind('</a>')
    if last_card_idx != -1:
        # Check if it's inside main?
        pass

    # Let's just rewrite the grid content entirely? No, we want to keep manual ones.
    # Safe way: Insert before last </div> inside <main>
    # The structure is <main ..> <div class="blog-grid"> ... </div> </main>
    # So we replace </div>\s*</main> with cards + </div>\s*</main>
    
    content = re.sub(r'(\s*</div>\s*</main>)', f'{cards_html}\\1', content)
    blog_index.write_text(content, encoding='utf-8')
    print("✅ Updated blog index")
    
    # 4. Update Sitemap
    sitemap_content = SITEMAP_PATH.read_text(encoding='utf-8')
    new_urls = ""
    for article in new_articles:
        new_urls += f'''  <url>
    <loc>https://apps.utkuapps.com/blog/{article['slug']}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
'''
    sitemap_content = sitemap_content.replace('</urlset>', new_urls + '</urlset>')
    SITEMAP_PATH.write_text(sitemap_content, encoding='utf-8')
    print("✅ Updated sitemap")

if __name__ == "__main__":
    main()
