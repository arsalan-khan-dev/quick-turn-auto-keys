/* ==========================================================================
   QUICK TURN AUTO KEYS — HERO SLIDER
   Automatic, subtle crossfade slideshow for the hero visual.
   - Respects prefers-reduced-motion (no auto-rotation if set)
   - Does not cause layout shift (slides are absolutely positioned)
   - Degrades gracefully with only 1 slide present
   ========================================================================== */

(function () {
  const visual = document.querySelector('[data-hero-slider]');
  if (!visual) return;

  const slides = Array.from(visual.querySelectorAll('.hero-slide'));
  const dotsWrap = visual.querySelector('.hero-dots');
  if (slides.length <= 1) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const INTERVAL = 4000;
  let current = slides.findIndex(function (s) { return s.classList.contains('active'); });
  if (current === -1) current = 0;
  let timer = null;

  // Build dots
  let dots = [];
  if (dotsWrap) {
    dotsWrap.innerHTML = '';
    slides.forEach(function (_, i) {
      const dot = document.createElement('button');
      dot.className = 'hero-dot' + (i === current ? ' active' : '');
      dot.setAttribute('aria-label', 'Show slide ' + (i + 1));
      dot.addEventListener('click', function () {
        goTo(i);
        restart();
      });
      dotsWrap.appendChild(dot);
    });
    dots = Array.from(dotsWrap.children);
  }

  function goTo(index) {
    slides[current].classList.remove('active');
    if (dots[current]) dots[current].classList.remove('active');
    current = index;
    slides[current].classList.add('active');
    if (dots[current]) dots[current].classList.add('active');
  }

  function next() {
    goTo((current + 1) % slides.length);
  }

  function start() {
    if (prefersReducedMotion) return;
    timer = setInterval(next, INTERVAL);
  }

  function stop() {
    if (timer) clearInterval(timer);
  }

  function restart() {
    stop();
    start();
  }

  start();

  // Pause when tab is not visible to avoid wasted cycles
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) stop(); else start();
  });
})();
