#!/usr/bin/env python3
"""
FULL CONTENT TRANSLATION SCRIPT
Translates ALL text content (not just UI elements) for maximum SEO impact
Uses Google Translate API via deep-translator for accurate translations
"""

import os
import re
import time
import json
from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Configuration 
BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")

# Target languages
LANGUAGES = {
    'de': 'german',
    'fr': 'french', 
    'es': 'spanish',
    'it': 'italian',
    'nl': 'dutch',
    'pt': 'portuguese',
    'pl': 'polish',
    'sv': 'swedish',
    'da': 'danish',
    'no': 'norwegian',
}

LANGUAGE_LOCALES = {
    'de': 'de_DE',
    'fr': 'fr_FR',
    'es': 'es_ES', 
    'it': 'it_IT',
    'nl': 'nl_NL',
    'pt': 'pt_PT',
    'pl': 'pl_PL',
    'sv': 'sv_SE',
    'da': 'da_DK',
    'no': 'nb_NO',
}

# Translation cache to avoid re-translating same text
translation_cache = {}

def get_translator(lang_code):
    """Get translator for target language"""
    target = LANGUAGES[lang_code]
    return GoogleTranslator(source='english', target=target)

def translate_text(text, lang_code):
    """Translate text with caching"""
    if not text or not text.strip():
        return text
    
    # Skip if too short or just numbers/symbols
    clean_text = text.strip()
    if len(clean_text) < 3 or clean_text.isdigit():
        return text
    
    # Check cache
    cache_key = f"{lang_code}:{clean_text}"
    if cache_key in translation_cache:
        return translation_cache[cache_key]
    
    try:
        translator = get_translator(lang_code)
        translated = translator.translate(clean_text)
        translation_cache[cache_key] = translated
        return translated
    except Exception as e:
        print(f"    Translation error: {e}")
        return text

