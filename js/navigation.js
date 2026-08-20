/* ==========================================================================
   QUICK TURN AUTO KEYS — NAVIGATION
   Mobile menu toggle + accessible dropdown behaviour.

   Root-cause fix: .site-header has position:sticky + z-index which creates
   a stacking context. Any position:fixed child lives inside that stacking
   context, so the header-actions bleed over the panel.
   Solution: move .mobile-panel to a direct child of <body> on init so it
   escapes the header stacking context entirely.
   ========================================================================== */

(function () {
  /* ── 1. (Panel is now in body directly in HTML) ─────── */
  const panel = document.querySelector('.mobile-panel');
  if (!panel) return;

  const toggle = document.querySelector('.nav-toggle');
  if (!toggle) return;

  /* ── 2. Toggle helpers ─────────────────────────────────────────────────── */
  function openPanel() {
    panel.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closePanel() {
    panel.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', function () {
    panel.classList.contains('open') ? closePanel() : openPanel();
  });

  /* ── 3. Auto-close on link click inside panel ──────────────────────────── */
  panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closePanel);
  });

  /* ── 4. Escape key ─────────────────────────────────────────────────────── */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && panel.classList.contains('open')) {
      closePanel();
    }
  });

  /* ── 5. Close on resize to desktop ────────────────────────────────────── */
  window.addEventListener('resize', function () {
    if (window.innerWidth > 920 && panel.classList.contains('open')) {
      closePanel();
    }
  });
})();
