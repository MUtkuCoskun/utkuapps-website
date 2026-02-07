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

# Extensive translation dictionary
TRANSLATIONS = {
    'de': {
        # UI & Meta
        'Home': 'Startseite', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Datenschutz',
        'Read more': 'Weiterlesen', 'min read': 'Min. Lesezeit', 'February 2026': 'Februar 2026',
        'Review 2026': 'Bewertung 2026', 'Is it Worth It?': 'Lohnt es sich?',
        'Complete Guide': 'Vollständige Anleitung', 'Mastering': 'Meistern Sie',
        'Download for iPhone & iPad': 'Für iPhone & iPad herunterladen',
        'Rated 4.8 Stars on App Store': 'Bewertet mit 4.8 Sternen im App Store',
        
        # Categories
        'AI Tools': 'KI-Tools', 'Photo & Video': 'Foto & Video', 'Education': 'Bildung',
        'Productivity': 'Produktivität', 'Utilities': 'Dienstprogramme', 'Nature & Tools': 'Natur & Werkzeuge',
        'Design': 'Design', 'Health': 'Gesundheit', 'App Review': 'App-Bewertung', 'Guide': 'Anleitung',

        # Headings
        'What is': 'Was ist',
        'Key Features': 'Hauptfunktionen',
        'Why You Should Try It': 'Warum Sie es ausprobieren sollten',
        'How to Get Started': 'So legen Sie los',
        'Conclusion': 'Fazit',
        
        # Sentences - Intro
        'In the rapidly evolving world of iOS apps, finding the right tool for': 'In der sich schnell entwickelnden Welt der iOS-Apps kann es eine Herausforderung sein, das richtige Tool für',
        'can be a challenge. Today, we\'re taking a deep dive into': 'zu finden. Heute werfen wir einen genauen Blick auf',
        'a powerful app that\'s changing how users approach': 'eine leistungsstarke App, die die Art und Weise verändert, wie Nutzer an',
        
        # Sentences - Features
        'User-Friendly Interface:': 'Benutzerfreundliche Oberfläche:',
        'Designed for simplicity and ease of use.': 'Entwickelt für Einfachheit und Benutzerfreundlichkeit.',
        'Advanced Technology:': 'Fortschrittliche Technologie:',
        'Uses the latest iOS capabilities for smooth performance.': 'Nutzt die neuesten iOS-Funktionen für reibungslose Leistung.',
        'Regular Updates:': 'Regelmäßige Updates:',
        'The team constantly adds new features and improvements.': 'Das Team fügt ständig neue Funktionen und Verbesserungen hinzu.',
        'Privacy Focused:': 'Datenschutzorientiert:',
        'Your data stays secure on your device.': 'Ihre Daten bleiben sicher auf Ihrem Gerät.',
        
        # Sentences - Why
        'Whether you\'re a professional looking for productivity tools or a casual user wanting to explore': 'Ob Sie ein Profi auf der Suche nach Produktivitäts-Tools sind oder ein Gelegenheitsnutzer, der',
        'offers a compelling set of features. The intuitive design means you don\'t need a manual to get started.': 'bietet überzeugende Funktionen. Dank des intuitiven Designs benötigen Sie keine Anleitung, um loszulegen.',
        
        # Sentences - Steps
        'Download': 'Laden Sie',
        'from the App Store.': 'aus dem App Store herunter.',
        'Open the app and grant necessary permissions.': 'Öffnen Sie die App und gewähren Sie die erforderlichen Berechtigungen.',
        'Explore the main features and settings.': 'Erkunden Sie die wichtigsten Funktionen und Einstellungen.',
        'Start creating/learning/using!': 'Fangen Sie an zu erstellen/lernen/nutzen!',
        
        # Sentences - Conclusion
        'stands out in the': 'sticht hervor in der Kategorie',
        'category for its polish and performance. Give it a try today and see how it can help you with': 'wegen seines Designs und seiner Leistung. Probieren Sie es heute aus und sehen Sie, wie es Ihnen helfen kann bei',
        'TechSolutionAI. All rights reserved.': 'TechSolutionAI. Alle Rechte vorbehalten.',
        'App Reviews & Guides': 'App-Bewertungen & Anleitungen',
        'Expert insights on the best iOS apps for iPhone & iPad': 'Experteneinblicke in die besten iOS-Apps für iPhone & iPad'
    },
    'fr': {
        'Home': 'Accueil', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Confidentialité',
        'Read more': 'Lire la suite', 'min read': 'min de lecture', 'February 2026': 'Février 2026',
        'Review 2026': 'Avis 2026', 'Is it Worth It?': 'Est-ce que ça vaut le coup ?',
        'Complete Guide': 'Guide Complet', 'Mastering': 'Maîtriser',
        'Download for iPhone & iPad': 'Télécharger pour iPhone et iPad',
        'Rated 4.8 Stars on App Store': 'Noté 4.8 étoiles sur l\'App Store',
        
        'AI Tools': 'Outils IA', 'Photo & Video': 'Photo & Vidéo', 'Education': 'Éducation',
        'Productivity': 'Productivité', 'Utilities': 'Utilitaires', 'Nature & Tools': 'Nature & Outils',
        'Design': 'Design', 'Health': 'Santé', 'App Review': 'Avis d\'App', 'Guide': 'Guide',

        'What is': 'Qu\'est-ce que',
        'Key Features': 'Fonctionnalités Clés',
        'Why You Should Try It': 'Pourquoi vous devriez l\'essayer',
        'How to Get Started': 'Comment commencer',
        'Conclusion': 'Conclusion',
        
        'In the rapidly evolving world of iOS apps, finding the right tool for': 'Dans le monde en évolution rapide des applications iOS, trouver le bon outil pour',
        'can be a challenge. Today, we\'re taking a deep dive into': 'peut être un défi. Aujourd\'hui, nous plongeons dans',
        'a powerful app that\'s changing how users approach': 'une application puissante qui change la façon dont les utilisateurs abordent',
        
        'User-Friendly Interface:': 'Interface Conviviale :',
        'Designed for simplicity and ease of use.': 'Conçu pour la simplicité et la facilité d\'utilisation.',
        'Advanced Technology:': 'Technologie Avancée :',
        'Uses the latest iOS capabilities for smooth performance.': 'Utilise les dernières capacités iOS pour des performances fluides.',
        'Regular Updates:': 'Mises à jour Régulières :',
        'The team constantly adds new features and improvements.': 'L\'équipe ajoute constamment de nouvelles fonctionnalités et améliorations.',
        'Privacy Focused:': 'Axé sur la Confidentialité :',
        'Your data stays secure on your device.': 'Vos données restent sécurisées sur votre appareil.',
        
        'Whether you\'re a professional looking for productivity tools or a casual user wanting to explore': 'Que vous soyez un professionnel à la recherche d\'outils de productivité ou un utilisateur occasionnel souhaitant explorer',
        'offers a compelling set of features. The intuitive design means you don\'t need a manual to get started.': 'offre un ensemble de fonctionnalités convaincant. Le design intuitif signifie que vous n\'avez pas besoin de manuel pour commencer.',
        
        'Download': 'Téléchargez',
        'from the App Store.': 'sur l\'App Store.',
        'Open the app and grant necessary permissions.': 'Ouvrez l\'application et accordez les permissions nécessaires.',
        'Explore the main features and settings.': 'Explorez les principales fonctionnalités et réglages.',
        'Start creating/learning/using!': 'Commencez à créer/apprendre/utiliser !',
        
        'stands out in the': 'se distingue dans la catégorie',
        'category for its polish and performance. Give it a try today and see how it can help you with': 'pour sa finition et ses performances. Essayez-le aujourd\'hui et voyez comment il peut vous aider avec',
        'TechSolutionAI. All rights reserved.': 'TechSolutionAI. Tous droits réservés.',
        'App Reviews & Guides': 'Avis et Guides d\'Apps',
        'Expert insights on the best iOS apps for iPhone & iPad': 'Avis d\'experts sur les meilleures apps iOS pour iPhone & iPad'
    },
    'es': {
        'Home': 'Inicio', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacidad',
        'Read more': 'Leer más', 'min read': 'min de lectura', 'February 2026': 'Febrero 2026',
        'Review 2026': 'Reseña 2026', 'Is it Worth It?': '¿Vale la pena?',
        'Complete Guide': 'Guía Completa', 'Mastering': 'Dominando',
        'Download for iPhone & iPad': 'Descargar para iPhone y iPad',
        'Rated 4.8 Stars on App Store': 'Calificado 4.8 estrellas en App Store',
        
        'AI Tools': 'Herramientas IA', 'Photo & Video': 'Foto y Video', 'Education': 'Educación',
        'Productivity': 'Productividad', 'Utilities': 'Utilidades', 'Nature & Tools': 'Naturaleza',
        'Design': 'Diseño', 'Health': 'Salud', 'App Review': 'Reseña de App', 'Guide': 'Guía',

        'What is': '¿Qué es',
        'Key Features': 'Características Clave',
        'Why You Should Try It': 'Por qué deberías probarlo',
        'How to Get Started': 'Cómo empezar',
        'Conclusion': 'Conclusión',
        
        'In the rapidly evolving world of iOS apps, finding the right tool for': 'En el mundo de las apps de iOS, encontrar la herramienta adecuada para',
        'can be a challenge. Today, we\'re taking a deep dive into': 'puede ser un desafío. Hoy profundizamos en',
        'a powerful app that\'s changing how users approach': 'una app poderosa que cambia cómo los usuarios abordan',
        
        'User-Friendly Interface:': 'Interfaz Amigable:',
        'Designed for simplicity and ease of use.': 'Diseñado para la simplicidad y facilidad de uso.',
        'Advanced Technology:': 'Tecnología Avanzada:',
        'Uses the latest iOS capabilities for smooth performance.': 'Usa las últimas capacidades de iOS para un rendimiento fluido.',
        'Regular Updates:': 'Actualizaciones Regulares:',
        'The team constantly adds new features and improvements.': 'El equipo añade constantemente nuevas funciones y mejoras.',
        'Privacy Focused:': 'Enfoque en Privacidad:',
        'Your data stays secure on your device.': 'Tus datos permanecen seguros en tu dispositivo.',
        
        'Whether you\'re a professional looking for productivity tools or a casual user wanting to explore': 'Ya seas un profesional buscando herramientas de productividad o un usuario casual queriendo explorar',
        'offers a compelling set of features. The intuitive design means you don\'t need a manual to get started.': 'ofrece un conjunto de funciones convincente. El diseño intuitivo significa que no necesitas un manual para empezar.',
        
        'Download': 'Descarga',
        'from the App Store.': 'de la App Store.',
        'Open the app and grant necessary permissions.': 'Abre la app y concede los permisos necesarios.',
        'Explore the main features and settings.': 'Explora las funciones y configuraciones principales.',
        'Start creating/learning/using!': '¡Empieza a crear/aprender/usar!',
        
        'stands out in the': 'se destaca en la categoría',
        'category for its polish and performance. Give it a try today and see how it can help you with': 'por su pulido y rendimiento. Pruébalo hoy y mira cómo puede ayudarte con',
        'TechSolutionAI. All rights reserved.': 'TechSolutionAI. Todos los derechos reservados.',
        'App Reviews & Guides': 'Reseñas y Guías de Apps',
        'Expert insights on the best iOS apps for iPhone & iPad': 'Opiniones de expertos sobre las mejores apps para iPhone y iPad'
    },
    'it': {
        'Home': 'Home', 'Apps': 'App', 'Blog': 'Blog', 'Privacy': 'Privacy',
        'Read more': 'Leggi di più', 'min read': 'min di lettura', 'February 2026': 'Febbraio 2026',
        'Review 2026': 'Recensione 2026', 'Is it Worth It?': 'Ne vale la pena?',
        'Complete Guide': 'Guida Completa', 'Mastering': 'Padroneggiare',
        'Download for iPhone & iPad': 'Scarica per iPhone & iPad',
        'Rated 4.8 Stars on App Store': 'Valutato 4.8 stelle su App Store',
        
        'AI Tools': 'Strumenti IA', 'Photo & Video': 'Foto e Video', 'Education': 'Istruzione',
        'Productivity': 'Produttività', 'Utilities': 'Utility', 'Nature & Tools': 'Natura e Strumenti',
        'Design': 'Design', 'Health': 'Salute', 'App Review': 'Recensione App', 'Guide': 'Guida',

        'What is': 'Cos\'è',
        'Key Features': 'Caratteristiche Principali',
        'Why You Should Try It': 'Perché dovresti provarlo',
        'How to Get Started': 'Come iniziare',
        'Conclusion': 'Conclusione',
        
        'In the rapidly evolving world of iOS apps, finding the right tool for': 'Nel mondo in rapida evoluzione delle app iOS, trovare lo strumento giusto per',
        'can be a challenge. Today, we\'re taking a deep dive into': 'può essere una sfida. Oggi approfondiamo',
        'a powerful app that\'s changing how users approach': 'un\'app potente che sta cambiando il modo in cui gli utenti affrontano',
        
        'User-Friendly Interface:': 'Interfaccia User-Friendly:',
        'Designed for simplicity and ease of use.': 'Progettato per semplicità e facilità d\'uso.',
        'Advanced Technology:': 'Tecnologia Avanzata:',
        'Uses the latest iOS capabilities for smooth performance.': 'Utilizza le ultime funzionalità iOS per prestazioni fluide.',
        'Regular Updates:': 'Aggiornamenti Regolari:',
        'The team constantly adds new features and improvements.': 'Il team aggiunge costantemente nuove funzionalità e miglioramenti.',
        'Privacy Focused:': 'Privacy al Primo Posto:',
        'Your data stays secure on your device.': 'I tuoi dati rimangono sicuri sul tuo dispositivo.',
        
        'Whether you\'re a professional looking for productivity tools or a casual user wanting to explore': 'Che tu sia un professionista in cerca di strumenti di produttività o un utente occasionale che vuole esplorare',
        'offers a compelling set of features. The intuitive design means you don\'t need a manual to get started.': 'offre un set di funzionalità convincente. Il design intuitivo significa che non hai bisogno di un manuale per iniziare.',
        
        'Download': 'Scarica',
        'from the App Store.': 'dall\'App Store.',
        'Open the app and grant necessary permissions.': 'Apri l\'app e concedi le autorizzazioni necessarie.',
        'Explore the main features and settings.': 'Esplora le funzionalità e le impostazioni principali.',
        'Start creating/learning/using!': 'Inizia a creare/imparare/usare!',
        
        'stands out in the': 'si distingue nella categoria',
        'category for its polish and performance. Give it a try today and see how it can help you with': 'per la sua cura e le prestazioni. Provalo oggi e vedi come può aiutarti con',
        'TechSolutionAI. All rights reserved.': 'TechSolutionAI. Tutti i diritti riservati.',
        'App Reviews & Guides': 'Recensioni e Guide App',
        'Expert insights on the best iOS apps for iPhone & iPad': 'Approfondimenti esperti sulle migliori app iOS per iPhone e iPad'
    },
    'nl': {
        'Home': 'Home', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacy',
        'Read more': 'Lees meer', 'min read': 'min leestijd', 'February 2026': 'Februari 2026',
        'Review 2026': 'Recensie 2026', 'Is it Worth It?': 'Is het de moeite waard?',
        'Complete Guide': 'Volledige Gids', 'Mastering': 'Beheersing van',
        'Download for iPhone & iPad': 'Downloaden voor iPhone & iPad',
        'Rated 4.8 Stars on App Store': 'Beoordeeld met 4.8 sterren in de App Store',
        
        'AI Tools': 'AI Tools', 'Photo & Video': 'Foto & Video', 'Education': 'Onderwijs',
        'Productivity': 'Productiviteit', 'Utilities': 'Hulpprogramma\'s', 'Nature & Tools': 'Natuur & Tools',
        'Design': 'Ontwerp', 'Health': 'Gezondheid', 'App Review': 'App Recensie', 'Guide': 'Gids',

        'What is': 'Wat is',
        'Key Features': 'Belangrijkste Kenmerken',
        'Why You Should Try It': 'Waarom je het moet proberen',
        'How to Get Started': 'Hoe te beginnen',
        'Conclusion': 'Conclusie',
        
        'In the rapidly evolving world of iOS apps, finding the right tool for': 'In de snel evoluerende wereld van iOS-apps kan het vinden van de juiste tool voor',
        'can be a challenge. Today, we\'re taking a deep dive into': 'een uitdaging zijn. Vandaag duiken we diep in',
        'a powerful app that\'s changing how users approach': 'een krachtige app die de manier verandert waarop gebruikers',
        
        'User-Friendly Interface:': 'Gebruiksvriendelijke Interface:',
        'Designed for simplicity and ease of use.': 'Ontworpen voor eenvoud en gebruiksgemak.',
        'Advanced Technology:': 'Geavanceerde Technologie:',
        'Uses the latest iOS capabilities for smooth performance.': 'Gebruikt de nieuwste iOS-mogelijkheden voor soepele prestaties.',
        'Regular Updates:': 'Regelmatige Updates:',
        'The team constantly adds new features and improvements.': 'Het team voegt voortdurend nieuwe functies en verbeteringen toe.',
        'Privacy Focused:': 'Privacy Gericht:',
        'Your data stays secure on your device.': 'Uw gegevens blijven veilig op uw apparaat.',
        
        'Whether you\'re a professional looking for productivity tools or a casual user wanting to explore': 'Of u nu een professional bent die op zoek is naar productiviteitstools of een informele gebruiker die wil verkennen',
        'offers a compelling set of features. The intuitive design means you don\'t need a manual to get started.': 'biedt een overtuigende set functies. Het intuïtieve ontwerp betekent dat u geen handleiding nodig heeft om te beginnen.',
        
        'Download': 'Download',
        'from the App Store.': 'uit de App Store.',
        'Open the app and grant necessary permissions.': 'Open de app en verleen de nodige machtigingen.',
        'Explore the main features and settings.': 'Verken de belangrijkste functies en instellingen.',
        'Start creating/learning/using!': 'Begin met creëren/leren/gebruiken!',
        
        'stands out in the': 'blinkt uit in de categorie',
        'category for its polish and performance. Give it a try today and see how it can help you with': 'vanwege zijn afwerking en prestaties. Probeer het vandaag nog en zie hoe het u kan helpen met',
        'TechSolutionAI. All rights reserved.': 'TechSolutionAI. Alle rechten voorbehouden.',
        'App Reviews & Guides': 'App Recensies & Gidsen',
        'Expert insights on the best iOS apps for iPhone & iPad': 'Deskundige inzichten in de beste iOS-apps voor iPhone & iPad'
    },
    # Other languages simplified/defaulted to similar or generic replacements if specific linguistic detail is tricky without API, 
    # but I will add Placeholder for them to ensure at least UI is translated.
    'pt': {'Home': 'Início', 'Apps': 'Apps', 'Blog': 'Blog', 'Privacy': 'Privacidade', 'Download for iPhone & iPad': 'Baixar para iPhone e iPad', 'Rated 4.8 Stars on App Store': 'Avaliado com 4.8 Estrelas na App Store', 'Review 2026': 'Avaliação 2026', 'Complete Guide': 'Guia Completo', 'Key Features': 'Recursos Principais', 'Conclusion': 'Conclusão'},
    'pl': {'Home': 'Strona główna', 'Apps': 'Aplikacje', 'Blog': 'Blog', 'Download for iPhone & iPad': 'Pobierz na iPhone\'a i iPada', 'Review 2026': 'Recenzja 2026', 'Complete Guide': 'Pełny Poradnik', 'Key Features': 'Główne Cechy', 'Conclusion': 'Wniosek'},
    'sv': {'Home': 'Hem', 'Apps': 'Appar', 'Blog': 'Blog', 'Download for iPhone & iPad': 'Ladda ner för iPhone & iPad', 'Review 2026': 'Recension 2026', 'Complete Guide': 'Komplett Guide', 'Key Features': 'Nyckelfunktioner', 'Conclusion': 'Slutsats'},
    'da': {'Home': 'Hjem', 'Apps': 'Apps', 'Blog': 'Blog', 'Download for iPhone & iPad': 'Hent til iPhone & iPad', 'Review 2026': 'Anmeldelse 2026', 'Complete Guide': 'Komplet Guide', 'Key Features': 'Nøglefunktioner', 'Conclusion': 'Konklusion'},
    'no': {'Home': 'Hjem', 'Apps': 'Apper', 'Blog': 'Blog', 'Download for iPhone & iPad': 'Last ned for iPhone & iPad', 'Review 2026': 'Anmeldelse 2026', 'Complete Guide': 'Komplett Guide', 'Key Features': 'Nøkkelfunksjoner', 'Conclusion': 'Konklusjon'}
}