def translate_html_content(html_content, lang_code):
    """Translate all text content in HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update HTML lang attribute
    html_tag = soup.find('html')
    if html_tag:
        html_tag['lang'] = lang_code
    
    # Translate title
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        title_tag.string = translate_text(title_tag.string, lang_code)
    
    # Translate meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        meta_desc['content'] = translate_text(meta_desc['content'], lang_code)
    
    # Translate og:title
    og_title = soup.find('meta', attrs={'property': 'og:title'})
    if og_title and og_title.get('content'):
        og_title['content'] = translate_text(og_title['content'], lang_code)
    
    # Translate og:description
    og_desc = soup.find('meta', attrs={'property': 'og:description'})
    if og_desc and og_desc.get('content'):
        og_desc['content'] = translate_text(og_desc['content'], lang_code)
    
    # Add og:locale
    locale = LANGUAGE_LOCALES.get(lang_code, f'{lang_code}_{lang_code.upper()}')
    existing_locale = soup.find('meta', attrs={'property': 'og:locale'})
    if existing_locale:
        existing_locale['content'] = locale
    else:
        og_type = soup.find('meta', attrs={'property': 'og:type'})
        if og_type:
            new_locale = soup.new_tag('meta', property='og:locale', content=locale)
            og_type.insert_before(new_locale)
    
    # Elements to translate (text content)
    text_elements = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'li', 'button', 'label']
    
    for tag_name in text_elements:
        for element in soup.find_all(tag_name):
            # Skip if has only child elements (no direct text)
            if element.string:
                element.string = translate_text(element.string, lang_code)
            else:
                # Handle mixed content (text + child elements)
                for content in element.contents:
                    if isinstance(content, str) and content.strip():
                        translated = translate_text(content, lang_code)
                        content.replace_with(translated)
    
    # Translate FAQ structured data
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            if script.string:
                data = json.loads(script.string)
                if data and isinstance(data, dict) and data.get('@type') == 'FAQPage':
                    main_entity = data.get('mainEntity', [])
                    if isinstance(main_entity, list):
                        for item in main_entity:
                            if isinstance(item, dict):
                                if item.get('name'):
                                    item['name'] = translate_text(item['name'], lang_code)
                                accepted = item.get('acceptedAnswer')
                                if isinstance(accepted, dict) and accepted.get('text'):
                                    accepted['text'] = translate_text(accepted['text'], lang_code)
                        script.string = json.dumps(data, ensure_ascii=False, indent=2)
        except (json.JSONDecodeError, AttributeError, TypeError):
            pass
    
    return str(soup)

def add_hreflang_tags(html_content, app_slug, current_lang):
    """Add hreflang tags"""
    soup = BeautifulSoup(html_content, 'html.parser')
    head = soup.find('head')
    
    if not head:
        return html_content
    
    # Remove existing hreflang tags
    for link in soup.find_all('link', rel='alternate'):
        if link.get('hreflang'):
            link.decompose()
    
    # Add new hreflang tags
    base_url = f"https://apps.utkuapps.com/{app_slug}/"
    
    # English as default
    en_link = soup.new_tag('link', rel='alternate', hreflang='en', href=base_url)
    head.append(en_link)
    
    default_link = soup.new_tag('link', rel='alternate', hreflang='x-default', href=base_url)
    head.append(default_link)
    
    # All language versions
    for lang in LANGUAGES.keys():
        lang_url = f"https://apps.utkuapps.com/{lang}/{app_slug}/"
        lang_link = soup.new_tag('link', rel='alternate', hreflang=lang, href=lang_url)
        head.append(lang_link)
    
    return str(soup)

def update_paths(html_content, lang_code):
    """Update asset paths for language subdirectory"""
    # CSS/JS paths need to go up one more level
    html_content = html_content.replace('href="../css/', 'href="../../css/')
    html_content = html_content.replace('href="../js/', 'href="../../js/')
    html_content = html_content.replace('src="../icons/', 'src="../../icons/')
    html_content = html_content.replace('src="../images/', 'src="../../images/')
    
    # Fix navigation links  
    html_content = html_content.replace('href="/"', f'href="/{lang_code}/"')
    html_content = html_content.replace('href="../"', f'href="../../{lang_code}/"')
    
    return html_content

def process_app_page(source_path, app_slug, lang_code):
    """Process single app page with full translation"""
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Full content translation
    content = translate_html_content(content, lang_code)
    
    # Add hreflang tags
    content = add_hreflang_tags(content, app_slug, lang_code)
    
    # Update paths
    content = update_paths(content, lang_code)
    
    return content

def generate_all_translations():
    """Generate fully translated pages for all languages"""
    # Find all app directories
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    
    app_dirs = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude_dirs:
            index_path = item / 'index.html'
            if index_path.exists():
                app_dirs.append(item.name)
    
    print(f"📁 Found {len(app_dirs)} app directories")
    total_pages = 0
    
    for lang_code in LANGUAGES.keys():
        print(f"\n🌍 Translating to {LANGUAGES[lang_code].upper()} ({lang_code})...")
        
        # Create/update language directory
        lang_dir = BASE_DIR / lang_code
        lang_dir.mkdir(exist_ok=True)
        
        for i, app_slug in enumerate(app_dirs):
            source_path = BASE_DIR / app_slug / 'index.html'
            dest_dir = lang_dir / app_slug
            dest_dir.mkdir(exist_ok=True)
            
            try:
                print(f"  [{i+1}/{len(app_dirs)}] {app_slug}...", end=" ", flush=True)
                
                content = process_app_page(source_path, app_slug, lang_code)
                
                dest_path = dest_dir / 'index.html'
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("✅")
                total_pages += 1
                
                # Rate limiting to avoid API blocks
                time.sleep(0.5)
                
            except Exception as e:
                print(f"❌ Error: {e}")
    
    return total_pages

def update_english_hreflang():
    """Add hreflang to original English pages"""
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    
    updated = 0
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude_dirs:
            index_path = item / 'index.html'
            if index_path.exists():
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = add_hreflang_tags(content, item.name, 'en')
                
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated += 1
    
    print(f"✅ Updated {updated} English pages with hreflang")
    return updated

def generate_sitemaps():
    """Generate all sitemaps"""
    # Sitemap index
    sitemap_index = '''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://apps.utkuapps.com/sitemap-en.xml</loc>
  </sitemap>
'''
    
    for lang in LANGUAGES.keys():
        sitemap_index += f'''  <sitemap>
    <loc>https://apps.utkuapps.com/sitemap-{lang}.xml</loc>
  </sitemap>
'''
    
    sitemap_index += '</sitemapindex>'
    
    with open(BASE_DIR / 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_index)
    
    # Language-specific sitemaps
    for lang in LANGUAGES.keys():
        lang_dir = BASE_DIR / lang
        urls = []
        
        if lang_dir.exists():
            for app_dir in lang_dir.iterdir():
                if app_dir.is_dir() and (app_dir / 'index.html').exists():
                    urls.append(f'https://apps.utkuapps.com/{lang}/{app_dir.name}/')
        
        sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''
        
        for url in urls:
            app_slug = url.split('/')[-2]
            sitemap_content += f'''  <url>
    <loc>{url}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/{app_slug}/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/{app_slug}/"/>
'''
            for other_lang in LANGUAGES.keys():
                sitemap_content += f'''    <xhtml:link rel="alternate" hreflang="{other_lang}" href="https://apps.utkuapps.com/{other_lang}/{app_slug}/"/>
'''
            sitemap_content += '''    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
        
        sitemap_content += '</urlset>'
        
        with open(BASE_DIR / f'sitemap-{lang}.xml', 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        
        print(f"📄 sitemap-{lang}.xml: {len(urls)} URLs")
    
    # English sitemap
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    en_urls = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude_dirs:
            if (item / 'index.html').exists():
                en_urls.append(f'https://apps.utkuapps.com/{item.name}/')
    
    en_sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''
    
    for url in en_urls:
        app_slug = url.split('/')[-2]
        en_sitemap += f'''  <url>
    <loc>{url}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{url}"/>
'''
        for lang in LANGUAGES.keys():
            en_sitemap += f'''    <xhtml:link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app_slug}/"/>
'''
        en_sitemap += '''    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
'''
    
    en_sitemap += '</urlset>'
    
    with open(BASE_DIR / 'sitemap-en.xml', 'w', encoding='utf-8') as f:
        f.write(en_sitemap)
    
    print(f"📄 sitemap-en.xml: {len(en_urls)} URLs")

def save_translation_cache():
    """Save translation cache for future use"""
    cache_path = BASE_DIR / '.translation_cache.json'
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump(translation_cache, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved {len(translation_cache)} translations to cache")

def load_translation_cache():
    """Load existing translation cache"""
    global translation_cache
    cache_path = BASE_DIR / '.translation_cache.json'
    if cache_path.exists():
        with open(cache_path, 'r', encoding='utf-8') as f:
            translation_cache = json.load(f)
        print(f"📂 Loaded {len(translation_cache)} cached translations")

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 FULL CONTENT TRANSLATION - SEO OPTIMIZATION")
    print("=" * 60)
    
    # Load cache if exists
    load_translation_cache()
    
    # Step 1: Translate all pages
    total = generate_all_translations()
    
    # Step 2: Update English pages with hreflang
    update_english_hreflang()
    
    # Step 3: Generate sitemaps with hreflang
    generate_sitemaps()
    
    # Step 4: Save cache
    save_translation_cache()
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE! Fully translated {total} pages across {len(LANGUAGES)} languages")
    print("=" * 60)
