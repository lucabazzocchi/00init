SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 860, "controlli_ok": False},
]


def filtra_controlli_non_validi(aeromobili: list) -> list[dict]:
    """Restituisce gli aeromobili con controlli non validi."""
    return [
        aeromobile
        for aeromobile in aeromobili
        if aeromobile["controlli_ok"] is False
    ]


def filtra_oltre_soglia(aeromobili: list, soglia: int) -> list:
    """Restituisce gli aeromobili che superano la soglia di ore di volo."""
    return [
        aeromobile
        for aeromobile in aeromobili
        if isinstance(aeromobile["ore_volo"], int)
        and aeromobile["ore_volo"] > soglia
    ]