import os
import re
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
BLOG_DIR = BASE_DIR / "blog"
SITEMAP_PATH = BASE_DIR / "sitemap-en.xml"
TODAY = "2026-02-08"

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
    
    /* Premium App Card CSS */
    .app-card {{
      background: #ffffff;
      color: #1a1a1a;
      border-radius: 24px;
      padding: 3rem 2rem;
      margin: 3rem 0;
      text-align: center;
      border: 1px solid rgba(0,0,0,0.08);
      box-shadow: 0 20px 60px -10px rgba(0,0,0,0.12);
      position: relative;
      overflow: hidden;
    }}
    .app-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, #007AFF, #00C6FF);
    }}
    .app-card img {{
      width: 128px;
      height: 128px;
      border-radius: 28px;
      margin-bottom: 1.5rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
      border: 1px solid rgba(0,0,0,0.05);
    }}
    .app-card h3 {{
      margin: 0.5rem 0;
      font-size: 1.8rem;
      font-weight: 800;
      color: #111111;
      letter-spacing: -0.5px;
    }}
    .app-card p {{
      color: #555555;
      font-size: 1.1rem;
      margin-bottom: 2rem;
      font-weight: 500;
    }}
    .download-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #000000;
      color: #ffffff !important;
      padding: 16px 36px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1.1rem;
      transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
      box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}
    .download-btn:hover {{
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 15px 30px rgba(0,0,0,0.3);
      background: #222;
    }}
    .download-btn::after {{
      content: '↓';
      font-weight: bold;
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
        <a href="/blog/" class="active">Blog</a>
        <a href="/privacy.html">Privacy</a>
      </nav>
    </div>
  </header>

  <article>
    <header class="article-hero">
      <div class="container">
        <span style="font-size: 5rem; display: block; margin-bottom: 1rem; text-shadow: 0 10px 30px rgba(0,0,0,0.2);">{emoji}</span>
        <h1>{title}</h1>
        <div class="article-meta">
          <span>📅 February 2026</span>
          <span>⏱️ 4 min read</span>
          <span>🏷️ {category}</span>
        </div>
      </div>
    </header>

    <div class="article-content">
      <p class="intro-text">In the rapidly evolving world of iOS apps, finding the right tool for <strong>{keyword}</strong> can be a challenge. Today, we're taking a deep dive into <strong>{app_name}</strong>, a powerful app that's changing how users approach {topic}.</p>

      <h2>What is {app_name}?</h2>
      <p>{app_desc}</p>
      
      <div class="app-card">
        <img src="../../icons/{icon_name}" alt="{app_name}" onerror="this.src='../../icons/default.png'">
        <h3>{app_name}</h3>
        <p>⭐️⭐️⭐️⭐️⭐️ Rated 4.8 Stars on App Store</p>
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

MANUAL_CARDS = '''
            <a href="best-ai-photo-editor-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">📸
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">AI & Photo</span>
                    <h2>Best AI Photo Editor Apps for iPhone 2026</h2>
                    <p>Discover the top AI-powered photo editing apps that transform your images with one tap.
                        Background removal, filters, and more.</p>
                    <div class="blog-card-meta">
                        <span>5 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="language-learning-apps-guide/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">🌍
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Language</span>
                    <h2>Top Language Learning Apps: French, German, Spanish & More</h2>
                    <p>Master a new language with these powerful apps. Compare features, pricing, and effectiveness for
                        beginners to advanced learners.</p>
                    <div class="blog-card-meta">
                        <span>7 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="home-design-apps-review/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">🏠
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Home Design</span>
                    <h2>Home Design Apps That Transform Your Space</h2>
                    <p>Visualize room makeovers, kitchen remodels, and backyard designs with AI-powered interior design
                        apps.</p>
                    <div class="blog-card-meta">
                        <span>6 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="plant-bird-identifier-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);">🌿
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Identifier</span>
                    <h2>Ultimate Guide to Plant & Bird Identifier Apps</h2>
                    <p>Identify plants, birds, insects, and more with your camera. Compare the best identifier apps for
                        nature enthusiasts.</p>
                    <div class="blog-card-meta">
                        <span>5 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="sat-asvab-prep-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">📚
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Education</span>
                    <h2>SAT & ASVAB Prep: Best Study Apps for 2026</h2>
                    <p>Ace your exams with these comprehensive prep apps. Practice tests, flashcards, and study guides
                        all in one place.</p>
                    <div class="blog-card-meta">
                        <span>6 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="ai-companion-apps-review/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #ff0844 0%, #ffb199 100%);">💕
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">AI</span>
                    <h2>AI Girlfriend & Boyfriend Apps: Complete Review</h2>
                    <p>Explore the world of AI companions. Chat, roleplay, and create meaningful connections with
                        virtual partners.</p>
                    <div class="blog-card-meta">
                        <span>8 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="coin-antique-identifier-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);">🪙
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Identifier</span>
                    <h2>Free Coin & Antique Identifier Apps</h2>
                    <p>Discover the value of your coins, antiques, and collectibles. Scan, identify, and get instant
                        valuations.</p>
                    <div class="blog-card-meta">
                        <span>5 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="background-remover-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%);">✂️
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">AI & Photo</span>
                    <h2>Background Remover Apps Comparison 2026</h2>
                    <p>Remove backgrounds instantly with AI. Compare the best tools for product photos, portraits, and
                        creative projects.</p>
                    <div class="blog-card-meta">
                        <span>4 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="tattoo-design-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #232526 0%, #414345 100%);">🎨
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">AI & Design</span>
                    <h2>Best Tattoo Design Generator Apps</h2>
                    <p>Design your perfect tattoo with AI. Generate unique designs, try them on virtually, and find
                        inspiration.</p>
                    <div class="blog-card-meta">
                        <span>5 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>

            <a href="anatomy-learning-apps/" class="blog-card">
                <div class="blog-card-image" style="background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);">🫀
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Education</span>
                    <h2>Anatomy & Physiology Learning Apps for Students</h2>
                    <p>Master human anatomy with 3D models, flashcards, and quizzes. Perfect for medical students and
                        healthcare professionals.</p>
                    <div class="blog-card-meta">
                        <span>6 min read</span>
                        <span>Feb 2026</span>
                    </div>
                </div>
            </a>
'''

BASE_INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-TFMJWDH0ST"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());
        gtag('config', 'G-TFMJWDH0ST');
    </script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - TechSolutionAI | App Reviews, Guides & Tips</title>
    <meta name="description" content="Discover the best iOS apps with our expert reviews, guides, and tips. AI photo editors, language learning, home design, and more.">
    <meta name="keywords" content="ios app reviews, best iphone apps, app guides, ai apps, photo editor apps, language learning apps">
    <meta name="author" content="TechSolutionAI">
    <meta name="robots" content="index, follow">

    <meta property="og:type" content="website">
    <meta property="og:title" content="Blog - TechSolutionAI">
    <meta property="og:description" content="Expert reviews and guides for the best iOS apps.">
    <meta property="og:url" content="https://apps.utkuapps.com/blog/">

    <link rel="canonical" href="https://apps.utkuapps.com/blog/">
    <link rel="stylesheet" href="../css/style.css">

    <style>
        .blog-hero {{
            background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
            padding: 80px 0 60px;
            text-align: center;
            color: white;
        }}

        .blog-hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}

        .blog-hero p {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}

        .blog-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
            padding: 3rem 0;
        }}

        .blog-card {{
            background: var(--bg-secondary);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            text-decoration: none;
            color: inherit;
        }}

        .blog-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        }}

        .blog-card-image {{
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
        }}

        .blog-card-content {{
            padding: 1.5rem;
        }}

        .blog-card-category {{
            display: inline-block;
            background: var(--accent-primary);
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }}

        .blog-card h2 {{
            font-size: 1.25rem;
            margin-bottom: 0.75rem;
            color: var(--text-primary);
        }}

        .blog-card p {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.6;
        }}

        .blog-card-meta {{
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
            font-size: 0.8rem;
            color: var(--text-tertiary);
        }}
    </style>
