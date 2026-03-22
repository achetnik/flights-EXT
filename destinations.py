"""Exeter Airport (EXT) destinations."""

DESTINATIONS = {
    "EXT": {
        "name": "Exeter",
        "routes": {
            "AGP": "Malaga",
            "ALC": "Alicante",
            "ACE": "Lanzarote",
            "AYT": "Antalya",
            "CFU": "Corfu",
            "DLM": "Dalaman",
            "FAO": "Faro",
            "FUE": "Fuerteventura",
            "GNB": "Grenoble",
            "GVA": "Geneva",
            "HER": "Heraklion",
            "LPA": "Gran Canaria",
            "MJV": "Murcia",
            "PMI": "Palma",
            "TFS": "Tenerife",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
