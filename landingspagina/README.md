# Holt & Vance · Landingspagina "Built to Last"

Nieuwsbrief-landingspagina voor het fictieve parfummerk Holt & Vance (Noir & Amber).
Schoolproject Creative Automation. Puur HTML, CSS en JavaScript, geen build-stap en geen externe mailingdienst.

## Inhoud

| Bestand | Rol |
|---|---|
| `index.html` | Structuur: hero, brand story, geuren, film, visuals + Instagram-feed, nieuwsbrief, footer, privacy-dialoog |
| `style.css` | Huisstijl (charcoal HSL(0,0%,18%), amber #C8963E, bone #EDE8DF) en responsieve layout (desktop · tablet ≤1024px · mobiel ≤720px) |
| `script.js` | Instagram-feed uit een data-array, scroll-animaties, video's, privacy-dialoog, formuliervalidatie en succesmelding |
| `assets/video/` | `hero.mp4` (video 2 smoke, ingekort tot 9,2 s zonder eindtitel) · `film.mp4` (video 1) |
| `assets/img/` | Product- en sfeerfoto's uit de map *figma buzz*, webklaar gemaakt (max. 1200×1600, JPG 80%) |
| `assets/feed/` | 12 Instagram-posts uit Figma Buzz (bulk create) |
| `nieuwsbriefcampagne/` | Overzicht van de e-mailcampagne: formulier, automation-illustratie met 2 scenario's, logica-tabel en de 3 e-mails (`emails/`). De mails worden gegenereerd met `maak_emails.py`. |
| `.nojekyll` | Zorgt dat GitHub Pages alle bestanden ongewijzigd serveert |

Fonts: Bebas Neue (titels), Barlow (tekst), Barlow Condensed (labels, knoppen) via Google Fonts.

## Formulier

- Velden: voornaam, e-mailadres, toestemmingsvakje (niet vooraf aangevinkt).
- JavaScript-validatie bij verlaten van een veld en bij verzenden, met foutmeldingen per veld (`aria-invalid`, `aria-live`).
- Na geldig verzenden verschijnt een persoonlijke succesmelding.
- **Er wordt niets verstuurd of opgeslagen**: geen `fetch`, geen `localStorage`, geen MailerLite.

## Publiceren op GitHub Pages

1. Maak op github.com een nieuwe publieke repository, bv. `holt-vance`.
2. Klik **Add file → Upload files** en sleep de *inhoud* van deze map erin (index.html, style.css, script.js, README.md, .nojekyll en de map assets). Klik **Commit changes**.
   *Tip: `.nojekyll` is op de Mac verborgen. Druk Cmd+Shift+. in Finder om het te zien. Zonder dit bestand werkt de site ook.*
3. Ga naar **Settings → Pages**, kies bij *Source* "Deploy from a branch", branch `main`, map `/ (root)`, en klik **Save**.
4. Na 1 à 2 minuten staat de site live op `https://<gebruikersnaam>.github.io/holt-vance/`.

## Lokaal bekijken

Open `index.html` in de browser, of start een mini-server in deze map: `python3 -m http.server` en ga naar http://localhost:8000.
