#!/usr/bin/env python3
"""
OPTIMIZED FULL CONTENT TRANSLATION
Uses pre-built translation dictionaries for faster execution
Combines static translations with pattern-based content translation
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")

LANGUAGES = {
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

# Comprehensive translations for all common text patterns
TRANSLATIONS = {
    'de': {
        # Page titles and meta
        'Free Download for iPhone & iPad': 'Kostenloser Download für iPhone & iPad',
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-Apps für iPhone & iPad',
        
        # Navigation
        'Home': 'Startseite',
        'All Apps': 'Alle Apps',
        'Apps': 'Apps',
        'Privacy': 'Datenschutz',
        'Privacy Policy': 'Datenschutzrichtlinie',
        'Contact': 'Kontakt',
        
        # Categories
        'Education': 'Bildung',
        'AI & Photo': 'KI & Foto',
        'Language': 'Sprache',
        'Home Design': 'Wohndesign',
        'Identifier': 'Erkennung',
        'Other': 'Andere',
        
        # App page content
        'About': 'Über',
        'Features': 'Funktionen',
        'Key Features': 'Hauptfunktionen',
        'FAQ': 'Häufige Fragen',
        'Frequently Asked Questions': 'Häufig gestellte Fragen',
        
        # Download section
        'Download on the': 'Laden im',
        'App Store': 'App Store',
        'Download Free': 'Kostenlos herunterladen',
        'Free Download': 'Kostenloser Download',
        'Free on App Store': 'Kostenlos im App Store',
        'Get it on App Store': 'Im App Store herunterladen',
        
        # Device info
        'for iPhone & iPad': 'für iPhone & iPad',
        'for iPhone and iPad': 'für iPhone und iPad',
        'iPhone & iPad': 'iPhone & iPad',
        
        # Common paragraphs (patterns)
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'bietet ein leistungsstarkes, intuitives Erlebnis, das speziell für iOS-Benutzer entwickelt wurde, die das Beste verlangen',
        'Whether you\'re a professional seeking advanced features or a beginner looking for an easy-to-use solution': 'Egal, ob Sie ein Profi sind, der erweiterte Funktionen sucht, oder ein Anfänger, der eine benutzerfreundliche Lösung sucht',
        'our app provides everything you need in one streamlined package': 'unsere App bietet alles, was Sie brauchen, in einem optimierten Paket',
        'Developed with cutting-edge technology and refined through extensive user feedback': 'Mit modernster Technologie entwickelt und durch umfangreiches Benutzerfeedback verfeinert',
        'has earned its place as a top-rated application': 'hat sich seinen Platz als erstklassige Anwendung verdient',
        'in the': 'in der',
        'category on the App Store': 'Kategorie im App Store',
        'Our team continuously updates the app with new features, performance improvements, and enhanced functionality': 'Unser Team aktualisiert die App kontinuierlich mit neuen Funktionen, Leistungsverbesserungen und erweiterter Funktionalität',
        'to ensure you always have access to the latest innovations': 'um sicherzustellen, dass Sie immer Zugang zu den neuesten Innovationen haben',
        'With millions of downloads worldwide and consistently high ratings': 'Mit Millionen von Downloads weltweit und durchweg hohen Bewertungen',
        'has become the trusted choice for users across the globe': 'ist zur vertrauenswürdigen Wahl für Benutzer auf der ganzen Welt geworden',
        'The app features a clean, modern interface that makes complex tasks simple': 'Die App verfügt über eine saubere, moderne Benutzeroberfläche, die komplexe Aufgaben einfach macht',
        'while providing the depth and capabilities that power users require': 'und gleichzeitig die Tiefe und Fähigkeiten bietet, die erfahrene Benutzer benötigen',
        'Download': 'Laden Sie',
        'today and discover why it\'s the preferred choice for discerning iOS users': 'noch heute herunter und entdecken Sie, warum es die bevorzugte Wahl für anspruchsvolle iOS-Benutzer ist',
        'Available exclusively on the App Store for iPhone and iPad devices running iOS 15.0 or later': 'Exklusiv im App Store für iPhone und iPad mit iOS 15.0 oder höher verfügbar',
        
        # CTA section
        'Today': 'Heute',
        'Join millions of satisfied users': 'Schließen Sie sich Millionen zufriedener Benutzer an',
        'Free on the App Store for iPhone and iPad': 'Kostenlos im App Store für iPhone und iPad',
        
        # FAQ content
        'Is': 'Ist',
        'free to download': 'kostenlos zum Herunterladen',
        'Yes': 'Ja',
        'completely free to download from the App Store': 'völlig kostenlos im App Store herunterzuladen',
        'Some premium features may be available through optional in-app purchases': 'Einige Premium-Funktionen sind möglicherweise durch optionale In-App-Käufe verfügbar',
        'What devices are compatible with': 'Welche Geräte sind kompatibel mit',
        'is designed for iPhone and iPad devices running iOS 15.0 or later': 'ist für iPhone und iPad mit iOS 15.0 oder höher konzipiert',
        'The app is optimized for all screen sizes': 'Die App ist für alle Bildschirmgrößen optimiert',
        'ensuring a great experience on any compatible device': 'und gewährleistet ein großartiges Erlebnis auf jedem kompatiblen Gerät',
        'How do I get started with': 'Wie fange ich an mit',
        'Simply download': 'Laden Sie einfach',
        'from the App Store and follow the intuitive setup process': 'aus dem App Store herunter und folgen Sie dem intuitiven Einrichtungsprozess',
        'The app includes helpful onboarding guides to help you make the most of all features': 'Die App enthält hilfreiche Einführungsanleitungen, die Ihnen helfen, alle Funktionen optimal zu nutzen',
        'Is my data safe with': 'Sind meine Daten sicher bei',
        'We prioritize your privacy and security': 'Wir priorisieren Ihre Privatsphäre und Sicherheit',
        'Your data is stored securely and we never share your personal information with third parties': 'Ihre Daten werden sicher gespeichert und wir teilen Ihre persönlichen Informationen niemals mit Dritten',
        'Please review our Privacy Policy for more details': 'Bitte lesen Sie unsere Datenschutzrichtlinie für weitere Details',
        
        # Footer
        'All rights reserved': 'Alle Rechte vorbehalten',
        'Terms of Service': 'Nutzungsbedingungen',
        
        # General
        'Learn more': 'Mehr erfahren',
        'Get started': 'Loslegen',
        'Try now': 'Jetzt testen',
        'No': 'Nein',
    },
    'fr': {
        'Free Download for iPhone & iPad': 'Téléchargement gratuit pour iPhone et iPad',
        'Premium iOS Apps for iPhone & iPad': 'Applications iOS Premium pour iPhone et iPad',
        'Home': 'Accueil',
        'All Apps': 'Toutes les applications',
        'Apps': 'Applications',
        'Privacy': 'Confidentialité',
        'Privacy Policy': 'Politique de confidentialité',
        'Contact': 'Contact',
        'Education': 'Éducation',
        'AI & Photo': 'IA et Photo',
        'Language': 'Langue',
        'Home Design': 'Design d\'intérieur',
        'Identifier': 'Identification',
        'Other': 'Autre',
        'About': 'À propos',
        'Features': 'Fonctionnalités',
        'Key Features': 'Fonctionnalités principales',
        'FAQ': 'FAQ',
        'Frequently Asked Questions': 'Questions fréquemment posées',
        'Download on the': 'Télécharger sur l\'',
        'App Store': 'App Store',
        'Download Free': 'Télécharger gratuitement',
        'Free Download': 'Téléchargement gratuit',
        'Free on App Store': 'Gratuit sur l\'App Store',
        'Get it on App Store': 'Télécharger sur l\'App Store',
        'for iPhone & iPad': 'pour iPhone et iPad',
        'for iPhone and iPad': 'pour iPhone et iPad',
        'iPhone & iPad': 'iPhone et iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'offre une expérience puissante et intuitive conçue spécifiquement pour les utilisateurs iOS exigeants',
        'Whether you\'re a professional seeking advanced features or a beginner looking for an easy-to-use solution': 'Que vous soyez un professionnel à la recherche de fonctionnalités avancées ou un débutant cherchant une solution facile à utiliser',
        'our app provides everything you need in one streamlined package': 'notre application fournit tout ce dont vous avez besoin dans un package optimisé',
        'Developed with cutting-edge technology and refined through extensive user feedback': 'Développée avec une technologie de pointe et affinée grâce aux retours utilisateurs',
        'has earned its place as a top-rated application': 'a gagné sa place en tant qu\'application de premier plan',
        'in the': 'dans la catégorie',
        'category on the App Store': 'sur l\'App Store',
        'Our team continuously updates the app with new features, performance improvements, and enhanced functionality': 'Notre équipe met continuellement à jour l\'application avec de nouvelles fonctionnalités et améliorations',
        'to ensure you always have access to the latest innovations': 'pour vous assurer un accès aux dernières innovations',
        'With millions of downloads worldwide and consistently high ratings': 'Avec des millions de téléchargements dans le monde et des évaluations toujours élevées',
        'has become the trusted choice for users across the globe': 'est devenue le choix de confiance pour les utilisateurs du monde entier',
        'The app features a clean, modern interface that makes complex tasks simple': 'L\'application dispose d\'une interface moderne et épurée qui simplifie les tâches complexes',
        'while providing the depth and capabilities that power users require': 'tout en offrant la profondeur et les capacités requises par les utilisateurs avancés',
        'Download': 'Téléchargez',
        'today and discover why it\'s the preferred choice for discerning iOS users': 'aujourd\'hui et découvrez pourquoi c\'est le choix préféré des utilisateurs iOS exigeants',
        'Available exclusively on the App Store for iPhone and iPad devices running iOS 15.0 or later': 'Disponible exclusivement sur l\'App Store pour iPhone et iPad sous iOS 15.0 ou ultérieur',
        'Today': 'Aujourd\'hui',
        'Join millions of satisfied users': 'Rejoignez des millions d\'utilisateurs satisfaits',
        'Free on the App Store for iPhone and iPad': 'Gratuit sur l\'App Store pour iPhone et iPad',
        'Is': 'Est-ce que',
        'free to download': 'gratuit à télécharger',
        'Yes': 'Oui',
        'completely free to download from the App Store': 'entièrement gratuit à télécharger sur l\'App Store',
        'Some premium features may be available through optional in-app purchases': 'Certaines fonctionnalités premium peuvent être disponibles via des achats intégrés optionnels',
        'What devices are compatible with': 'Quels appareils sont compatibles avec',
        'is designed for iPhone and iPad devices running iOS 15.0 or later': 'est conçu pour les iPhone et iPad sous iOS 15.0 ou ultérieur',
        'The app is optimized for all screen sizes': 'L\'application est optimisée pour toutes les tailles d\'écran',
        'ensuring a great experience on any compatible device': 'garantissant une excellente expérience sur tout appareil compatible',
        'How do I get started with': 'Comment commencer avec',
        'Simply download': 'Téléchargez simplement',
        'from the App Store and follow the intuitive setup process': 'depuis l\'App Store et suivez le processus de configuration intuitif',
        'The app includes helpful onboarding guides to help you make the most of all features': 'L\'application comprend des guides utiles pour vous aider à tirer le meilleur parti de toutes les fonctionnalités',
        'Is my data safe with': 'Mes données sont-elles en sécurité avec',
        'We prioritize your privacy and security': 'Nous priorisons votre confidentialité et votre sécurité',
        'Your data is stored securely and we never share your personal information with third parties': 'Vos données sont stockées en toute sécurité et nous ne partageons jamais vos informations personnelles avec des tiers',
        'Please review our Privacy Policy for more details': 'Veuillez consulter notre politique de confidentialité pour plus de détails',
        'All rights reserved': 'Tous droits réservés',
        'Terms of Service': 'Conditions d\'utilisation',
        'Learn more': 'En savoir plus',
        'Get started': 'Commencer',
        'Try now': 'Essayer maintenant',
        'No': 'Non',
    },
    'es': {
        'Free Download for iPhone & iPad': 'Descarga gratuita para iPhone y iPad',
        'Premium iOS Apps for iPhone & iPad': 'Aplicaciones iOS Premium para iPhone y iPad',
        'Home': 'Inicio',
        'All Apps': 'Todas las aplicaciones',
        'Apps': 'Aplicaciones',
        'Privacy': 'Privacidad',
        'Privacy Policy': 'Política de privacidad',
        'Contact': 'Contacto',
        'Education': 'Educación',
        'AI & Photo': 'IA y Foto',
        'Language': 'Idioma',
        'Home Design': 'Diseño del hogar',
        'Identifier': 'Identificador',
        'Other': 'Otro',
        'About': 'Acerca de',
        'Features': 'Características',
        'Key Features': 'Características principales',
        'FAQ': 'Preguntas frecuentes',
        'Frequently Asked Questions': 'Preguntas frecuentes',
        'Download on the': 'Descargar en',
        'App Store': 'App Store',
        'Download Free': 'Descargar gratis',
        'Free Download': 'Descarga gratuita',
        'Free on App Store': 'Gratis en App Store',
        'Get it on App Store': 'Obtener en App Store',
        'for iPhone & iPad': 'para iPhone y iPad',
        'for iPhone and iPad': 'para iPhone y iPad',
        'iPhone & iPad': 'iPhone y iPad',
        'delivers a powerful, intuitive experience designed specifically for iOS users who demand the best': 'ofrece una experiencia potente e intuitiva diseñada específicamente para usuarios de iOS que exigen lo mejor',
        'Whether you\'re a professional seeking advanced features or a beginner looking for an easy-to-use solution': 'Ya seas un profesional que busca funciones avanzadas o un principiante que busca una solución fácil de usar',
        'our app provides everything you need in one streamlined package': 'nuestra aplicación proporciona todo lo que necesitas en un paquete optimizado',
        'Developed with cutting-edge technology and refined through extensive user feedback': 'Desarrollada con tecnología de vanguardia y perfeccionada a través de comentarios de usuarios',
        'has earned its place as a top-rated application': 'se ha ganado su lugar como una aplicación de primer nivel',
        'in the': 'en la categoría de',
        'category on the App Store': 'en App Store',
        'Our team continuously updates the app with new features, performance improvements, and enhanced functionality': 'Nuestro equipo actualiza continuamente la aplicación con nuevas funciones y mejoras de rendimiento',
        'to ensure you always have access to the latest innovations': 'para asegurar que siempre tengas acceso a las últimas innovaciones',
        'With millions of downloads worldwide and consistently high ratings': 'Con millones de descargas en todo el mundo y calificaciones constantemente altas',
        'has become the trusted choice for users across the globe': 'se ha convertido en la opción de confianza para usuarios de todo el mundo',
        'The app features a clean, modern interface that makes complex tasks simple': 'La aplicación cuenta con una interfaz limpia y moderna que simplifica tareas complejas',
        'while providing the depth and capabilities that power users require': 'mientras proporciona la profundidad y capacidades que los usuarios avanzados requieren',
        'Download': 'Descarga',
        'today and discover why it\'s the preferred choice for discerning iOS users': 'hoy y descubre por qué es la opción preferida de los usuarios de iOS exigentes',
        'Available exclusively on the App Store for iPhone and iPad devices running iOS 15.0 or later': 'Disponible exclusivamente en App Store para iPhone y iPad con iOS 15.0 o posterior',
        'Today': 'Hoy',
        'Join millions of satisfied users': 'Únete a millones de usuarios satisfechos',
        'Free on the App Store for iPhone and iPad': 'Gratis en App Store para iPhone y iPad',
        'Is': '¿Es',
        'free to download': 'gratis para descargar',
        'Yes': 'Sí',
        'completely free to download from the App Store': 'completamente gratis para descargar desde App Store',
        'Some premium features may be available through optional in-app purchases': 'Algunas funciones premium pueden estar disponibles a través de compras opcionales dentro de la aplicación',
        'What devices are compatible with': '¿Qué dispositivos son compatibles con',
        'is designed for iPhone and iPad devices running iOS 15.0 or later': 'está diseñada para iPhone y iPad con iOS 15.0 o posterior',
        'The app is optimized for all screen sizes': 'La aplicación está optimizada para todos los tamaños de pantalla',
        'ensuring a great experience on any compatible device': 'garantizando una excelente experiencia en cualquier dispositivo compatible',
        'How do I get started with': '¿Cómo empiezo con',
        'Simply download': 'Simplemente descarga',
        'from the App Store and follow the intuitive setup process': 'desde App Store y sigue el proceso de configuración intuitivo',
        'The app includes helpful onboarding guides to help you make the most of all features': 'La aplicación incluye guías útiles para ayudarte a aprovechar al máximo todas las funciones',
        'Is my data safe with': '¿Están mis datos seguros con',
        'We prioritize your privacy and security': 'Priorizamos tu privacidad y seguridad',
        'Your data is stored securely and we never share your personal information with third parties': 'Tus datos se almacenan de forma segura y nunca compartimos tu información personal con terceros',
        'Please review our Privacy Policy for more details': 'Por favor revisa nuestra Política de Privacidad para más detalles',
        'All rights reserved': 'Todos los derechos reservados',
        'Terms of Service': 'Términos de servicio',
        'Learn more': 'Saber más',
        'Get started': 'Comenzar',
        'Try now': 'Probar ahora',
        'No': 'No',
    },
    'it': {
        'Free Download for iPhone & iPad': 'Download gratuito per iPhone e iPad',
        'Premium iOS Apps for iPhone & iPad': 'App iOS Premium per iPhone e iPad',
        'Home': 'Home',
        'All Apps': 'Tutte le App',
        'Apps': 'App',
        'Privacy': 'Privacy',
        'Privacy Policy': 'Informativa sulla privacy',
        'Contact': 'Contatti',
        'Education': 'Istruzione',
        'AI & Photo': 'IA e Foto',
        'Download on the': 'Scarica su',
        'App Store': 'App Store',
        'Download Free': 'Scarica gratis',
        'Free Download': 'Download gratuito',
        'Free on App Store': 'Gratis su App Store',
        'for iPhone & iPad': 'per iPhone e iPad',
        'for iPhone and iPad': 'per iPhone e iPad',
        'About': 'Informazioni',
        'Features': 'Funzionalità',
        'Key Features': 'Funzionalità principali',
        'FAQ': 'FAQ',
        'Frequently Asked Questions': 'Domande frequenti',
        'Today': 'Oggi',
        'Join millions of satisfied users': 'Unisciti a milioni di utenti soddisfatti',
        'Free on the App Store for iPhone and iPad': 'Gratis su App Store per iPhone e iPad',
        'Yes': 'Sì',
        'No': 'No',
        'All rights reserved': 'Tutti i diritti riservati',
    },
    'nl': {
        'Free Download for iPhone & iPad': 'Gratis download voor iPhone en iPad',
        'Premium iOS Apps for iPhone & iPad': 'Premium iOS-apps voor iPhone en iPad',
        'Home': 'Home',
        'All Apps': 'Alle Apps',
        'Apps': 'Apps',
        'Privacy': 'Privacy',
        'Privacy Policy': 'Privacybeleid',
        'Contact': 'Contact',
        'Education': 'Onderwijs',
        'AI & Photo': 'AI & Foto',
        'Download on the': 'Download op de',
        'App Store': 'App Store',
        'Download Free': 'Gratis downloaden',
        'Free Download': 'Gratis download',
        'Free on App Store': 'Gratis in App Store',
        'for iPhone & iPad': 'voor iPhone en iPad',
        'for iPhone and iPad': 'voor iPhone en iPad',
        'About': 'Over',
        'Features': 'Functies',
        'Key Features': 'Belangrijkste functies',
        'FAQ': 'FAQ',
        'Frequently Asked Questions': 'Veelgestelde vragen',
        'Today': 'Vandaag',
        'Join millions of satisfied users': 'Sluit je aan bij miljoenen tevreden gebruikers',
        'Free on the App Store for iPhone and iPad': 'Gratis in App Store voor iPhone en iPad',
        'Yes': 'Ja',
        'No': 'Nee',
        'All rights reserved': 'Alle rechten voorbehouden',
    },
    'pt': {
        'Free Download for iPhone & iPad': 'Download gratuito para iPhone e iPad',
        'Premium iOS Apps for iPhone & iPad': 'Apps iOS Premium para iPhone e iPad',
        'Home': 'Início',
        'All Apps': 'Todos os Apps',
        'Apps': 'Apps',
        'Privacy': 'Privacidade',
        'Privacy Policy': 'Política de privacidade',
        'Contact': 'Contato',
        'Education': 'Educação',
        'AI & Photo': 'IA e Foto',
        'Download on the': 'Baixar na',
        'App Store': 'App Store',
        'Download Free': 'Baixar grátis',
        'Free Download': 'Download grátis',
        'Free on App Store': 'Grátis na App Store',
        'for iPhone & iPad': 'para iPhone e iPad',
        'for iPhone and iPad': 'para iPhone e iPad',
        'About': 'Sobre',
        'Features': 'Recursos',
        'Key Features': 'Recursos principais',
        'FAQ': 'Perguntas frequentes',
        'Frequently Asked Questions': 'Perguntas frequentes',
        'Today': 'Hoje',
        'Join millions of satisfied users': 'Junte-se a milhões de usuários satisfeitos',
        'Free on the App Store for iPhone and iPad': 'Grátis na App Store para iPhone e iPad',
        'Yes': 'Sim',
        'No': 'Não',
        'All rights reserved': 'Todos os direitos reservados',
    },
    'pl': {
        'Free Download for iPhone & iPad': 'Bezpłatne pobieranie na iPhone i iPad',
        'Home': 'Strona główna',
        'All Apps': 'Wszystkie aplikacje',
        'Apps': 'Aplikacje',
        'Privacy': 'Prywatność',
        'Education': 'Edukacja',
        'Download on the': 'Pobierz z',
        'App Store': 'App Store',
        'Download Free': 'Pobierz za darmo',
        'Free Download': 'Bezpłatne pobieranie',
        'Free on App Store': 'Za darmo w App Store',
        'for iPhone & iPad': 'na iPhone i iPad',
        'About': 'O aplikacji',
        'Features': 'Funkcje',
        'FAQ': 'FAQ',
        'Today': 'Dziś',
        'Join millions of satisfied users': 'Dołącz do milionów zadowolonych użytkowników',
        'Yes': 'Tak',
        'No': 'Nie',
    },
    'sv': {
        'Free Download for iPhone & iPad': 'Gratis nedladdning för iPhone och iPad',
        'Home': 'Hem',
        'All Apps': 'Alla appar',
        'Apps': 'Appar',
        'Privacy': 'Integritet',
        'Education': 'Utbildning',
        'Download on the': 'Ladda ner på',
        'App Store': 'App Store',
        'Download Free': 'Ladda ner gratis',
        'Free Download': 'Gratis nedladdning',
        'Free on App Store': 'Gratis i App Store',
        'for iPhone & iPad': 'för iPhone och iPad',
        'About': 'Om',
        'Features': 'Funktioner',
        'FAQ': 'FAQ',
        'Today': 'Idag',
        'Join millions of satisfied users': 'Gå med miljontals nöjda användare',
        'Yes': 'Ja',
        'No': 'Nej',
    },
    'da': {
        'Free Download for iPhone & iPad': 'Gratis download til iPhone og iPad',
        'Home': 'Hjem',
        'All Apps': 'Alle apps',
        'Apps': 'Apps',
        'Privacy': 'Privatliv',
        'Education': 'Uddannelse',
        'Download on the': 'Download på',
        'App Store': 'App Store',
        'Download Free': 'Download gratis',
        'Free Download': 'Gratis download',
        'Free on App Store': 'Gratis i App Store',
        'for iPhone & iPad': 'til iPhone og iPad',
        'About': 'Om',
        'Features': 'Funktioner',
        'FAQ': 'FAQ',
        'Today': 'I dag',
        'Join millions of satisfied users': 'Slut dig til millioner af tilfredse brugere',
        'Yes': 'Ja',
        'No': 'Nej',
    },
    'no': {
        'Free Download for iPhone & iPad': 'Gratis nedlasting for iPhone og iPad',
        'Home': 'Hjem',
        'All Apps': 'Alle apper',
        'Apps': 'Apper',
        'Privacy': 'Personvern',
        'Education': 'Utdanning',
        'Download on the': 'Last ned fra',
        'App Store': 'App Store',
        'Download Free': 'Last ned gratis',
        'Free Download': 'Gratis nedlasting',
        'Free on App Store': 'Gratis i App Store',
        'for iPhone & iPad': 'for iPhone og iPad',
        'About': 'Om',
        'Features': 'Funksjoner',
        'FAQ': 'FAQ',
        'Today': 'I dag',
        'Join millions of satisfied users': 'Bli med millioner av fornøyde brukere',
        'Yes': 'Ja',
        'No': 'Nei',
    },
}

def translate_content(text, lang):
    """Translate text using dictionary with longest match first"""
    if not text:
        return text
    
    translations = TRANSLATIONS.get(lang, {})
    result = text
    
    # Sort by length (longest first) to avoid partial replacements
    for eng, translated in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(eng, translated)
    
    return result

def process_html(content, lang):
    """Process HTML content with translations"""
    soup = BeautifulSoup(content, 'html.parser')
    
    # Update HTML lang
    html_tag = soup.find('html')
    if html_tag:
        html_tag['lang'] = lang
    
    # Translate title
    title = soup.find('title')
    if title and title.string:
        title.string = translate_content(str(title.string), lang)
    
    # Translate meta description
    for meta in soup.find_all('meta', attrs={'name': 'description'}):
        if meta.get('content'):
            meta['content'] = translate_content(meta['content'], lang)
    
    # Translate og:title and og:description
    for meta in soup.find_all('meta', attrs={'property': ['og:title', 'og:description']}):
        if meta.get('content'):
            meta['content'] = translate_content(meta['content'], lang)
    
    # Add og:locale
    og_locale = soup.find('meta', attrs={'property': 'og:locale'})
    if og_locale:
        og_locale['content'] = LANGUAGES[lang]
    else:
        og_type = soup.find('meta', attrs={'property': 'og:type'})
        if og_type:
            new_meta = soup.new_tag('meta')
            new_meta['property'] = 'og:locale'
            new_meta['content'] = LANGUAGES[lang]
            og_type.insert_before(new_meta)
    
    # Translate all text content
    text_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'li', 'button', 'label', 'strong', 'em']
    for tag_name in text_tags:
        for el in soup.find_all(tag_name):
            if el.string:
                el.string = translate_content(str(el.string), lang)
    
    return str(soup)

def add_hreflang(content, app_slug, lang):
    """Add hreflang tags"""
    soup = BeautifulSoup(content, 'html.parser')
    head = soup.find('head')
    if not head:
        return content
    
    # Remove existing hreflang
    for link in list(soup.find_all('link', rel='alternate')):
        if link and hasattr(link, 'get') and link.get('hreflang'):
            link.decompose()
    
    # Add hreflang tags
    base = f"https://apps.utkuapps.com/{app_slug}/"
    
    tags = [
        ('en', base),
        ('x-default', base),
    ]
    for l in LANGUAGES.keys():
        tags.append((l, f"https://apps.utkuapps.com/{l}/{app_slug}/"))
    
    for hreflang, href in tags:
        link = soup.new_tag('link')
        link['rel'] = 'alternate'
        link['hreflang'] = hreflang
        link['href'] = href
        head.append(link)
    
    return str(soup)

def fix_paths(content, lang):
    """Fix asset paths for subdirectory"""
    content = content.replace('href="../css/', 'href="../../css/')
    content = content.replace('href="../js/', 'href="../../js/')
    content = content.replace('src="../icons/', 'src="../../icons/')
    content = content.replace('src="../images/', 'src="../../images/')
    return content

def generate_pages():
    """Generate all translated pages"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    
    apps = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude:
            if (item / 'index.html').exists():
                apps.append(item.name)
    
    print(f"📁 Found {len(apps)} apps")
    total = 0
    
    for lang in LANGUAGES.keys():
        print(f"\n🌍 {lang.upper()}...", flush=True)
        lang_dir = BASE_DIR / lang
        lang_dir.mkdir(exist_ok=True)
        
        for app in apps:
            src = BASE_DIR / app / 'index.html'
            dest_dir = lang_dir / app
            dest_dir.mkdir(exist_ok=True)
            
            try:
                with open(src, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = process_html(content, lang)
                content = add_hreflang(content, app, lang)
                content = fix_paths(content, lang)
                
                with open(dest_dir / 'index.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                total += 1
                print(f"  ✅ {app}")
            except Exception as e:
                print(f"  ❌ {app}: {e}")
    
    return total

def update_english_hreflang():
    """Add hreflang to English pages"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    count = 0
    
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name not in exclude:
            index = item / 'index.html'
            if index.exists():
                with open(index, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = add_hreflang(content, item.name, 'en')
                with open(index, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    
    print(f"✅ Updated {count} English pages")
    return count

def generate_sitemaps():
    """Generate sitemaps with hreflang"""
    exclude = {'css', 'js', 'icons', 'images', '.git', 'node_modules', 'privacy'} | set(LANGUAGES.keys())
    
    # English sitemap
    apps = [d.name for d in BASE_DIR.iterdir() if d.is_dir() and d.name not in exclude and (d / 'index.html').exists()]
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    
    for app in apps:
        url = f"https://apps.utkuapps.com/{app}/"
        sitemap += f'  <url>\n    <loc>{url}</loc>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="{url}"/>\n'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url}"/>\n'
        for lang in LANGUAGES.keys():
            sitemap += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="https://apps.utkuapps.com/{lang}/{app}/"/>\n'
        sitemap += '    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n  </url>\n'
    
    sitemap += '</urlset>'
    
    with open(BASE_DIR / 'sitemap-en.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"📄 sitemap-en.xml: {len(apps)} URLs")
    
    # Language sitemaps
    for lang in LANGUAGES.keys():
        lang_dir = BASE_DIR / lang
        if lang_dir.exists():
            lang_apps = [d.name for d in lang_dir.iterdir() if d.is_dir() and (d / 'index.html').exists()]
            
            sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            
            for app in lang_apps:
                url = f"https://apps.utkuapps.com/{lang}/{app}/"
                sitemap += f'  <url>\n    <loc>{url}</loc>\n'
                sitemap += f'    <xhtml:link rel="alternate" hreflang="en" href="https://apps.utkuapps.com/{app}/"/>\n'
                sitemap += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://apps.utkuapps.com/{app}/"/>\n'
                for l in LANGUAGES.keys():
                    sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://apps.utkuapps.com/{l}/{app}/"/>\n'
                sitemap += '    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
            
            sitemap += '</urlset>'
            
            with open(BASE_DIR / f'sitemap-{lang}.xml', 'w', encoding='utf-8') as f:
                f.write(sitemap)
            print(f"📄 sitemap-{lang}.xml: {len(lang_apps)} URLs")
    
    # Sitemap index
    index = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    index += '  <sitemap><loc>https://apps.utkuapps.com/sitemap-en.xml</loc></sitemap>\n'
    for lang in LANGUAGES.keys():
        index += f'  <sitemap><loc>https://apps.utkuapps.com/sitemap-{lang}.xml</loc></sitemap>\n'
    index += '</sitemapindex>'
    
    with open(BASE_DIR / 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(index)
    print("📄 sitemap.xml (index)")

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 OPTIMIZED FULL TRANSLATION")
    print("=" * 60)
    
    total = generate_pages()
    update_english_hreflang()
    generate_sitemaps()
    
    print("\n" + "=" * 60)
    print(f"✅ DONE! {total} pages across {len(LANGUAGES)} languages")
    print("=" * 60)
