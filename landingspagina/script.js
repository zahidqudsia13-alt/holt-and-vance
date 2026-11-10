/* ==========================================================
   HOLT & VANCE · Landingspagina "Built to Last"
   Geen externe dienst: het formulier valideert en toont een
   succesmelding, maar verstuurt of bewaart niets.
   ========================================================== */

(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- 1. Instagram-feed vanuit data ----------
     Herbruikbaar: voeg een rij toe en de feed groeit mee.
     Beelden = Figma Buzz-posts (bulk create uit de Excel). */
  const FEED = [
    { img: "post-01.jpg", geur: "Amber", tekst: "Dust behind. Sun ahead." },
    { img: "post-02.jpg", geur: "Noir",  tekst: "Empty road. After the rain." },
    { img: "post-03.jpg", geur: "Amber", tekst: "Fire's lit. Camp is set." },
    { img: "post-04.jpg", geur: "Noir",  tekst: "Into the mist. Bend after bend." },
    { img: "post-05.jpg", geur: "Amber", tekst: "Helmet off. View on." },
    { img: "post-06.jpg", geur: "Noir",  tekst: "Rain on the tank. Streetlights on." },
    { img: "post-07.jpg", geur: "Amber", tekst: "Top of the pass. Sun in your back." },
    { img: "post-08.jpg", geur: "Noir",  tekst: "Above the fog. First light." },
    { img: "post-09.jpg", geur: "Amber", tekst: "Deep in the canyon. Far from everything." },
    { img: "post-10.jpg", geur: "Noir",  tekst: "Tools out. Lights on." },
    { img: "post-11.jpg", geur: "Amber", tekst: "One road. One direction." },
    { img: "post-12.jpg", geur: "Noir",  tekst: "Cold hands. Firm grip." }
  ];

  const feed = document.getElementById("feed");
  if (feed) {
    const item = (p, hidden) =>
      `<li${hidden ? ' aria-hidden="true"' : ""}><img src="assets/feed/${p.img}" alt="${hidden ? "" : `Instagram-post Holt & Vance ${p.geur}: ${p.tekst}`}" loading="lazy" width="640" height="640"></li>`;
    // twee keer na elkaar voor een naadloze loop; de kopie is verborgen voor schermlezers
    feed.innerHTML = FEED.map(p => item(p, false)).join("") + FEED.map(p => item(p, true)).join("");
  }

  /* ---------- 2. Navigatie krijgt achtergrond na scrollen ---------- */
  const nav = document.getElementById("nav");
  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 40);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- 3. Scroll-reveal ---------- */
  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-in"));
  }

  /* ---------- 4. Video's ---------- */
  const hero = document.querySelector(".hero__video");
  // hero speelt één keer de volledige video en blijft staan op het laatste beeld (rook + "500 km later. Still there.")
  const heroSection = document.querySelector(".hero");
  if (hero && reduceMotion) {
    hero.removeAttribute("autoplay"); hero.pause();
    hero.poster = "assets/img/hero-end.jpg";
    heroSection.classList.add("hero--endcard");
  } else if (hero) {
    hero.addEventListener("ended", () => heroSection.classList.add("hero--endcard"));
    // geluid: browsers starten video's altijd zonder geluid; met de knop speelt de video opnieuw af mét geluid
    const heroSound = document.getElementById("hero-sound");
    if (heroSound) heroSound.addEventListener("click", () => {
      const on = hero.muted;
      hero.muted = !on;
      if (on) { heroSection.classList.remove("hero--endcard"); hero.currentTime = 0; hero.play().catch(() => {}); }
      heroSound.setAttribute("aria-pressed", String(on));
      heroSound.querySelector(".sound__label").textContent = on ? "Geluid uit" : "Geluid aan";
    });
  }

  const film = document.getElementById("film");
  const sound = document.getElementById("sound");
  if (film && "IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting && !reduceMotion) film.play().catch(() => {});
      else film.pause();
    }, { threshold: 0.35 }).observe(film);
  }
  if (film && sound) {
    sound.addEventListener("click", () => {
      const on = film.muted;
      film.muted = !on;
      if (on) { film.currentTime = 0; film.play().catch(() => {}); }
      sound.setAttribute("aria-pressed", String(on));
      sound.querySelector(".sound__label").textContent = on ? "Geluid uit" : "Geluid aan";
    });
  }

  /* ---------- 5. Privacy-dialoog ---------- */
  const dialog = document.getElementById("privacy");
  document.querySelectorAll("[data-open-privacy]").forEach((btn) =>
    btn.addEventListener("click", () => (dialog.showModal ? dialog.showModal() : dialog.setAttribute("open", "")))
  );
  document.getElementById("privacy-close").addEventListener("click", () => dialog.close ? dialog.close() : dialog.removeAttribute("open"));
  dialog.addEventListener("click", (e) => { if (e.target === dialog) dialog.close(); });

  /* ---------- 6. Nieuwsbriefformulier ---------- */
  const form = document.getElementById("signup");
  const success = document.getElementById("success");
  const submit = document.getElementById("submit");
  const fields = {
    voornaam: form.elements.voornaam,
    email: form.elements.email,
    toestemming: form.elements.toestemming
  };

  const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  const NAME_RE = /^[\p{L}][\p{L}' -]*$/u;

  const rules = {
    voornaam(v) {
      v = v.trim();
      if (!v) return "Vul je voornaam in.";
      if (v.length < 2) return "Je voornaam is te kort.";
      if (v.length > 40) return "Je voornaam is te lang (max. 40 tekens).";
      if (!NAME_RE.test(v)) return "Gebruik alleen letters, een spatie, - of '.";
      return "";
    },
    email(v) {
      v = v.trim();
      if (!v) return "Vul je e-mailadres in.";
      if (!EMAIL_RE.test(v)) return "Dit e-mailadres klopt niet. Voorbeeld: jij@voorbeeld.be";
      return "";
    },
    toestemming(_, el) {
      return el.checked ? "" : "Vink dit vakje aan om je in te schrijven.";
    }
  };

  function validate(name) {
    const el = fields[name];
    const msg = rules[name](el.value, el);
    const err = document.getElementById(`${name}-error`);
    err.textContent = msg;
    el.setAttribute("aria-invalid", msg ? "true" : "false");
    el.classList.toggle("is-valid", !msg && el.type !== "checkbox");
    return !msg;
  }

  // valideren bij verlaten van een veld, en live corrigeren zodra er al een fout stond
  Object.keys(fields).forEach((name) => {
    const el = fields[name];
    const touched = () => el.dataset.touched === "1";
    el.addEventListener("blur", () => { if (el.value || name === "toestemming") { el.dataset.touched = "1"; validate(name); } });
    el.addEventListener(el.type === "checkbox" ? "change" : "input", () => { if (touched()) validate(name); });
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const results = Object.keys(fields).map((n) => { fields[n].dataset.touched = "1"; return [n, validate(n)]; });
    const firstInvalid = results.find(([, ok]) => !ok);
    if (firstInvalid) { fields[firstInvalid[0]].focus(); return; }

    // "verzenden" zonder iets door te sturen of op te slaan
    submit.disabled = true;
    submit.classList.add("is-loading");
    submit.querySelector(".btn__label").textContent = "Even geduld";

    const naam = fields.voornaam.value.trim();
    setTimeout(() => {
      document.getElementById("success-name").textContent = naam;
      form.reset();
      form.hidden = true;
      success.hidden = false;
      success.focus();
      submit.disabled = false;
      submit.classList.remove("is-loading");
      submit.querySelector(".btn__label").textContent = "Join the ride";
      Object.values(fields).forEach((el) => { el.removeAttribute("aria-invalid"); el.classList.remove("is-valid"); delete el.dataset.touched; });
    }, 900);
  });

  document.getElementById("reset").addEventListener("click", () => {
    success.hidden = true;
    form.hidden = false;
    fields.voornaam.focus();
  });
})();
