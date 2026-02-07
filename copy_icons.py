#!/usr/bin/env python3
import shutil
import os

BASE = "/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects"
ICONS = f"{BASE}/utkuapps-website/icons"

copies = [
    (f"{BASE}/Body Editor Hagi/Body Editor Hagi/Assets.xcassets/AppIcon.appiconset/body_editor_neon.png", 
     f"{ICONS}/body-editor.png"),
    
    (f"{BASE}/Pawlo/Pawlo/Assets.xcassets/AppIcon.appiconset/pawlo.png", 
     f"{ICONS}/dog-to-human.png"),
    
    (f"{BASE}/Makeup Editor MUE/Makeup Editor MUE/Assets.xcassets/AppIcon.appiconset/ChatGPT Image Nov 18, 2025 at 08_51_08 PM.png", 
     f"{ICONS}/ai-makeup-beauty.png"),
    
    (f"{BASE}/Headshot AI Linc/Headshot AI Linc/Assets.xcassets/AppIcon.appiconset/ChatGPT Image Oct 25, 2025 at 04_21_24 PM.png", 
     f"{ICONS}/ai-headshot.png"),
    
    (f"{BASE}/Waifu AI Anime Girlfriend/Waifu AI Anime Girlfriend/Assets.xcassets/AppIcon.appiconset/DALLE2025-03-0417.28.52-Abeautifulandstylishanimegirlwithlongflowinghairandaconfidentalluringexpression.Shewearsafashionableoutfitthathighlightsherch-ezgif.com-webp-to-jpg-converter.jpg", 
     f"{ICONS}/waifu-ai.jpg"),
    
    (f"{BASE}/Quizzy/Quizzy/Assets.xcassets/AppIcon.appiconset/DALL·E 2024-10-07 21.44.38 - Create a minimalist app logo featuring a simple AI chip icon with a small note or document symbol inside it. The AI chip should have clean lines and s.jpg", 
     f"{ICONS}/ai-note-taker.jpg"),
    
    (f"{BASE}/Marcus AI Stoic/Marcus AI Stoic/Assets.xcassets/AppIcon.appiconset/DALL·E 2024-08-21 13.46.06 - A minimalistic digital rendering of a classical Greek temple icon with a black background. The temple features a triangular pediment with a central ci.jpg", 
     f"{ICONS}/stoic-therapy.jpg"),
]

for src, dst in copies:
    try:
        shutil.copy2(src, dst)
        print(f"OK: {os.path.basename(dst)}")
    except Exception as e:
        print(f"FAIL: {os.path.basename(dst)} - {e}")

print(f"\nTotal icons: {len(os.listdir(ICONS))}")
