/* Bilingual helper: translation toggle + popup when text is selected.
 * Translations are the ones already embedded in the page (no browser translate). */
(function () {
  "use strict";

  var KEY = "bi-show-vi";
  var HEADINGS = "h1,h2,h3,h4,h5,h6";
  var btn = null;
  var popup = null;
  var timer = null;
  var mouseDown = false;

  function load() {
    try { return localStorage.getItem(KEY) === "1"; } catch (e) { return false; }
  }
  function save(v) {
    try { localStorage.setItem(KEY, v ? "1" : "0"); } catch (e) { /* ignore */ }
  }
  function isOn() {
    return document.body.classList.contains("show-vi");
  }
  function esc(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function setOn(on) {
    document.body.classList.toggle("show-vi", on);
    if (btn) {
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.textContent = on ? "Ẩn bản dịch" : "Dịch (VI)";
    }
    hidePopup();
  }

  function hidePopup() {
    if (popup) {
      popup.remove();
      popup = null;
    }
  }

  /* Which translated blocks does this selection touch? */
  function collect(range) {
    var anc = range.commonAncestorContainer;
    var root = anc.nodeType === 1 ? anc : anc.parentElement;
    if (!root || !root.closest(".md-content__inner")) return [];
    if (root.closest(".vi, .bi-popup")) return [];

    var single = root.closest(".bi") || root.closest(HEADINGS);
    var candidates = single
      ? [single]
      : Array.prototype.slice
          .call(root.querySelectorAll(".bi, " + HEADINGS))
          .filter(function (el) { return range.intersectsNode(el); });

    var items = [];
    candidates.forEach(function (el) {
      if (items.length >= 10) return;
      if (el.classList.contains("bi")) {
        var v = el.querySelector(".vi");
        if (v) items.push(v.innerHTML);
      } else {
        var h = el.querySelector(".vi-h");
        if (h && h.dataset.vi) items.push(esc(h.dataset.vi));
      }
    });
    return items;
  }

  function showPopup(items, rect) {
    hidePopup();
    popup = document.createElement("div");
    popup.className = "bi-popup";
    popup.setAttribute("role", "note");
    popup.innerHTML = items
      .map(function (h) {
        return '<div class="bi-popup-item"><span class="bi-popup-label">Tiếng Việt</span>' + h + "</div>";
      })
      .join("");
    document.body.appendChild(popup);

    var sx = window.pageXOffset, sy = window.pageYOffset;
    var vw = document.documentElement.clientWidth;
    var pw = popup.offsetWidth, ph = popup.offsetHeight;
    var left = Math.min(Math.max(8, rect.left + sx), sx + vw - pw - 8);
    var top = rect.bottom + sy + 8;
    if (rect.bottom + ph + 16 > window.innerHeight && rect.top - ph - 8 > 0) {
      top = rect.top + sy - ph - 8;
    }
    popup.style.left = left + "px";
    popup.style.top = top + "px";
  }

  function check() {
    var sel = window.getSelection();
    if (sel && sel.anchorNode && popup && popup.contains(sel.anchorNode)) return;
    if (!sel || sel.rangeCount === 0 || sel.isCollapsed || !sel.toString().trim() || isOn()) {
      hidePopup();
      return;
    }
    var range = sel.getRangeAt(0);
    var rect = range.getBoundingClientRect();
    var items = collect(range);
    if (!items.length || (rect.width === 0 && rect.height === 0)) {
      hidePopup();
      return;
    }
    showPopup(items, rect);
  }

  function schedule(ms) {
    clearTimeout(timer);
    timer = setTimeout(check, ms);
  }

  function init() {
    // Monolingual pages have nothing to translate: no button, no popup.
    if (!document.querySelector(".bi, .vi-h")) return;
    var header = document.querySelector(".md-header__inner");
    btn = document.createElement("button");
    btn.type = "button";
    btn.className = "bi-toggle";
    btn.title = "Hiện / ẩn bản dịch tiếng Việt cho toàn trang";
    btn.addEventListener("click", function () {
      var on = !isOn();
      save(on);
      setOn(on);
    });
    if (header) {
      header.insertBefore(btn, header.querySelector(".md-search"));
    } else {
      btn.classList.add("bi-float");
      document.body.appendChild(btn);
    }
    setOn(load());

    document.addEventListener("mousedown", function (e) {
      if (popup && popup.contains(e.target)) return;
      mouseDown = true;
      hidePopup();
    });
    document.addEventListener("mouseup", function () {
      mouseDown = false;
      schedule(10);
    });
    document.addEventListener("touchend", function () { schedule(400); });
    document.addEventListener("keyup", function (e) {
      if (e.key === "Shift" || e.key.indexOf("Arrow") === 0) schedule(200);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") hidePopup();
    });
    document.addEventListener("selectionchange", function () {
      if (!mouseDown) schedule(350);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
