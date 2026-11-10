"""
Holt & Vance · e-mailgenerator
------------------------------
Bouwt de drie campagnemails (welkom, brand story, reminder) uit één template
en één data-blok. Herbruikbaar: pas de teksten in MAILS aan of voeg een mail toe
en draai opnieuw:  python3 maak_emails.py

Output: emails/01-welkom.html, 02-brand-story.html, 03-reminder.html
E-mailveilige HTML: tabellen, inline styles, 600 px breed, web-fonts met fallback.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent / "emails"

# ---------- huisstijl ----------
C = {
    "zwart": "#111111",
    "asfalt": "#1A1A1A",
    "lijn": "#2E2E2E",          # hoofdkleur HSL(0,0%,18%)
    "beige": "#EDE8DF",
    "beige_dim": "#BDB6AA",
    "leer": "#8B5A2B",          # lederbruin (knoppen, vlakken)
    "leer_licht": "#B9824D",    # lederbruin voor tekst op zwart (AA)
}
DISPLAY = "'Bebas Neue', Impact, 'Arial Narrow', Arial, sans-serif"
BODY = "'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
COND = "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
SITE = "../../index.html"  # op GitHub Pages: https://<gebruiker>.github.io/<repo>/


# ---------- bouwstenen ----------
def p(text, size=16, color=None, align="left", pad="0 40px 18px"):
    return f"""<tr><td style="padding:{pad};font-family:{BODY};font-size:{size}px;line-height:1.65;color:{color or C['beige_dim']};text-align:{align};">{text}</td></tr>"""


def label(text, color=None, pad="0 40px 10px", align="left"):
    return f"""<tr><td style="padding:{pad};font-family:{COND};font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{color or C['leer_licht']};text-align:{align};">{text}</td></tr>"""


def h1(text, size=64, pad="0 40px 20px", color=None, align="left"):
    return f"""<tr><td style="padding:{pad};font-family:{DISPLAY};font-size:{size}px;line-height:.95;letter-spacing:1px;text-transform:uppercase;color:{color or C['beige']};text-align:{align};">{text}</td></tr>"""


def img(src, alt, pad="0", w=600):
    return f"""<tr><td style="padding:{pad};"><img src="img/{src}" width="{w}" alt="{escape(alt)}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;"></td></tr>"""


def button(text, href, pad="10px 40px 36px", align="left"):
    return f"""<tr><td style="padding:{pad};" align="{align}">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
        <td bgcolor="{C['leer']}" style="background:{C['leer']};">
          <a href="{href}" style="display:inline-block;padding:17px 34px;font-family:{COND};font-size:15px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{C['beige']};text-decoration:none;">{text} &rarr;</a>
        </td></tr></table>
    </td></tr>"""


def divider(pad="8px 40px 30px"):
    return f"""<tr><td style="padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid {C['lijn']};font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>"""


def checklist(items):
    rows = "".join(
        f"""<tr><td width="34" valign="top" style="padding:0 0 14px;font-family:{DISPLAY};font-size:22px;line-height:1;color:{C['leer_licht']};">{i:02d}</td>
        <td style="padding:0 0 14px;font-family:{BODY};font-size:16px;line-height:1.5;color:{C['beige']};"><strong style="font-weight:600;">{t}</strong><br><span style="color:{C['beige_dim']};font-size:15px;">{s}</span></td></tr>"""
        for i, (t, s) in enumerate(items, 1))
    return f"""<tr><td style="padding:0 40px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table></td></tr>"""


def beige_block(inner_rows):
    return f"""<tr><td bgcolor="{C['beige']}" style="background:{C['beige']};padding:40px 0 22px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{inner_rows}</table></td></tr>"""


def code_box(code, sub):
    return f"""<tr><td style="padding:0 40px 30px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px dashed {C['leer_licht']};"><tr>
        <td style="padding:22px 24px;font-family:{COND};font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{C['beige_dim']};">Jouw code<br>
          <span style="font-family:{DISPLAY};font-size:40px;letter-spacing:4px;color:{C['beige']};line-height:1.2;">{code}</span></td>
        <td align="right" style="padding:22px 24px;font-family:{BODY};font-size:14px;line-height:1.5;color:{C['beige_dim']};">{sub}</td>
      </tr></table></td></tr>"""


