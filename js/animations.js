/* ==========================================================================
   QUICK TURN AUTO KEYS — ANIMATIONS & PAGE TRANSITIONS
   ========================================================================== */

(function () {
  'use strict';

  /* ---------------------------------------------------------------------- */
  /* Helper: safely normalise a URL for comparison (strip trailing slash)   */
  /* ---------------------------------------------------------------------- */
  function normalise(href) {
    try {
      const u = new URL(href, window.location.href);
      // Strip trailing slash, ignore query/hash for same-page check
      return u.origin + u.pathname.replace(/\/$/, '');
    } catch (_) {
      return href;
    }
  }

  /* ---------------------------------------------------------------------- */
  /* 1. Inject the curtain element                                           */
  /* ---------------------------------------------------------------------- */
  let curtain = null;

  function ensureCurtain() {
    if (curtain) return curtain;
    curtain = document.createElement('div');
    curtain.id = 'page-curtain';
    // Curtain starts covering the screen (coming in from above)
    // on entry it will be set to page-entering to fly off
    document.body.appendChild(curtain);
    return curtain;
  }

  /* ---------------------------------------------------------------------- */
  /* 2. On page load — dismiss the curtain & reveal content                 */
  /* ---------------------------------------------------------------------- */
  function pageEnter() {
    ensureCurtain();

    // Stamp "entering" first so curtain knows which direction to go
    document.body.classList.add('page-entering');
    document.body.classList.remove('page-exiting');

    // Double rAF ensures browser has painted before we start transitions
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        document.body.classList.add('page-loaded');

        // Clean up stale class after animation completes (0.68s + 0.1s delay)
        setTimeout(() => {
          document.body.classList.remove('page-entering');
        }, 900);
      });
    });
  }

  /* ---------------------------------------------------------------------- */
  /* 3. On link click — slide curtain UP, then navigate                     */
  /* ---------------------------------------------------------------------- */
  let isExiting = false; // guard against double-click

  function pageExit(href) {
    if (isExiting) return;
    isExiting = true;

    // If the user prefers reduced motion, skip the curtain animation and
    // navigate immediately — the CSS already neutralises the visual curtain,
    // but we must also skip the JS delay so navigation is instant.
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) {
      window.location.href = href;
      return;
    }

    document.body.classList.remove('page-loaded', 'page-entering');
    document.body.classList.add('page-exiting');

    // 720ms CSS duration + small buffer
    setTimeout(() => {
      window.location.href = href;
    }, 740);
  }

  /* ---------------------------------------------------------------------- */
  /* 4. Intercept all internal link clicks                                   */
  /* ---------------------------------------------------------------------- */
  function attachLinkListeners() {
    document.querySelectorAll('a[href]').forEach(link => {
      if (link.dataset.transitionBound) return;
      link.dataset.transitionBound = '1';

      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');

        // Skip: empty, hash, tel, mailto, javascript, external, new-tab, download
        if (
          !href ||
          href.startsWith('#') ||
          href.startsWith('tel:') ||
          href.startsWith('mailto:') ||
          href.startsWith('javascript:') ||
          link.target === '_blank' ||
          link.hasAttribute('download')
        ) return;

        // Skip external links
        if (href.startsWith('http') || href.startsWith('//')) {
          try {
            const linkHost = new URL(href).hostname;
            if (linkHost !== window.location.hostname) return;
          } catch (_) { return; }
        }

        // Skip same-page links (normalised comparison)
        const currentPage = normalise(window.location.href);
        const targetPage  = normalise(href);
        if (targetPage === currentPage) return;

        e.preventDefault();
        pageExit(link.href);
      });
    });
  }

  /* ---------------------------------------------------------------------- */
  /* 5. Scroll-reveal for .reveal elements                                   */
  /* ---------------------------------------------------------------------- */
  function initReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          obs.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.08
    });

    els.forEach(el => observer.observe(el));
  }

  /* ---------------------------------------------------------------------- */
  /* 6. Back/Forward cache fix (bfcache)                                     */
  /* Browsers may restore the page from cache with the curtain still visible */
  /* ---------------------------------------------------------------------- */
  window.addEventListener('pageshow', (e) => {
    if (e.persisted) {
      isExiting = false;
      document.body.classList.remove('page-exiting');
      pageEnter();
    }
  });

  /* ---------------------------------------------------------------------- */
  /* 7. Boot                                                                  */
  /* ---------------------------------------------------------------------- */
  function boot() {
    ensureCurtain();
    pageEnter();
    initReveal();
    attachLinkListeners();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

})();
