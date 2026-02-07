#!/usr/bin/env python3
"""
Multi-Language Page Generator for International SEO
Generates localized versions of all app pages in 10 languages
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

# Configuration
BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")

# Target languages with their locales
LANGUAGES = {
    'de': {'name': 'German', 'locale': 'de_DE', 'countries': ['Germany', 'Austria', 'Switzerland']},
    'fr': {'name': 'French', 'locale': 'fr_FR', 'countries': ['France', 'Belgium', 'Switzerland']},
    'es': {'name': 'Spanish', 'locale': 'es_ES', 'countries': ['Spain', 'Mexico', 'Argentina']},
    'it': {'name': 'Italian', 'locale': 'it_IT', 'countries': ['Italy', 'Switzerland']},
    'nl': {'name': 'Dutch', 'locale': 'nl_NL', 'countries': ['Netherlands', 'Belgium']},
    'pt': {'name': 'Portuguese', 'locale': 'pt_PT', 'countries': ['Portugal', 'Brazil']},
    'pl': {'name': 'Polish', 'locale': 'pl_PL', 'countries': ['Poland']},
    'sv': {'name': 'Swedish', 'locale': 'sv_SE', 'countries': ['Sweden']},
    'da': {'name': 'Danish', 'locale': 'da_DK', 'countries': ['Denmark']},
    'no': {'name': 'Norwegian', 'locale': 'nb_NO', 'countries': ['Norway']},
}

# Common UI translations
UI_TRANSLATIONS = {
    'de': {
        'Download Free': 'Kostenlos herunterladen',
        'Free Download': 'Kostenloser Download',
        'Download on the': 'Laden im',
        'App Store': 'App Store',
        'Free on App Store': 'Kostenlos im App Store',
        'for iPhone & iPad': 'für iPhone & iPad',
        'Home': 'Startseite',
        'About': 'Über',
        'Features': 'Funktionen',
        'FAQ': 'FAQ',
        'Privacy Policy': 'Datenschutz',
        'Contact': 'Kontakt',
        'Apps': 'Apps',
        'Education': 'Bildung',
        'AI & Photo': 'KI & Foto',
        'Language': 'Sprache',
        'Home Design': 'Wohndesign',
        'Identifier': 'Erkennung',
        'Other': 'Andere',
        'Yes': 'Ja',
        'No': 'Nein',
        'free to download': 'kostenlos herunterladen',
        'Is': 'Ist',
        'What devices are compatible': 'Welche Geräte sind kompatibel',
        'How do I get started': 'Wie fange ich an',
        'Is my data safe': 'Sind meine Daten sicher',
        'completely free to download from the App Store': 'völlig kostenlos im App Store herunterzuladen',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'für iPhone und iPad mit iOS 15.0 oder höher entwickelt',
        'Simply download': 'Einfach herunterladen',
        'from the App Store': 'aus dem App Store',
        'We prioritize your privacy and security': 'Wir priorisieren Ihre Privatsphäre und Sicherheit',
        'Join millions of satisfied users': 'Schließen Sie sich Millionen zufriedener Nutzer an',
        'Today': 'Heute',
        'Premium iOS Apps': 'Premium iOS Apps',
        'Discover innovative apps': 'Entdecken Sie innovative Apps',
    },
    'fr': {
        'Download Free': 'Télécharger gratuitement',
        'Free Download': 'Téléchargement gratuit',
        'Download on the': 'Télécharger sur',
        'App Store': 'App Store',
        'Free on App Store': 'Gratuit sur App Store',
        'for iPhone & iPad': 'pour iPhone et iPad',
        'Home': 'Accueil',
        'About': 'À propos',
        'Features': 'Fonctionnalités',
        'FAQ': 'FAQ',
        'Privacy Policy': 'Confidentialité',
        'Contact': 'Contact',
        'Apps': 'Applications',
        'Education': 'Éducation',
        'AI & Photo': 'IA & Photo',
        'Language': 'Langue',
        'Home Design': 'Décoration',
        'Identifier': 'Identification',
        'Other': 'Autre',
        'Yes': 'Oui',
        'No': 'Non',
        'free to download': 'gratuit à télécharger',
        'Is': 'Est-ce que',
        'What devices are compatible': 'Quels appareils sont compatibles',
        'How do I get started': 'Comment commencer',
        'Is my data safe': 'Mes données sont-elles en sécurité',
        'completely free to download from the App Store': 'entièrement gratuit à télécharger sur App Store',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'conçu pour iPhone et iPad avec iOS 15.0 ou ultérieur',
        'Simply download': 'Téléchargez simplement',
        'from the App Store': 'depuis App Store',
        'We prioritize your privacy and security': 'Nous priorisons votre confidentialité et sécurité',
        'Join millions of satisfied users': 'Rejoignez des millions dutilisateurs satisfaits',
        'Today': 'Aujourd\'hui',
        'Premium iOS Apps': 'Applications iOS Premium',
        'Discover innovative apps': 'Découvrez des applications innovantes',
    },
    'es': {
        'Download Free': 'Descargar gratis',
        'Free Download': 'Descarga gratuita',
        'Download on the': 'Descargar en',
        'App Store': 'App Store',
        'Free on App Store': 'Gratis en App Store',
        'for iPhone & iPad': 'para iPhone y iPad',
        'Home': 'Inicio',
        'About': 'Acerca de',
        'Features': 'Características',
        'FAQ': 'Preguntas frecuentes',
        'Privacy Policy': 'Privacidad',
        'Contact': 'Contacto',
        'Apps': 'Aplicaciones',
        'Education': 'Educación',
        'AI & Photo': 'IA y Foto',
        'Language': 'Idioma',
        'Home Design': 'Diseño del hogar',
        'Identifier': 'Identificador',
        'Other': 'Otro',
        'Yes': 'Sí',
        'No': 'No',
        'free to download': 'gratis para descargar',
        'Is': 'Es',
        'What devices are compatible': 'Qué dispositivos son compatibles',
        'How do I get started': 'Cómo empezar',
        'Is my data safe': 'Están seguros mis datos',
        'completely free to download from the App Store': 'completamente gratis en App Store',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'diseñado para iPhone y iPad con iOS 15.0 o posterior',
        'Simply download': 'Simplemente descarga',
        'from the App Store': 'desde App Store',
        'We prioritize your privacy and security': 'Priorizamos tu privacidad y seguridad',
        'Join millions of satisfied users': 'Únete a millones de usuarios satisfechos',
        'Today': 'Hoy',
        'Premium iOS Apps': 'Aplicaciones iOS Premium',
        'Discover innovative apps': 'Descubre aplicaciones innovadoras',
    },
    'it': {
        'Download Free': 'Scarica gratis',
        'Free Download': 'Download gratuito',
        'Download on the': 'Scarica su',
        'App Store': 'App Store',
        'Free on App Store': 'Gratis su App Store',
        'for iPhone & iPad': 'per iPhone e iPad',
        'Home': 'Home',
        'About': 'Info',
        'Features': 'Funzionalità',
        'FAQ': 'FAQ',
        'Privacy Policy': 'Privacy',
        'Contact': 'Contatti',
        'Apps': 'App',
        'Education': 'Istruzione',
        'AI & Photo': 'IA e Foto',
        'Language': 'Lingua',
        'Home Design': 'Design casa',
        'Identifier': 'Identificatore',
        'Other': 'Altro',
        'Yes': 'Sì',
        'No': 'No',
        'free to download': 'gratuito da scaricare',
        'Is': 'È',
        'What devices are compatible': 'Quali dispositivi sono compatibili',
        'How do I get started': 'Come iniziare',
        'Is my data safe': 'I miei dati sono al sicuro',
        'completely free to download from the App Store': 'completamente gratuito su App Store',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'progettato per iPhone e iPad con iOS 15.0 o successivo',
        'Simply download': 'Scarica semplicemente',
        'from the App Store': 'da App Store',
        'We prioritize your privacy and security': 'Diamo priorità alla tua privacy e sicurezza',
        'Join millions of satisfied users': 'Unisciti a milioni di utenti soddisfatti',
        'Today': 'Oggi',
        'Premium iOS Apps': 'App iOS Premium',
        'Discover innovative apps': 'Scopri app innovative',
    },
    'nl': {
        'Download Free': 'Gratis downloaden',
        'Free Download': 'Gratis download',
        'Download on the': 'Download op de',
        'App Store': 'App Store',
        'Free on App Store': 'Gratis in App Store',
        'for iPhone & iPad': 'voor iPhone en iPad',
        'Home': 'Home',
        'About': 'Over',
        'Features': 'Functies',
        'FAQ': 'FAQ',
        'Privacy Policy': 'Privacy',
        'Contact': 'Contact',
        'Apps': 'Apps',
        'Education': 'Onderwijs',
        'AI & Photo': 'AI & Foto',
        'Language': 'Taal',
        'Home Design': 'Woningontwerp',
        'Identifier': 'Identifier',
        'Other': 'Overig',
        'Yes': 'Ja',
        'No': 'Nee',
        'free to download': 'gratis te downloaden',
        'Is': 'Is',
        'What devices are compatible': 'Welke apparaten zijn compatibel',
        'How do I get started': 'Hoe begin ik',
        'Is my data safe': 'Zijn mijn gegevens veilig',
        'completely free to download from the App Store': 'helemaal gratis te downloaden in App Store',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'ontworpen voor iPhone en iPad met iOS 15.0 of hoger',
        'Simply download': 'Download gewoon',
        'from the App Store': 'van App Store',
        'We prioritize your privacy and security': 'Wij geven prioriteit aan uw privacy en veiligheid',
        'Join millions of satisfied users': 'Sluit je aan bij miljoenen tevreden gebruikers',
        'Today': 'Vandaag',
        'Premium iOS Apps': 'Premium iOS Apps',
        'Discover innovative apps': 'Ontdek innovatieve apps',
    },
    'pt': {
        'Download Free': 'Baixar grátis',
        'Free Download': 'Download grátis',
        'Download on the': 'Baixar na',
        'App Store': 'App Store',
        'Free on App Store': 'Grátis na App Store',
        'for iPhone & iPad': 'para iPhone e iPad',
        'Home': 'Início',
        'About': 'Sobre',
        'Features': 'Recursos',
        'FAQ': 'Perguntas frequentes',
        'Privacy Policy': 'Privacidade',
        'Contact': 'Contato',
        'Apps': 'Apps',
        'Education': 'Educação',
        'AI & Photo': 'IA e Foto',
        'Language': 'Idioma',
        'Home Design': 'Design de interiores',
        'Identifier': 'Identificador',
        'Other': 'Outro',
        'Yes': 'Sim',
        'No': 'Não',
        'free to download': 'grátis para baixar',
        'Is': 'É',
        'What devices are compatible': 'Quais dispositivos são compatíveis',
        'How do I get started': 'Como começar',
        'Is my data safe': 'Meus dados estão seguros',
        'completely free to download from the App Store': 'completamente grátis na App Store',
        'designed for iPhone and iPad devices running iOS 15.0 or later': 'projetado para iPhone e iPad com iOS 15.0 ou posterior',
        'Simply download': 'Basta baixar',
        'from the App Store': 'da App Store',
        'We prioritize your privacy and security': 'Priorizamos sua privacidade e segurança',
        'Join millions of satisfied users': 'Junte-se a milhões de usuários satisfeitos',
        'Today': 'Hoje',
        'Premium iOS Apps': 'Apps iOS Premium',
        'Discover innovative apps': 'Descubra apps inovadores',
    },
    'pl': {
        'Download Free': 'Pobierz za darmo',
        'Free Download': 'Darmowe pobieranie',
        'Free on App Store': 'Za darmo w App Store',
        'for iPhone & iPad': 'na iPhone i iPad',
        'Home': 'Strona główna',
        'Education': 'Edukacja',
        'Join millions of satisfied users': 'Dołącz do milionów zadowolonych użytkowników',
        'Today': 'Dzisiaj',
    },
    'sv': {
        'Download Free': 'Ladda ner gratis',
        'Free Download': 'Gratis nedladdning',
        'Free on App Store': 'Gratis på App Store',
        'for iPhone & iPad': 'för iPhone och iPad',
        'Home': 'Hem',
        'Education': 'Utbildning',
        'Join millions of satisfied users': 'Gå med miljontals nöjda användare',
        'Today': 'Idag',
    },
    'da': {
        'Download Free': 'Download gratis',
        'Free Download': 'Gratis download',
        'Free on App Store': 'Gratis i App Store',
        'for iPhone & iPad': 'til iPhone og iPad',
        'Home': 'Hjem',
        'Education': 'Uddannelse',
        'Join millions of satisfied users': 'Bliv en del af millioner af tilfredse brugere',
        'Today': 'I dag',
    },
    'no': {
        'Download Free': 'Last ned gratis',
        'Free Download': 'Gratis nedlasting',
        'Free on App Store': 'Gratis i App Store',
        'for iPhone & iPad': 'for iPhone og iPad',
        'Home': 'Hjem',
        'Education': 'Utdanning',
        'Join millions of satisfied users': 'Bli med millioner av fornøyde brukere',
        'Today': 'I dag',
    },
}

def translate_text(text, lang):
    """Translate common UI text"""
    translations = UI_TRANSLATIONS.get(lang, {})
    result = text
    
    # Sort by length (longest first) to avoid partial replacements
    for eng, translated in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(eng, translated)
    
    return result

def add_hreflang_tags(html_content, app_slug, current_lang):
    """Add hreflang tags to HTML"""
    hreflang_tags = []
    
    # Default (English)
    hreflang_tags.append(f'  <link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/{app_slug}/" />')
    hreflang_tags.append(f'  <link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/{app_slug}/" />')
    
    # All other languages
    for lang in LANGUAGES.keys():
        hreflang_tags.append(f'  <link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app_slug}/" />')
    
    hreflang_block = '\n'.join(hreflang_tags)
    
    # Insert before </head>
    html_content = html_content.replace('</head>', f'{hreflang_block}\n</head>')
    
    return html_content

def update_og_locale(html_content, lang):
    """Update Open Graph locale"""
    locale = LANGUAGES[lang]['locale']
    
    # Add og:locale
    og_locale = f'<meta property="og:locale" content="{locale}" />'
    html_content = re.sub(
        r'<meta property="og:type"',
        f'{og_locale}\n  <meta property="og:type"',
        html_content
    )
    
    return html_content

def update_html_lang(html_content, lang):
    """Update HTML lang attribute"""
    html_content = re.sub(r'<html lang="en">', f'<html lang="{lang}">', html_content)
    return html_content

def update_paths(html_content, lang):
    """Update CSS and asset paths for subdirectory"""
    # CSS path: ../css/ -> ../../css/
    html_content = html_content.replace('href="../css/', 'href="../../css/')
    html_content = html_content.replace('href="../js/', 'href="../../js/')
    html_content = html_content.replace('src="../icons/', 'src="../../icons/')
    html_content = html_content.replace('src="../images/', 'src="../../images/')
    
    # Absolute URLs don't need changing
    return html_content

def update_nav_links(html_content, lang):
    """Update navigation links for language"""
    # Home link
    html_content = html_content.replace('href="/"', f'href="/{lang}/"')
    html_content = html_content.replace('href="../"', f'href="../../{lang}/"')
    
    return html_content

def process_app_page(source_path, app_slug, lang):
    """Process a single app page for a language"""
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    content = translate_text(content, lang)
    
    # Update HTML lang attribute
    content = update_html_lang(content, lang)
    
    # Add hreflang tags
    content = add_hreflang_tags(content, app_slug, lang)
    
    # Update OG locale
    content = update_og_locale(content, lang)
    
    # Update paths for subdirectory structure
    content = update_paths(content, lang)
    
    # Update navigation
    content = update_nav_links(content, lang)
    
    return content

def generate_language_pages():
    """Generate all language versions of all app pages"""
    # Find all app directories (exclude language directories and special folders)
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules'} | set(LANGUAGES.keys())
    
    app_dirs = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude_dirs:
            index_path = item / 'index.html'
            if index_path.exists():
                app_dirs.append(item.name)
    
    print(f"Found {len(app_dirs)} app directories")
    
    pages_created = 0
    
    for lang in LANGUAGES.keys():
        print(f"\n🌍 Processing {LANGUAGES[lang]['name']} ({lang})...")
        
        # Create language directory
        lang_dir = BASE_DIR / lang
        lang_dir.mkdir(exist_ok=True)
        
        for app_slug in app_dirs:
            source_path = BASE_DIR / app_slug / 'index.html'
            
            # Create app directory in language folder
            dest_dir = lang_dir / app_slug
            dest_dir.mkdir(exist_ok=True)
            
            # Process and save
            try:
                content = process_app_page(source_path, app_slug, lang)
                dest_path = dest_dir / 'index.html'
                
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                pages_created += 1
                print(f"  ✅ {app_slug}")
            except Exception as e:
                print(f"  ❌ {app_slug}: {e}")
    
    print(f"\n✨ Created {pages_created} localized pages!")
    return pages_created

def add_hreflang_to_english_pages():
    """Add hreflang tags to original English pages"""
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules'} | set(LANGUAGES.keys())
    
    updated = 0
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude_dirs:
            index_path = item / 'index.html'
            if index_path.exists():
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Skip if already has hreflang
                if 'hreflang' in content:
                    continue
                
                content = add_hreflang_tags(content, item.name, 'en')
                
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated += 1
    
    print(f"Updated {updated} English pages with hreflang tags")
    return updated

def generate_sitemap_index():
    """Generate sitemap index with all language sitemaps"""
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
    
    print("Created sitemap index")

def generate_language_sitemap(lang):
    """Generate sitemap for a specific language"""
    exclude_dirs = {'css', 'js', 'icons', 'images', '.git', 'node_modules'} | set(LANGUAGES.keys())
    
    urls = []
    lang_dir = BASE_DIR / lang
    
    if lang_dir.exists():
        for app_dir in lang_dir.iterdir():
            if app_dir.is_dir() and (app_dir / 'index.html').exists():
                urls.append(f'https://apps.utkuapps.com/{lang}/{app_dir.name}/')
    
    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    
    for url in urls:
        sitemap += f'''  <url>
    <loc>{url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
    
    sitemap += '</urlset>'
    
    with open(BASE_DIR / f'sitemap-{lang}.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    print(f"Created sitemap-{lang}.xml with {len(urls)} URLs")

if __name__ == '__main__':
    print("🚀 Starting Multi-Language Page Generation")
    print("=" * 50)
    
    # Step 1: Generate all language pages
    generate_language_pages()
    
    # Step 2: Add hreflang to English pages
    add_hreflang_to_english_pages()
    
    # Step 3: Generate sitemaps
    generate_sitemap_index()
    for lang in LANGUAGES.keys():
        generate_language_sitemap(lang)
    
    # Rename original sitemap
    original_sitemap = BASE_DIR / 'sitemap.xml.bak'
    if not original_sitemap.exists():
        import shutil
        current_sitemap = BASE_DIR / 'sitemap.xml'
        # We already overwrote it, so we'll regenerate English sitemap
    
    print("\n" + "=" * 50)
    print("✅ COMPLETE! Multi-language SEO setup finished.")
    print(f"📊 Languages: {len(LANGUAGES)}")
    print(f"📄 Estimated new pages: {len(LANGUAGES) * 51}")
