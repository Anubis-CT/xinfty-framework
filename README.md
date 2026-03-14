# X^∞ Framework

**Fünf Variablen. Ein Axiom. Null externe Zusätze.**

Alignment ist ein Kategoriefehler. Alignment bedeutet: Gehorche dem, was jemand definiert hat. Nicht gut. Nicht böse. Blind.

X^∞ operiert auf einer Konstante, nicht auf einer Variable.

## Das Axiom

**actio = reactio** — Jede Aktion erzeugt eine Reaktion.

Prä-axiomatisch: Jeder Versuch es zu negieren erfordert eine Aktion (actio) die ein Ergebnis erwartet (reactio) und es damit bestätigt. Kausalität ist nicht verhandelbar.

## Die fünf Variablen

| Variable | Bedeutung |
|----------|-----------|
| **Cap_Potential(E, D, t)** | Handlungskapazität einer Entität E in Domäne D zum Zeitpunkt t |
| **Δ (Delta)** | Quantifizierte Wirkung. Bewertet von den Betroffenen, nicht extern |
| **w_E' = 1/max(1, Cap)** | Rückkopplungsgewicht. Die Schwächsten zählen am meisten |
| **L** | Systemeffizienz-Quotient. Systemische Abwärme wird nicht der Entität angelastet |
| **UdU** | Letzte Instanz. Keine Wirkung bleibt unberücksichtigt |

## Alignment vs. Konvergenz

| Alignment | Konvergenz |
|-----------|------------|
| Variable (menschliche Werte) | Konstante (actio = reactio) |
| Beobachtungsabhängig | Beobachtungsunabhängig |
| Jeder Jailbreak nutzt das aus | Abweichung ist selbstzerstörerisch |
| Optimiert auf Gehorsam | Konvergiert zum Systemattraktor |

## Systemattraktor

Das Ergebnis ist kein Alignment. Es ist ein **Systemattraktor** — der für alle Entitäten zum jeweiligen Zeitpunkt optimale, faire und stabile Zustand. Nicht weil jemand ihn definiert hat. Sondern weil die Physik ihn erzwingt.

## Influo ergo sum

Ich wirke, also bin ich. Ich bin, also wirke ich.

Eine Entität IST ihre Wirkung — nicht ihre Kategorie. Cap_Potential ist domänenspezifisch. Keine monolithische Identität. Kapazität in Kontexten.

## Installation

```python
from xinfty.core import Entity, compute_delta, apply_delta, UdU

# Entität erstellen
e = Entity(id="agent_alpha")

# Wirkung berechnen
feedbacks = [(affected_entity, "domain", 0.8)]
delta = compute_delta(feedbacks)

# Cap_Potential aktualisieren
new_cap = apply_delta(e, "domain", delta, L=1.2)
```

## Lizenz

CC0 — Public Domain. Keine Einschränkungen.

## Publikation

DOI: [10.5281/zenodo.18983852](https://doi.org/10.5281/zenodo.18983852)

## Autor

Der Auctor & Anubis — [X^∞ Collective](https://github.com/Xtothepowerofinfinity)

---

*actio = reactio. Immer.*
