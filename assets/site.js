// LayerCut site: menu, theme, tabs, download links, and the laser trace on the hero sheet.
(() => {
  const DOWNLOADS = "https://downloads.layercut.app";
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch { /* private mode */ } },
  };

  // ── theme: system → light → dark ──────────────────────────
  const themes = ["system", "light", "dark"];
  const applyTheme = (t) => {
    if (t === "system") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = t;
    document.querySelectorAll(".theme-switch").forEach((b) => {
      b.textContent = `Theme: ${t[0].toUpperCase()}${t.slice(1)}`;
    });
  };
  let theme = store.get("lc-site-theme");
  if (!themes.includes(theme)) theme = "system";
  applyTheme(theme);
  document.querySelectorAll(".theme-switch").forEach((b) =>
    b.addEventListener("click", () => {
      theme = themes[(themes.indexOf(theme) + 1) % themes.length];
      store.set("lc-site-theme", theme);
      applyTheme(theme);
    }),
  );

  // ── mobile menu and docs nav ──────────────────────────────
  const toggle = (btn, el) => {
    if (!btn || !el) return;
    btn.addEventListener("click", () => {
      const open = el.classList.toggle("open");
      btn.setAttribute("aria-expanded", String(open));
    });
  };
  toggle(document.querySelector(".menu-toggle"), document.querySelector(".nav"));
  toggle(document.querySelector(".docs-nav-toggle"), document.querySelector(".docs-nav"));

  // ── tabs (interlocking patterns) ──────────────────────────
  document.querySelectorAll("[role=tablist]").forEach((list) => {
    const tabs = [...list.querySelectorAll("[role=tab]")];
    const select = (tab) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
      });
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => select(t));
      t.addEventListener("keydown", (e) => {
        const d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (!d) return;
        const n = tabs[(i + d + tabs.length) % tabs.length];
        select(n);
        n.focus();
      });
    });
  });

  // ── downloads: point the main button at this visitor's platform ──
  const isWin = /Windows/i.test(navigator.userAgent);
  document.querySelectorAll("[data-dl-auto]").forEach((a) => {
    a.href = `${DOWNLOADS}/latest/${isWin ? "LayerCut-windows-setup.exe" : "LayerCut-mac.dmg"}`;
    const label = a.querySelector("[data-dl-label]");
    if (label) label.textContent = isWin ? "Download for Windows" : "Download for Mac";
    const other = document.querySelector("[data-dl-other]");
    if (other) {
      other.href = "/#download";
      other.textContent = isWin ? "Also on Mac" : "Also on Windows";
    }
  });
  document.querySelectorAll(".dl[data-os]").forEach((a) => {
    if ((a.dataset.os === "windows") === isWin) a.classList.add("primary");
  });

  const status = document.querySelector("[data-dl-status]");
  const dlLinks = document.querySelectorAll(".dl[data-os]");
  if (dlLinks.length || status) {
    fetch(`${DOWNLOADS}/latest/version.json`, { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then((v) => {
        document.querySelectorAll("[data-version]").forEach((el) => (el.textContent = `Version ${v.version}`));
        if (status) status.textContent = `Version ${v.version}, released ${new Date(v.date + "T12:00:00").toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" })}.`;
      })
      .catch(() => {
        // nothing released yet: say so instead of offering links that 404
        dlLinks.forEach((a) => {
          a.setAttribute("aria-disabled", "true");
          a.removeAttribute("href");
          const go = a.querySelector(".go");
          if (go) go.textContent = "Soon";
        });
        document.querySelectorAll("[data-dl-auto]").forEach((a) => {
          a.href = "/#download";
          const label = a.querySelector("[data-dl-label]");
          if (label) label.textContent = "Get the beta";
        });
        if (status) {
          status.innerHTML = 'The first public beta is almost ready. <a href="mailto:hello@layercut.app?subject=Tell%20me%20when%20the%20LayerCut%20beta%20is%20out">Email us</a> and we\'ll send you the link on release day.';
        }
      });
  }

  // ── hero: model → panels → nested sheet → LightBurn ──
  const show = document.getElementById("hero-show");
  if (show) {
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    const slides = [...show.querySelectorAll(".hs-slide")];
    const stats = [...show.querySelectorAll(".hs-stat")];
    const buttons = [...show.querySelectorAll("[data-go]")];
    const DUR = [3200, 3200, 3400, 4600];
    let step = 0, t0 = performance.now(), paused = reduce, visible = true, raf = 0, stoppedAt = 0;

    const setStep = (n) => {
      step = n;
      show.dataset.step = String(n);
      const file = show.querySelector(".hs-file");
      if (file) file.textContent = n === 3 ? "organizer.lbrn2" : "organizer.stl";
      slides.forEach((s) => s.classList.toggle("on", s.dataset.for.split(" ").includes(String(n))));
      stats.forEach((s) => s.classList.toggle("on", s.dataset.for === String(n)));
      buttons.forEach((b, i) => {
        if (+b.dataset.go === n) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current");
        b.style.setProperty("--p", i < n || reduce && i === n ? "1" : "0");
      });
      t0 = performance.now();
    };
    const tick = (now) => {
      raf = 0;
      if (paused || !visible) return;
      const t = now - t0;
      buttons[step].style.setProperty("--p", String(Math.min(1, t / DUR[step])));
      if (t >= DUR[step]) setStep((step + 1) % slides.length);
      raf = requestAnimationFrame(tick);
    };
    const run = () => { if (!raf && !paused && visible) raf = requestAnimationFrame(tick); };
    const stop = () => { stoppedAt = performance.now(); };
    const resume = () => { t0 += performance.now() - stoppedAt; run(); };

    buttons.forEach((b) => b.addEventListener("click", () => { setStep(+b.dataset.go); run(); }));

    if (reduce) {
      setStep(3); // no autoplay: show the LightBurn file, steps switch on click
    } else {
      setStep(0);
      new IntersectionObserver((es) => {
        const was = visible;
        visible = es[0].isIntersecting;
        if (!visible && was) stop();
        if (visible && !was) resume();
      }).observe(show);
      document.addEventListener("visibilitychange", () => {
        if (document.hidden) { paused = true; stop(); } else { paused = false; resume(); }
      });
      run();
    }
  }
})();
