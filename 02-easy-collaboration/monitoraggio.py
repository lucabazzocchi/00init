
SOGLIA_ORE = 1000

# Elenco degli aeromobili della flotta
aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 860, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "A220", "ore_volo": 1035, "controlli_ok": True},
    {"codice": "I-JKL", "modello": "ATR72", "ore_volo": 540, "controlli_ok": True},
]


def stampa_riepilogo(aeromobili) -> None:
    """Stampa tutte le informazioni sugli aeromobili."""
    print("Riepilogo flotta:")
    for aeromobile in aeromobili:
        print(
            f"- {aeromobile['codice']} ({aeromobile['modello']}), "
            f"{aeromobile['ore_volo']} ore di volo, "
            f"controlli {'OK' if aeromobile['controlli_ok'] else 'non validi'}"
        )