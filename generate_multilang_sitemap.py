import os
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
DOMAIN = "https://apps.utkuapps.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

LANGUAGES = ['de', 'fr', 'es', 'it', 'nl', 'pt', 'pl', 'sv', 'da', 'no']

SITEMAP_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>'''

URL_TEMPLATE = '''  <url>
    <loc>{loc}</loc>
    <lastmod>{date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>'''

INDEX_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemaps}
</sitemapindex>'''

SITEMAP_ENTRY_TEMPLATE = '''  <sitemap>
    <loc>{loc}</loc>
    <lastmod>{date}</lastmod>
  </sitemap>'''

def generate_language_sitemap(lang):
    print(f"🗺️ Generating sitemap for {lang}...", end=" ", flush=True)
    lang_dir = BASE_DIR / lang / "blog"
    if not lang_dir.exists():
        print("Skipping (Dir not found)")
        return False

    urls = ""
    # Add Index
    urls += URL_TEMPLATE.format(loc=f"{DOMAIN}/{lang}/blog/", date=TODAY)
    
    # Add Posts
    for post in lang_dir.iterdir():
        if post.is_dir() and (post / "index.html").exists():
            urls += "\n" + URL_TEMPLATE.format(loc=f"{DOMAIN}/{lang}/blog/{post.name}/", date=TODAY)
            
    sitemap_content = SITEMAP_TEMPLATE.format(urls=urls)
    (BASE_DIR / f"sitemap-{lang}.xml").write_text(sitemap_content, encoding='utf-8')
    print("✅ Done")
    return True

def generate_sitemap_index(generated_langs):
    print("🗂️ Generating Sitemap Index...", end=" ", flush=True)
    entries = ""
    # Add existing English sitemap if it exists
    if (BASE_DIR / "sitemap.xml").exists():
         entries += SITEMAP_ENTRY_TEMPLATE.format(loc=f"{DOMAIN}/sitemap.xml", date=TODAY)
    
    for lang in generated_langs:
        entries += "\n" + SITEMAP_ENTRY_TEMPLATE.format(loc=f"{DOMAIN}/sitemap-{lang}.xml", date=TODAY)
        
    index_content = INDEX_TEMPLATE.format(sitemaps=entries)
    (BASE_DIR / "sitemap-index.xml").write_text(index_content, encoding='utf-8')
    print("✅ Done")

def main():
    generated = []
    for lang in LANGUAGES:
        if generate_language_sitemap(lang):
            generated.append(lang)
            
    generate_sitemap_index(generated)

if __name__ == "__main__":
    main()
