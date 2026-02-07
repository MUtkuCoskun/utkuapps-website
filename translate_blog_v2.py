import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
BLOG_DIR = BASE_DIR / "blog"

LANGUAGES = {
    'de': 'de_DE', 'fr': 'fr_FR', 'es': 'es_ES', 'it': 'it_IT',
    'nl': 'nl_NL', 'pt': 'pt_PT', 'pl': 'pl_PL', 'sv': 'sv_SE',
    'da': 'da_DK', 'no': 'nb_NO',
}

# Simple translation dictionary for common UI elements
TRANSLATIONS = {
    'de': {'Home': 'Startseite', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Datenschutz', 'Read more': 'Weiterlesen', 'min read': 'Min. Lesezeit', 'Review': 'Bewertung', 'Guide': 'Anleitung', 'How to Use': 'Wie man benutzt', 'Conclusion': 'Fazit', 'Key Features': 'Hauptfunktionen', 'Download': 'Herunterladen', 'Share': 'Teilen', 'Related Articles': 'Ähnliche Artikel', 'All rights reserved': 'Alle Rechte vorbehalten'},
    'fr': {'Home': 'Accueil', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Confidentialité', 'Read more': 'Lire la suite', 'min read': 'min de lecture', 'Review': 'Avis', 'Guide': 'Guide', 'How to Use': 'Comment utiliser', 'Conclusion': 'Conclusion', 'Key Features': 'Fonctionnalités clés', 'Download': 'Télécharger', 'Share': 'Partager', 'Related Articles': 'Articles connexes', 'All rights reserved': 'Tous droits réservés'},
    'es': {'Home': 'Inicio', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacidad', 'Read more': 'Leer más', 'min read': 'min de lectura', 'Review': 'Reseña', 'Guide': 'Guía', 'How to Use': 'Cómo usar', 'Conclusion': 'Conclusión', 'Key Features': 'Características clave', 'Download': 'Descargar', 'Share': 'Compartir', 'Related Articles': 'Artículos relacionados', 'All rights reserved': 'Todos los derechos reservados'},
    'it': {'Home': 'Home', 'Apps': 'App', 'Blog': 'Blog', 'Privacy': 'Privacy', 'Read more': 'Leggi di più', 'min read': 'min di lettura', 'Review': 'Recensione', 'Guide': 'Guida', 'How to Use': 'Come usare', 'Conclusion': 'Conclusione', 'Key Features': 'Caratteristiche principali', 'Download': 'Scarica', 'Share': 'Condividi', 'Related Articles': 'Articoli correlati', 'All rights reserved': 'Tutti i diritti riservati'},
    'nl': {'Home': 'Home', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacy', 'Read more': 'Lees meer', 'min read': 'min leestijd', 'Review': 'Beoordeling', 'Guide': 'Gids', 'How to Use': 'Hoe te gebruiken', 'Conclusion': 'Conclusie', 'Key Features': 'Belangrijkste kenmerken', 'Download': 'Downloaden', 'Share': 'Delen', 'Related Articles': 'Gerelateerde artikelen', 'All rights reserved': 'Alle rechten voorbehouden'},
    'pt': {'Home': 'Início', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacidade', 'Read more': 'Leia mais', 'min read': 'min de leitura', 'Review': 'Avaliação', 'Guide': 'Guia', 'How to Use': 'Como usar', 'Conclusion': 'Conclusão', 'Key Features': 'Recursos principais', 'Download': 'Baixar', 'Share': 'Compartilhar', 'Related Articles': 'Artigos relacionados', 'All rights reserved': 'Todos os direitos reservados'},
    'pl': {'Home': 'Strona główna', 'Apps': 'Aplikacje', 'Blog': 'Blog', 'Privacy': 'Prywatność', 'Read more': 'Czytaj więcej', 'min read': 'min czytania', 'Review': 'Recenzja', 'Guide': 'Poradnik', 'How to Use': 'Jak używać', 'Conclusion': 'Wniosek', 'Key Features': 'Główne cechy', 'Download': 'Pobierz', 'Share': 'Udostępnij', 'Related Articles': 'Powiązane artykuły', 'All rights reserved': 'Wszelkie prawa zastrzeżone'},
    'sv': {'Home': 'Hem', 'Apps': 'Appar', 'Blog': 'Blog', 'Privacy': 'Integritet', 'Read more': 'Läs mer', 'min read': 'min läsning', 'Review': 'Recension', 'Guide': 'Guide', 'How to Use': 'Hur man använder', 'Conclusion': 'Slutsats', 'Key Features': 'Nyckelfunktioner', 'Download': 'Ladda ner', 'Share': 'Dela', 'Related Articles': 'Relaterade artiklar', 'All rights reserved': 'Alla rättigheter förbehållna'},
    'da': {'Home': 'Hjem', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privatliv', 'Read more': 'Læs mere', 'min read': 'min læsning', 'Review': 'Anmeldelse', 'Guide': 'Guide', 'How to Use': 'Sådan bruges', 'Conclusion': 'Konklusion', 'Key Features': 'Nøglefunktioner', 'Download': 'Hent', 'Share': 'Del', 'Related Articles': 'Relaterede artikler', 'All rights reserved': 'Alle rettigheder forbeholdes'},
    'no': {'Home': 'Hjem', 'Apps': 'Apper', 'Blog': 'Blog', 'Privacy': 'Personvern', 'Read more': 'Les mer', 'min read': 'min lesing', 'Review': 'Anmeldelse', 'Guide': 'Guide', 'How to Use': 'Hvordan bruke', 'Conclusion': 'Konklusjon', 'Key Features': 'Nøkkelfunksjoner', 'Download': 'Last ned', 'Share': 'Del', 'Related Articles': 'Relaterte artikler', 'All rights reserved': 'Alle rettigheter forbeholdt'},
}

def translate_text(text, lang):
    if not text: return text
    # Simple substitution for now
    trans = TRANSLATIONS.get(lang, {})
    for k, v in trans.items():
        text = text.replace(k, v)
    return text

def fix_paths(content, depth=2):
    """
    Fix relative paths based on depth.
    Original (English) has depth 2: ../../css/style.css
    Translated (Lang) has depth 3: ../../../css/style.css
    """
    if depth == 2:
        content = content.replace('href="../../', 'href="../../../')
        content = content.replace('src="../../', 'src="../../../')
    elif depth == 1: # Blog index
        content = content.replace('href="../', 'href="../../')
        content = content.replace('src="../', 'src="../../')
    return content

def add_hreflang(content, slug, lang, is_index=False):
    soup = BeautifulSoup(content, 'html.parser')
    head = soup.find('head')
    if not head: return content
    
    # Remove existing
    for link in list(soup.find_all('link', rel='alternate')):
        link.decompose()
        
    path = f"blog/{slug}/" if not is_index else "blog/"
    
    # Add new
    base = f"https://apps.utkuapps.com/{path}"
    tags = [('en', base), ('x-default', base)]
    for l in LANGUAGES:
        tags.append((l, f"https://apps.utkuapps.com/{l}/{path}"))
        
    for h, u in tags:
        link = soup.new_tag('link')
        link['rel'] = 'alternate'
        link['hreflang'] = h
        link['href'] = u
        head.append(link)
        
    return str(soup)

def main():
    print("🚀 Starting Blog Translation...")
    
    # 1. Provide list of all blog posts
    posts = [p for p in BLOG_DIR.iterdir() if p.is_dir() and (p / "index.html").exists()]
    print(f"📦 Found {len(posts)} blog posts")
    
    for lang in LANGUAGES.keys():
        print(f"\n🌍 {lang.upper()}...", flush=True)
        lang_blog_dir = BASE_DIR / lang / "blog"
        lang_blog_dir.mkdir(parents=True, exist_ok=True)
        
        # 2. Translate Blog Index
        src_index = BLOG_DIR / "index.html"
        if src_index.exists():
            content = src_index.read_text(encoding='utf-8')
            content = translate_text(content, lang)
            content = fix_paths(content, depth=1)
            content = add_hreflang(content, "", lang, is_index=True)
            
            # Correct links to posts: href="post-slug/" -> href="post-slug/" (relative stays same)
            # But wait, blog/index.html links are like href="slug/". 
            # In de/blog/index.html, href="slug/" points to de/blog/slug/. This is correct!
            
            (lang_blog_dir / "index.html").write_text(content, encoding='utf-8')
            print(f"  ✅ Blog Index")
            
        # 3. Translate Blog Posts
        for post in posts:
            slug = post.name
            src_post = post / "index.html"
            dest_dir = lang_blog_dir / slug
            dest_dir.mkdir(exist_ok=True)
            
            content = src_post.read_text(encoding='utf-8')
            
            # Translate content
            content = translate_text(content, lang)
            
            # Update HTML lang
            content = content.replace('lang="en"', f'lang="{lang}"')
            
            # Fix paths (depth 2 -> 3)
            content = fix_paths(content, depth=2)
            
            # Add Hreflang
            content = add_hreflang(content, slug, lang)
            
            (dest_dir / "index.html").write_text(content, encoding='utf-8')
            # Don't print every single one to avoid huge logs, just a progress dot
            if posts.index(post) % 10 == 0:
                print(".", end="", flush=True)

    print("\n✅ Blog translation complete!")

if __name__ == "__main__":
    main()
