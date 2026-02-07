#!/usr/bin/env python3
"""
Generate SEO-optimized landing pages for all UtkuApps iOS applications.
"""

import os

# App data: (name, apple_id, slug, category, description, keywords)
APPS = [
    # AI & Photo Editing
    ("Hair AI Allz: Hairstyle Try-On", "6752910932", "hair-ai-hairstyle-try-on", "ai-photo", "Try different hairstyles instantly with AI. See how you look with new hair colors, styles, and cuts before visiting the salon.", "hairstyle app, hair color changer, virtual makeover, AI hairstyle"),
    ("AI Art Photo Generator: Synap", "6757766271", "ai-art-photo-generator-synap", "ai-photo", "Transform your photos into stunning AI artwork. Create unique digital art with powerful AI image generation.", "AI art generator, photo to art, digital art creator, AI image"),
    ("Mosaic Face Blur Photo Effect", "6755252956", "mosaic-face-blur-photo", "ai-photo", "Blur faces and add mosaic effects to your photos. Protect privacy with easy-to-use censoring tools.", "face blur app, mosaic effect, censor photo, privacy blur"),
    ("AI Makeup: Beauty Face Editor", "6755445775", "ai-makeup-beauty-editor", "ai-photo", "Apply virtual makeup with AI. Try lipstick, eyeshadow, and more before buying.", "virtual makeup, beauty editor, makeup try on, face editor"),
    ("Vintage AI Camera Photo Editor", "6755054572", "vintage-ai-camera", "ai-photo", "Create nostalgic vintage photos with AI filters. Add retro effects to your images.", "vintage photo editor, retro filter, old photo effect, film camera"),
    ("AI Face Swap & Morph: Ciro", "6753283724", "ai-face-swap-ciro", "ai-photo", "Swap faces with celebrities, friends, or AI-generated faces. Create fun face morphs.", "face swap app, face morph, AI face changer, funny face"),
    ("Body Editor: Slim & Muscle AI", "6754536106", "body-editor-slim-muscle", "ai-photo", "Reshape and enhance body photos with AI. Add muscles or slim down for the perfect look.", "body editor, slim app, muscle editor, body reshape"),
    ("AI Video Generator Cartoon Roy", "6754221955", "ai-video-generator-cartoon", "ai-photo", "Convert videos to cartoons with AI. Create animated versions of your clips.", "video to cartoon, AI animation, cartoon video, video editor"),
    ("Cartoon Photo Editor: AI Art", "6753689528", "cartoon-photo-editor", "ai-photo", "Turn your photos into cartoons. Multiple cartoon styles powered by AI.", "cartoon photo, photo to cartoon, AI cartoon, toon effect"),
    ("Preppy Wallpaper AI Generator", "6737566105", "preppy-wallpaper-generator", "ai-photo", "Generate aesthetic preppy wallpapers with AI. Custom backgrounds for your phone.", "preppy wallpaper, aesthetic background, wallpaper generator, cute wallpaper"),
    ("AI Anime Art Generator Villor", "6670369690", "ai-anime-art-villor", "ai-photo", "Create anime art from photos with AI. Transform yourself into an anime character.", "anime art generator, photo to anime, AI anime, manga art"),
    ("Background Remover: Eraser Dio", "6755402671", "background-remover-dio", "ai-photo", "Remove photo backgrounds instantly with AI. Create transparent or custom backgrounds.", "background remover, remove bg, transparent background, photo eraser"),
    ("AI Logo Maker: Design Create", "6746450374", "ai-logo-maker", "ai-photo", "Design professional logos with AI assistance. Create brand identity in minutes.", "logo maker, AI logo, logo design, brand creator"),
    ("Retro Camera: Aesthetic Video", "6755106439", "retro-camera-aesthetic", "ai-photo", "Record videos with retro VHS effects. Create nostalgic content with vintage filters.", "retro camera, VHS effect, vintage video, retro filter"),
    ("Tattoo AI Generator Try-On Lui", "6752377181", "tattoo-ai-generator", "ai-photo", "Try tattoos before getting inked. AI-powered virtual tattoo placement on your body.", "tattoo try on, virtual tattoo, AI tattoo, tattoo preview"),
    ("AI Headshot Photo Generator HS", "6754511323", "ai-headshot-generator", "ai-photo", "Generate professional headshots with AI. Perfect for LinkedIn and business profiles.", "AI headshot, professional photo, business portrait, LinkedIn photo"),
    ("Waifu AI Anime Girlfriend", "6737455692", "waifu-ai-anime-girlfriend", "ai-photo", "Chat with your AI anime companion. Create and customize your virtual girlfriend.", "AI girlfriend, anime chat, virtual companion, waifu AI"),
    ("AI Girlfriend 18 Lova", "6737166215", "ai-girlfriend-lova", "ai-photo", "Your AI companion for meaningful conversations. Build a virtual relationship.", "AI girlfriend, virtual companion, chat AI, romantic AI"),
    
    # Home & Interior Design
    ("Kitchen Planner: Home Remodel", "6755612494", "kitchen-planner-remodel", "home-design", "Design your dream kitchen with AI. Visualize renovations before spending money.", "kitchen planner, home remodel, kitchen design, interior design"),
    ("Backyard Remodel AI Landscape", "6752511141", "backyard-remodel-ai", "home-design", "Transform your backyard with AI landscape design. Visualize outdoor renovations.", "backyard design, landscape AI, garden planner, outdoor remodel"),
    ("Remodel AI: Room Planner", "6751861148", "remodel-ai-room-planner", "home-design", "Plan room renovations with AI visualization. See changes before you make them.", "room planner, home remodel, interior design AI, renovation app"),
    ("Home Remodel & Office Design", "6753745938", "home-remodel-office", "home-design", "Design home office and living spaces. AI-powered interior visualization.", "home design, office planner, interior remodel, room design"),
    ("Baby Room Decor: Home Design", "6755531528", "baby-room-decor", "home-design", "Design the perfect nursery with AI. Create beautiful baby room layouts.", "baby room design, nursery planner, kids room decor, nursery ideas"),
    ("Outfit Maker: AI Stylist Deco", "6753125218", "outfit-maker-stylist", "home-design", "Get AI fashion advice. Create outfits and plan your wardrobe.", "outfit maker, AI stylist, fashion app, wardrobe planner"),
    
    # Language Learning
    ("Learn French: Speak & Study", "6757562478", "learn-french", "language", "Master French with AI-powered lessons. Improve speaking, listening, and vocabulary.", "learn French, French app, French lessons, language learning"),
    ("Learn Italian: Speak & Study", "6757639699", "learn-italian", "language", "Learn Italian with interactive AI lessons. Perfect your pronunciation and grammar.", "learn Italian, Italian app, Italian lessons, language learning"),
    ("Learn German: Master Deutsch", "6757373485", "learn-german", "language", "Become fluent in German with AI tutoring. Comprehensive lessons for all levels.", "learn German, German app, Deutsch lernen, language learning"),
    ("Learn Korean: Speak & Hangul", "6757364765", "learn-korean", "language", "Master Korean and Hangul with AI. Learn to speak and read Korean fluently.", "learn Korean, Korean app, Hangul, K-pop language"),
    ("Japanese Learning: Speak, Read", "6756924419", "learn-japanese", "language", "Learn Japanese with AI assistance. Master hiragana, katakana, and kanji.", "learn Japanese, Japanese app, hiragana, kanji learning"),
    ("Learn Spanish: Speak, Practice", "6756527683", "learn-spanish", "language", "Speak Spanish confidently with AI practice. Interactive lessons for all levels.", "learn Spanish, Spanish app, Spanish lessons, language learning"),
    ("Anatomy & Physiology Learning", "6755895361", "anatomy-physiology", "education", "Master human anatomy with 3D models. Interactive lessons for students and professionals.", "anatomy app, physiology learning, medical education, body systems"),
    
    # Identifier Apps
    ("Banknote Identifier: Currency", "6747310232", "banknote-identifier", "identifier", "Identify banknotes and currency from around the world. Learn about money history.", "banknote identifier, currency scanner, money identifier, bill scanner"),
    ("Coin Scanner - Coinx", "6738133672", "coin-scanner-coinx", "identifier", "Scan and identify coins instantly. Discover coin values and history.", "coin scanner, coin identifier, numismatic app, coin value"),
    ("Rock Identifier: Crystal Stone", "6737857344", "rock-identifier", "identifier", "Identify rocks and crystals with AI. Learn about geology and minerals.", "rock identifier, crystal scanner, mineral app, geology"),
    ("Bird Identifier AI – Birdpicx", "6748220508", "bird-identifier", "identifier", "Identify birds by photo or sound. Perfect for birdwatching enthusiasts.", "bird identifier, bird scanner, birdwatching app, ornithology"),
    ("Dog to Human - Pawlo", "6686407778", "dog-to-human-pawlo", "identifier", "See what you'd look like as a dog or what your dog looks like as human.", "dog to human, pet app, funny photo, AI pet"),
    ("Antique Identifier: AI Value", "6744258862", "antique-identifier", "identifier", "Identify antiques and estimate their value. AI-powered appraisal tool.", "antique identifier, antique value, collectible scanner, appraisal"),
    ("Tree Identifier: Plant Care", "6743724721", "tree-identifier", "identifier", "Identify trees and plants with AI. Get care tips for your garden.", "tree identifier, plant scanner, garden app, plant care"),
    ("Dog Breed Identifier & Scan AI", "6749544872", "dog-breed-identifier", "identifier", "Identify dog breeds instantly with AI. Learn about breed characteristics.", "dog breed identifier, dog scanner, pet app, breed detector"),
    ("Fish Identifier: Fishing AI", "6743320057", "fish-identifier", "identifier", "Identify fish species for fishing and marine enthusiasts.", "fish identifier, fishing app, marine species, fish scanner"),
    ("Bug Identifier Insect Scan Fox", "6738428901", "bug-identifier", "identifier", "Identify insects and bugs with AI. Learn about the creatures around you.", "bug identifier, insect scanner, entomology app, bug detector"),
    
    # Education & Productivity
    ("SAT Prep & Practice: Digital", "6757205619", "sat-prep-practice", "education", "Prepare for SAT with comprehensive practice tests and AI tutoring.", "SAT prep, SAT practice, college prep, test preparation"),
    ("ASVAB 2026: Practice Test Prep", "6756375056", "asvab-practice-test", "education", "Get ready for ASVAB with practice tests. Military aptitude test preparation.", "ASVAB prep, military test, ASVAB practice, aptitude test"),
    ("AI Note Taker & Audio – Quizzy", "6736929252", "ai-note-taker-quizzy", "education", "Take notes with AI assistance. Record lectures and get automatic summaries.", "AI notes, note taker, lecture recorder, study app"),
    
    # Other Apps
    ("Car Mod & Tuning AI - Paul", "6752488950", "car-mod-tuning-ai", "other", "Visualize car modifications with AI. See how mods look before buying.", "car mod, tuning app, car customization, vehicle design"),
    ("Gluten Free Food Scanner: Leto", "6744889720", "gluten-free-scanner", "other", "Scan food labels for gluten. Essential for celiac and gluten sensitivity.", "gluten free app, food scanner, celiac app, allergy scanner"),
    ("AI Party Planner: Event Plan", "6753711010", "ai-party-planner", "other", "Plan perfect parties with AI. Get ideas for decorations, food, and activities.", "party planner, event planning, party ideas, celebration app"),
    ("AI Boyfriend Anime Wonn", "6738020035", "ai-boyfriend-wonn", "other", "Chat with your AI anime boyfriend. Virtual companion for conversations.", "AI boyfriend, anime chat, virtual companion, chat AI"),
    ("Stoic Daily Therapy AI Marcus", "6645269377", "stoic-therapy-marcus", "other", "Daily stoic philosophy and wisdom. AI-powered mental wellness companion.", "stoic app, philosophy, mental health, daily wisdom"),
    ("Positive IO: Meditate & Affirm", "6739349188", "positive-io-meditate", "other", "Daily affirmations and meditation. Build positive habits with AI guidance.", "meditation app, affirmations, mindfulness, positive thinking"),
    ("Travel Guide AI Scanner Buddy", "6742664822", "travel-guide-scanner", "other", "Scan landmarks and get travel info. AI-powered tour guide in your pocket.", "travel guide, landmark scanner, tourist app, travel AI"),
]

