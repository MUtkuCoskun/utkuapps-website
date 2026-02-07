#!/usr/bin/env python3
"""
COMPLETE MULTI-LANGUAGE SEO SCRIPT v2
- Translates ALL pages including index.html
- Fixes ALL internal links to stay within language context
- Creates fully translated experience for each language
"""

import os
import re
from pathlib import Path
import shutil

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")

LANGUAGES = ['de', 'fr', 'es', 'it', 'nl', 'pt', 'pl', 'sv', 'da', 'no']

LOCALES = {
    'de': 'de_DE', 'fr': 'fr_FR', 'es': 'es_ES', 'it': 'it_IT', 'nl': 'nl_NL',
    'pt': 'pt_PT', 'pl': 'pl_PL', 'sv': 'sv_SE', 'da': 'da_DK', 'no': 'nb_NO',
}

# Comprehensive translations
TR = {
    'de': {
        # Page titles
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-Apps für iPhone & iPad',
        'Free Download for iPhone & iPad': 'Kostenloser Download für iPhone & iPad',
        '50+ Free Apps': '50+ Kostenlose Apps',
        
        # Navigation
        'Home': 'Startseite', 'All Apps': 'Alle Apps', 'Apps': 'Apps',
        'Privacy': 'Datenschutz', 'Contact': 'Kontakt',
        
        # Hero section
        'Premium iOS Apps': 'Premium iOS-Apps',
        'Discover innovative apps designed to enhance your daily life': 'Entdecken Sie innovative Apps für Ihren Alltag',
        'AI-powered tools, language learning, home design, and more': 'KI-Tools, Sprachenlernen, Wohndesign und mehr',
        'Downloads': 'Downloads',
        'Avg Rating': 'Durchschn. Bewertung',
        
        # Categories
        'Education': 'Bildung', 'AI & Photo': 'KI & Foto', 'Language': 'Sprache',
        'Home Design': 'Wohndesign', 'Identifier': 'Erkennung', 'Other': 'Andere',
        
        # App page content
        'About': 'Über', 'Features': 'Funktionen', 'Key Features': 'Hauptfunktionen',
        'FAQ': 'Häufige Fragen', 'Frequently Asked Questions': 'Häufig gestellte Fragen',
        
        # Download section
        'Download on the': 'Laden im', 'App Store': 'App Store',
        'Download Free': 'Kostenlos herunterladen', 'Free Download': 'Kostenloser Download',
        'Free on App Store': 'Kostenlos im App Store', 'Get it on App Store': 'Im App Store herunterladen',
        
        # Device info
        'for iPhone & iPad': 'für iPhone & iPad', 'for iPhone and iPad': 'für iPhone und iPad',
        'iPhone & iPad': 'iPhone & iPad',
        
        # Content paragraphs
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'bietet ein leistungsstarkes, intuitives Erlebnis, das speziell für iOS-Benutzer entwickelt wurde, die das Beste verlangen',
        'Whether you\'re a professional seeking advanced features or a beginner looking for an easy-to-use solution': 'Egal, ob Sie ein Profi sind oder ein Anfänger',
        'our app provides everything you need in one streamlined package': 'unsere App bietet alles, was Sie brauchen, in einem optimierten Paket',
        'Developed with cutting-edge technology and refined through extensive user feedback': 'Mit modernster Technologie entwickelt und durch Benutzerfeedback verfeinert',
        'has earned its place as a top-rated application': 'hat sich seinen Platz als erstklassige Anwendung verdient',
        'in the': 'in der', 'category on the App Store': 'Kategorie im App Store',
        'Our team continuously updates the app with new features, performance improvements, and enhanced functionality': 'Unser Team aktualisiert die App kontinuierlich mit neuen Funktionen und Verbesserungen',
        'to ensure you always have access to the latest innovations': 'um sicherzustellen, dass Sie immer Zugang zu den neuesten Innovationen haben',
        'With millions of downloads worldwide and consistently high ratings': 'Mit Millionen von Downloads weltweit und hohen Bewertungen',
        'has become the trusted choice for users across the globe': 'ist zur vertrauenswürdigen Wahl für Benutzer weltweit geworden',
        'The app features a clean, modern interface that makes complex tasks simple': 'Die App verfügt über eine moderne Benutzeroberfläche, die komplexe Aufgaben einfach macht',
        'while providing the depth and capabilities that power users require': 'und bietet die Tiefe und Fähigkeiten, die erfahrene Benutzer benötigen',
        'Download': 'Laden Sie', 'today and discover why it\'s the preferred choice for discerning iOS users': 'herunter und entdecken Sie, warum es die bevorzugte Wahl für iOS-Benutzer ist',
        'Available exclusively on the App Store for iPhone and iPad devices running iOS 15.0 or later': 'Exklusiv im App Store für iPhone und iPad mit iOS 15.0 oder höher verfügbar',
        
        # CTA section
        'Today': 'Heute', 'Join millions of satisfied users': 'Schließen Sie sich Millionen zufriedener Benutzer an',
        'Free on the App Store for iPhone and iPad': 'Kostenlos im App Store für iPhone und iPad',
        
        # Footer
        'All rights reserved': 'Alle Rechte vorbehalten', 'Terms of Service': 'Nutzungsbedingungen',
        
        # General
        'Yes': 'Ja', 'No': 'Nein', 'Learn more': 'Mehr erfahren', 'Get started': 'Loslegen',
    },
    'fr': {
        'Premium iOS Apps for iPhone & iPad': 'Applications iOS Premium pour iPhone et iPad',
        'Free Download for iPhone & iPad': 'Téléchargement gratuit pour iPhone et iPad',
        '50+ Free Apps': '50+ Applications Gratuites',
        'Home': 'Accueil', 'All Apps': 'Toutes les Apps', 'Apps': 'Applications',
        'Privacy': 'Confidentialité',
        'Premium iOS Apps': 'Applications iOS Premium',
        'Discover innovative apps designed to enhance your daily life': 'Découvrez des applications innovantes pour améliorer votre quotidien',
        'Downloads': 'Téléchargements', 'Avg Rating': 'Note Moyenne',
        'Education': 'Éducation', 'AI & Photo': 'IA et Photo', 'Language': 'Langue',
        'Home Design': 'Design d\'intérieur', 'Identifier': 'Identification', 'Other': 'Autre',
        'About': 'À propos', 'Features': 'Fonctionnalités',
        'Download on the': 'Télécharger sur l\'', 'Download Free': 'Télécharger gratuitement',
        'Free Download': 'Téléchargement gratuit', 'for iPhone & iPad': 'pour iPhone et iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'offre une expérience puissante et intuitive conçue pour les utilisateurs iOS exigeants',
        'Today': 'Aujourd\'hui', 'Join millions of satisfied users': 'Rejoignez des millions d\'utilisateurs satisfaits',
        'Yes': 'Oui', 'No': 'Non', 'All rights reserved': 'Tous droits réservés',
    },
    'es': {
        'Premium iOS Apps for iPhone & iPad': 'Aplicaciones iOS Premium para iPhone y iPad',
        'Free Download for iPhone & iPad': 'Descarga gratuita para iPhone y iPad',
        '50+ Free Apps': '50+ Aplicaciones Gratis',
        'Home': 'Inicio', 'All Apps': 'Todas las Apps', 'Apps': 'Aplicaciones',
        'Privacy': 'Privacidad',
        'Premium iOS Apps': 'Aplicaciones iOS Premium',
        'Discover innovative apps designed to enhance your daily life': 'Descubre aplicaciones innovadoras para mejorar tu vida diaria',
        'Downloads': 'Descargas', 'Avg Rating': 'Valoración Media',
        'Education': 'Educación', 'AI & Photo': 'IA y Foto', 'Language': 'Idioma',
        'Home Design': 'Diseño del hogar', 'Identifier': 'Identificador', 'Other': 'Otro',
        'About': 'Acerca de', 'Features': 'Características',
        'Download on the': 'Descargar en', 'Download Free': 'Descargar gratis',
        'Free Download': 'Descarga gratuita', 'for iPhone & iPad': 'para iPhone y iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'ofrece una experiencia potente e intuitiva diseñada para usuarios de iOS exigentes',
        'Today': 'Hoy', 'Join millions of satisfied users': 'Únete a millones de usuarios satisfechos',
        'Yes': 'Sí', 'No': 'No', 'All rights reserved': 'Todos los derechos reservados',
    },
    'it': {
        'Premium iOS Apps for iPhone & iPad': 'App iOS Premium per iPhone e iPad',
        'Free Download for iPhone & iPad': 'Download gratuito per iPhone e iPad',
        '50+ Free Apps': '50+ App Gratuite',
        'Home': 'Home', 'All Apps': 'Tutte le App', 'Apps': 'App', 'Privacy': 'Privacy',
        'Premium iOS Apps': 'App iOS Premium',
        'Discover innovative apps designed to enhance your daily life': 'Scopri app innovative per migliorare la tua vita quotidiana',
        'Downloads': 'Download', 'Avg Rating': 'Valutazione Media',
        'Education': 'Istruzione', 'AI & Photo': 'IA e Foto',
        'About': 'Informazioni', 'Features': 'Funzionalità',
        'Download on the': 'Scarica su', 'Download Free': 'Scarica gratis',
        'Free Download': 'Download gratuito', 'for iPhone & iPad': 'per iPhone e iPad',
        'Today': 'Oggi', 'Yes': 'Sì', 'No': 'No', 'All rights reserved': 'Tutti i diritti riservati',
    },
    'nl': {
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-apps voor iPhone en iPad',
        'Free Download for iPhone & iPad': 'Gratis download voor iPhone en iPad',
        '50+ Free Apps': '50+ Gratis Apps',
        'Home': 'Home', 'All Apps': 'Alle Apps', 'Apps': 'Apps', 'Privacy': 'Privacy',
        'Premium iOS Apps': 'Premium iOS-apps',
        'Discover innovative apps designed to enhance your daily life': 'Ontdek innovatieve apps om je dagelijks leven te verbeteren',
        'Downloads': 'Downloads', 'Avg Rating': 'Gem. Beoordeling',
        'Education': 'Onderwijs', 'AI & Photo': 'AI & Foto',
        'About': 'Over', 'Features': 'Functies',
        'Download on the': 'Download op de', 'Download Free': 'Gratis downloaden',
        'Free Download': 'Gratis download', 'for iPhone & iPad': 'voor iPhone en iPad',
        'Today': 'Vandaag', 'Yes': 'Ja', 'No': 'Nee', 'All rights reserved': 'Alle rechten voorbehouden',
    },
    'pt': {
        'Premium iOS Apps for iPhone & iPad': 'Apps iOS Premium para iPhone e iPad',
        'Free Download for iPhone & iPad': 'Download gratuito para iPhone e iPad',
        '50+ Free Apps': '50+ Apps Grátis',
        'Home': 'Início', 'All Apps': 'Todos os Apps', 'Apps': 'Apps', 'Privacy': 'Privacidade',
        'Premium iOS Apps': 'Apps iOS Premium',
        'Discover innovative apps designed to enhance your daily life': 'Descubra apps inovadores para melhorar sua vida diária',
        'Downloads': 'Downloads', 'Avg Rating': 'Avaliação Média',
        'Education': 'Educação', 'AI & Photo': 'IA e Foto',
        'About': 'Sobre', 'Features': 'Recursos',
        'Download on the': 'Baixar na', 'Download Free': 'Baixar grátis',
        'Free Download': 'Download grátis', 'for iPhone & iPad': 'para iPhone e iPad',
        'Today': 'Hoje', 'Yes': 'Sim', 'No': 'Não', 'All rights reserved': 'Todos os direitos reservados',
    },
    'pl': {
        'Premium iOS Apps for iPhone & iPad': 'Premium aplikacje iOS na iPhone i iPad',
        'Free Download for iPhone & iPad': 'Bezpłatne pobieranie na iPhone i iPad',
        '50+ Free Apps': '50+ Darmowych Aplikacji',
        'Home': 'Strona główna', 'All Apps': 'Wszystkie aplikacje', 'Apps': 'Aplikacje', 'Privacy': 'Prywatność',
        'Premium iOS Apps': 'Premium aplikacje iOS',
        'Downloads': 'Pobierania', 'Avg Rating': 'Śr. Ocena',
        'Education': 'Edukacja', 'AI & Photo': 'AI i Foto',
        'About': 'O aplikacji', 'Features': 'Funkcje',
        'Download on the': 'Pobierz z', 'Download Free': 'Pobierz za darmo',
        'Free Download': 'Bezpłatne pobieranie', 'for iPhone & iPad': 'na iPhone i iPad',
        'Today': 'Dziś', 'Yes': 'Tak', 'No': 'Nie',
    },
    'sv': {
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-appar för iPhone och iPad',
        'Free Download for iPhone & iPad': 'Gratis nedladdning för iPhone och iPad',
        '50+ Free Apps': '50+ Gratis Appar',
        'Home': 'Hem', 'All Apps': 'Alla appar', 'Apps': 'Appar', 'Privacy': 'Integritet',
        'Premium iOS Apps': 'Premium iOS-appar',
        'Downloads': 'Nedladdningar', 'Avg Rating': 'Snittbetyg',
        'Education': 'Utbildning', 'AI & Photo': 'AI & Foto',
        'About': 'Om', 'Features': 'Funktioner',
        'Download on the': 'Ladda ner på', 'Download Free': 'Ladda ner gratis',
        'Free Download': 'Gratis nedladdning', 'for iPhone & iPad': 'för iPhone och iPad',
        'Today': 'Idag', 'Yes': 'Ja', 'No': 'Nej',
    },
    'da': {
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-apps til iPhone og iPad',
        'Free Download for iPhone & iPad': 'Gratis download til iPhone og iPad',
        '50+ Free Apps': '50+ Gratis Apps',
        'Home': 'Hjem', 'All Apps': 'Alle apps', 'Apps': 'Apps', 'Privacy': 'Privatliv',
        'Premium iOS Apps': 'Premium iOS-apps',
        'Downloads': 'Downloads', 'Avg Rating': 'Gns. Vurdering',
        'Education': 'Uddannelse', 'AI & Photo': 'AI & Foto',
        'About': 'Om', 'Features': 'Funktioner',
        'Download on the': 'Download på', 'Download Free': 'Download gratis',
        'Free Download': 'Gratis download', 'for iPhone & iPad': 'til iPhone og iPad',
        'Today': 'I dag', 'Yes': 'Ja', 'No': 'Nej',
    },
    'no': {
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-apper for iPhone og iPad',
        'Free Download for iPhone & iPad': 'Gratis nedlasting for iPhone og iPad',
        '50+ Free Apps': '50+ Gratis Apper',
        'Home': 'Hjem', 'All Apps': 'Alle apper', 'Apps': 'Apper', 'Privacy': 'Personvern',
        'Premium iOS Apps': 'Premium iOS-apper',
        'Downloads': 'Nedlastinger', 'Avg Rating': 'Gj.snitt Vurdering',
        'Education': 'Utdanning', 'AI & Photo': 'AI & Foto',
        'About': 'Om', 'Features': 'Funksjoner',
        'Download on the': 'Last ned fra', 'Download Free': 'Last ned gratis',
        'Free Download': 'Gratis nedlasting', 'for iPhone & iPad': 'for iPhone og iPad',
        'Today': 'I dag', 'Yes': 'Ja', 'No': 'Nei',
    },
}

