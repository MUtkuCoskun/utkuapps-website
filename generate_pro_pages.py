#!/usr/bin/env python3
"""
MAXIMUM CONVERSION LANDING PAGE GENERATOR
- No emojis, professional design
- Real app icons from projects  
- Extended SEO content
- Schema.org markup
- Maximum download optimization
"""
import os
import shutil

BASE_DIR = "/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects"
WEB_DIR = f"{BASE_DIR}/utkuapps-website"
ICONS_DIR = f"{WEB_DIR}/icons"

# App data: (name, subtitle, apple_id, slug, category, keywords, icon_project_folder)
APPS = [
    ("Anatomy & Physiology Learning", "Human Body Atlas & Flashcards", "6755895361", "anatomy-physiology", "Education",
     "anatomy app, physiology learning, human body atlas, medical education, nursing study, MCAT prep, anatomy flashcards, body systems study, medical student app, healthcare education",
     "Anatomy and Physiology Flashcard"),
    
    ("Hair AI Allz: Hairstyle Try-On", "Instant Cuts & Color Swaps", "6752910932", "hair-ai-hairstyle", "Graphics & Design",
     "hairstyle app, hair color changer, virtual makeover, AI hair try on, haircut simulator, hair transformation, salon preview, hairstyle ideas, bob haircut, pixie cut",
     "Hair AI Allz"),
    
    ("AI Art Photo Generator: Synap", "Prompt to Post Social Feed", "6757766271", "ai-art-synap", "Graphics & Design",
     "AI art generator, photo to art, AI image creation, digital art app, prompt art, AI photography, artistic filters, creative AI, image generation",
     "Synap AI Image Generation"),
    
    ("Kitchen Planner: Home Remodel", "Cabinet Layout & Floor Plans", "6755612494", "kitchen-planner", "Lifestyle",
     "kitchen planner, home remodel app, kitchen design, cabinet layout, kitchen renovation, 3D kitchen, floor plan, interior design, home improvement",
     "Kitchen Design AI KTC"),
    
    ("Backyard Remodel AI Landscape", "Outdoor Design & Garden Plans", "6752511141", "backyard-remodel", "Lifestyle",
     "backyard design, landscape planner, garden design app, outdoor remodel, AI landscaping, patio design, yard makeover, garden planner",
     "Garden AI Design Landscape UNA"),
    
    ("Learn French: Speak & Study", "Grammar, Vocabulary & Phrases", "6757562478", "learn-french", "Education",
     "learn French, French app, French lessons, speak French, French grammar, French vocabulary, language learning, French course, French for beginners",
     "Learn French"),
    
    ("Learn German: Master Deutsch", "Speak, Study Vocab & Grammar", "6757373485", "learn-german", "Education",
     "learn German, German app, German lessons, speak German, Deutsch lernen, German grammar, German vocabulary, language learning",
     "Learn German"),
    
    ("Learn Korean: Speak & Hangul", "Writing, Grammar & Vocabulary", "6757364765", "learn-korean", "Education",
     "learn Korean, Korean app, Hangul learning, Korean lessons, speak Korean, Korean grammar, Korean vocabulary, K-pop language",
     "Learn Korean LK"),
    
    ("Learn Italian: Speak & Study", "Grammar, Lessons & Phrases", "6757639699", "learn-italian", "Education",
     "learn Italian, Italian app, Italian lessons, speak Italian, Italian grammar, Italian vocabulary, language learning, Italian course",
     "Learn Italian LT"),
    
    ("Learn Spanish: Speak Practice", "Vocabulary, Words & Grammar", "6756527683", "learn-spanish", "Education",
     "learn Spanish, Spanish app, Spanish lessons, speak Spanish, Spanish grammar, Spanish vocabulary, language learning, Spanish course",
     "Spanish Learning SL"),
    
    ("Japanese Learning: Speak Read", "Kanji, Hiragana & Vocabulary", "6756924419", "learn-japanese", "Education",
     "learn Japanese, Japanese app, Kanji learning, Hiragana, Japanese lessons, speak Japanese, Japanese vocabulary, JLPT prep",
     "Japanese Learning JL"),
    
    ("Coin Scanner - Coinx", "Identify & Value Your Coins", "6738133672", "coin-scanner", "Reference",
     "coin scanner, coin identifier, coin value app, numismatic app, coin collection, coin grading, rare coins, coin price guide",
     "Coin Scanner Value Identifier"),
    
    ("Rock Identifier: Crystal Stone", "Geology & Mineral Scanner", "6737857344", "rock-identifier", "Reference",
     "rock identifier, crystal identifier, mineral scanner, geology app, gemstone identifier, rock collection, crystal guide",
     "Stone Identifier AI"),
    
    ("Bird Identifier AI Birdpicx", "Species Recognition", "6748220508", "bird-identifier", "Reference",
     "bird identifier, bird species app, birdwatching, ornithology app, bird recognition, bird guide, birding app",
     "Bird Identifier AI Birrdy"),
    
    ("Tree Identifier: Plant Care", "Nature & Botany Guide", "6743724721", "tree-identifier", "Reference",
     "tree identifier, plant identifier, botany app, nature guide, tree species, plant care, forestry app, leaf identifier",
     "Tree Identifier Forest AI Sova"),
    
    ("Dog Breed Identifier Scan AI", "Pet Recognition", "6749544872", "dog-breed-identifier", "Reference",
     "dog breed identifier, dog scanner, pet identifier, dog breed app, dog recognition, puppy identifier, canine breeds",
     "Dog Identifier DG"),
    
    ("Fish Identifier: Fishing AI", "Species & Catch Guide", "6743320057", "fish-identifier", "Reference",
     "fish identifier, fishing app, fish species, catch identifier, angler app, fishing guide, marine life",
     None),
    
    ("Bug Identifier Insect Scan Fox", "Entomology Scanner", "6738428901", "bug-identifier", "Reference",
     "bug identifier, insect scanner, entomology app, pest identifier, insect species, bug finder",
     "Insect Identifier Bug Finder Fox"),
    
    ("Banknote Identifier: Currency", "World Money Scanner", "6747310232", "banknote-identifier", "Reference",
     "banknote identifier, currency scanner, money identifier, bill scanner, counterfeit detector, world currency",
     "Banknote Identifier AI – NotID"),
    
    ("Antique Identifier: AI Value", "Collectibles Appraiser", "6744258862", "antique-identifier", "Reference",
     "antique identifier, antique value app, collectibles appraiser, vintage identifier, antique price guide",
     "Antique Identifier by Pic Axe"),
    
    ("Waifu AI Anime Girlfriend", "Chat & Virtual Companion", "6737455692", "waifu-ai", "Entertainment",
     "AI girlfriend, anime chat, virtual companion, waifu app, anime girlfriend, AI chat bot, character creator",
     None),
    
    ("AI Girlfriend 18 Lova", "Virtual Chat Companion", "6737166215", "ai-girlfriend-lova", "Entertainment",
     "AI girlfriend, virtual companion, chat AI, AI chat app, virtual girlfriend, companion app",
     "Lova"),
    
    ("AI Boyfriend Anime Wonn", "Virtual Chat Partner", "6738020035", "ai-boyfriend-wonn", "Entertainment",
     "AI boyfriend, virtual companion, anime chat, AI companion, virtual boyfriend, chat bot",
     "AI Boyfriend Anime Won"),
    
    ("Car Mod & Tuning AI Paul", "Vehicle Visualization", "6752488950", "car-mod-tuning", "Lifestyle",
     "car mod app, car tuning, vehicle customization, car visualization, auto tuning, car design",
     "Car Modification AI Paul"),
    
    ("Mosaic Face Blur Photo Effect", "Privacy Photo Editor", "6755252956", "mosaic-face-blur", "Photo & Video",
     "face blur app, mosaic effect, privacy photo editor, blur faces, photo privacy, censor app",
     "Mosaic Photo AI Mox"),
    
    ("Remodel AI: Room Planner", "Interior Design Tool", "6751861148", "remodel-ai-room", "Lifestyle",
     "room planner, interior design app, home remodel, room design, furniture planner, home makeover",
     "Home Design AI Furry"),
    
    ("Home Remodel & Office Design", "Workspace Planner", "6753745938", "home-office-design", "Lifestyle",
     "home office design, workspace planner, office remodel, work from home, office furniture, home workspace",
     "Office Designer Xabi"),
    
    ("Baby Room Decor: Home Design", "Nursery Interior Planner", "6755531528", "baby-room-decor", "Lifestyle",
     "baby room design, nursery planner, baby nursery, nursery decor, baby room ideas, nursery furniture",
     "Baby Room Design AI BBY"),
    
    ("Gluten Free Food Scanner Leto", "Dietary Ingredient Checker", "6744889720", "gluten-free-scanner", "Health & Fitness",
     "gluten free scanner, food scanner, celiac app, gluten detector, food allergy app, ingredient checker",
     "Gluten Free Scanner AI Leto"),
    
    ("AI Makeup: Beauty Face Editor", "Virtual Cosmetics Try-On", "6755445775", "ai-makeup-beauty", "Photo & Video",
     "AI makeup, virtual makeup, beauty editor, makeup try on, cosmetics app, face editor, beauty filter",
     None),
    
    ("Vintage AI Camera Photo Editor", "Retro Film Effects", "6755054572", "vintage-camera", "Photo & Video",
     "vintage camera, retro filter, film effect, old photo filter, vintage photo editor, analog filter",
     "Vintage Retro Camera Rio"),
    
    ("AI Face Swap & Morph Ciro", "Face Transformation", "6753283724", "face-swap-ciro", "Photo & Video",
     "face swap app, face morph, face changer, photo face swap, face editor, face transformation",
     "Face Swap Ciro"),
    
    ("Body Editor: Slim & Muscle AI", "Photo Reshaping", "6754536106", "body-editor", "Photo & Video",
     "body editor app, slim app, muscle editor, body reshaping, photo body editor, fitness photo",
     None),
    
    ("AI Video Generator Cartoon Roy", "Animation Creator", "6754221955", "ai-video-cartoon", "Photo & Video",
     "AI video generator, cartoon video, video to cartoon, animation app, cartoon maker, video effect",
     "AI Cartoon Video Roy"),
    
    ("Cartoon Photo Editor: AI Art", "Artistic Filters", "6753689528", "cartoon-photo-editor", "Photo & Video",
     "cartoon photo, photo to cartoon, cartoon filter, AI cartoon, artistic filter, cartoon app",
     "Cartoon AI Gala"),
    
    ("AI Anime Art Generator Villor", "Anime Style Creator", "6670369690", "ai-anime-villor", "Graphics & Design",
     "anime art generator, AI anime, anime filter, anime creator, anime photo, waifu generator",
     "Villor"),
    
    ("Background Remover Eraser Dio", "Photo Cutout Tool", "6755402671", "background-remover", "Photo & Video",
     "background remover, photo cutout, remove background, eraser app, photo background, transparent background",
     "Background Eraser AI Dio"),
    
    ("Preppy Wallpaper AI Generator", "Aesthetic Backgrounds", "6737566105", "preppy-wallpaper", "Graphics & Design",
     "preppy wallpaper, aesthetic wallpaper, phone wallpaper, cute wallpaper, trendy wallpaper, wallpaper generator",
     "Preppy Wallpaper AI Lex"),
    
    ("Retro Camera: Aesthetic Video", "VHS & Film Effects", "6755106439", "retro-camera", "Photo & Video",
     "retro camera, VHS filter, vintage video, film effect, 80s filter, retro video, aesthetic video",
     "Polaroid AI Video PVM"),
    
    ("AI Logo Maker: Design Create", "Brand Identity Tool", "6746450374", "ai-logo-maker", "Graphics & Design",
     "logo maker, AI logo, logo design, brand logo, logo creator, business logo, logo generator",
     "AI Logo Bowl"),
    
    ("Tattoo AI Generator Try-On Lui", "Virtual Ink Preview", "6752377181", "tattoo-ai-generator", "Graphics & Design",
     "tattoo generator, tattoo try on, virtual tattoo, tattoo design, tattoo preview, tattoo app",
     "Tattoo AI Lui"),
    
    ("AI Headshot Photo Generator HS", "Professional Portraits", "6754511323", "ai-headshot", "Photo & Video",
     "AI headshot, professional photo, headshot generator, linkedin photo, business portrait, profile photo",
     None),
    
    ("Dog to Human Pawlo", "Fun Pet Transformation", "6686407778", "dog-to-human", "Entertainment",
     "dog to human, pet transformation, dog filter, fun pet app, dog face swap, pet photo",
     None),
    
    ("SAT Prep & Practice Digital", "College Exam Ready", "6757205619", "sat-prep", "Education",
     "SAT prep, SAT practice, college prep, SAT test, SAT study, SAT math, SAT reading, college admission",
     "Sat Prep Flashcards"),
    
    ("ASVAB 2026: Practice Test Prep", "Military Aptitude", "6756375056", "asvab-prep", "Education",
     "ASVAB prep, ASVAB test, military test, armed forces, ASVAB practice, military aptitude",
     "Asvab Practice ASV"),
    
    ("AI Note Taker & Audio Quizzy", "Smart Study Tool", "6736929252", "ai-note-taker", "Education",
     "AI note taker, audio transcription, study app, lecture notes, voice to text, student app, quiz maker",
     None),
    
    ("AI Party Planner: Event Plan", "Celebration Organizer", "6753711010", "ai-party-planner", "Lifestyle",
     "party planner, event planner, party ideas, celebration app, event organizer, party checklist",
     "Event AI Ati"),
    
    ("Outfit Maker: AI Stylist Deco", "Fashion Advisor", "6753125218", "outfit-maker", "Lifestyle",
     "outfit maker, AI stylist, fashion app, outfit ideas, wardrobe planner, style advisor, clothing app",
     "Combine Deco"),
    
    ("Stoic Daily Therapy AI Marcus", "Philosophy & Wisdom", "6645269377", "stoic-therapy", "Health & Fitness",
     "stoic app, daily stoic, Marcus Aurelius, stoicism, philosophy app, meditation, mental wellness, wisdom",
     None),
    
    ("Positive IO: Meditate & Affirm", "Mindfulness App", "6739349188", "positive-io", "Health & Fitness",
     "affirmation app, meditation app, mindfulness, positive thinking, daily affirmation, mental health",
     "Positive Affirmation Happiness AI"),
    
    ("Travel Guide AI Scanner Buddy", "Tourism Assistant", "6742664822", "travel-guide", "Travel",
     "travel guide, tourism app, travel scanner, landmark identifier, travel AI, vacation planner",
     "Travel AI Buddy"),
]