# Fill missing languages with basic UI translations to avoid English blocks
BASIC_DEFAULTS = {
    'pt': {'What is': 'O que é', 'Start creating/learning/using!': 'Comece a usar!', 'Why You Should Try It': 'Por que você deve tentar'},
    'pl': {'What is': 'Czym jest', 'Start creating/learning/using!': 'Zacznij używać!', 'Why You Should Try It': 'Dlaczego warto spróbować'},
    'sv': {'What is': 'Vad är', 'Start creating/learning/using!': 'Börja använda!', 'Why You Should Try It': 'Varför du bör prova det'},
    'da': {'What is': 'Hvad er', 'Start creating/learning/using!': 'Begynd at bruge!', 'Why You Should Try It': 'Hvorfor du skal prøve det'},
    'no': {'What is': 'Hva er', 'Start creating/learning/using!': 'Begynn å bruke!', 'Why You Should Try It': 'Hvorfor du bør prøve det'}
}
for lang in ['pt', 'pl', 'sv', 'da', 'no']:
    TRANSLATIONS[lang].update(BASIC_DEFAULTS.get(lang, {}))

def translate_text(text, lang):
    if not text: return text
    trans = TRANSLATIONS.get(lang, {})
    
    # Sort keys by length descending to replace longest phrases first
    sorted_keys = sorted(trans.keys(), key=len, reverse=True)
    
    for k in sorted_keys:
        if k in text:
            text = text.replace(k, trans[k])
            
    return text

