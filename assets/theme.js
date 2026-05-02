/* ============================================================
   Theme: light / dark with localStorage persistence.

   Two entry points:

   1) applyStoredTheme()  — run SYNCHRONOUSLY in <head> before
      paint, so users don't see a flash of the wrong theme.

   2) initThemeToggle()   — run after DOMContentLoaded to wire
      up the toggle button in the masthead.
   ============================================================ */

(function () {
  'use strict';

  var STORAGE_KEY = 'cs5520-theme';

  function getStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (_e) { return null; }
  }

  function systemPrefersDark() {
    return window.matchMedia &&
           window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
  }

  // Run immediately — before body paint if included in <head>
  var stored = getStoredTheme();
  var initial = stored || (systemPrefersDark() ? 'dark' : 'light');
  applyTheme(initial);

  // Expose a global so the toggle button can flip it
  window.CS5520Theme = {
    toggle: function () {
      var cur = document.documentElement.getAttribute('data-theme') || 'light';
      var next = cur === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (_e) {}
    },

    // Wire up the toggle button. Idempotent; safe to call on every page.
    init: function () {
      var btn = document.querySelector('.theme-toggle');
      if (!btn) return;
      btn.addEventListener('click', function () {
        window.CS5520Theme.toggle();
      });
    }
  };

  // Auto-init after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', window.CS5520Theme.init);
  } else {
    window.CS5520Theme.init();
  }

  // React to system preference changes *only* if the user hasn't
  // explicitly chosen a theme yet.
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function (e) {
      if (getStoredTheme()) return;
      applyTheme(e.matches ? 'dark' : 'light');
    };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }
})();
