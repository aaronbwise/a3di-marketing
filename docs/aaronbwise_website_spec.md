# aaronbwise.com Rebuild — Design & Development Spec

> A modern, single-page CV website that harmonises with a3di.dev's brand,
> leads with a strong profile/skills hero, shows consolidated experience,
> and offers a full PDF download.

---

## 1. Site Architecture

**Single HTML file** (`index.html`) + a CSS file (`style.css`) + your headshot image + a PDF.
No build tools, no frameworks, no JavaScript dependencies. Pure HTML/CSS with minimal
vanilla JS for smooth scrolling, mobile nav toggle, and maybe a scroll-triggered fade-in.

Hosted on GitHub Pages as today.

### File structure
```
aaronbwise.github.io/
├── index.html
├── css/
│   └── style.css
├── assets/
│   ├── img/
│   │   ├── headshot.jpg          (your current photo)
│   │   └── a3di-logo-small.svg   (optional, for the A3DI callout)
│   └── docs/
│       └── Aaron_Wise_CV_2026.pdf
├── CNAME                          (if using custom domain)
└── favicon.ico
```

---

## 2. Brand Harmonisation with a3di.dev

### Colour Palette
Pull directly from a3di.dev's visual identity:

| Token | Hex | Usage |
|-------|-----|-------|
| `--navy` | `#1B3A5C` | Primary headings, nav background, hero section |
| `--teal` | `#2A9D8F` | Accent colour, links, hover states, skill tags, section dividers |
| `--light-bg` | `#F0F7FA` | Alternate section backgrounds |
| `--white` | `#FFFFFF` | Main content background |
| `--dark` | `#2D3436` | Body text |
| `--muted` | `#636E72` | Secondary text, dates, locations |

### Typography
Use Google Fonts that complement a3di.dev's clean, professional feel:

| Role | Font | Weight | Fallback |
|------|------|--------|----------|
| Headings | **Source Sans 3** (or Source Sans Pro) | 600, 700 | system-ui, sans-serif |
| Body | **Source Sans 3** | 400, 600 | system-ui, sans-serif |
| Accent/Tags | Same family, smaller size | 500 | — |

**Why Source Sans:** It's professional, highly legible, has excellent weight range, and
pairs well with the clean aesthetic of a3di.dev without looking like a generic Bootstrap
template. It's also the font family used by many UN/development organisations, so it
feels familiar to your audience.

**Alternative:** If you want something with more personality, consider **Outfit** for
headings + **Source Sans 3** for body. Outfit has a modern geometric feel without being
trendy.

### Design Principles
- Clean, generous whitespace — not cramped
- No sidebar layout (that's the old Bootstrap Resume template look)
- Full-width, vertically scrolling sections
- Subtle section dividers (thin teal line or background colour alternation)
- Mobile-first responsive design
- Print-friendly (basic `@media print` styles)

---

## 3. Page Sections (top to bottom)

### 3.1 Navigation Bar (sticky)

**Layout:** Horizontal top nav, sticky on scroll. Transparent at top, transitions to
white with shadow on scroll.

```
[Aaron Wise]                    [Profile] [Experience] [Education] [Skills] [Publications] [Download CV ↓]
```

- Left: Your name (links to top)
- Right: Section links + a **teal CTA button** for "Download CV" (links to PDF)
- Mobile: Hamburger menu that slides down
- Active section highlighting on scroll (optional, via Intersection Observer)

**CSS notes:**
```css
nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(0,0,0,0.05);
  transition: box-shadow 0.3s ease;
}
```

---

### 3.2 Hero / Profile Section (THE MOST IMPORTANT SECTION)

This is the "above the fold" content. It should immediately communicate who you are,
what you do, and why someone should keep reading. Think of it as a visual executive
summary.

**Layout:** Full-width section, navy background (`--navy`), white text. Two-column on
desktop (text left, photo right). Stacks vertically on mobile.

```
┌─────────────────────────────────────────────────────────────────┐
│  [NAVY BACKGROUND]                                              │
│                                                                 │
│  AARON WISE                          ┌─────────────┐           │
│                                      │             │           │
│  Food Security & Data Specialist     │  [HEADSHOT] │           │
│                                      │   circular  │           │
│  15+ years with WFP, UNICEF &        │   with thin │           │
│  NGOs across Asia & Africa           │   teal      │           │
│                                      │   border    │           │
│  [2-3 sentence profile paragraph     │             │           │
│   — punchy, not the full About]      └─────────────┘           │
│                                                                 │
│  [📧 Email]  [🔗 LinkedIn]  [💻 GitHub]  [🌐 a3di.dev]          │
│                                                                 │
│             [ ↓ Download Full CV (PDF) ]    ← teal button      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Profile paragraph (the key text):**
> International development data specialist with 15+ years of experience leading
> food security analysis, survey design, and data pipeline development for WFP,
> UNICEF, and NGOs across more than a dozen countries in Asia and Africa. Currently
> deepening software engineering skills through a Computer Science degree at Oregon
> State University. Available for consulting engagements through
> [A3DI](https://www.a3di.dev).

**Contact links:** Use simple inline icons (Font Awesome or Lucide icons) with text.
Keep them horizontal, centered below the profile text.

**CSS notes:**
```css
.hero {
  background: var(--navy);
  color: #fff;
  padding: 5rem 2rem;
  min-height: 60vh;
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  align-items: center;
  gap: 3rem;
}

.hero img {
  width: 250px;
  height: 250px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--teal);
}