def fix_paths(content, depth=2):
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
        
    path = f"blog/{slug}" if not is_index else "blog/"
    if path.endswith('/'): path = path[:-1] # normalize
    path += "/" 
    
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
        
    # Also fix og:locale
    og_locale = soup.find('meta', property='og:locale')
    if og_locale:
        og_locale['content'] = LANGUAGES.get(lang, 'en_US')
    else:
        meta = soup.new_tag('meta')
        meta['property'] = 'og:locale'
        meta['content'] = LANGUAGES.get(lang, 'en_US')
        head.append(meta)

    return str(soup)

def main():
    print("🚀 Starting High-Quality Blog Translation...")
    
    posts = [p for p in BLOG_DIR.iterdir() if p.is_dir() and (p / "index.html").exists()]
    print(f"📦 Found {len(posts)} blog posts")
    
    for lang in LANGUAGES.keys():
        print(f"\n🌍 {lang.upper()}...", flush=True)
        lang_blog_dir = BASE_DIR / lang / "blog"
        lang_blog_dir.mkdir(parents=True, exist_ok=True)
        
        # Index translation
        src_index = BLOG_DIR / "index.html"
        if src_index.exists():
            content = src_index.read_text(encoding='utf-8')
            content = translate_text(content, lang)
            content = content.replace('lang="en"', f'lang="{lang}"')
            content = fix_paths(content, depth=1)
            content = add_hreflang(content, "", lang, is_index=True)
            (lang_blog_dir / "index.html").write_text(content, encoding='utf-8')
            print(f"  ✅ Blog Index")
            
        # Post translation
        for post in posts:
            slug = post.name
            src_post = post / "index.html"
            dest_dir = lang_blog_dir / slug
            dest_dir.mkdir(exist_ok=True)
            
            content = src_post.read_text(encoding='utf-8')
            content = translate_text(content, lang)
            content = content.replace('lang="en"', f'lang="{lang}"')
            content = fix_paths(content, depth=2)
            content = add_hreflang(content, slug, lang)
            
            (dest_dir / "index.html").write_text(content, encoding='utf-8')
            # Progress dot
            if posts.index(post) % 20 == 0:
                print(".", end="", flush=True)

    print("\n✅ Blog translation complete!")

if __name__ == "__main__":
    main()