def scent_cards():
    def card(img_src, naam, tijd, tekst, noten, side):
        padl, padr = ("40px", "8px") if side == "l" else ("8px", "40px")
        return f"""<td class="stack" width="50%" valign="top" style="padding:0 {padr} 0 {padl};">
          <img src="img/{img_src}" width="252" alt="Holt &amp; Vance {naam}" style="display:block;width:100%;height:auto;border:0;">
          <p style="margin:16px 0 2px;font-family:{COND};font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{C['leer_licht']};">{tijd}</p>
          <p style="margin:0 0 8px;font-family:{DISPLAY};font-size:44px;line-height:1;color:{C['beige']};">{naam}</p>
          <p style="margin:0 0 10px;font-family:{BODY};font-size:15px;line-height:1.55;color:{C['beige_dim']};">{tekst}</p>
          <p style="margin:0 0 26px;font-family:{COND};font-size:13px;letter-spacing:1px;text-transform:uppercase;color:{C['beige']};">{noten}</p>
        </td>"""
    return f"""<tr><td style="padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      {card('story-noir.jpg', 'Noir', '00:40 · Koude start', 'Koel, donker en scherp. Voor de rit of tocht die begint als de rest nog slaapt.', 'Zwarte peper · Vetiver · Zwart leer', 'l')}
      {card('story-amber.jpg', 'Amber', '19:50 · Einde van de rit', 'Warm, rokerig en diep. Voor het einde van de dag, als de tent staat en het vuur brandt.', 'Houtrook · Tabak · Warm leer', 'r')}
    </tr></table></td></tr>"""


def header(nr, naam):
    return f"""<tr><td style="padding:28px 40px;border-bottom:1px solid {C['lijn']};">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        <td style="font-family:{DISPLAY};font-size:28px;letter-spacing:1px;color:{C['beige']};">HOLT <span style="color:{C['leer_licht']};">&amp;</span> VANCE</td>
        <td align="right" style="font-family:{COND};font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{C['beige_dim']};">Nº {nr} · {naam}</td>
      </tr></table></td></tr>"""


def footer():
    return f"""<tr><td bgcolor="{C['zwart']}" style="background:{C['zwart']};padding:36px 40px 40px;text-align:center;">
      <p style="margin:0 0 6px;font-family:{DISPLAY};font-size:26px;letter-spacing:1px;color:{C['beige']};">Built for the long road.</p>
      <p style="margin:0 0 22px;font-family:{COND};font-size:12px;letter-spacing:3px;text-transform:uppercase;">
        <a href="{SITE}#geuren" style="color:{C['leer_licht']};text-decoration:none;">Geuren</a> &nbsp;·&nbsp;
        <a href="{SITE}#verhaal" style="color:{C['leer_licht']};text-decoration:none;">Verhaal</a> &nbsp;·&nbsp;
        <a href="{SITE}#onderweg" style="color:{C['leer_licht']};text-decoration:none;">Instagram</a></p>
      <p style="margin:0 0 10px;font-family:{BODY};font-size:12px;line-height:1.6;color:#8C867C;">Je ontvangt deze mail omdat je je met {{{{email}}}} inschreef via de website van Holt &amp; Vance en daarvoor toestemming gaf.<br>
        <a href="#uitschrijven" style="color:{C['beige_dim']};text-decoration:underline;">Uitschrijven</a> &nbsp;·&nbsp; <a href="#voorkeuren" style="color:{C['beige_dim']};text-decoration:underline;">Voorkeuren</a> &nbsp;·&nbsp; <a href="{SITE}#join" style="color:{C['beige_dim']};text-decoration:underline;">Privacy</a></p>
      <p style="margin:0;font-family:{BODY};font-size:11px;color:#6E695F;">Holt &amp; Vance · Fictief merk · Schoolproject Creative Automation</p>
    </td></tr>"""


