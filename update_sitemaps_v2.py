import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
BLOG_DIR = BASE_DIR / "blog"
TODAY = datetime.now().strftime("%Y-%m-%d")

LANGUAGES = {
    'de': 'de_DE', 'fr': 'fr_FR', 'es': 'es_ES', 'it': 'it_IT',
    'nl': 'nl_NL', 'pt': 'pt_PT', 'pl': 'pl_PL', 'sv': 'sv_SE',
    'da': 'da_DK', 'no': 'nb_NO',
}

def get_apps():
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy', 'blog', 'press'} | set(LANGUAGES.keys())
    return [d.name for d in BASE_DIR.iterdir() if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]

def get_blog_posts():
    return [d.name for d in BLOG_DIR.iterdir() if d.is_dir() and (d / 'index.html').exists()]

def generate_sitemap(lang=None):
    is_default = lang is None
    lang_prefix = f"{lang}/" if lang else ""
    
    apps = get_apps()
    posts = get_blog_posts()
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    
    # 1. Apps
    for app in apps:
        url = f"https://apps.utkuapps.com/{lang_prefix}{app}/"
        sitemap += f'  <url>\n    <loc>{url}</loc>\n'
        sitemap += f'    <lastmod>{TODAY}</lastmod>\n'
        sitemap += f'    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n'
        
        # Hreflang
        sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/{app}/"/>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/{app}/"/>\n'
        for l in LANGUAGES:
            sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/{app}/"/>\n'
        sitemap += '  </url>\n'

    # 2. Blog Index
    url = f"https://apps.utkuapps.com/{lang_prefix}blog/"
    sitemap += f'  <url>\n    <loc>{url}</loc>\n'
    sitemap += f'    <lastmod>{TODAY}</lastmod>\n'
    sitemap += f'    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n'
    sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/blog/"/>\n'
    sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/blog/"/>\n'
    for l in LANGUAGES:
        sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/blog/"/>\n'
    sitemap += '  </url>\n'

    # 3. Blog Posts
    for post in posts:
        url = f"https://apps.utkuapps.com/{lang_prefix}blog/{post}/"
        sitemap += f'  <url>\n    <loc>{url}</loc>\n'
        sitemap += f'    <lastmod>{TODAY}</lastmod>\n'
        sitemap += f'    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
        
        # Hreflang
        sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/blog/{post}/"/>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/blog/{post}/"/>\n'
        for l in LANGUAGES:
            sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/blog/{post}/"/>\n'
        sitemap += '  </url>\n'
        
    sitemap += '</urlset>'
    
    filename = f"sitemap-{lang}.xml" if lang else "sitemap-en.xml"
    with open(BASE_DIR / filename, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"✅ Generated {filename} with {len(apps) + len(posts) + 1} URLs")

def generate_index():
    index = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    index += '  <sitemap><loc>https://apps.utkuapps.com/sitemap-en.xml</loc></sitemap>\n'
    for lang in LANGUAGES:
        index += f'  <sitemap><loc>https://apps.utkuapps.com/sitemap-{lang}.xml</loc></sitemap>\n'
    index += '</sitemapindex>'
    
    with open(BASE_DIR / 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(index)
    print("✅ Generated sitemap.xml index")

if __name__ == "__main__":
    print("🚀 Generating Comprehensive Sitemaps...")
    generate_sitemap(None) # English
    for lang in LANGUAGES:
        generate_sitemap(lang)
    generate_index()
    print("✨ Sitemaps Done!")