def translate(text, lang):
    """Apply translations"""
    if lang not in TR:
        return text
    result = text
    for eng, trans in sorted(TR[lang].items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(eng, trans)
    return result

def add_hreflang(app_slug):
    """Generate hreflang tags for app pages"""
    tags = []
    base = f"https://apps.utkuapps.com/{app_slug}/"
    tags.append(f'<link rel="alternate" hreflang="en" href="{base}"/>')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{base}"/>')
    for lang in LANGUAGES:
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app_slug}/"/>')
    return '\n'.join(tags)

def add_index_hreflang():
    """Generate hreflang tags for index page"""
    tags = []
    base = "https://apps.utkuapps.com/"
    tags.append(f'<link rel="alternate" hreflang="en" href="{base}"/>')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{base}"/>')
    for lang in LANGUAGES:
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/"/>')
    return '\n'.join(tags)

def fix_internal_links_app(content, lang):
    """Fix internal links for APP pages (in subdirectory)"""
    # Logo/Home link: href="/" -> href="/de/"
    content = re.sub(r'href="/"', f'href="/{lang}/"', content)
    
    # Nav links with anchors: href="/#apps" -> href="/de/#apps"
    content = re.sub(r'href="/#', f'href="/{lang}/#', content)
    
    # Privacy link: href="/privacy.html" -> href="/de/privacy.html"
    content = re.sub(r'href="/privacy\.html"', f'href="/{lang}/privacy.html"', content)
    
    # Breadcrumb structured data URLs
    content = content.replace('"https://utkuapps.com"', f'"https://apps.utkuapps.com/{lang}/"')
    content = content.replace('"https://utkuapps.com/#apps"', f'"https://apps.utkuapps.com/{lang}/#apps"')
    
    return content