def wrap(title, preheader, nr, naam, rows):
    return f"""<!doctype html>
<html lang="nl" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="dark">
<title>{escape(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600&family=Barlow:wght@400;600&family=Bebas+Neue&display=swap" rel="stylesheet">
<style>
  body {{ margin:0; padding:0; background:{C['zwart']}; }}
  a {{ color:{C['leer_licht']}; }}
  @media (max-width: 620px) {{
    .container {{ width:100% !important; }}
    .stack {{ display:block !important; width:100% !important; box-sizing:border-box !important; padding:0 24px !important; }}
    td[style*="padding:0 40px"] {{ padding-left:24px !important; padding-right:24px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{C['zwart']};">
<!-- preheader: zichtbaar in de inbox-preview, verborgen in de mail -->
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{C['zwart']};">{escape(preheader)}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="{C['zwart']}" style="background:{C['zwart']};">
<tr><td align="center" style="padding:24px 12px;">
  <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" bgcolor="{C['asfalt']}" style="width:600px;max-width:600px;background:{C['asfalt']};">
    {header(nr, naam)}
    {''.join(rows)}
    {footer()}
  </table>
</td></tr>
</table>
</body>
</html>
"""


# ---------- de drie mails ----------
MAILS = [
    {
        "bestand": "01-welkom.html", "nr": "01", "naam": "Welkom",
        "onderwerp": "Welkom op de weg, {{voornaam}}",
        "preheader": "Je staat op de lijst. Dit mag je van ons verwachten (en een cadeau voor onderweg).",
        "rows": [
            img("welkom-hero.jpg", "Motorrijder op een stoffig bergpad richting de ondergaande zon"),
            label("Je staat op de lijst", pad="40px 40px 12px"),
            h1("Welcome to<br>the ride."),
            p("Hoi {{voornaam}},", color=C["beige"], size=17),
            p("Goed dat je erbij bent. Holt &amp; Vance maakt parfum voor wie nooit de makkelijke weg kiest: eerlijk, functioneel en gemaakt om mee te gaan. Net als goede uitrusting."),
            p("Vanaf nu rij je mee. Dit mag je van ons verwachten:", pad="0 40px 24px"),
            checklist([
                ("Als eerste bij de lancering", "Noir en Amber gaan binnenkort de weg op. Jij hoort het vóór iedereen."),
                ("Verhalen van onderweg", "Routes, tochten en de mensen achter het merk."),
                ("Maximaal twee mails per maand", "Geen spam. Uitschrijven kan altijd met één klik."),
            ]),
            divider(),
            label("Welkomstcadeau"),
            p("Als dank voor het instappen krijg je 10% korting op je eerste flacon.", pad="0 40px 20px", color=C["beige"]),
            code_box("FIRSTRIDE", "10% op je eerste flacon<br>Geldig 14 dagen"),
            button("Ontdek de geuren", SITE + "#geuren"),
            p("Tot op de weg,<br><span style=\"font-family:" + DISPLAY + ";font-size:26px;letter-spacing:1px;color:" + C["beige"] + ";\">Holt &amp; Vance</span>", pad="0 40px 40px"),
        ],
    },
    {
        "bestand": "02-brand-story.html", "nr": "02", "naam": "Het verhaal",
        "onderwerp": "Hoe Holt & Vance begon (langs de kant van de weg)",
        "preheader": "Een paar avonturiers, een lege tank en een geur die bleef hangen.",
        "rows": [
            img("story-hero.jpg", "Rijder in leren jas trekt zijn handschoenen aan naast een motor in het avondlicht"),
            label("Het verhaal", pad="40px 40px 12px"),
            h1("Born on the<br>long way round."),
            p("Hoi {{voornaam}},", color=C["beige"], size=17),
            p("Holt &amp; Vance begon niet in een lab, maar onderweg. Op de motor, op een bergpas, rond een kampvuur ver van alles. Een paar avonturiers, een lege tank en een avond die langer duurde dan gepland."),
            p("Wat bleef hangen was niet het uitzicht, maar de geur. Nat asfalt bij het vertrek. Warm leer, stof en houtrook bij aankomst. Daar draait alles om: één geur die de hele rit blijft.", pad="0 40px 34px"),
            beige_block(
                label("Waar we voor staan", color=C["leer"])
                + "".join(
                    f"""<tr><td style="padding:0 40px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
                    <td width="150" valign="top" style="font-family:{DISPLAY};font-size:30px;line-height:1;color:{C['zwart']};">{t}</td>
                    <td valign="top" style="font-family:{BODY};font-size:15px;line-height:1.55;color:#4A443C;">{s}</td></tr></table></td></tr>"""
                    for t, s in [
                        ("Freedom", "Geen route, geen planning. Alleen de weg voor je en de tijd die je zelf kiest."),
                        ("Adventure", "Op twee wielen, te voet of met een rugzak vol kampeerspul. Regen, stof en kou horen erbij."),
                        ("Individuality", "Niet voor iedereen, en dat is de bedoeling. Je draagt het op je eigen manier."),
                    ])
            ),
            img("story-band.jpg", "Motor op een kronkelende bergweg tussen dennen en mist"),
            label("Twee geuren, één rit", pad="40px 40px 12px"),
            h1("From cold start<br>to last light.", size=48, pad="0 40px 28px"),
            scent_cards(),
            button("Kies jouw geur", SITE + "#geuren", pad="4px 40px 24px"),
            p("PS: je welkomstcode <strong style=\"color:" + C["beige"] + ";\">FIRSTRIDE</strong> (10%) is nog een week geldig.", size=14, pad="0 40px 40px"),
        ],
    },
    {
        "bestand": "03-reminder.html", "nr": "03", "naam": "Herinnering",
        "onderwerp": "{{voornaam}}, je rit staat nog klaar",
        "preheader": "Je welkomstcadeau verloopt binnenkort. Eén klik en je bent vertrokken.",
        "rows": [
            img("reminder-hero.jpg", "Holt &amp; Vance Noir fles midden op een lege natte weg in de schemering"),
            label("Nog niet vertrokken?", pad="40px 40px 12px"),
            h1("Your ride<br>is waiting."),
            p("Hoi {{voornaam}},", color=C["beige"], size=17),
            p("Een paar dagen geleden stapte je in, maar je bent nog niet vertrokken. Geen probleem: de beste ritten beginnen soms wat later."),
            p("We hebben je welkomstcadeau even voor je vastgehouden.", pad="0 40px 24px", color=C["beige"]),
            code_box("FIRSTRIDE", "10% op je eerste flacon<br><strong style=\"color:" + C["beige"] + ";\">Nog 4 dagen geldig</strong>"),
            button("Claim je 10%", SITE + "#geuren", pad="0 40px 30px"),
            divider(),
            label("Twijfel je tussen twee geuren?"),
            p("<strong style=\"color:" + C["beige"] + ";\">Noir</strong> is voor de koude start: zwarte peper, vetiver en zwart leer.<br><strong style=\"color:" + C["beige"] + ";\">Amber</strong> is voor het einde van de rit: houtrook, tabak en warm leer.", pad="0 40px 30px"),
            p("Liever geen mails meer? Geen probleem, je kunt je <a href=\"#uitschrijven\" style=\"color:" + C["leer_licht"] + ";\">hier uitschrijven</a>. We blijven niet aandringen.", size=14, pad="0 40px 40px"),
        ],
    },
]


def main():
    OUT.mkdir(exist_ok=True)
    for m in MAILS:
        html = wrap(m["onderwerp"], m["preheader"], m["nr"], m["naam"], m["rows"])
        (OUT / m["bestand"]).write_text(html, encoding="utf-8")
        print("✓", m["bestand"], "·", m["onderwerp"])


if __name__ == "__main__":
    main()
