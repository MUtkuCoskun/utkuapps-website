#!/usr/bin/env python3
"""Complete generator for all 51 TechSolutionAI app landing pages"""
import os

APPS = [
    ("Anatomy & Physiology Learning", "Human Body Atlas & Flashcards", "6755895361", "anatomy-physiology", "education", "Education", "4.3", "Master anatomy with 3D models, interactive flashcards, and comprehensive quizzes covering all body systems."),
    ("Hair AI Allz: Hairstyle Try-On", "Instant Cuts & Color Swaps", "6752910932", "hair-ai-hairstyle-try-on", "ai-photo", "Graphics & Design", "4.2", "Try hundreds of hairstyles and colors instantly with AI-powered virtual makeover technology."),
    ("AI Art Photo Generator: Synap", "Prompt to Post: Social Feed", "6757766271", "ai-art-synap", "ai-photo", "Graphics & Design", "4.5", "Transform your ideas into stunning AI artwork with our advanced image generation technology."),
    ("Kitchen Planner: Home Remodel", "Cabinet Layout & Floor Plans", "6755612494", "kitchen-planner", "home-design", "Lifestyle", "3.0", "Design your dream kitchen with 3D visualization, cabinet layouts, and professional floor plans."),
    ("Backyard Remodel AI Landscape", "Outdoor Design & Garden Plans", "6752511141", "backyard-remodel", "home-design", "Lifestyle", "4.0", "Transform your outdoor space with AI-powered landscape design and garden visualization."),
    ("Learn French: Speak & Study", "Grammar, Vocabulary & Phrases", "6757562478", "learn-french", "language", "Education", "4.5", "Master French with AI-powered lessons covering grammar, vocabulary, and real conversation practice."),
    ("Learn German: Master Deutsch", "Speak, Study Vocab & Grammar", "6757373485", "learn-german", "language", "Education", "4.4", "Become fluent in German with comprehensive lessons, exercises, and AI speech recognition."),
    ("Learn Korean: Speak & Hangul", "Writing, Grammar & Vocabulary", "6757364765", "learn-korean", "language", "Education", "4.3", "Learn Korean from scratch including Hangul writing, grammar patterns, and vocabulary."),
    ("Learn Italian: Speak & Study", "Grammar, Lessons & Phrases", "6757639699", "learn-italian", "language", "Education", "4.4", "Master Italian with structured lessons, grammar explanations, and conversational phrases."),
    ("Learn Spanish: Speak, Practice", "Vocabulary, Words & Grammar", "6756527683", "learn-spanish", "language", "Education", "4.2", "Speak Spanish confidently with AI tutoring, vocabulary building, and grammar exercises."),
    ("Japanese Learning: Speak, Read", "Kanji, Hiragana & Vocabulary", "6756924419", "learn-japanese", "language", "Education", "4.3", "Learn Japanese including Kanji, Hiragana, Katakana, and essential vocabulary."),
    ("Coin Scanner - Coinx", "Identify & Value Your Coins", "6738133672", "coin-scanner", "identifier", "Reference", "4.1", "Instantly identify coins from around the world and get current market valuations."),
    ("Rock Identifier: Crystal Stone", "Geology & Mineral Scanner", "6737857344", "rock-identifier", "identifier", "Reference", "4.0", "Identify rocks, crystals, and minerals with AI-powered image recognition."),
    ("Bird Identifier AI – Birdpicx", "Species Recognition", "6748220508", "bird-identifier", "identifier", "Reference", "4.2", "Identify bird species from photos with detailed information about each species."),
    ("Tree Identifier: Plant Care", "Nature & Botany Guide", "6743724721", "tree-identifier", "identifier", "Reference", "4.1", "Identify trees and plants with care tips and detailed botanical information."),
    ("Dog Breed Identifier & Scan AI", "Pet Recognition", "6749544872", "dog-breed-identifier", "identifier", "Reference", "4.3", "Identify any dog breed instantly with detailed breed information and characteristics."),
    ("Fish Identifier: Fishing AI", "Species & Catch Guide", "6743320057", "fish-identifier", "identifier", "Reference", "3.9", "Identify fish species with fishing tips and habitat information."),
    ("Bug Identifier Insect Scan Fox", "Entomology Scanner", "6738428901", "bug-identifier", "identifier", "Reference", "3.8", "Identify insects and bugs with detailed species information."),
    ("Banknote Identifier: Currency", "World Money Scanner", "6747310232", "banknote-identifier", "identifier", "Reference", "4.0", "Identify and verify world currencies with anti-counterfeit features."),
    ("Antique Identifier: AI Value", "Collectibles Appraiser", "6744258862", "antique-identifier", "identifier", "Reference", "4.1", "Identify antiques and get estimated values for your collectibles."),
    ("Waifu AI Anime Girlfriend", "Chat & Virtual Companion", "6737455692", "waifu-ai", "ai-photo", "Entertainment", "4.0", "Create and chat with your personalized anime companion powered by AI."),
    ("AI Girlfriend 18 Lova", "Virtual Chat Companion", "6737166215", "ai-girlfriend-lova", "ai-photo", "Entertainment", "3.8", "Experience natural conversations with an AI companion who remembers you."),
    ("AI Boyfriend Anime Wonn", "Virtual Chat Partner", "6738020035", "ai-boyfriend-wonn", "ai-photo", "Entertainment", "3.9", "Chat with your AI anime companion with unique personality traits."),
    ("Car Mod & Tuning AI - Paul", "Vehicle Visualization", "6752488950", "car-mod-tuning", "other", "Lifestyle", "4.2", "Visualize car modifications and tuning options before making changes."),
    ("Mosaic Face Blur Photo Effect", "Privacy Photo Editor", "6755252956", "mosaic-face-blur", "ai-photo", "Photo & Video", "4.1", "Blur faces and sensitive content with mosaic effects for privacy."),
    ("Remodel AI: Room Planner", "Interior Design Tool", "6751861148", "remodel-ai-room", "home-design", "Lifestyle", "4.3", "Plan room renovations with AI-powered interior design visualization."),
    ("Home Remodel & Office Design", "Workspace Planner", "6753745938", "home-office-design", "home-design", "Lifestyle", "4.0", "Design your home office and workspace with professional planning tools."),
    ("Baby Room Decor: Home Design", "Nursery Interior Planner", "6755531528", "baby-room-decor", "home-design", "Lifestyle", "4.2", "Create the perfect nursery with AI-powered baby room design tools."),
    ("Gluten Free Food Scanner: Leto", "Dietary Ingredient Checker", "6744889720", "gluten-free-scanner", "other", "Health & Fitness", "4.0", "Scan products to detect gluten and manage your celiac-friendly diet."),
    ("AI Makeup: Beauty Face Editor", "Virtual Cosmetics Try-On", "6755445775", "ai-makeup-beauty", "ai-photo", "Photo & Video", "4.1", "Try on makeup looks virtually with AI-powered beauty filters."),
    ("Vintage AI Camera Photo Editor", "Retro Film Effects", "6755054572", "vintage-camera", "ai-photo", "Photo & Video", "4.2", "Apply authentic vintage and retro film effects to your photos."),
    ("AI Face Swap & Morph: Ciro", "Face Transformation", "6753283724", "face-swap-ciro", "ai-photo", "Photo & Video", "4.0", "Swap and morph faces with realistic AI-powered transformations."),
    ("Body Editor: Slim & Muscle AI", "Photo Reshaping", "6754536106", "body-editor", "ai-photo", "Photo & Video", "3.9", "Reshape body proportions in photos with AI editing tools."),
    ("AI Video Generator Cartoon Roy", "Animation Creator", "6754221955", "ai-video-cartoon", "ai-photo", "Photo & Video", "4.1", "Convert videos and photos into cartoon-style animations."),
    ("Cartoon Photo Editor: AI Art", "Artistic Filters", "6753689528", "cartoon-photo-editor", "ai-photo", "Photo & Video", "4.2", "Transform photos into cartoon and comic-style artwork."),
    ("AI Anime Art Generator Villor", "Anime Style Creator", "6670369690", "ai-anime-villor", "ai-photo", "Graphics & Design", "4.0", "Generate anime-style artwork from photos and prompts."),
    ("Background Remover: Eraser Dio", "Photo Cutout Tool", "6755402671", "background-remover", "ai-photo", "Photo & Video", "4.3", "Remove backgrounds instantly with AI-powered precision erasing."),
    ("Preppy Wallpaper AI Generator", "Aesthetic Backgrounds", "6737566105", "preppy-wallpaper", "ai-photo", "Graphics & Design", "3.8", "Generate aesthetic preppy-style wallpapers for your devices."),
    ("Retro Camera: Aesthetic Video", "VHS & Film Effects", "6755106439", "retro-camera", "ai-photo", "Photo & Video", "4.1", "Capture retro VHS-style videos with authentic film effects."),
    ("AI Logo Maker: Design Create", "Brand Identity Tool", "6746450374", "ai-logo-maker", "ai-photo", "Graphics & Design", "4.0", "Create professional logos with AI-powered design assistance."),
    ("Tattoo AI Generator Try-On Lui", "Virtual Ink Preview", "6752377181", "tattoo-ai-generator", "ai-photo", "Graphics & Design", "4.4", "Preview tattoo designs on your body before committing to ink."),
    ("AI Headshot Photo Generator HS", "Professional Portraits", "6754511323", "ai-headshot", "ai-photo", "Photo & Video", "4.0", "Generate professional AI headshots for LinkedIn and business use."),
    ("Dog to Human - Pawlo", "Fun Pet Transformation", "6686407778", "dog-to-human", "other", "Entertainment", "4.2", "See what you would look like as a dog with fun AI transformations."),
    ("SAT Prep & Practice: Digital", "College Exam Ready", "6757205619", "sat-prep", "education", "Education", "4.5", "Comprehensive SAT preparation with practice tests, math, and reading sections."),
    ("ASVAB 2026: Practice Test Prep", "Military Aptitude", "6756375056", "asvab-prep", "education", "Education", "4.3", "Prepare for the ASVAB military aptitude test with practice exams."),
    ("AI Note Taker & Audio – Quizzy", "Smart Study Tool", "6736929252", "ai-note-taker", "education", "Education", "4.2", "AI-powered note-taking with audio transcription and quiz generation."),
    ("AI Party Planner: Event Plan", "Celebration Organizer", "6753711010", "ai-party-planner", "other", "Lifestyle", "4.0", "Plan perfect parties with AI-powered event suggestions and checklists."),
    ("Outfit Maker: AI Stylist Deco", "Fashion Advisor", "6753125218", "outfit-maker", "other", "Lifestyle", "4.1", "Get AI fashion advice and outfit recommendations."),
    ("Stoic Daily Therapy AI Marcus", "Philosophy & Wisdom", "6645269377", "stoic-therapy", "other", "Health & Fitness", "4.4", "Daily stoic wisdom and philosophical guidance for mental wellness."),
    ("Positive IO: Meditate & Affirm", "Mindfulness App", "6739349188", "positive-io", "other", "Health & Fitness", "4.2", "Daily affirmations and guided meditation for positive mindset."),
    ("Travel Guide AI Scanner Buddy", "Tourism Assistant", "6742664822", "travel-guide", "other", "Travel", "4.0", "AI-powered travel guide with landmark recognition and local tips."),
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - Free Download for iPhone | TechSolutionAI</title>
  <meta name="description" content="{description}">
  <meta name="apple-itunes-app" content="app-id={apple_id}">
  <meta property="og:title" content="{name} - {subtitle}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utkuapps.com/{slug}/">
  <meta property="og:site_name" content="TechSolutionAI">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://utkuapps.com/{slug}/">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{name}","description":"{description}","operatingSystem":"iOS","applicationCategory":"{category_display}Application","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"{rating}","ratingCount":"10"}},"author":{{"@type":"Organization","name":"TechSolutionAI"}}}}
  </script>
</head>
<body>
  <header class="header">
    <div class="container header-inner">
      <a href="/" class="logo"><div class="logo-icon">⚡</div><span>TechSolutionAI</span></a>
      <nav class="nav"><a href="/#apps">All Apps</a><a href="/privacy.html">Privacy</a></nav>
    </div>
  </header>
  <main class="app-page">
    <section class="app-hero">
      <div class="container">
        <div class="app-hero-content">
          <div class="app-icon-large" style="background:linear-gradient(135deg,#007AFF,#5856D6);display:flex;align-items:center;justify-content:center;font-size:72px;color:#fff;">{icon}</div>
          <div class="app-hero-text">
            <h1>{name}</h1>
            <p class="app-subtitle">{subtitle}</p>
            <div class="app-meta">
              <span class="rating">⭐ {rating}</span>
              <span class="category">{category_display}</span>
            </div>
            <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn-large" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
              <div><span class="small">Download on the</span><span class="big">App Store</span></div>
            </a>
          </div>
        </div>
      </div>
    </section>
    <section class="description-section">
      <div class="container">
        <h2>About {name}</h2>
        <div class="description-content"><p>{description}</p><p>Download now for free and discover why thousands of users trust {name} for their daily needs. Available exclusively on the App Store for iPhone and iPad.</p></div>
      </div>
    </section>
    <section class="faq-section">
      <div class="container">
        <h2>FAQ</h2>
        <div class="faq-list">
          <div class="faq-item"><h3 class="faq-question">Is {name} free?</h3><p class="faq-answer">Yes, {name} is free to download with optional premium features available via in-app purchase.</p></div>
          <div class="faq-item"><h3 class="faq-question">What devices are supported?</h3><p class="faq-answer">{name} works on iPhone and iPad running iOS 15.0 or later.</p></div>
          <div class="faq-item"><h3 class="faq-question">Is my data safe?</h3><p class="faq-answer">Yes, we prioritize your privacy. Data processing happens on-device whenever possible.</p></div>
        </div>
      </div>
    </section>
    <section class="cta-section">
      <div class="container">
        <h2>Download {name} Today</h2>
        <p>Join thousands of satisfied users. Free on the App Store!</p>
        <a href="https://apps.apple.com/app/id{apple_id}" class="appstore-btn-large" target="_blank">
          <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
          <div><span class="small">Download on the</span><span class="big">App Store</span></div>
        </a>
      </div>
    </section>
  </main>
  <footer class="footer"><div class="container"><div class="footer-links"><a href="/">Home</a><a href="/privacy.html">Privacy</a></div><p>© 2024 TechSolutionAI</p></div></footer>
</body>
</html>'''

ICONS = {"education":"📚","ai-photo":"🎨","home-design":"🏠","language":"🗣️","identifier":"🔍","other":"⚡"}

def main():
    base = "/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website"
    for name, subtitle, apple_id, slug, category, category_display, rating, description in APPS:
        d = os.path.join(base, slug)
        os.makedirs(d, exist_ok=True)
        html = TEMPLATE.format(name=name, subtitle=subtitle, apple_id=apple_id, slug=slug,
            category=category, category_display=category_display, rating=rating,
            description=description, icon=ICONS.get(category, "⚡"))
        with open(os.path.join(d, "index.html"), "w") as f:
            f.write(html)
        print(f"✓ {slug}")
    print(f"\n✅ Generated {len(APPS)} pages!")

if __name__ == "__main__":
    main()