@media (max-width: 768px) {
  .hero { grid-template-columns: 1fr; text-align: center; }
  .hero img { margin: 0 auto; }
}
```

---

### 3.3 Core Competencies / Skills Strip

**Immediately below the hero.** This is a high-density visual summary of your key skills
before the reader hits the experience detail. Think of it as the "at a glance" row.

**Layout:** Full-width, light background (`--light-bg`). A horizontal row of skill
"cards" or tags grouped by category.

```
┌─────────────────────────────────────────────────────────────────┐
│  [LIGHT BACKGROUND]                                             │
│                                                                 │
│  WHAT I DO                                                      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Food Security│  │ Data         │  │ Survey       │          │
│  │ Analysis     │  │ Pipelines    │  │ Design       │          │
│  │              │  │              │  │              │          │
│  │ IPC, mVAM,  │  │ Python, SQL, │  │ ODK, Kobo,   │          │
│  │ targeting,   │  │ PostgreSQL,  │  │ mobile &     │          │
│  │ emergency    │  │ automated    │  │ phone-based  │          │
│  │ assessment   │  │ ETL, REST    │  │ collection   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Visualisation│  │ Training &   │  │ Software     │          │
│  │ & Reporting  │  │ Capacity     │  │ Engineering  │          │
│  │              │  │ Building     │  │              │          │
│  │ Tableau,     │  │ M&E teams,   │  │ Python, R,   │          │
│  │ PowerBI,     │  │ enumerator   │  │ Flask, Git,  │          │
│  │ infographics │  │ training     │  │ HTML/CSS,    │          │
│  └──────────────┘  └──────────────┘  │ Bash         │          │
│                                      └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

