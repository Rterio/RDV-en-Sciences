# Site du RDV en Sciences : guide de modification

Ce guide explique comment modifier le site **rdv-en-sciences.aesgul.com**, même sans expérience en programmation. Il s'adresse aux prochains comités organisateurs et à toute IA (ChatGPT, Claude, Copilot…) qu'on utiliserait pour faire les modifications.

**Le plus important à retenir :**
- Le site est fait de simples fichiers texte (HTML, CSS, JavaScript). Il n'y a rien à installer ni à « compiler » : ce que vous enregistrez est ce qui est publié.
- Pour modifier une page, on **copie un bloc existant qui ressemble à ce qu'on veut**, on le colle à côté et on change le texte. Presque toutes les tâches de ce guide fonctionnent comme ça.
- Les noms de fichiers d'images s'écrivent **en minuscules, sans accents ni espaces**, avec des tirets : `marie-tremblay.jpg`, pas `Marie Tremblay.JPG`.

---

## Table des matières

1. [Comment le site fonctionne](#1-comment-le-site-fonctionne)
2. [Outils et publication](#2-outils-et-publication)
3. [Règles d'or](#3-règles-dor)
4. [Plan des fichiers](#4-plan-des-fichiers)
5. [Tâches courantes](#5-tâches-courantes)
6. [Le passage à une nouvelle édition (chaque année)](#6-le-passage-à-une-nouvelle-édition-chaque-année)
7. [Les pages d'édition, bloc par bloc](#7-les-pages-dédition-bloc-par-bloc)
8. [Couleurs, polices et identité visuelle](#8-couleurs-polices-et-identité-visuelle)
9. [Images](#9-images)
10. [Fichiers à ne pas supprimer](#10-fichiers-à-ne-pas-supprimer)
11. [Dépannage](#11-dépannage)
12. [Utiliser une IA pour modifier le site](#12-utiliser-une-ia-pour-modifier-le-site)
13. [Annexe : bibliothèque d'icônes](#13-annexe--bibliothèque-dicônes)

---

## 1. Comment le site fonctionne

**Chaque dossier est une page.** Le fichier `index.html` d'un dossier est la page qui s'affiche à cette adresse :

| Adresse | Fichier |
|---|---|
| rdv-en-sciences.aesgul.com/ | `index.html` |
| …/activites/ | `activites/index.html` |
| …/partenaires/ | `partenaires/index.html` |
| …/organisation/ | `organisation/index.html` |
| …/editions/ | `editions/index.html` |
| …/editions/2025/ | `editions/2025/index.html` |

**Trois types de fichiers :**
- **HTML** (`.html`) : le contenu de la page, c'est-à-dire le texte, les images et les liens. C'est ici qu'on fait 90 % des modifications.
- **CSS** (`.css`, dans `assets/`) : l'apparence, soit les couleurs, les polices et la mise en page.
- **JavaScript** (`assets/site.js`) : le menu et le pied de page, communs à toutes les pages, et l'affichage des images de remplacement.

**Lire du HTML en 30 secondes.** Le HTML est du texte entouré de balises : `<p>Bonjour</p>` est un paragraphe. Une balise ouvrante `<p>` a toujours une balise fermante `</p>`. Le mot après `class=` sert à donner une apparence (définie dans le CSS) : on peut le copier, mais pas l'inventer.

```html
<li>                                   ← début d'un élément de liste
  <span class="name">Zoé Jargaille</span>   ← le texte à modifier
  <span class="role">Présidente</span>
</li>                                  ← fin de l'élément
```

**Règle d'or :** modifiez le texte **entre** les balises, et ne touchez aux balises que pour copier ou supprimer un bloc complet, de sa balise ouvrante à sa balise fermante.

---

## 2. Outils et publication

### Ce qu'il vous faut
- **Visual Studio Code** (gratuit) pour modifier les fichiers. Ouvrez le dossier complet du site avec *Fichier > Ouvrir le dossier*.
- L'extension **Live Server** dans VS Code, pour voir le site sur votre ordinateur avant de le publier : clic droit sur `index.html`, puis *Open with Live Server*. La page se met à jour à chaque enregistrement.
  - Sans Live Server, ouvrez un terminal dans le dossier et tapez `python3 -m http.server 8000`, puis allez sur http://localhost:8000.
  - Évitez d'ouvrir les fichiers en double-cliquant dessus : les liens entre les pages ne fonctionneraient pas.

### Publier les changements
Le site est hébergé sur **GitHub Pages**. Tout ce qui est envoyé sur GitHub est publié automatiquement, en général en 1 à 2 minutes.

Trois façons d'envoyer vos changements, de la plus simple à la plus pratique :
1. **Directement sur github.com** : ouvrez le fichier dans le dépôt, cliquez sur le crayon (*Edit*), modifiez, puis *Commit changes*. Pour ajouter des images : allez dans le bon dossier, puis *Add file > Upload files*.
2. **GitHub Desktop** (application gratuite) : modifiez les fichiers sur votre ordinateur, puis *Commit* et *Push origin*.
3. **VS Code** : onglet *Source Control* (icône de branches), écrivez un message, *Commit*, puis *Sync*.

**Après publication**, si vous ne voyez pas le changement, forcez le rechargement sans cache : `Ctrl + F5` (Windows) ou `Cmd + Shift + R` (Mac).

### Le nom de domaine
Le fichier `CNAME` à la racine contient seulement `rdv-en-sciences.aesgul.com` (s'il n'existe pas encore, créez-le au moment de brancher le domaine, ou réglez le domaine dans *Settings > Pages* du dépôt GitHub). Chez le gestionnaire DNS d'aesgul.com, l'entrée `rdv-en-sciences` est un enregistrement CNAME qui pointe vers `<compte-github>.github.io`. On n'y touche que si on change de compte GitHub.

---

## 3. Règles d'or

1. **Faites une modification à la fois, et vérifiez-la** dans Live Server avant de passer à la suivante.
2. **Copiez un bloc existant** plutôt que de partir de zéro.
3. **Noms de fichiers : minuscules, sans accents, tirets à la place des espaces.** GitHub fait la différence entre `Photo.JPG` et `photo.jpg` : un seul caractère différent et l'image ne s'affiche pas.
4. **Les chemins sont relatifs.** `../` veut dire « remonter d'un dossier ». Une page dans `organisation/` écrit `../images/…`, et une page dans `editions/2025/` écrit `../../images/…`. Quand vous copiez un bloc d'une page à une autre, vérifiez le nombre de `../`.
5. **Gardez les accents dans le texte** (é, à, ç) : seuls les noms de fichiers n'en ont pas.
6. **Ne supprimez pas les dossiers avec des accents** (`activités/`, `éditions-passées/`, etc.) : ce sont des redirections pour les anciens liens (voir la [section 10](#10-fichiers-à-ne-pas-supprimer)).
7. **Si quelque chose casse**, annulez avec `Ctrl + Z` (ou `Cmd + Z`) ; sur GitHub, l'historique (*History*) permet de revenir à n'importe quelle version précédente.

---

## 4. Plan des fichiers

```
rdv-en-sciences/
├── index.html                 Accueil
├── activites/index.html       Programmation de l'année en cours
├── partenaires/index.html     Partenaires de l'année en cours
├── organisation/index.html    Comité organisateur de l'année en cours
├── editions/
│   ├── index.html             Liste des éditions passées
│   ├── 2023/index.html        Une page par édition passée
│   ├── 2024/index.html
│   ├── 2025/index.html
│   └── 2026/index.html
├── assets/
│   ├── site.js                Menu, pied de page, lien de billetterie, réseaux sociaux
│   ├── style.css              Apparence générale et couleurs de l'année en cours
│   ├── editions.css           Couleurs et mise en page des pages d'édition
│   ├── carousel.js            Carrousel de photos des pages d'édition
│   └── fonts/                 Polices installées localement (ex. roca-one.woff2)
├── images/
│   ├── logo.png               Logo de l'en-tête et icône d'onglet
│   ├── embleme.png            Grand emblème de la page d'accueil
│   ├── partage-2027.png       Image d'aperçu sur Facebook, Messenger, etc.
│   ├── activites-1.jpg …      Affiches de la programmation
│   ├── organisation/          Photos de l'équipe
│   ├── partenaires/           Logos des partenaires
│   └── editions/              Logos et photos des éditions passées
├── scripts/telecharger-images.py   Récupérait les images de l'ancien site Google Sites
├── 404.html                   Page « introuvable »
├── CNAME                      Nom de domaine (ne pas modifier)
├── .nojekyll                  Réglage GitHub Pages (ne pas supprimer)
└── activités/, accueil/, éditions-passées/, édition-2027/, partenaires-2026/
                               Redirections des anciennes adresses (ne pas supprimer)
```

---

## 5. Tâches courantes

### 5.1 Changer le lien de billetterie, le courriel ou les réseaux sociaux
Tout est en haut de `assets/site.js` :

```js
const SITE = {
  billets: "https://evelya.co/…",          ← lien des boutons « Acheter un billet »
  courriel: "presidence@rdv-en-sciences.aesgul.com",
  facebook: "https://www.facebook.com/RDVenSciences",
  instagram: "https://www.instagram.com/rdv_en_sciences/",
  menu: [ … ],                             ← les liens du menu principal
};
```

Changez seulement ce qui est entre guillemets. Le changement s'applique automatiquement à toutes les pages.

### 5.2 Changer les dates, le lieu ou le texte de l'accueil
Dans `index.html` :

```html
<p class="hero-kicker">5e édition, campus de l'Université Laval</p>
<h1>RDV en Sciences</h1>
<p class="hero-dates"><span>19–21 mars</span><span class="year">2027</span></p>
```

Plus bas dans le même fichier se trouvent le texte de présentation, la vidéo YouTube (changez seulement l'identifiant après `embed/`), l'adresse et la carte.

### 5.3 Ajouter, modifier ou retirer un membre de l'équipe
Dans `organisation/index.html`, chaque personne est un bloc `<li>…</li>` :

```html
<li>
  <img data-initials="ZJ" data-placeholder="Photo à venir" src="../images/organisation/zoe-jargaille.jpg" alt="" loading="lazy" width="400" height="400">
  <span class="name">Zoé Jargaille</span>
  <span class="study">Baccalauréat en biochimie</span>
  <span class="role">Présidence</span>
</li>
```

- **Ajouter :** copiez un bloc `<li>…</li>` complet, collez-le à l'endroit voulu, puis changez le nom, le programme d'études, le rôle, le nom du fichier photo et les initiales (`data-initials`).
- **Retirer :** supprimez le bloc `<li>…</li>` au complet.
- **Photo :** déposez la photo dans `images/organisation/` avec **exactement** le nom écrit dans `src` (ex. `zoe-jargaille.jpg`). Format carré, environ 600 × 600 px. Tant que la photo n'existe pas, les initiales s'affichent.
- La ligne `study` est facultative. Si elle ne s'affiche pas sur sa propre ligne, ajoutez ceci à la fin de `assets/style.css` :
  ```css
  .people .study { display: block; color: var(--slate); font-size: 0.9rem; font-style: italic; }
  .people .role { display: block; }
  ```

### 5.4 Modifier la programmation (page Activités)
`activites/index.html` affiche deux affiches : `images/activites-1.jpg` et `images/activites-2.jpg`. Le plus simple est de remplacer ces fichiers par les nouvelles affiches, **en gardant les mêmes noms**. Pour présenter plutôt la programmation sous forme de cartes, comme sur les pages d'édition, demandez-le à une IA (voir la [section 12](#12-utiliser-une-ia-pour-modifier-le-site)) : il faut adapter un peu le code de la [section 7.4](#74-la-programmation).

### 5.5 Mettre à jour les partenaires de l'année
Dans `partenaires/index.html`, chaque niveau (Platine, Or, Argent, Bronze…) est un bloc `<section class="tier …">`, et chaque partenaire est un bloc `<article class="partner">` :

```html
<section class="tier tier-bronze" aria-labelledby="tier-bronze">
  <h2 class="tier-name" id="tier-bronze">Bronze</h2>
  <div class="partners compact">
    <article class="partner">
      <div class="partner-logo"><img src="../images/partenaires/ibis.png" alt="Logo IBIS" loading="lazy" onerror="this.remove()"></div>
      <div>
        <h3><a href="https://www.ibis.ulaval.ca/">Institut de biologie intégrative et des systèmes (IBIS)</a></h3>
      </div>
    </article>
  </div>
</section>
```

- **Niveaux disponibles** (pour la couleur de la pastille) : `tier-platine`, `tier-or`, `tier-argent`, `tier-bronze`. Changez aussi le texte du `<h2>` et l'`id` (ex. `tier-or`).
- `partners` donne de grandes cartes avec description ; `partners compact` donne de petites cartes sans description, sur plusieurs colonnes.
- **Description** (facultative) : ajoutez `<p>Texte…</p>` sous le `<h3>`.
- **Sans site web :** retirez `<a href="…">` et `</a>` autour du nom.
- **Logo :** fichier PNG dans `images/partenaires/`, au nom écrit dans `src`. Sans logo, la carte affiche seulement le nom.
- **Logo entièrement blanc :** ajoutez `class="logo-dark-bg"` dans la balise `<img>` pour l'afficher sur une pastille foncée. Le mieux reste de demander au partenaire une version couleur.

### 5.6 Élargir un paragraphe
Les paragraphes sont limités à environ 65 caractères par ligne pour rester lisibles. Pour qu'un paragraphe prenne toute la largeur : `<p class="lead" style="max-width: none">`.

---

## 6. Le passage à une nouvelle édition (chaque année)

Après l'évènement, il y a deux choses à faire : **archiver l'édition terminée** dans les éditions passées, puis **préparer le site pour l'édition suivante**. Les exemples ci-dessous utilisent 2027 (édition terminée) et 2028 (prochaine édition) : remplacez-les par les bonnes années.

### Étape A : archiver l'édition terminée (ex. 2027)

**A1. Créer la page.** Copiez le dossier `editions/2026/` et renommez la copie `editions/2027/`.

**A2. Ajouter les couleurs de l'année** dans `assets/editions.css`, en copiant le bloc `.ed-2026 { … }` et en le renommant `.ed-2027`. Les couleurs viennent du logo de l'année (voir la [section 8](#8-couleurs-polices-et-identité-visuelle) pour le rôle de chaque couleur).

**A3. Ajouter le logo** de l'année dans `images/editions/logo-2027.png` (PNG à fond transparent, environ 700 px de large).

**A4. Adapter `editions/2027/index.html`.** Dans le fichier, remplacez :
- `<body class="edition ed-2026">` par `ed-2027` ;
- le `<title>`, les balises `<meta>` du haut et le `<h1>` ;
- `<span class="ed-ordinal">4e édition</span>` par `5e édition` ;
- le thème (`<p class="ed-theme">…</p>`) et le paragraphe de résumé (`<p class="lead">`) ;
- le logo : `logo-2026.png` devient `logo-2027.png` (dans le haut de la page) ;
- les chiffres, la programmation, les activités, les partenaires et les photos (détails à la [section 7](#7-les-pages-dédition-bloc-par-bloc)) ;
- l'illustration du thème : voir la [section 7.1](#71-le-haut-de-page-et-lillustration-du-thème).

**A5. Mettre à jour les boutons d'année.** Dans **chaque** page `editions/AAAA/index.html`, ajoutez la nouvelle année en tête des boutons « Choisir une édition », et marquez la bonne année avec `aria-current="page"` dans la nouvelle page :

```html
<a href="../../editions/2027/" aria-current="page">2027</a>
<a href="../../editions/2026/">2026</a>
```

**A6. Mettre à jour les liens « Édition précédente / suivante »** en bas des pages (voir la [section 7.7](#77-édition-précédente--suivante)) :
- dans `editions/2026/index.html`, ajoutez un lien « Édition suivante » vers 2027 ;
- dans `editions/2027/index.html`, gardez seulement « Édition précédente » vers 2026.

**A7. Ajouter l'année aux lignes du temps** de `index.html` (accueil) et de `editions/index.html`, en copiant un bloc `<li>…</li>` existant :

```html
<li>
  <a class="tl-card ed-2027" href="editions/2027/">
    <img class="tl-logo" src="images/editions/logo-2027.png" alt="" width="48" height="43">
    <span class="yr">2027</span>
    <span class="num">Plus de 150 participants</span>
    <span class="detail">5 conférences, 2 tables rondes</span>
    <span class="more">Voir l'édition</span>
  </a>
</li>
```

Dans `editions/index.html`, les chemins commencent par `../` (`../editions/2027/`, `../images/…`).

La ligne du temps est prévue pour 4 colonnes. Avec une 5e année, dans `assets/style.css`, changez `repeat(4, 1fr)` en `repeat(5, 1fr)` sur la ligne qui commence par `.timeline {`. Vous pouvez aussi retirer la plus ancienne année de l'accueil, puisqu'elle reste accessible dans *Éditions passées*.

Pour la couleur du point sur la ligne du temps, ajoutez à la fin de `assets/editions.css` :
```css
.timeline li:nth-child(5)::before { border-color: #COULEUR_FONCÉE_2027; }
```

**A8. Ajouter la carte de 2027** à la section « Partenaires des éditions précédentes » de `partenaires/index.html`, en copiant une carte existante.

### Étape B : préparer l'édition suivante (ex. 2028)

1. **Accueil** (`index.html`) : numéro d'édition, dates, lieu, texte (voir la [section 5.2](#52-changer-les-dates-le-lieu-ou-le-texte-de-laccueil)).
2. **Billetterie** dans `assets/site.js` (voir la [section 5.1](#51-changer-le-lien-de-billetterie-le-courriel-ou-les-réseaux-sociaux)).
3. **Identité visuelle** : nouveaux logos et nouvelles couleurs (voir la [section 8](#8-couleurs-polices-et-identité-visuelle)).
4. **Organisation** : la nouvelle équipe (voir la [section 5.3](#53-ajouter-modifier-ou-retirer-un-membre-de-léquipe)).
5. **Partenaires** : changez le titre (`Partenaires 2028`) et remplacez la liste. En attendant les confirmations, vous pouvez afficher seulement le bloc « Votre organisation veut s'impliquer? ».
6. **Activités** : nouvelles affiches ou nouvelles cartes.
7. **Image de partage** : remplacez `images/partage-2027.png` par une image de 1200 × 630 px, et mettez à jour son nom dans la balise `og:image` de `index.html`.

---

## 7. Les pages d'édition, bloc par bloc

Chaque page `editions/AAAA/index.html` est faite des mêmes blocs, dans cet ordre. Tous sont facultatifs : pour retirer une section, supprimez le bloc `<section …>…</section>` au complet.

### 7.1 Le haut de page et l'illustration du thème
Le bloc `<section class="ed-hero has-art">` contient :
- l'**illustration du thème** : une longue balise `<svg class="ed-art">…</svg>` (étoiles et aurore en 2025, réseau de neurones en 2024, ampoule en 2026) ;
- le numéro d'édition, le titre, le thème, le résumé, les boutons d'année et le logo.

**Pour une nouvelle année, trois options :**
1. **Pas d'illustration :** supprimez toute la balise `<svg class="ed-art">…</svg>` et retirez `has-art` de `<section class="ed-hero has-art">`. Un motif d'hexagones discret s'affiche à la place.
2. **Réutiliser une illustration** d'une autre année : elle prendra automatiquement les couleurs de la nouvelle année. Si elle utilise `var(--e-line)`, définissez `--e-line` dans le bloc de couleurs de l'année.
3. **Demander une nouvelle illustration à une IA** (voir la [section 12](#12-utiliser-une-ia-pour-modifier-le-site)).

**Thème de l'année** (facultatif), sous le `<h1>` :
```html
<p class="ed-theme"><span>Thème</span> Innovations scientifiques</p>
```

### 7.2 Les chiffres (ruche d'hexagones)
```html
<ul class="honeycomb">
  <li class="ed-stat"><span class="q">Plus de</span><span class="n">150</span><span class="l">participants</span></li>
  <li class="ed-stat"><span class="n">5</span><span class="l">conférences</span></li>
</ul>
```
- `q` : petit texte au-dessus du chiffre (facultatif) ; `n` : le chiffre ; `l` : ce qu'il compte.
- Les couleurs des hexagones alternent automatiquement selon les couleurs de l'année. De 4 à 6 chiffres, c'est l'idéal.

### 7.3 Les sujets abordés (liste simple, facultative)
Si vous n'avez que des thèmes sans détails, utilisez une liste plutôt que la programmation complète :
```html
<section class="ed-topics">
  <div class="wrap">
    <h2>Les sujets abordés</h2>
    <ul class="topic-list">
      <li>ICÔNE ICI<span>L’intelligence artificielle</span></li>
    </ul>
  </div>
</section>
```
Remplacez `ICÔNE ICI` par une icône de l'[annexe](#13-annexe--bibliothèque-dicônes).

### 7.4 La programmation
Chaque activité est une carte :
```html
<li class="session c-k1">
  <div class="session-top">ICÔNE ICI<span class="session-type">Conférence</span></div>
  <h3>Titre de la conférence</h3>
  <p class="session-who"><strong>Nom de la personne</strong><br>Son rôle ou sa profession</p>
</li>
```
- **Icône :** copiez une icône de l'[annexe](#13-annexe--bibliothèque-dicônes) à la place de `ICÔNE ICI`.
- **Sans conférencier connu :** supprimez la ligne `<p class="session-who">…</p>`. Sans rôle : supprimez `<br>` et le rôle.
- **Couleur de la carte** (le mot après `session`) :
  - `c-k1`, `c-k2`, `c-k3` : trois couleurs tirées automatiquement de la palette de l'année. Par convention, `c-k1` pour les conférences, `c-k2` pour les ateliers et `c-k3` pour les tables rondes et panels.
  - Couleurs fixes, pour imiter les couleurs des affiches : `c-blue`, `c-red`, `c-orange`, `c-yellow`, `c-green`, `c-sky`, `c-purple`.
- Modifiez aussi la phrase d'introduction au-dessus des cartes (ex. « Cinq conférences, un atelier… »).

### 7.5 Aussi au programme
```html
<ul class="extras"><li>Soirée brise-glace</li><li>Cocktail de réseautage</li></ul>
```
Une activité par `<li>…</li>`.

### 7.6 Les photos et les partenaires
**Photos (carrousel)** : bloc `<section class="ed-photos">`. Chaque photo est une ligne `<figure class="gf-slide">` dans `<div class="gf-track">` :
```html
<figure class="gf-slide"><img src="../../images/editions/2027-01.webp" data-thumb="../../images/editions/2027-01-mini.webp" alt="Cocktail de réseautage" data-placeholder="Photo de l’édition 2027" loading="lazy" width="1400" height="933"><figcaption>Cocktail de réseautage</figcaption></figure>
```
- **Ajouter une photo :** copiez une ligne `<figure>…</figure>`, changez le nom du fichier, le texte `alt` et la légende (`<figcaption>`). Les flèches, le compteur et les miniatures se mettent à jour tout seuls.
- **Retirer une photo :** supprimez sa ligne `<figure>…</figure>`.
- **Ordre :** l'ordre des lignes est l'ordre du carrousel. Mettez la plus belle photo en premier : c'est celle qu'on voit en arrivant. Entre 8 et 15 photos, c'est l'idéal.
- La première photo n'a pas `loading="lazy"` (elle s'affiche tout de suite) ; les suivantes l'ont.
- `data-thumb` (la miniature) est facultatif ; sans lui, la photo complète sert de miniature.
- Le cadre, les flèches et les hexagones décoratifs prennent automatiquement les couleurs de l'année.

**Préparer les photos (important pour l'espace disque) :** ne mettez jamais les fichiers originaux du photographe sur le site (souvent 5 à 10 Mo chacun). Convertissez-les au format **WebP** :
- photo : 1400 × 933 px, qualité 70 à 75 → environ 80 à 150 Ko ;
- miniature (`-mini.webp`) : 360 × 240 px, qualité 65 → environ 15 Ko.

Le plus simple : https://squoosh.app (gratuit, dans le navigateur). Glissez la photo, choisissez *WebP*, cochez *Resize* (largeur 1400), puis téléchargez. Nommez les fichiers `AAAA-01.webp`, `AAAA-01-mini.webp`, etc., dans `images/editions/`. Une IA ou un petit script Python (bibliothèque Pillow) peut aussi convertir tout un dossier d'un coup.

Gardez les originaux ailleurs (Google Drive de l'association, par exemple), pas dans le dépôt GitHub.

**Partenaires de l'édition** : bloc `<section class="ed-partners" id="partenaires">`. Chaque niveau :
```html
<div class="p-tier p-or"><h3>Or</h3><div class="p-cards">
  <a class="p-card" href="https://site-du-partenaire.ca"><img src="../../images/partenaires/nom.png" alt="" loading="lazy" onerror="this.remove()"><span>Nom du partenaire</span></a>
</div></div>
```
- Niveaux : `p-platine`, `p-diamant`, `p-beryl`, `p-or`, `p-argent`, `p-bronze`, `p-autres`.
- Sans site web : remplacez `<a class="p-card" href="…">…</a>` par `<div class="p-card">…</div>`.
- Astuce : à la fin de l'édition, les partenaires de `partenaires/index.html` sont ceux à recopier ici.

### 7.7 Édition précédente / suivante
```html
<nav class="ed-pager" aria-label="Autres éditions">
  <div class="wrap">
    <a class="prev ed-2025" href="../../editions/2025/">
      <img src="../../images/editions/logo-2025.png" alt="" width="72" height="64">
      <span><span class="dir">Édition précédente</span><span class="yr">2025</span><span class="go">Voir l’édition 2025</span></span>
    </a>
    <a class="next ed-2027" href="../../editions/2027/">
      <img src="../../images/editions/logo-2027.png" alt="" width="72" height="64">
      <span><span class="dir">Édition suivante</span><span class="yr">2027</span><span class="go">Voir l’édition 2027</span></span>
    </a>
  </div>
</nav>
```
Chaque carte prend les couleurs de l'année vers laquelle elle mène (classe `ed-AAAA`).

---

## 8. Couleurs, polices et identité visuelle

### Couleurs de l'année en cours (tout le site)
En haut de `assets/style.css`, dans le bloc `:root { … }` :

| Variable | Rôle | 2027 |
|---|---|---|
| `--ink` | Fond foncé (en-tête, pied de page, haut des pages) et texte principal | `#164a36` |
| `--ink-2` | Variante un peu plus claire de `--ink` | `#1e5a42` |
| `--green` | Boutons sur fond clair | `#326b4e` |
| `--sage` | Boutons et accents sur fond foncé | `#a4b793` |
| `--paper` | Fond clair | `#f5f1e8` |
| `--frost` | Bordures | `#e1e5d6` |
| `--slate` | Texte secondaire | `#4b6457` |
| `--rust`, `--sky`, `--navy` | Petits accents | |

Changez seulement les codes de couleur (`#…`). Gardez un bon contraste : texte foncé sur fond clair, et l'inverse.

### Couleurs des éditions passées
Dans `assets/editions.css`, chaque année a son bloc `.ed-AAAA { … }` :

| Variable | Rôle |
|---|---|
| `--e-bg` | Couleur foncée principale : haut de page, titres, cartes |
| `--e-fill` | Couleur vive de remplissage du logo : boutons, pastilles |
| `--e-c1`, `--e-c2`, `--e-c3` | Les trois couleurs d'accent du logo (atome, ADN, sigma) |
| `--e-line` | Facultatif : couleur de contour, utilisée pour l'ombre du titre |
| `--e-tint` | Version très pâle de la couleur de remplissage (fonds de photos à venir) |
| `--e-on-fill` | Couleur du texte posé sur `--e-fill` |
| `--e-t1`, `--e-t2`, `--e-t3` | Facultatif : texte foncé sur les accents trop pâles pour du texte blanc |
| `--e-font` | Facultatif : police propre à l'année (ex. 2026) |

### Polices
- **Titres :** Roca One (police de l'identité 2027). Le fichier doit se trouver dans `assets/fonts/roca-one.woff2` ; sinon, Young Serif est utilisée.
- **Texte :** Schibsted Grotesk, chargée depuis Google Fonts.
- **Police propre à une édition** (comme 2026) : ajoutez la police Google Fonts dans le `<head>` de la page d'édition, puis `--e-font: "Nom de la police", serif;` dans son bloc `.ed-AAAA`.

### Logos
| Fichier | Où il apparaît | Format conseillé |
|---|---|---|
| `images/logo.png` | En-tête de toutes les pages, icône d'onglet | Carré, fond transparent, 512 × 512 px |
| `images/embleme.png` | Grand emblème de l'accueil | Carré, fond transparent, 1024 × 1024 px |
| `images/partage-AAAA.png` | Aperçu des liens partagés sur les réseaux | 1200 × 630 px |
| `images/editions/logo-AAAA.png` | Pages et cartes des éditions passées | Fond transparent, environ 700 px de large |

---

## 9. Images

**Où les mettre :**
- Équipe : `images/organisation/prenom-nom.jpg`
- Partenaires : `images/partenaires/nom.png`
- Éditions passées : `images/editions/AAAA-01.webp`, `AAAA-01-mini.webp`…
- Affiches de la programmation : `images/activites-1.jpg`, `images/activites-2.jpg`

**Tailles et formats conseillés :**
- Photos : WebP (ou JPG), 1400 px de large au maximum, moins de 200 Ko. Pour réduire une image : https://squoosh.app (gratuit, dans le navigateur). Voir aussi la [section 7.6](#76-les-photos-et-les-partenaires).
- Portraits : carrés, environ 600 × 600 px.
- Logos : PNG à fond transparent.

**Images de remplacement automatiques.** Une image qui porte `data-placeholder="…"` (ou `data-initials="…"` pour un portrait) affiche un encadré avec ce texte tant que le fichier n'existe pas. Dès que le fichier est ajouté avec le bon nom, la vraie image s'affiche, sans rien modifier dans le code. Les logos de partenaires avec `onerror="this.remove()"` disparaissent simplement s'il n'y a pas de fichier, et la carte affiche le nom.

**Ajoutez toujours un texte `alt`** qui décrit l'image pour les personnes malvoyantes, sauf pour les images purement décoratives (`alt=""`).

---

## 10. Fichiers à ne pas supprimer

- **Dossiers avec accents** (`activités/`, `accueil/`, `éditions-passées/…`, `édition-2027/organisation/`, `partenaires-2026/`) : ce sont les adresses de l'ancien site Google Sites. Chacun redirige automatiquement vers la nouvelle page, pour que les anciens liens et favoris fonctionnent encore. Ne les modifiez pas.
- **`CNAME`** : relie le site au nom de domaine rdv-en-sciences.aesgul.com.
- **`.nojekyll`** : indique à GitHub Pages de publier les fichiers tels quels.
- **`404.html`** : la page affichée pour une adresse qui n'existe pas.
- **`scripts/telecharger-images.py`** : a servi à récupérer les images de l'ancien site ; il ne fonctionne que tant que l'ancien site Google Sites existe.

---

## 11. Dépannage

| Problème | Cause probable et solution |
|---|---|
| Une image ne s'affiche pas | Le nom du fichier ne correspond pas exactement au `src` (majuscules, accents, extension `.jpg` vs `.jpeg` vs `.png`). |
| Une page s'affiche sans mise en forme | Le chemin vers `assets/style.css` a le mauvais nombre de `../`. Comparez avec une autre page dans un dossier de même profondeur. |
| Le menu ou le pied de page a disparu | Erreur dans `assets/site.js` (souvent un guillemet ou une virgule manquante dans le bloc `SITE`). Annulez la dernière modification. |
| Le changement n'apparaît pas en ligne | Attendez 1 à 2 minutes après l'envoi sur GitHub, puis rechargez sans cache (`Ctrl + F5` ou `Cmd + Shift + R`). Vérifiez dans l'onglet *Actions* du dépôt GitHub que la publication a réussi. |
| La mise en page est décalée après une modification | Une balise n'est pas fermée (ex. un `<div>` sans `</div>`). Dans VS Code, cliquez sur une balise : sa jumelle est surlignée. |
| VS Code remplace le texte au lieu d'insérer | Mode « refrappe » activé par erreur : appuyez sur la touche `Insert` (ou `Ctrl/Cmd + Shift + P` > *Toggle Overtype/Insert Mode*). |
| Un texte reste coupé en largeur | Voir la [section 5.6](#56-élargir-un-paragraphe). |

---

## 12. Utiliser une IA pour modifier le site

Une IA peut faire la plupart des modifications de ce guide. Donnez-lui ce fichier `README.md` et le ou les fichiers à modifier.

### Consignes pour l'IA
Si vous êtes une IA qui modifie ce site, respectez ces règles :

- **Site 100 % statique :** HTML, CSS et JavaScript simples, sans framework, sans étape de compilation, sans gestionnaire de paquets. Ne proposez pas de migrer vers React, Jekyll, Tailwind, etc.
- **Réutilisez les classes et les structures existantes** décrites dans ce guide. N'inventez pas de nouvelles classes si une classe existante convient ; si vous devez en créer, ajoutez le CSS à la fin du bon fichier (`style.css` pour tout le site, `editions.css` pour les pages d'édition), avec un commentaire en français.
- **Chemins relatifs uniquement** (`../`, `../../`), jamais de chemins commençant par `/`. Le site doit fonctionner à la fois sur le domaine et sur l'adresse `compte.github.io/depot/`.
- **Le menu et le pied de page** sont générés par `assets/site.js` à partir des balises `<div data-site-header></div>` et `<div data-site-footer></div>`. Ne les copiez pas en HTML dans les pages.
- **Contenu en français du Québec**, avec l'écriture inclusive déjà utilisée sur le site (« étudiants et étudiantes », « conférencier·ères »).
- **Ne supprimez pas** les dossiers de redirection, `CNAME`, `.nojekyll` ni `404.html`.
- **Accessibilité :** textes `alt` pour les images, contraste suffisant, une seule balise `<h1>` par page.
- **N'inventez pas d'informations** (noms, chiffres, dates, partenaires) : demandez-les si elles manquent.
- **Ne modifiez que ce qui est demandé**, et indiquez clairement quels fichiers ont changé.

### Exemples de demandes
> Voici le README du site et le fichier `organisation/index.html`. Ajoute Marie Tremblay, Baccalauréat en physique, VP Communications, dans le comité d'organisation, après Zoé Jargaille. Sa photo s'appellera `marie-tremblay.jpg`.

> Voici le README, `editions/2026/index.html` et `assets/editions.css`. Crée la page de l'édition 2027 en suivant l'étape A de la section 6. Couleurs du logo 2027 : fond #164a36, remplissage #a4b793, atome #b0673f, ADN #31547c, sigma #4098cb. Programmation : [liste]. Partenaires : [liste]. Chiffres : [liste].

> Voici le README et `editions/2027/index.html`. Le thème de 2027 était « [thème] ». Dessine une illustration SVG pour le haut de page, sur le modèle des balises `<svg class="ed-art">` des autres années : 900 × 520, couleurs uniquement avec les variables `var(--e-c1)`, `var(--e-c2)`, `var(--e-c3)`, `var(--e-fill)` et du blanc, avec le sujet principal dans la moitié droite pour laisser le texte lisible à gauche.

---

## 13. Annexe : bibliothèque d'icônes

Ces icônes s'utilisent dans les cartes de programmation (`session-top`) et dans les listes de sujets (`topic-list`). Copiez le bloc complet à la place de `ICÔNE ICI`. L'icône prend automatiquement la couleur de sa carte.

Pour une nouvelle icône, prenez une icône « outline » 24 × 24 sur https://lucide.dev, copiez seulement les balises `<path>`, `<circle>`, etc., et collez-les à la place de celles d'une icône ci-dessous.

**Espace, planète, astronomie** (`espace`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><ellipse cx="12" cy="12" rx="10.5" ry="3.6" transform="rotate(-20 12 12)"/></svg></span>
```

**Fusée, exploration spatiale, astrophysique** (`fusee`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4c3-1 5-1 6 0 1 1 1 3 0 6l-6 6-4-4z"/><path d="m10 12-3 1-3 3 4 1M12 14l-1 3-3 3-1-4"/><circle cx="16" cy="8" r="1.5"/></svg></span>
```

**Nord, flocon, Arctique** (`nord`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7"/><path d="m9.5 3.5 2.5 2 2.5-2M9.5 20.5l2.5-2 2.5 2"/></svg></span>
```

**Globe, international, science ouverte** (`international`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg></span>
```

**Feuille, savoirs autochtones, environnement** (`autochtones`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14z"/><path d="M5 19 13 11"/></svg></span>
```

**Ampoule, idée, entrepreneuriat** (`entrepreneuriat`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.3 1 2.2h5.2c0-.9.4-1.7 1-2.2A6 6 0 0 0 12 3z"/></svg></span>
```

**Ampoule avec horloge, innovation, recherche** (`innovation`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.3 1 2.2h5.2c0-.9.4-1.7 1-2.2A6 6 0 0 0 12 3z"/><path d="M12 7v3l1.5 1.5"/></svg></span>
```

**Document, articles scientifiques** (`articles`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg></span>
```

**Bulle de dialogue, communication, vulgarisation** (`communication`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></svg></span>
```

**Loupe, pensée critique** (`pensee`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg></span>
```

**Balance, éthique** (`ethique`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M7 20h10M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/></svg></span>
```

**Puce électronique, intelligence artificielle** (`ia`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg></span>
```

**Cerveau, neurosciences, biais cognitifs** (`cerveau`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/></svg></span>
```

**Horloge, conciliation travail-vie** (`equilibre`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg></span>
```

**Personnes, société** (`societe`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="3"/><circle cx="16.5" cy="9" r="2.5"/><path d="M2.5 20c0-3.3 2.5-6 5.5-6s5.5 2.7 5.5 6M13.5 14.6c.9-.4 1.9-.6 3-.6 2.8 0 5 2.4 5 5.4"/></svg></span>
```

**Fiole, femmes en sciences, chimie** (`femmes`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v6l-5.5 9.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7.5 15h9"/></svg></span>
```

**Masque, syndrome de l’imposteur** (`imposteur`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5c5 1.5 11 1.5 16 0v6a8 8 0 0 1-16 0z"/><path d="M8 10.5c.8-.7 1.7-.7 2.5 0M13.5 10.5c.8-.7 1.7-.7 2.5 0M9 15c1.8 1.3 4.2 1.3 6 0"/></svg></span>
```

**Trois cercles, interdisciplinarité, collaboration** (`interdisciplinaire`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="9.5" r="5"/><circle cx="15" cy="9.5" r="5"/><circle cx="12" cy="14.5" r="5"/></svg></span>
```

**Recyclage, déchets** (`recyclage`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7l2.3-4"/><path d="M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7l-1.2-2.1"/><path d="m14 16-3 3 3 3"/><path d="M8.3 6.7 9.5 4.6a1.8 1.8 0 0 1 3.1 0l1.9 3.3"/><path d="m4.2 10.4 1.3 1.9 2.3-.5"/><path d="M13.3 8.7l1.2-.8 1.9 1.3"/></svg></span>
```

**Goutte, sang, santé** (`sang`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/></svg></span>
```

**Crayon, illustration, art** (`illustration`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m15 4 5 5L9 20H4v-5z"/><path d="m13 6 5 5"/></svg></span>
```

**Feuille cochée, évaluation, éducation** (`notes`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12v18H6z"/><path d="M9 8h6M9 12h3"/><path d="m13 16 1.5 1.5L18 14"/></svg></span>
```

**ADN, génétique, OGM** (`adn`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3c0 6 10 6 10 12s-10 6-10 6M17 3c0 6-10 6-10 12"/><path d="M8.5 6h7M8.5 18h7M10 9.5h4M10 14.5h4"/></svg></span>
```

**Lentille, optique, physique** (`optique`)
```html
<span class="topic-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h6"/><ellipse cx="12" cy="12" rx="2.5" ry="7"/><path d="m15 9.5 7-3M15 12h7M15 14.5l7 3"/></svg></span>
```