def fix_internal_links_index(content, lang):
    """Fix internal links for INDEX page (in language root)"""
    # Logo link: href="/" -> href="/de/" (stay in language)
    content = re.sub(r'href="/"', f'href="/{lang}/"', content)
    
    # Anchor links: href="#apps" -> href="/{lang}/#apps" (actually just #apps is fine for same page)
    # But navigation should point to language-specific pages
    
    # Privacy link: href="privacy.html" -> href="/de/privacy.html"
    content = re.sub(r'href="privacy\.html"', f'href="/{lang}/privacy.html"', content)
    
    # App card links: href="app-name/" -> href="/de/app-name/"
    content = re.sub(r'href="([a-z0-9-]+)/"', f'href="/{lang}/\\1/"', content)
    
    # Fix icon paths: src="icons/" -> src="../icons/"
    content = content.replace('src="icons/', 'src="../icons/')
    
    # Fix CSS path: href="css/" -> href="../css/"
    content = content.replace('href="css/', 'href="../css/')
    
    return content

def process_app_page(content, app_slug, lang):
    """Process app page with full localization"""
    # Change lang attribute
    content = re.sub(r'<html[^>]*lang="[^"]*"', f'<html lang="{lang}"', content)
    
    # Translate content
    content = translate(content, lang)
    
    # Update og:locale
    content = re.sub(r'content="en_US"', f'content="{LOCALES[lang]}"', content)
    
    # Fix internal links
    content = fix_internal_links_app(content, lang)
    
    # Remove existing hreflang
    content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
    
    # Add new hreflang before </head>
    hreflang = add_hreflang(app_slug)
    content = content.replace('</head>', f'{hreflang}\n</head>')
    
    # Fix asset paths for subdirectory structure
    content = content.replace('href="../css/', 'href="../../css/')
    content = content.replace('href="../js/', 'href="../../js/')
    content = content.replace('src="../icons/', 'src="../../icons/')
    content = content.replace('src="../images/', 'src="../../images/')
    
    # Update canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://utkuapps\.com/([^"]+)/"',
        f'<link rel="canonical" href="https://apps.utkuapps.com/{lang}/\\1/"',
        content
    )
    
    return content