**CSS notes:**
- Use CSS Grid: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`
- Each card: white background, subtle border or shadow, teal top-border accent (3px)
- Cards should NOT have icons — the content speaks for itself. Icons tend to look
  generic and don't add information.

---

### 3.4 Experience (Consolidated)

**Layout:** White background. Timeline-style layout with a thin vertical teal line on
the left, and entries to the right of it.

**Use the consolidated structure from the LinkedIn guide:**

| # | Title | Organisation | Dates |
|---|-------|-------------|-------|
| 1 | Food Security Analyst (Consultant) | WFP | May 2022 – Mar 2025 |
| 2 | Regional Food Security Analyst | WFP | Aug 2014 – Dec 2020 |
| 3 | Data Analyst (Consultant) | FHI 360 / Alive & Thrive | Apr 2022 – Dec 2022 |
| 4 | Nutrition Information Specialist | UNICEF | Jun 2007 – Jul 2014 |
| 5 | Various short consultancies | IGN, Concern Worldwide | 2010, 2020 |

**Entry layout:**
```
┌─ ● ──────────────────────────────────────────────────┐
│                                                       │
│  FOOD SECURITY ANALYST (CONSULTANT)                   │
│  World Food Programme (WFP)                           │
│  May 2022 – Mar 2025  ·  Remote | Multiple Offices   │
│                                                       │
│  • Led analyses of WFP Afghanistan beneficiary data   │
│    to develop targeting recommendations...            │
│  • Supported joint WFP-FAO food security survey       │
│    in Myanmar, feeding into IPC classifications...    │
│  • [3-5 bullet points — cherry-picked strongest]      │
│                                                       │
│  Countries: Afghanistan, Myanmar, Timor-Leste,        │
│  Pakistan, Sri Lanka, Lao PDR, Philippines            │
│                                                       │
└───────────────────────────────────────────────────────┘
```

**CSS notes:**
```css
.timeline {
  position: relative;
  padding-left: 2rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--teal);
}

.timeline-entry {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 1.5rem;
}

.timeline-entry::before {
  content: '';
  position: absolute;
  left: -2.35rem;
  top: 0.5rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--teal);
  border: 3px solid var(--white);
}
```

**Important:** Include a note at the bottom of the Experience section:
> *For the complete list of individual engagements, [download the full CV (PDF)](#).*

---

### 3.5 Education

**Layout:** Simple, compact. Same light background (`--light-bg`). No timeline needed —
just clean cards or rows.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  EDUCATION                                                      │
│                                                                 │
│  BS Computer Science (In Progress)        2023 – Present        │
│  Oregon State University                                        │
│                                                                 │
│  MPH — International Health & Development 2006 – 2007           │
│  Tulane University                                              │
│  Concentration: Nutrition in Developing Countries               │
│                                                                 │
│  BA — Chemistry (Biochemistry)            2001 – 2005           │
│  Washington University in St. Louis                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.6 Publications

**Layout:** Simple list, white background. Just the two entries you have, properly
formatted with DOI link.

---

### 3.7 A3DI Callout Banner

**A prominent but tasteful banner** near the bottom, before the footer. This bridges the
personal CV site to the consultancy site.

**Layout:** Teal background (`--teal`), white text, centered.

```
┌─────────────────────────────────────────────────────────────────┐
│  [TEAL BACKGROUND]                                              │
│                                                                 │
│  Looking for data support for your programme?                   │
│                                                                 │
│  Through A3DI, I offer consulting services in survey design,    │
│  data pipelines, dashboards, and training for development       │
│  and humanitarian organisations.                                │
│                                                                 │
│             [ Visit a3di.dev → ]    ← white outlined button     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.8 Footer

**Layout:** Navy background, minimal.

