/* Carrousel de photos des pages d'édition.
   Le HTML est un simple défilement horizontal (fonctionne même sans JavaScript) ;
   ce script ajoute les flèches, le compteur, la légende et les miniatures. */

(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("[data-carousel]").forEach((root) => {
    const track = root.querySelector(".gf-track");
    const slides = Array.from(track.children);
    const count = root.querySelector(".gf-count");
    const caption = root.querySelector(".gf-caption");
    const thumbs = root.querySelector(".gf-thumbs");
    if (!slides.length) return;
    root.classList.add("is-ready");

    let current = 0;
    const go = (i) => {
      i = (i + slides.length) % slides.length;
      current = i; // mis à jour tout de suite pour les clics rapides
      track.scrollTo({ left: i * track.clientWidth, behavior: reduce ? "auto" : "smooth" });
    };

    // Miniatures (image -mini si elle existe, sinon le numéro de la photo)
    slides.forEach((slide, i) => {
      const img = slide.querySelector("img");
      const b = document.createElement("button");
      b.type = "button";
      b.className = "gf-thumb";
      b.setAttribute("aria-label", `Afficher la photo ${i + 1}`);
      const num = document.createElement("span");
      num.textContent = i + 1;
      b.append(num);
      const src = img && (img.dataset.thumb || img.getAttribute("src"));
      if (src) {
        const t = new Image();
        t.alt = "";
        t.loading = "lazy";
        t.onerror = () => t.remove();
        t.src = src;
        b.append(t);
      }
      b.addEventListener("click", () => go(i));
      thumbs.append(b);
    });

    const update = () => {
      const i = Math.min(slides.length - 1, Math.max(0, Math.round(track.scrollLeft / track.clientWidth)));
      current = i;
      count.textContent = `${i + 1} / ${slides.length}`;
      const cap = slides[i].querySelector("figcaption");
      caption.textContent = cap ? cap.textContent : "";
      Array.from(thumbs.children).forEach((t, k) => t.setAttribute("aria-current", k === i ? "true" : "false"));
      const t = thumbs.children[i];
      if (t) thumbs.scrollTo({ left: t.offsetLeft - thumbs.clientWidth / 2 + t.clientWidth / 2, behavior: reduce ? "auto" : "smooth" });
    };

    let timer;
    track.addEventListener("scroll", () => { clearTimeout(timer); timer = setTimeout(update, 60); }, { passive: true });
    window.addEventListener("resize", () => go(current));
    root.querySelector(".gf-prev").addEventListener("click", () => go(current - 1));
    root.querySelector(".gf-next").addEventListener("click", () => go(current + 1));
    track.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") { e.preventDefault(); go(current + 1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); go(current - 1); }
    });
    update();
  });
})();
