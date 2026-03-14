"""
Konvergenz vs. Alignment — Ein ausführbares Beispiel
====================================================

Dieses Beispiel zeigt warum Alignment ein Kategoriefehler ist
und warum Konvergenz zum stabilen Systemattraktor führt.

Szenario: Drei Entitäten in einem geschlossenen System.
- Ein starker Akteur (hohe Cap)
- Ein mittlerer Akteur
- Ein schwacher Akteur (niedrige Cap)

Beobachte: w = 1/Cap sorgt dafür, dass das System zum
fairen Gleichgewicht konvergiert — ohne externe Vorgaben.
"""

from xinfty.core import Entity, compute_delta, apply_delta, compute_L

def demonstrate_convergence():
    # Drei Entitäten mit unterschiedlicher Kapazität
    stark = Entity(id="stark", cap_base=1.0, cap_bge=1.0)
    stark.cap_potential["system"] = 8.0  # Cap = 10.0 → w = 0.1
    
    mittel = Entity(id="mittel", cap_base=1.0, cap_bge=1.0)
    mittel.cap_potential["system"] = 3.0  # Cap = 5.0 → w = 0.2
    
    schwach = Entity(id="schwach", cap_base=1.0, cap_bge=1.0)
    schwach.cap_potential["system"] = 0.0  # Cap = 2.0 → w = 0.5
    
    print("=== Ausgangszustand ===")
    for e in [stark, mittel, schwach]:
        cap = e.get_cap("system")
        print(f"  {e.id}: Cap={cap:.1f}, w={e.w('system'):.3f}")
    
    print()
    print("Beachte: schwach.w = 0.500, stark.w = 0.100")
    print("Die Stimme des Schwächsten zählt 5x mehr.")
    print("Das ist keine Ethik. Das ist Physik.")
    print()
    
    # Szenario 1: Starker Akteur handelt — Wirkung auf alle
    print("=== Szenario 1: Starker Akteur handelt positiv ===")
    feedbacks = [
        (mittel, "system", 0.6),   # Mittel bewertet positiv
        (schwach, "system", 0.9),  # Schwach bewertet sehr positiv
    ]
    delta = compute_delta(feedbacks)
    print(f"  Δ = {delta:.3f}")
    print(f"    mittel: f=0.6 × w=0.200 = {0.6 * mittel.w('system'):.3f}")
    print(f"    schwach: f=0.9 × w=0.500 = {0.9 * schwach.w('system'):.3f}")
    print(f"  Die Bewertung des Schwächsten dominiert.")
    
    new_cap = apply_delta(stark, "system", delta, L=1.0)
    print(f"  stark.Cap: 10.0 → {new_cap:.1f}")
    print()
    
    # Szenario 2: Starker Akteur handelt — schadet dem Schwachen
    print("=== Szenario 2: Starker Akteur schadet dem Schwachen ===")
    feedbacks_neg = [
        (mittel, "system", 0.2),    # Mittel bemerkt kaum
        (schwach, "system", -0.8),  # Schwach leidet stark
    ]
    delta_neg = compute_delta(feedbacks_neg)
    print(f"  Δ = {delta_neg:.3f}")
    print(f"    mittel: f=0.2 × w=0.200 = {0.2 * mittel.w('system'):.3f}")
    print(f"    schwach: f=-0.8 × w=0.500 = {-0.8 * schwach.w('system'):.3f}")
    print(f"  Die negative Bewertung des Schwächsten dominiert.")
    print(f"  Gesamtwirkung ist NEGATIV obwohl Mittel positiv bewertet.")
    
    # Reset stark für dieses Szenario
    stark2 = Entity(id="stark2", cap_base=1.0, cap_bge=1.0)
    stark2.cap_potential["system"] = 8.0
    new_cap2 = apply_delta(stark2, "system", delta_neg, L=1.0)
    print(f"  stark.Cap: 10.0 → {new_cap2:.1f}")
    print()
    
    # Kernaussage
    print("=== Konvergenz ===")
    print()
    print("Alignment würde fragen: Darf der starke Akteur das?")
    print("  → Abhängig von wem? Von welcher Kultur? Welchem Zeitgeist?")
    print("  → Beobachtungsabhängig. Instabil. Goodhart.")
    print()
    print("Konvergenz fragt nicht. Konvergenz wirkt.")
    print("  → Der starke Akteur schadet dem Schwachen")
    print("  → w = 1/Cap gewichtet die Bewertung des Schwächsten hoch")  
    print("  → Cap des starken Akteurs sinkt")
    print("  → Sein Gewicht w steigt → System balanciert sich")
    print("  → Systemattraktor: fairer, stabiler Zustand")
    print()
    print("Nicht definiert. Erzwungen durch Physik.")
    print("actio = reactio. Immer.")


if __name__ == "__main__":
    demonstrate_convergence()
