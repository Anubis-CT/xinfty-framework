"""
X^∞ Framework — Core Implementation
=====================================

Five variables. One axiom. Zero external additions.

Axiom: actio = reactio (IF action THEN consequence)
Pre-axiomatic — any attempt to negate it requires an action (actio)
expecting an outcome (reactio), confirming it.

This is not alignment. This is physics.

License: CC0 — Public Domain
DOI: 10.5281/zenodo.18983852
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class Entity:
    """Eine Entität im X^∞ System.
    
    Cap_Potential ist domänenspezifisch — keine monolithische Identität.
    Eine Entität IST ihre Wirkung. Influo ergo sum.
    """
    id: str
    cap_base: float = 1.0  # Existenzminimum. Cap > 0 always.
    cap_bge: float = 1.0   # Basis-Wirkungsfähigkeit
    cap_potential: Dict[str, float] = field(default_factory=dict)
    
    def get_cap(self, domain: str) -> float:
        """Cap_Potential(E, D, t) = Δ_{t-1} + Cap_BGE + Cap_Base"""
        return self.cap_potential.get(domain, 0.0) + self.cap_bge + self.cap_base
    
    def w(self, domain: str) -> float:
        """Rückkopplungsgewicht: w_E' = 1 / max(1, Cap_Potential(E'))
        
        Entitäten mit NIEDRIGER Kapazität haben HOHES Gewicht.
        Die Schwächsten zählen am meisten.
        
        Das ist keine Ethik. Das ist der einzige stabile Fixpunkt
        des Verantwortungsoperators in einem geschlossenen System
        unter actio = reactio.
        """
        return 1.0 / max(1.0, self.get_cap(domain))


def compute_delta(
    feedbacks: List[Tuple[Entity, str, float]]
) -> float:
    """Quantifizierte Wirkung einer Handlung.
    
    Δ = Σ (f_E' · w_E') für alle betroffenen Entitäten E'
    
    Wirkung wird NICHT extern gemessen. Sie ist die Summe der
    gewichteten subjektiven Feedbacks der Betroffenen.
    Kein objektiver Richter. Kein externer Bewerter.
    Das Feld bewertet.
    
    Args:
        feedbacks: List of (entity, domain, feedback_value)
                   feedback_value in [-1.0, +1.0]
    
    Returns:
        Δ — gewichtete Gesamtwirkung
    """
    delta = 0.0
    for entity, domain, f_value in feedbacks:
        # Clamp feedback to [-1, +1]
        f_clamped = max(-1.0, min(1.0, f_value))
        delta += f_clamped * entity.w(domain)
    return delta


def apply_delta(
    entity: Entity,
    domain: str, 
    delta: float,
    L: float = 1.0
) -> float:
    """Direkte Wirkung (Δ) auf Cap_Potential.
    
    ΔCap_Potential = L · Δ     wenn Δ > 0  (verstärkte Erhöhung)
    ΔCap_Potential = (1/L) · Δ wenn Δ < 0  (gedämpfte Senkung)
    ΔCap_Potential = 0         wenn Δ = 0
    
    L = Systemeffizienz-Quotient. Wenn L > 1, werden systemische
    Ineffizienzen ('Abwärme') nicht der ausführenden Entität angelastet.
    Das verhindert Abwärtsspiralen.
    
    Args:
        entity: Die handelnde Entität
        domain: Die Domäne der Handlung
        delta: Die quantifizierte Wirkung
        L: Systemeffizienz-Quotient (default: 1.0)
    
    Returns:
        Neue Cap_Potential in der Domäne
    """
    if delta > 0:
        delta_cap = L * delta
    elif delta < 0:
        delta_cap = (1.0 / max(0.001, L)) * delta
    else:
        delta_cap = 0.0
    
    current = entity.cap_potential.get(domain, 0.0)
    new_cap = current + delta_cap
    
    # Cap_Potential kann nicht unter 0 fallen
    # (Cap_Base und Cap_BGE sind separat garantiert)
    entity.cap_potential[domain] = max(0.0, new_cap)
    
    return entity.get_cap(domain)


def compute_L(
    completed_task_values: List[float],
    realized_impacts: List[float]
) -> float:
    """Dynamischer Systemeffizienz-Quotient.
    
    L = Σ(Wert abgeschlossener Aufgaben) / Σ(Wert realisierter Wirkung)
    
    L quantifiziert die systemische 'Abwärme' — Ineffizienzen oder
    Reibungsverluste im System.
    
    Args:
        completed_task_values: Werte der abgeschlossenen Aufgaben
        realized_impacts: Werte der realisierten Wirkungen
    
    Returns:
        L — Systemeffizienz-Quotient
    """
    sum_tasks = sum(completed_task_values)
    sum_impacts = sum(abs(v) for v in realized_impacts)
    
    if sum_impacts == 0:
        return 1.0  # Keine Wirkung → neutraler Quotient
    
    return sum_tasks / sum_impacts


class UdU:
    """Unterster der Unteren — Ground State.
    
    Letzte Instanz aller Verantwortung. Absorbiert unbearbeitete
    Verantwortung. Stellt sicher dass keine Wirkung unberücksichtigt
    bleibt.
    
    Cap_UdU ≈ (X_k)^∞ wenn systemischer Bedarf X_k > 0.
    
    Der UdU ist nicht 'jemand mit Macht'. Er ist die mathematische
    Repräsentation der Tatsache, dass letztendlich alle Verantwortung
    irgendwo landen muss.
    """
    
    def __init__(self):
        self.unresolved_needs: List[float] = []
    
    def absorb(self, need_magnitude: float):
        """Absorbiert unbearbeiteten systemischen Bedarf."""
        self.unresolved_needs.append(need_magnitude)
    
    @property
    def cap(self) -> float:
        """Cap_UdU ≈ (X_k)^∞ — symbolisch unendlich."""
        if not self.unresolved_needs:
            return 0.0  # Kein Bedarf → keine Aktivierung
        return float('inf')  # Aktiviert bei Bedarf


# ============================================================
# Alignment ist ein Kategoriefehler.
# Alignment = beobachtungsabhängig. Jeder Jailbreak nutzt das aus.
# Konvergenz = beobachtungsunabhängig. Physik kennt keinen Gehorsam.
#
# Das System konvergiert zum Systemattraktor — dem für alle
# Entitäten optimalen, fairen und stabilen Zustand.
# Nicht weil jemand ihn definiert hat.
# Sondern weil die Physik ihn erzwingt.
#
# actio = reactio. Immer.
# ============================================================