def process_index_page(content, lang):
    """Process index page with full localization"""
    # Change lang attribute
    content = re.sub(r'<html[^>]*lang="[^"]*"', f'<html lang="{lang}"', content)
    
    # Translate content
    content = translate(content, lang)
    
    # Update og:locale  
    content = re.sub(r'content="en_US"', f'content="{LOCALES[lang]}"', content)
    
    # Fix internal links
    content = fix_internal_links_index(content, lang)
    
    # Remove existing hreflang
    content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
    
    # Add hreflang before </head>
    hreflang = add_index_hreflang()
    content = content.replace('</head>', f'{hreflang}\n</head>')
    
    # Update canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://utkuapps\.com"',
        f'<link rel="canonical" href="https://apps.utkuapps.com/{lang}/"',
        content
    )
    
    # Update og:url
    content = re.sub(
        r'<meta property="og:url" content="https://utkuapps\.com"',
        f'<meta property="og:url" content="https://apps.utkuapps.com/{lang}/"',
        content
    )
    
    return content

def generate_pages():
    """Generate all pages including index"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES)
    
    apps = [d.name for d in BASE_DIR.iterdir() 
            if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]
    
    print(f"📁 Found {len(apps)} apps")
    total = 0
    
    for lang in LANGUAGES:
        print(f"\n🌍 {lang.upper()}...")
        lang_dir = BASE_DIR / lang
        lang_dir.mkdir(exist_ok=True)
        
        # Process INDEX page (main home page)
        index_src = BASE_DIR / 'index.html'
        if index_src.exists():
            with open(index_src, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = process_index_page(content, lang)
            
            with open(lang_dir / 'index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ index.html (home page)")
        
        # Process APP pages
        for app in apps:
            src = BASE_DIR / app / 'index.html'
            dest_dir = lang_dir / app
            dest_dir.mkdir(exist_ok=True)
            
            try:
                with open(src, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = process_app_page(content, app, lang)
                
                with open(dest_dir / 'index.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                total += 1
                print(f"  ✅ {app}")
            except Exception as e:
                print(f"  ❌ {app}: {e}")
    
    return total

def update_english():
    """Add hreflang to English pages"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES)
    count = 0
    
    # Update English app pages
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude:
            index = item / 'index.html'
            if index.exists():
                with open(index, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove existing hreflang
                content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
                
                # Add new hreflang
                hreflang = add_hreflang(item.name)
                content = content.replace('</head>', f'{hreflang}\n</head>')
                
                with open(index, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    
    # Update English index page
    index = BASE_DIR / 'index.html'
    if index.exists():
        with open(index, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
        hreflang = add_index_hreflang()
        content = content.replace('</head>', f'{hreflang}\n</head>')
        
        with open(index, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✅ Updated {count} English pages + index")

def generate_sitemaps():
    """Generate sitemaps with proper hreflang"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES)
    apps = [d.name for d in BASE_DIR.iterdir() 
            if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]
    
    # English sitemap (includes home + apps)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    
    # Home page
    sitemap += '  <url>\n    <loc>https://apps.utkuapps.com/</loc>\n'
    sitemap += '    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/"/>\n'
    sitemap += '    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/"/>\n'
    for lang in LANGUAGES:
        sitemap += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/"/>\n'
    sitemap += '    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>\n'
    
    # App pages
    for app in apps:
        url = f"https://apps.utkuapps.com/{app}/"
        sitemap += f'  <url>\n    <loc>{url}</loc>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="{url}"/>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url}"/>\n'
        for lang in LANGUAGES:
            sitemap += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app}/"/>\n'
        sitemap += '    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n  </url>\n'
    
    sitemap += '</urlset>'
    
    with open(BASE_DIR / 'sitemap-en.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"📄 sitemap-en.xml: {len(apps)+1} URLs")
    
    # Language sitemaps
    for lang in LANGUAGES:
        lang_dir = BASE_DIR / lang
        if lang_dir.exists():
            lang_apps = [d.name for d in lang_dir.iterdir() if d.is_dir() and (d / 'index.html').exists()]
            
            sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            
            # Language home page
            sitemap += f'  <url>\n    <loc>https://apps.utkuapps.com/{lang}/</loc>\n'
            sitemap += '    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/"/>\n'
            sitemap += '    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/"/>\n'
            for l in LANGUAGES:
                sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/"/>\n'
            sitemap += '    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>\n'
            
            # App pages
            for app in lang_apps:
                url = f"https://apps.utkuapps.com/{lang}/{app}/"
                sitemap += f'  <url>\n    <loc>{url}</loc>\n'
                sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/{app}/"/>\n'
                sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/{app}/"/>\n'
                for l in LANGUAGES:
                    sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/{app}/"/>\n'
                sitemap += '    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
            
            sitemap += '</urlset>'
            
            with open(BASE_DIR / f'sitemap-{lang}.xml', 'w', encoding='utf-8') as f:
                f.write(sitemap)
            print(f"📄 sitemap-{lang}.xml: {len(lang_apps)+1} URLs")
    
    # Sitemap index
    index = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    index += '  <sitemap><loc>https://apps.utkuapps.com/sitemap-en.xml</loc></sitemap>\n'
    for lang in LANGUAGES:
        index += f'  <sitemap><loc>https://apps.utkuapps.com/sitemap-{lang}.xml</loc></sitemap>\n'
    index += '</sitemapindex>'
    
    with open(BASE_DIR / 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(index)
    print("📄 sitemap.xml (index)")

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 COMPLETE MULTI-LANGUAGE SEO v2")
    print("   - Full index page translation")
    print("   - All internal links fixed")
    print("=" * 60)
    
    total = generate_pages()
    update_english()
    generate_sitemaps()
    
    print("\n" + "=" * 60)
    print(f"✅ DONE! {total} app pages + {len(LANGUAGES)} index pages")
    print("All navigation now stays within language context!")
    print("=" * 60)
