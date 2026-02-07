#!/usr/bin/env python3
"""
SIMPLE REGEX-BASED TRANSLATION SCRIPT
No BeautifulSoup dependency issues
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")

LANGUAGES = ['de', 'fr', 'es', 'it', 'nl', 'pt', 'pl', 'sv', 'da', 'no']

LOCALES = {
    'de': 'de_DE', 'fr': 'fr_FR', 'es': 'es_ES', 'it': 'it_IT', 'nl': 'nl_NL',
    'pt': 'pt_PT', 'pl': 'pl_PL', 'sv': 'sv_SE', 'da': 'da_DK', 'no': 'nb_NO',
}

# Translations
TR = {
    'de': {
        'Free Download for iPhone & iPad': 'Kostenloser Download für iPhone & iPad',
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-Apps für iPhone & iPad',
        'Home': 'Startseite', 'All Apps': 'Alle Apps', 'Privacy': 'Datenschutz',
        'Education': 'Bildung', 'AI & Photo': 'KI & Foto', 'Language': 'Sprache',
        'Home Design': 'Wohndesign', 'Identifier': 'Erkennung', 'Other': 'Andere',
        'About': 'Über', 'Features': 'Funktionen', 'Key Features': 'Hauptfunktionen',
        'FAQ': 'Häufige Fragen', 'Frequently Asked Questions': 'Häufig gestellte Fragen',
        'Download on the': 'Laden im', 'Download Free': 'Kostenlos herunterladen',
        'Free Download': 'Kostenloser Download', 'Free on App Store': 'Kostenlos im App Store',
        'for iPhone & iPad': 'für iPhone & iPad', 'for iPhone and iPad': 'für iPhone und iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'bietet ein leistungsstarkes, intuitives Erlebnis, das speziell für iOS-Benutzer entwickelt wurde, die das Beste verlangen',
        'Whether you\'re a professional seeking advanced features or a beginner looking for an easy-to-use solution': 'Egal, ob Sie ein Profi sind, der erweiterte Funktionen sucht, oder ein Anfänger',
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
        'Today': 'Heute', 'Join millions of satisfied users': 'Schließen Sie sich Millionen zufriedener Benutzer an',
        'Free on the App Store for iPhone and iPad': 'Kostenlos im App Store für iPhone und iPad',
        'Is': 'Ist', 'free to download': 'kostenlos zum Herunterladen',
        'Yes': 'Ja', 'completely free to download from the App Store': 'völlig kostenlos im App Store herunterzuladen',
        'Some premium features may be available through optional in-app purchases': 'Einige Premium-Funktionen sind durch In-App-Käufe verfügbar',
        'What devices are compatible with': 'Welche Geräte sind kompatibel mit',
        'is designed for iPhone and iPad devices running iOS 15.0 or later': 'ist für iPhone und iPad mit iOS 15.0 oder höher konzipiert',
        'The app is optimized for all screen sizes': 'Die App ist für alle Bildschirmgrößen optimiert',
        'ensuring a great experience on any compatible device': 'und gewährleistet ein großartiges Erlebnis auf jedem kompatiblen Gerät',
        'How do I get started with': 'Wie fange ich an mit', 'Simply download': 'Laden Sie einfach',
        'from the App Store and follow the intuitive setup process': 'aus dem App Store herunter und folgen Sie dem Einrichtungsprozess',
        'The app includes helpful onboarding guides to help you make the most of all features': 'Die App enthält hilfreiche Anleitungen',
        'Is my data safe with': 'Sind meine Daten sicher bei',
        'We prioritize your privacy and security': 'Wir priorisieren Ihre Privatsphäre und Sicherheit',
        'Your data is stored securely and we never share your personal information with third parties': 'Ihre Daten werden sicher gespeichert',
        'Please review our Privacy Policy for more details': 'Bitte lesen Sie unsere Datenschutzrichtlinie',
        'All rights reserved': 'Alle Rechte vorbehalten', 'Terms of Service': 'Nutzungsbedingungen',
        'Learn more': 'Mehr erfahren', 'Get started': 'Loslegen', 'Try now': 'Jetzt testen', 'No': 'Nein',
    },
    'fr': {
        'Free Download for iPhone & iPad': 'Téléchargement gratuit pour iPhone et iPad',
        'Premium iOS Apps for iPhone & iPad': 'Applications iOS Premium pour iPhone et iPad',
        'Home': 'Accueil', 'All Apps': 'Toutes les applications', 'Privacy': 'Confidentialité',
        'Education': 'Éducation', 'AI & Photo': 'IA et Photo', 'Language': 'Langue',
        'Home Design': 'Design d\'intérieur', 'Identifier': 'Identification', 'Other': 'Autre',
        'About': 'À propos', 'Features': 'Fonctionnalités', 'Key Features': 'Fonctionnalités principales',
        'FAQ': 'FAQ', 'Frequently Asked Questions': 'Questions fréquemment posées',
        'Download on the': 'Télécharger sur l\'', 'Download Free': 'Télécharger gratuitement',
        'Free Download': 'Téléchargement gratuit', 'Free on App Store': 'Gratuit sur l\'App Store',
        'for iPhone & iPad': 'pour iPhone et iPad', 'for iPhone and iPad': 'pour iPhone et iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'offre une expérience puissante et intuitive conçue pour les utilisateurs iOS exigeants',
        'Today': 'Aujourd\'hui', 'Join millions of satisfied users': 'Rejoignez des millions d\'utilisateurs satisfaits',
        'Yes': 'Oui', 'No': 'Non', 'All rights reserved': 'Tous droits réservés',
    },
    'es': {
        'Free Download for iPhone & iPad': 'Descarga gratuita para iPhone y iPad',
        'Premium iOS Apps for iPhone & iPad': 'Aplicaciones iOS Premium para iPhone y iPad',
        'Home': 'Inicio', 'All Apps': 'Todas las aplicaciones', 'Privacy': 'Privacidad',
        'Education': 'Educación', 'AI & Photo': 'IA y Foto', 'Language': 'Idioma',
        'Home Design': 'Diseño del hogar', 'Identifier': 'Identificador', 'Other': 'Otro',
        'About': 'Acerca de', 'Features': 'Características', 'Key Features': 'Características principales',
        'FAQ': 'Preguntas frecuentes', 'Frequently Asked Questions': 'Preguntas frecuentes',
        'Download on the': 'Descargar en', 'Download Free': 'Descargar gratis',
        'Free Download': 'Descarga gratuita', 'Free on App Store': 'Gratis en App Store',
        'for iPhone & iPad': 'para iPhone y iPad', 'for iPhone and iPad': 'para iPhone y iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'ofrece una experiencia potente e intuitiva diseñada para usuarios de iOS exigentes',
        'Today': 'Hoy', 'Join millions of satisfied users': 'Únete a millones de usuarios satisfechos',
        'Yes': 'Sí', 'No': 'No', 'All rights reserved': 'Todos los derechos reservados',
    },
    'it': {
        'Free Download for iPhone & iPad': 'Download gratuito per iPhone e iPad',
        'Home': 'Home', 'All Apps': 'Tutte le App', 'Privacy': 'Privacy',
        'Education': 'Istruzione', 'About': 'Informazioni', 'Features': 'Funzionalità',
        'Download on the': 'Scarica su', 'Download Free': 'Scarica gratis',
        'Free Download': 'Download gratuito', 'for iPhone & iPad': 'per iPhone e iPad',
        'Today': 'Oggi', 'Yes': 'Sì', 'No': 'No', 'All rights reserved': 'Tutti i diritti riservati',
    },
    'nl': {
        'Free Download for iPhone & iPad': 'Gratis download voor iPhone en iPad',
        'Home': 'Home', 'All Apps': 'Alle Apps', 'Privacy': 'Privacy',
        'Education': 'Onderwijs', 'About': 'Over', 'Features': 'Functies',
        'Download on the': 'Download op de', 'Download Free': 'Gratis downloaden',
        'Free Download': 'Gratis download', 'for iPhone & iPad': 'voor iPhone en iPad',
        'Today': 'Vandaag', 'Yes': 'Ja', 'No': 'Nee', 'All rights reserved': 'Alle rechten voorbehouden',
    },
    'pt': {
        'Free Download for iPhone & iPad': 'Download gratuito para iPhone e iPad',
        'Home': 'Início', 'All Apps': 'Todos os Apps', 'Privacy': 'Privacidade',
        'Education': 'Educação', 'About': 'Sobre', 'Features': 'Recursos',
        'Download on the': 'Baixar na', 'Download Free': 'Baixar grátis',
        'Free Download': 'Download grátis', 'for iPhone & iPad': 'para iPhone e iPad',
        'Today': 'Hoje', 'Yes': 'Sim', 'No': 'Não', 'All rights reserved': 'Todos os direitos reservados',
    },
    'pl': {
        'Free Download for iPhone & iPad': 'Bezpłatne pobieranie na iPhone i iPad',
        'Home': 'Strona główna', 'All Apps': 'Wszystkie aplikacje', 'Privacy': 'Prywatność',
        'Education': 'Edukacja', 'About': 'O aplikacji', 'Features': 'Funkcje',
        'Download on the': 'Pobierz z', 'Download Free': 'Pobierz za darmo',
        'Free Download': 'Bezpłatne pobieranie', 'for iPhone & iPad': 'na iPhone i iPad',
        'Today': 'Dziś', 'Yes': 'Tak', 'No': 'Nie',
    },
    'sv': {
        'Free Download for iPhone & iPad': 'Gratis nedladdning för iPhone och iPad',
        'Home': 'Hem', 'All Apps': 'Alla appar', 'Privacy': 'Integritet',
        'Education': 'Utbildning', 'About': 'Om', 'Features': 'Funktioner',
        'Download on the': 'Ladda ner på', 'Download Free': 'Ladda ner gratis',
        'Free Download': 'Gratis nedladdning', 'for iPhone & iPad': 'för iPhone och iPad',
        'Today': 'Idag', 'Yes': 'Ja', 'No': 'Nej',
    },
    'da': {
        'Free Download for iPhone & iPad': 'Gratis download til iPhone og iPad',
        'Home': 'Hjem', 'All Apps': 'Alle apps', 'Privacy': 'Privatliv',
        'Education': 'Uddannelse', 'About': 'Om', 'Features': 'Funktioner',
        'Download on the': 'Download på', 'Download Free': 'Download gratis',
        'Free Download': 'Gratis download', 'for iPhone & iPad': 'til iPhone og iPad',
        'Today': 'I dag', 'Yes': 'Ja', 'No': 'Nej',
    },
    'no': {
        'Free Download for iPhone & iPad': 'Gratis nedlasting for iPhone og iPad',
        'Home': 'Hjem', 'All Apps': 'Alle apper', 'Privacy': 'Personvern',
        'Education': 'Utdanning', 'About': 'Om', 'Features': 'Funksjoner',
        'Download on the': 'Last ned fra', 'Download Free': 'Last ned gratis',
        'Free Download': 'Gratis nedlasting', 'for iPhone & iPad': 'for iPhone og iPad',
        'Today': 'I dag', 'Yes': 'Ja', 'No': 'Nei',
    },
}

def translate(text, lang):
    """Apply translations"""
    if not lang in TR:
        return text
    result = text
    for eng, trans in sorted(TR[lang].items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(eng, trans)
    return result

def add_hreflang(app_slug):
    """Generate hreflang tags"""
    tags = []
    base = f"https://apps.utkuapps.com/{app_slug}/"
    tags.append(f'<link rel="alternate" hreflang="en" href="{base}"/>')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{base}"/>')
    for lang in LANGUAGES:
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app_slug}/"/>')
    return '\n'.join(tags)

def process_page(content, app_slug, lang):
    """Process HTML page"""
    # Change lang attribute
    content = re.sub(r'<html[^>]*lang="[^"]*"', f'<html lang="{lang}"', content)
    
    # Translate content
    content = translate(content, lang)
    
    # Update og:locale
    if 'og:locale' in content:
        content = re.sub(r'content="en_US"(\s*/>|\s*>)(\s*<meta property="og:locale")?', 
                        f'content="{LOCALES[lang]}"\\1', content)
    
    # Remove existing hreflang
    content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
    
    # Add new hreflang before </head>
    hreflang = add_hreflang(app_slug)
    content = content.replace('</head>', f'{hreflang}\n</head>')
    
    # Fix paths
    content = content.replace('href="../css/', 'href="../../css/')
    content = content.replace('href="../js/', 'href="../../js/')
    content = content.replace('src="../icons/', 'src="../../icons/')
    content = content.replace('src="../images/', 'src="../../images/')
    
    return content

def generate_pages():
    """Generate all pages"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES)
    
    apps = [d.name for d in BASE_DIR.iterdir() 
            if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]
    
    print(f"📁 Found {len(apps)} apps")
    total = 0
    
    for lang in LANGUAGES:
        print(f"\n🌍 {lang.upper()}...")
        lang_dir = BASE_DIR / lang
        lang_dir.mkdir(exist_ok=True)
        
        for app in apps:
            src = BASE_DIR / app / 'index.html'
            dest_dir = lang_dir / app
            dest_dir.mkdir(exist_ok=True)
            
            try:
                with open(src, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = process_page(content, app, lang)
                
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
    
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude:
            index = item / 'index.html'
            if index.exists():
                with open(index, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove existing
                content = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', content)
                
                # Add new
                hreflang = add_hreflang(item.name)
                content = content.replace('</head>', f'{hreflang}\n</head>')
                
                with open(index, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    
    print(f"✅ Updated {count} English pages")

def generate_sitemaps():
    """Generate sitemaps"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES)
    apps = [d.name for d in BASE_DIR.iterdir() 
            if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]
    
    # English sitemap
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
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
    print(f"📄 sitemap-en.xml: {len(apps)} URLs")
    
    # Language sitemaps
    for lang in LANGUAGES:
        lang_dir = BASE_DIR / lang
        if lang_dir.exists():
            lang_apps = [d.name for d in lang_dir.iterdir() if d.is_dir() and (d / 'index.html').exists()]
            
            sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
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
            print(f"📄 sitemap-{lang}.xml: {len(lang_apps)} URLs")
    
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
    print("🚀 SIMPLE REGEX-BASED TRANSLATION")
    print("=" * 60)
    
    total = generate_pages()
    update_english()
    generate_sitemaps()
    
    print("\n" + "=" * 60)
    print(f"✅ DONE! {total} pages across {len(LANGUAGES)} languages")
    print("=" * 60)
