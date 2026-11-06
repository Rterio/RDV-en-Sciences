/* RDV en Sciences — en-tête et pied de page partagés.
   Modifiez le menu, le lien de billetterie ou les réseaux sociaux ICI :
   le changement s'applique à toutes les pages. */

const SITE = {
  billets: "https://evelya.co/universite-laval/rdv-en-sciences/rdv-en-sciences-2026-1700",
  courriel: "presidence@rdv-en-sciences.aesgul.com",
  facebook: "https://www.facebook.com/RDVenSciences",
  instagram: "https://www.instagram.com/rdv_en_sciences/",
  // Chemins relatifs à la racine du site (fonctionne aussi sur username.github.io/depot/).
  menu: [
    { label: "Accueil", href: "" },
    { label: "Activités", href: "activites/" },
    { label: "Partenaires", href: "partenaires/" },
    { label: "Organisation", href: "organisation/" },
    { label: "Éditions passées", href: "editions/" },
  ],
};

// Racine du site, déduite de l'emplacement de ce fichier (assets/site.js).
const ROOT_URL = new URL("../", document.currentScript.src);

(function () {
  const clean = (p) => p.replace(/index\.html$/, "");
  const here = clean(location.pathname);

  const isCurrent = (href) => {
    const target = clean(new URL(href, ROOT_URL).pathname);
    return href === "" ? here === target : here.startsWith(target);
  };

  const navLinks = SITE.menu
    .map(
      (item) =>
        `<a href="${new URL(item.href, ROOT_URL).href}"${isCurrent(item.href) ? ' aria-current="page"' : ""}>${item.label}</a>`
    )
    .join("");

  const header = document.querySelector("[data-site-header]");
  if (header) {
    header.outerHTML = `
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="${ROOT_URL.href}">
      <img src="${ROOT_URL.href}images/logo.png" alt="" width="36" height="36" onerror="this.remove()">
      RDV en Sciences
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav-principale">Menu</button>
    <nav class="nav" id="nav-principale" aria-label="Navigation principale">
      ${navLinks}
      <a class="btn" href="${SITE.billets}">Acheter un billet</a>
    </nav>
  </div>
</header>`;
  }

  const footer = document.querySelector("[data-site-footer]");
  if (footer) {
    footer.outerHTML = `
<footer class="site-footer">
  <div class="wrap">
    <div>
      <h2>RDV en Sciences</h2>
      <p>Une fin de semaine pour rassembler les étudiants et étudiantes en sciences pures de tout le Québec, propulsée par l'AESGUL.</p>
    </div>
    <div>
      <h2>Nous suivre</h2>
      <ul>
        <li><a href="${SITE.facebook}">Facebook</a></li>
        <li><a href="${SITE.instagram}">Instagram</a></li>
      </ul>
    </div>
    <div>
      <h2>Nous écrire</h2>
      <ul><li><a href="mailto:${SITE.courriel}">${SITE.courriel}</a></li></ul>
    </div>
    <p class="footer-small">© ${new Date().getFullYear()} RDV en Sciences, Association des étudiant(e)s en sciences et génie de l'Université Laval.</p>
  </div>
</footer>`;
  }

  // Tous les liens marqués data-billets pointent vers la billetterie.
  document.querySelectorAll("[data-billets]").forEach((a) => (a.href = SITE.billets));

  const toggle = document.querySelector(".menu-toggle");
  const nav = document.getElementById("nav-principale");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "Fermer" : "Menu";
    });
  }
})();
