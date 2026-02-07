# UtkuApps Website - Deployment Guide

## 🎉 Project Complete!

Your website is ready with **51 SEO-optimized landing pages**.

---

## 📁 Project Structure

```
utkuapps-website/
├── index.html              # Homepage with all apps
├── privacy.html            # Privacy policy
├── sitemap.xml            # For Google indexing
├── robots.txt             # Search engine directives
├── CNAME                  # Custom domain for GitHub Pages
├── css/style.css          # Modern dark theme styles
├── js/main.js             # Interactive features
├── generate_pages.py      # Script that generated all pages
│
└── 51 app folders/
    ├── anatomy-physiology/
    ├── hair-ai-hairstyle-try-on/
    ├── kitchen-planner-remodel/
    └── ... (48 more)
```

---

## 🚀 Deployment Steps

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `utkuapps-website`
3. Keep it **Public** (required for free GitHub Pages)
4. Click "Create repository"

### Step 2: Push Code to GitHub

Open Terminal and run these commands:

```bash
cd "/Users/utkucoskun/Desktop/Desktop - UTKU MacBook Air/App Projects/utkuapps-website"

git init
git add .
git commit -m "Initial commit - 51 app landing pages"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/utkuapps-website.git
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username!**

### Step 3: Enable GitHub Pages

1. Go to your repo: `https://github.com/YOUR_USERNAME/utkuapps-website`
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Source", select **Deploy from a branch**
4. Branch: **main** / **root**
5. Click **Save**
6. Under "Custom domain", enter: `utkuapps.com`
7. Check **Enforce HTTPS**

### Step 4: Configure GoDaddy DNS

1. Go to https://dcc.godaddy.com (your GoDaddy dashboard)
2. Click on **utkuapps.com** → **DNS** tab
3. **Delete** any existing A or CNAME records for @ and www
4. Add these **A Records**:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

5. Add this **CNAME Record**:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | YOUR_USERNAME.github.io | 600 |

6. Save all changes

### Step 5: Wait & Verify

- **DNS propagation**: 10-30 minutes
- **HTTPS certificate**: Up to 1 hour
- Check status in GitHub Pages settings

---

## ✅ After Deployment Checklist

### 1. Verify Website
- [ ] Visit https://utkuapps.com
- [ ] Check https://www.utkuapps.com (should redirect)
- [ ] Test a few app pages

### 2. Submit to Google
1. Go to https://search.google.com/search-console
2. Add property: `https://utkuapps.com`
3. Verify ownership (use DNS method - add TXT record)
4. Submit sitemap: `https://utkuapps.com/sitemap.xml`

### 3. Test Smart App Banner
- Open any app page on iPhone Safari
- You should see "OPEN" or "GET" banner at the top

### 4. Test SEO
- Use https://search.google.com/test/rich-results
- Enter any app URL to verify Schema.org markup

---

## 🔧 Future Updates

### To add a new app:
1. Edit `generate_pages.py`
2. Add new app to the `APPS` list
3. Run: `python3 generate_pages.py`
4. Update `sitemap.xml`
5. Update `index.html` (add app card)
6. Commit and push to GitHub

### To update styles:
Just edit `css/style.css` and push to GitHub.

---

## 📊 SEO Features Included

- ✅ Apple Smart App Banner (Safari native download prompt)
- ✅ Schema.org SoftwareApplication markup
- ✅ Open Graph meta tags (Facebook/LinkedIn)
- ✅ Twitter Card meta tags
- ✅ Canonical URLs
- ✅ XML Sitemap
- ✅ Robots.txt
- ✅ Mobile-responsive design
- ✅ Fast loading (static HTML)
- ✅ HTTPS (via GitHub Pages)

---

## 💰 Cost: $0

Everything is free:
- GitHub Pages hosting: **FREE**
- SSL certificate: **FREE**  
- Domain (already owned): ✓

---

## 📞 Support

If you need to update the website or add new apps, just ask!