</head>

<body>
    <header class="header">
        <div class="container header-inner">
            <a href="/" class="logo">
                <svg class="logo-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
                </svg>
                <span>TechSolutionAI</span>
            </a>
            <nav class="nav">
                <a href="/#apps">Apps</a>
                <a href="/blog/" class="active">Blog</a>
                <a href="/privacy.html">Privacy</a>
            </nav>
        </div>
    </header>

    <section class="blog-hero">
        <div class="container">
            <h1>📱 App Reviews & Guides</h1>
            <p>Expert insights on the best iOS apps for iPhone & iPad</p>
        </div>
    </section>

    <main class="container">
        <div class="blog-grid">
            {cards}
        </div>
    </main>
    
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
    <script>
        document.addEventListener('DOMContentLoaded', function () {{
            document.querySelectorAll('a[href*="apps.apple.com"]').forEach(function (link) {{
                link.addEventListener('click', function () {{
                    if (typeof gtag !== 'undefined') {{
                        gtag('event', 'app_store_click', {{
                            'app_name': document.title.split(' - ')[0],
                            'language': document.documentElement.lang,
                            'link_url': this.href
                        }});
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>'''

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
    
    # Extract Title - more robust regex
    title_match = re.search(r'<title>(.*?)<\/title>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        # Simplify title: take everything before |, - or :
        raw_title = title_match.group(1)
        title = re.split(r'[|\-:]', raw_title)[0].strip()
    else:
        title = folder_path.name.replace('-', ' ').title()
    
    # Extract Description
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else f"Download {title} for iPhone and iPad in 2026."
    
    # Extract Icon
    icon = f"{folder_path.name}.png" 
    
    # Extract App Link (Try to find App Store URL)
    link_match = re.search(r'href="(https://apps\.apple\.com/[^"]+)"', content)
    app_link = link_match.group(1) if link_match else "#"
    
    return {
        'name': title,
        'description': description,
        'slug': folder_path.name,
        'icon': icon,
        'link': app_link
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
    
    # 2. Generate Articles (Regenerate All to update CSS)
    for app in apps:
        cat_name, emoji, gradient = get_category_style(app['slug'])
        
        # Article 1: Review
        slug_review = f"{app['slug']}-review"
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
            icon_name=f"{app['slug']}.png",
            app_link=app['link']
        )
        
        # Write file (Overwrite)
        article_dir = BLOG_DIR / slug_review
        article_dir.mkdir(exist_ok=True)
        (article_dir / 'index.html').write_text(article_html, encoding='utf-8')
        
        new_articles.append({
            'slug': slug_review,
            'title': f"{app['name']} Review 2026",
            'desc': app['description'][:120] + "...",
            'gradient': gradient,
            'emoji': emoji,
            'category': cat_name
        })
        
        # Article 2: Guide
        slug_guide = f"how-to-use-{app['slug']}"
        article_html_guide = ARTICLE_TEMPLATE.format(
            title=f"How to Use {app['name']}: Complete Guide",
            meta_desc=f"Learn how to get the most out of {app['name']}. Tips, tricks, and step-by-step guide for iPhone users in 2026.",
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
            app_link=app['link']
        )
        (BLOG_DIR / slug_guide).mkdir(exist_ok=True)
        (BLOG_DIR / slug_guide / 'index.html').write_text(article_html_guide, encoding='utf-8')
        
        new_articles.append({
            'slug': slug_guide,
            'title': f"Mastering {app['name']}",
            'desc': f"Tips, tricks, and hidden features for {app['name']}",
            'gradient': gradient,
            'emoji': '📚',
            'category': 'Guide'
        })

    print(f"✨ Generated {len(new_articles)} articles")
    
    # 3. Rebuild Main Blog Index
    blog_index = BLOG_DIR / 'index.html'
    
    # Generate cards HTML
    new_cards_html = ""
    for article in new_articles:
        new_cards_html += BLOG_CARD_TEMPLATE.format(**article)
    
    # Combine Manual + New
    full_cards_html = MANUAL_CARDS + new_cards_html
    
    # Write Index
    blog_index.write_text(BASE_INDEX_TEMPLATE.format(cards=full_cards_html), encoding='utf-8')
    print("✅ Completely Rebuilt Blog Index")
    
    # 4. Update Sitemap (Simplified)
    sitemap_content = SITEMAP_PATH.read_text(encoding='utf-8')
    new_urls = ""
    # Only add if not exists
    existing_urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap_content))
    
    for article in new_articles:
        url = f"https://apps.utkuapps.com/blog/{article['slug']}/"
        if url not in existing_urls:
            new_urls += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
'''
    if new_urls:
        sitemap_content = sitemap_content.replace('</urlset>', new_urls + '</urlset>')
        SITEMAP_PATH.write_text(sitemap_content, encoding='utf-8')
        print("✅ Updated sitemap")

if __name__ == "__main__":
    main()