```
┌─────────────────────────────────────────────────────────────────┐
│  [NAVY BACKGROUND]                                              │
│                                                                 │
│  © 2026 Aaron Wise  ·  Gainesville, FL                          │
│  aaron@a3di.dev  ·  LinkedIn  ·  GitHub                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Interactive Elements

### PDF Download Button
- Two locations: hero section and nav bar
- Links directly to `assets/docs/Aaron_Wise_CV_2026.pdf`
- Use `download` attribute: `<a href="..." download>Download CV (PDF)</a>`
- Style as teal button with white text, subtle hover darkening

### Smooth Scroll
Minimal vanilla JS:
```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth', block: 'start'
    });
  });
});
```

### Mobile Navigation
- Hamburger toggle at 768px breakpoint
- Simple CSS + JS toggle (no library needed)
- Nav slides down from top, full-width

### Scroll Fade-In (optional, subtle)
Use Intersection Observer to add a `.visible` class as sections enter viewport:
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('section').forEach(s => observer.observe(s));
```
```css
section {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
section.visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 5. Responsive Breakpoints

| Breakpoint | Layout changes |
|------------|---------------|
| > 1024px | Full desktop: two-column hero, 3-column skill cards |
| 768–1024px | Tablet: two-column hero narrows, 2-column skill cards |
| < 768px | Mobile: single column everything, hamburger nav, stacked hero |

---

## 6. Performance & Hosting Notes

- **No build step.** Plain HTML/CSS/JS. Deploys to GitHub Pages as-is.
- **Google Fonts:** Load Source Sans 3 via `<link>` with `display=swap`
- **Headshot:** Optimise to ~50-80KB JPEG, 500px wide max (it displays at 250px)
- **Icons:** Use [Lucide](https://unpkg.com/lucide@latest) via CDN, or inline SVGs for the 4-5 icons you need (email, LinkedIn, GitHub, globe). Avoid loading all of Font Awesome for 5 icons.
- **Favicon:** Use the A3DI logo or your initials "AW" as a simple favicon
- **Meta tags:** Add Open Graph tags so the site looks good when shared on LinkedIn

```html
<meta property="og:title" content="Aaron Wise — Food Security & Data Specialist" />
<meta property="og:description" content="15+ years with WFP, UNICEF & NGOs across Asia & Africa. Consulting through A3DI." />
<meta property="og:image" content="https://www.aaronbwise.com/assets/img/headshot.jpg" />
<meta property="og:url" content="https://www.aaronbwise.com" />
```

---

## 7. Content Checklist (what needs updating)

Before building, prepare these:

- [ ] Updated headshot (or reuse existing — it's fine)
- [ ] Gainesville address / contact info (replace Rome)
- [ ] Updated email: `aaron@a3di.dev` (professional, matches brand)
- [ ] Consolidated experience entries (copy from `linkedin_profile_copy.md` in your repo)
- [ ] Oregon State CS degree added to Education
- [ ] Latest WFP role (the one you mentioned is missing) added to the top WFP entry
- [ ] Full CV exported as PDF: `Aaron_Wise_CV_2026.pdf`
- [ ] A3DI logo (small, for the callout section — grab from a3di.dev)

---

## 8. Things to Intentionally NOT Include

- **Sidebar layout** — this is the #1 visual marker of the old Bootstrap Resume template
- **Skill progress bars** — nobody believes them, and they're a design cliché
- **Star ratings for skills** — same problem
- **Colourful skill icons** — they add visual noise without information
- **"About Me" section separate from the hero** — fold it into the hero profile paragraph
- **Every individual consultancy** — the consolidated view + PDF download handles this
- **MS Access, SPSS** — keep these in the PDF but not on the web version; lead with Python/SQL/PostgreSQL

---

## 9. Quick Visual Summary

```
┌─────────────── STICKY NAV ──────────────────────────────────────┐
│ Aaron Wise          Profile  Experience  Education  [Download CV]│
├─────────────── HERO (navy bg) ──────────────────────────────────┤
│ Name + title + profile paragraph + links      [Circular photo]  │
│                    [Download CV button]                          │
├─────────────── SKILLS STRIP (light bg) ─────────────────────────┤
│ [Card]  [Card]  [Card]                                          │
│ [Card]  [Card]  [Card]                                          │
├─────────────── EXPERIENCE (white bg, timeline) ─────────────────┤
│ ● WFP — Food Security Analyst (2022–2025)                       │
│ ● WFP — Regional Analyst (2014–2020)                            │
│ ● FHI 360 (2022)                                                │
│ ● UNICEF (2007–2014)                                            │
│ ● Concern / IGN (short entries)                                 │
│                                                                 │
│ "For full details, download the CV (PDF)"                       │
├─────────────── EDUCATION (light bg) ────────────────────────────┤
│ Oregon State (CS) · Tulane (MPH) · WashU (BA)                   │
├─────────────── PUBLICATIONS (white bg) ─────────────────────────┤
│ Journal article · Conference presentation                       │
├─────────────── A3DI CALLOUT (teal bg) ──────────────────────────┤
│ "Looking for data support?" → a3di.dev                          │
├─────────────── FOOTER (navy bg) ────────────────────────────────┤
│ © 2026 · contact · links                                        │
└─────────────────────────────────────────────────────────────────┘
```