def generate_app_page(name, apple_id, slug, category, description, keywords):
    """Generate HTML for an app landing page."""
    
    category_display = {
        "ai-photo": "AI & Photo",
        "home-design": "Home Design", 
        "language": "Language Learning",
        "identifier": "Identifier",
        "education": "Education",
        "other": "Lifestyle"
    }.get(category, "App")
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - Download on App Store | UtkuApps</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  
  <!-- Apple Smart App Banner -->
  <meta name="apple-itunes-app" content="app-id={apple_id}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{name}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utkuapps.com/{slug}/">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{name}">
  <meta name="twitter:description" content="{description}">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utkuapps.com/{slug}/">
  
  <link rel="stylesheet" href="../css/style.css">
  
  <!-- Schema.org -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{name}",
    "operatingSystem": "iOS",
    "applicationCategory": "{category_display}Application",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.5",
      "ratingCount": "100"
    }}
  }}
  </script>
</head>
<body>
  <header class="header">
    <div class="container header-inner">
      <a href="/" class="logo">
        <div class="logo-icon">U</div>
        <span>UtkuApps</span>
      </a>
      <nav class="nav">
        <a href="/#apps">All Apps</a>
        <a href="/privacy.html">Privacy</a>
      </nav>
    </div>
  </header>

  <section class="app-page">
    <div class="app-header">
      <div class="container">
        <img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/00/00/00/{apple_id}/source/512x512bb.jpg" 
             alt="{name}" 
             class="app-icon"
             onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect fill=%22%23007AFF%22 width=%22100%22 height=%22100%22 rx=%2220%22/><text x=%2250%22 y=%2265%22 text-anchor=%22middle%22 fill=%22white%22 font-size=%2230%22 font-weight=%22bold%22>{name[0]}</text></svg>'">
        <h1>{name}</h1>
        <p class="app-category">{category_display}</p>
        <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
          Download on App Store
        </a>
      </div>
    </div>

    <section class="description">
      <div class="container">
        <h2>About {name}</h2>
        <p>{description}</p>
        <p>Download now and discover why thousands of users love this app. Available for iPhone and iPad.</p>
      </div>
    </section>

    <section class="features">
      <div class="container">
        <h2>Key Features</h2>
        <div class="features-grid">
          <div class="feature-item">
            <div class="feature-icon">✨</div>
            <h3>AI Powered</h3>
            <p>Advanced artificial intelligence for the best results.</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <h3>Fast & Easy</h3>
            <p>Intuitive interface for quick and seamless experience.</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🔒</div>
            <h3>Privacy First</h3>
            <p>Your data stays on your device. We respect your privacy.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container">
        <h2>Ready to Get Started?</h2>
        <p>Download {name} now and experience the difference.</p>
        <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
          Download Free on App Store
        </a>
      </div>
    </section>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-links">
        <a href="/">Home</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="mailto:support@utkuapps.com">Contact</a>
      </div>
      <p>© 2024 UtkuApps. All rights reserved.</p>
    </div>
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>'''
    
    return html


def main():
    base_dir = "/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website"
    
    for name, apple_id, slug, category, description, keywords in APPS:
        # Create folder
        app_dir = os.path.join(base_dir, slug)
        os.makedirs(app_dir, exist_ok=True)
        
        # Generate HTML
        html = generate_app_page(name, apple_id, slug, category, description, keywords)
        
        # Write file
        with open(os.path.join(app_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"✓ Created: {slug}/index.html")
    
    print(f"\n✅ Generated {len(APPS)} app landing pages!")


if __name__ == "__main__":
    main()
