# Génère carrousel.html (10 slides 1080x1350). Modifier HANDLE / textes puis relancer render.
HANDLE = "@mattscouverture"
BLUE, DARK = "#1E73BE", "#1f2933"
S = [
 ("cover", "Votre toit <span style=\"white-space:nowrap\">va-t-il</span> passer l'hiver ?", "5 signes à vérifier. Aucun ne demande de monter sur le toit."),
 ("stake", "Une tuile qui bouge en octobre, c'est une tache au plafond en décembre.", "Voici quoi regarder, depuis la rue et depuis les combles."),
 ("sign", "Depuis la rue", "1. Le faîtage n'est plus droit", "La ligne du haut du toit ondule ? C'est la structure qui travaille, pas seulement les tuiles."),
 ("sign", "Depuis la rue", "2. Des tuiles glissées ou manquantes", "Un problème de fixation ou de support. Le vent d'hiver finit le travail."),
 ("sign", "Depuis la rue", "3. Une gouttière qui déborde ou qui pend", "Avec les feuilles d'automne, l'eau passe par-dessus, mouille la façade et finit par entrer."),
 ("sign", "Depuis les combles", "4. Des points de lumière", "Montez au grenier par une journée de soleil. Si la lumière passe, l'eau passe aussi."),
 ("sign", "Combles · le plus oublié", "5. Des auréoles sombres sur le bois", "Elles dessinent le chemin de l'eau. L'entrée est souvent plusieurs mètres plus haut."),
 ("split", "Réparer ou refaire ?", [("On répare", "Le dégât est localisé et la charpente est saine."), ("On refait", "Le matériau est usé partout ou les fixations lâchent.")]),
 ("recap", "Avant l'hiver, vérifiez :", ["Le faîtage est droit", "Aucune tuile glissée ou manquante", "Les gouttières coulent bien", "Pas de lumière dans les combles", "Pas d'auréole sur le bois"]),
 ("cta", "Un doute sur un de ces signes ?", "Commentez TOIT", "Je passe faire le diagnostic. Devis gratuit.", "07 67 92 68 36 · matts-couverture.fr"),
]
N = len(S)
css = f"""
@page{{size:1080px 1350px;margin:0}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:'Montserrat',sans-serif}}
section{{width:1080px;height:1350px;position:relative;overflow:hidden;padding:150px 130px;display:flex;flex-direction:column;justify-content:center;page-break-after:always;background:{DARK};color:#fff}}
section.light{{background:#f2f2f2;color:{DARK}}}
.n{{position:absolute;top:70px;right:90px;font-size:32px;font-weight:600;opacity:.6}}
.h{{position:absolute;bottom:70px;left:90px;font-size:32px;font-weight:600;opacity:.7}}
.brand{{position:absolute;top:70px;left:90px;font-size:32px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:{BLUE}}}
.bar{{width:140px;height:14px;background:{BLUE};margin-bottom:50px}}
h1{{font-size:118px;line-height:1.05;font-weight:800}}
h2{{font-size:84px;line-height:1.1;font-weight:800;margin-bottom:50px}}
.tag{{font-size:36px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:{BLUE};margin-bottom:40px}}
p{{font-size:48px;line-height:1.35;font-weight:500}}
.sub{{font-size:50px;margin-top:60px;opacity:.85}}
.big{{font-size:72px;line-height:1.25;font-weight:700}}
ul{{list-style:none;padding:0}} li{{font-size:52px;font-weight:600;margin:0 0 38px;padding-left:80px;position:relative}}
li:before{{content:'✓';position:absolute;left:0;color:{BLUE};font-weight:800}}
.box{{border-left:14px solid {BLUE};padding:10px 0 10px 40px;margin-bottom:60px}}
.box b{{display:block;font-size:64px;margin-bottom:16px}}
.kw{{display:inline-block;background:{BLUE};color:#fff;font-size:80px;font-weight:800;padding:20px 50px;white-space:nowrap;margin:50px 0}}
"""
def sec(i, inner, cls=""):
    return f'<section class="{cls}"><div class="brand">Matt\'s Couverture</div><div class="n">{i}/{N}</div>{inner}<div class="h">{HANDLE}</div></section>'
out = []
for i, s in enumerate(S, 1):
    k = s[0]
    if k == "cover": out.append(sec(i, f'<div class="bar"></div><h1>{s[1]}</h1><p class="sub">{s[2]}</p>'))
    elif k == "stake": out.append(sec(i, f'<div class="bar"></div><p class="big">{s[1]}</p><p class="sub">{s[2]}</p>', "light"))
    elif k == "sign": out.append(sec(i, f'<div class="tag">{s[1]}</div><h2>{s[2]}</h2><p>{s[3]}</p>', "light" if i % 2 else ""))
    elif k == "split": out.append(sec(i, f'<h2>{s[1]}</h2>' + "".join(f'<div class="box"><b>{a}</b><p>{b}</p></div>' for a, b in s[2])))
    elif k == "recap": out.append(sec(i, f'<h2>{s[1]}</h2><ul>' + "".join(f"<li>{x}</li>" for x in s[2]) + "</ul>", "light"))
    elif k == "cta": out.append(sec(i, f'<h2>{s[1]}</h2><div><span class="kw">{s[2]}</span></div><p>{s[3]}</p><p class="sub">{s[4]}</p>'))
html = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet"><style>{css}</style></head><body>{"".join(out)}</body></html>'
open("carrousel.html", "w", encoding="utf-8").write(html)
