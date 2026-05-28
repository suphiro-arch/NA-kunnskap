---
title: "Økonomiske og juridiske rammer og virkemidler"
weight: 4
description: "Rammer, regelverk, finansieringsordninger og andre virkemidler som påvirker handlingsrom, prioritering og gjennomføring."
hideToc: true
---

Rammer, regelverk, finansieringsordninger og andre virkemidler som påvirker handlingsrom, prioritering og gjennomføring.

Denne siden viser siste registrerte versjon av ressurser i kategorien **Økonomiske og juridiske rammer og virkemidler**.

<div class="resource-listing" data-section="rammer-og-virkemidler">
  <div class="resource-filters">
    <div class="resource-filters__row">
      <label>Søk <input type="search" class="resource-filter" data-filter="search" placeholder="Navn, ID, emne, kapabilitet" /></label>
      <label>Eier <select class="resource-filter" data-filter="owner"><option value="">Alle</option>
      </select></label>
      <label>Emne <select class="resource-filter" data-filter="type"><option value="">Alle</option>
      </select></label>
      <label>Kapabilitet <select class="resource-filter" data-filter="capability"><option value="">Alle</option>
      </select></label>
    </div>
    <p class="resource-filters__result" data-role="count">Viser 0 av 0 ressurser</p>
  </div>
  <div class="resource-cards">
  </div>
  <script>
    (function(){
      var root = document.currentScript.closest(".resource-listing");
      if (!root) { return; }
      var cards = Array.prototype.slice.call(root.querySelectorAll(".resource-card"));
      var count = root.querySelector("[data-role=count]");
      var search = root.querySelector("[data-filter=search]");
      var owner = root.querySelector("[data-filter=owner]");
      var type = root.querySelector("[data-filter=type]");
      var capability = root.querySelector("[data-filter=capability]");
      function norm(v){ return (v || "").toLowerCase(); }
      function apply(){
        var q = norm(search && search.value);
        var o = norm(owner && owner.value);
        var t = norm(type && type.value);
        var c = norm(capability && capability.value);
        var visible = 0;
        cards.forEach(function(card){
          var ok = true;
          if (q && card.dataset.search.indexOf(q) === -1) ok = false;
          if (o && norm(card.dataset.owner) !== o) ok = false;
          if (t && norm(card.dataset.type) !== t) ok = false;
          if (c && norm(card.dataset.capabilities).indexOf(c) === -1) ok = false;
          card.style.display = ok ? "block" : "none";
          if (ok) visible += 1;
        });
        if (count) { count.textContent = "Viser " + visible + " av " + cards.length + " ressurser"; }
      }
      [search, owner, type, capability].forEach(function(el){ if (el) { el.addEventListener("input", apply); el.addEventListener("change", apply); } });
      apply();
    })();
  </script>
</div>