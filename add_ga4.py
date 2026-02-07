#!/usr/bin/env python3
"""Add GA4 tracking to all HTML pages"""
import os
from pathlib import Path

BASE_DIR = Path("/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website")
GA4_CODE = '''<!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPMJWDH0ST"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-TPMJWDH0ST');
  </script>
  '''

count = 0
for html_file in BASE_DIR.rglob("*.html"):
    if ".git" in str(html_file):
        continue
    try:
        content = html_file.read_text(encoding='utf-8')
        if 'G-TPMJWDH0ST' not in content and '<head>' in content:
            content = content.replace('<head>\n', f'<head>\n  {GA4_CODE}', 1)
            html_file.write_text(content, encoding='utf-8')
            count += 1
    except Exception as e:
        print(f"Error: {html_file}: {e}")

print(f"✅ Added GA4 to {count} HTML files")