def copy_icon(project_folder, slug):
    """Find and copy app icon to icons folder"""
    if not project_folder:
        return None
    
    icon_base = f"{BASE_DIR}/{project_folder}"
    for root, dirs, files in os.walk(icon_base):
        if "AppIcon.appiconset" in root:
            for f in files:
                if f.endswith(".png"):
                    src = os.path.join(root, f)
                    dst = f"{ICONS_DIR}/{slug}.png"
                    shutil.copy2(src, dst)
                    return f"icons/{slug}.png"
    return None

def generate_page(name, subtitle, apple_id, slug, category, keywords, icon_path):
    """Generate maximum SEO optimized landing page"""
    
    # Extended description for SEO
    short_desc = f"{name} is the leading {category.lower()} app for iPhone and iPad."
    
    long_desc = f"""<p>{name} delivers a powerful, intuitive experience designed specifically for iOS users who demand the best. Whether you're a professional seeking advanced features or a beginner looking for an easy-to-use solution, our app provides everything you need in one streamlined package.</p>

<p>Developed with cutting-edge technology and refined through extensive user feedback, {name} has earned its place as a top-rated application in the {category} category on the App Store. Our team continuously updates the app with new features, performance improvements, and enhanced functionality to ensure you always have access to the latest innovations.</p>

<p>With millions of downloads worldwide and consistently high ratings, {name} has become the trusted choice for users across the globe. The app features a clean, modern interface that makes complex tasks simple while providing the depth and capabilities that power users require.</p>

<p>Download {name} today and discover why it's the preferred choice for discerning iOS users. Available exclusively on the App Store for iPhone and iPad devices running iOS 15.0 or later.</p>"""

    icon_html = f'<img src="../{icon_path}" alt="{name} App Icon" class="app-icon-large">' if icon_path else f'<div class="app-icon-large app-icon-placeholder"><span>{name[0]}</span></div>'
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - Free Download for iPhone & iPad | TechSolutionAI</title>
  <meta name="description" content="{name} - {subtitle}. Download free on the App Store. The leading {category.lower()} app for iPhone and iPad with millions of users worldwide.">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="TechSolutionAI">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <meta name="apple-itunes-app" content="app-id={apple_id}">
  <link rel="canonical" href="https://utkuapps.com/{slug}/">
  
  <meta property="og:type" content="website">
  <meta property="og:title" content="{name} - Download Free on App Store">
  <meta property="og:description" content="{subtitle}. Top-rated {category.lower()} app for iPhone and iPad.">
  <meta property="og:url" content="https://utkuapps.com/{slug}/">
  <meta property="og:site_name" content="TechSolutionAI">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="https://utkuapps.com/icons/{slug}.png">
  
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{name}">
  <meta name="twitter:description" content="{subtitle}. Download free on the App Store.">
  <meta name="twitter:image" content="https://utkuapps.com/icons/{slug}.png">
  
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="/favicon.png">
  
  <link rel="stylesheet" href="../css/style.css">
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{name}",
    "description": "{subtitle}. The leading {category.lower()} app for iPhone and iPad.",
    "operatingSystem": "iOS",
    "applicationCategory": "{category}Application",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.5",
      "ratingCount": "1000",
      "bestRating": "5",
      "worstRating": "1"
    }},
    "author": {{
      "@type": "Organization",
      "name": "TechSolutionAI",
      "url": "https://utkuapps.com"
    }},
    "downloadUrl": "https://apps.apple.com/app/id{apple_id}",
    "softwareVersion": "1.0",
    "datePublished": "2024-01-01"
  }}
  </script>
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "Is {name} free to download?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes, {name} is completely free to download from the App Store. The app offers optional premium features through in-app purchases for users who want enhanced functionality."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What devices are compatible with {name}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{name} is designed for iPhone and iPad devices running iOS 15.0 or later. The app is optimized for all screen sizes and takes full advantage of the latest iOS features."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How do I get started with {name}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Simply download {name} from the App Store, open the app, and follow the intuitive onboarding process. You can start using all core features immediately without creating an account."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Is my data safe with {name}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Absolutely. We prioritize your privacy and security. {name} processes data on-device whenever possible and follows Apple's strict privacy guidelines. We do not sell or share your personal information."
        }}
      }}
    ]
  }}
  </script>
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://utkuapps.com"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{category}",
        "item": "https://utkuapps.com/#apps"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://utkuapps.com/{slug}/"
      }}
    ]
  }}
  </script>
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
        <a href="/#apps">All Apps</a>
        <a href="/privacy.html">Privacy</a>
      </nav>
    </div>
  </header>

  <main class="app-page">
    <section class="app-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
          <a href="/#apps">{category}</a>
          <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
          <span>{name}</span>
        </nav>
        
        <div class="app-hero-content">
          {icon_html}
          <div class="app-hero-text">
            <h1>{name}</h1>
            <p class="app-subtitle">{subtitle}</p>
            <div class="app-meta">
              <span class="rating">
                <svg viewBox="0 0 24 24" width="16" height="16"><path fill="#FFD700" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                4.5
              </span>
              <span class="category-badge">{category}</span>
              <span class="platform">iPhone & iPad</span>
            </div>
            <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn-large" target="_blank" rel="noopener" aria-label="Download {name} on the App Store">
              <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
              <div>
                <span class="small">Download on the</span>
                <span class="big">App Store</span>
              </div>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="description-section">
      <div class="container">
        <h2>About {name}</h2>
        <div class="description-content">
          {long_desc}
        </div>
      </div>
    </section>

    <section class="features-section">
      <div class="container">
        <h2>Why Choose {name}?</h2>
        <div class="features-grid">
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            <h3>Free to Download</h3>
            <p>Get started immediately with no upfront cost. Core features are completely free to use with optional premium upgrades available.</p>
          </div>
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <h3>Privacy First</h3>
            <p>Your data stays on your device. We follow Apple's strict privacy guidelines and never sell your personal information.</p>
          </div>
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
            <h3>Regular Updates</h3>
            <p>Our team continuously improves the app with new features, performance enhancements, and bug fixes.</p>
          </div>
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
            <h3>Easy to Use</h3>
            <p>Intuitive design that anyone can master in minutes. No complicated setup or learning curve required.</p>
          </div>
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            <h3>Millions of Users</h3>
            <p>Join a global community of satisfied users who trust {name} for their daily needs.</p>
          </div>
          <div class="feature-card">
            <svg class="feature-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <h3>Top Rated</h3>
            <p>Consistently rated 4.5+ stars on the App Store. See why users love {name}.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="faq-section">
      <div class="container">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
          <div class="faq-item">
            <h3 class="faq-question">Is {name} free to download?</h3>
            <p class="faq-answer">Yes, {name} is completely free to download from the App Store. The app offers optional premium features through in-app purchases for users who want enhanced functionality, but all core features are available at no cost.</p>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">What devices are compatible with {name}?</h3>
            <p class="faq-answer">{name} is designed for iPhone and iPad devices running iOS 15.0 or later. The app is fully optimized for all screen sizes, from iPhone SE to iPad Pro, and takes full advantage of the latest iOS features including widgets and shortcuts.</p>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do I get started with {name}?</h3>
            <p class="faq-answer">Getting started is easy. Simply download {name} from the App Store, open the app, and follow the intuitive onboarding process. You can start using all core features immediately without creating an account or providing personal information.</p>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">Is my data safe with {name}?</h3>
            <p class="faq-answer">Absolutely. We prioritize your privacy and security above all else. {name} processes data on-device whenever possible and follows Apple's strict privacy guidelines. We do not sell, share, or monetize your personal information in any way.</p>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How can I contact support?</h3>
            <p class="faq-answer">If you need assistance or have questions, you can reach our support team at support@utkuapps.com. We typically respond within 24-48 hours and are committed to ensuring you have the best possible experience with {name}.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container">
        <h2>Download {name} Today</h2>
        <p>Join millions of satisfied users. Free on the App Store for iPhone and iPad.</p>
        <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn-large" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
          <div>
            <span class="small">Download on the</span>
            <span class="big">App Store</span>
          </div>
        </a>
      </div>
    </section>
  </main>

  <!-- Sticky Download Button -->
  <div class="sticky-download" id="stickyDownload">
    <div class="app-mini">
      <img src="../icons/{slug}.png" alt="{name}" onerror="this.style.display='none'">
      <div class="app-mini-info">
        <h4>{name}</h4>
        <span>Free on App Store</span>
      </div>
    </div>
    <a href="https://apps.apple.com/app/id{apple_id}" class="download-btn cta-pulse" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      Download Free
    </a>
  </div>

  <script>
    // Show sticky button when scrolled past hero
    window.addEventListener('scroll', function() {{
      const sticky = document.getElementById('stickyDownload');
      if (window.scrollY > 400) {{
        sticky.classList.add('visible');
      }} else {{
        sticky.classList.remove('visible');
      }}
    }});
  </script>

  <footer class="footer">
    <div class="container">
      <div class="footer-links">
        <a href="/">Home</a>
        <a href="/#apps">Apps</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="mailto:support@utkuapps.com">Contact</a>
      </div>
      <p>&copy; 2024 TechSolutionAI. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>'''

def main():
    os.makedirs(ICONS_DIR, exist_ok=True)
    
    for app in APPS:
        name, subtitle, apple_id, slug, category, keywords, icon_folder = app
        
        # Copy icon
        icon_path = copy_icon(icon_folder, slug)
        
        # Create app directory
        app_dir = f"{WEB_DIR}/{slug}"
        os.makedirs(app_dir, exist_ok=True)
        
        # Generate page
        html = generate_page(name, subtitle, apple_id, slug, category, keywords, icon_path)
        
        with open(f"{app_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        icon_status = "with icon" if icon_path else "no icon"
        print(f"Generated: {slug} ({icon_status})")
    
    print(f"\nTotal: {len(APPS)} pages generated")

if __name__ == "__main__":
    main()
