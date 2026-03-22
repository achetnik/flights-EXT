"""Exeter Airport (EXT) destinations — verified March 2026."""

DESTINATIONS = {
    "EXT": {
        "name": "Exeter",
        "routes": {
            "ABZ": "Aberdeen",
            "ACE": "Lanzarote",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AYT": "Antalya",
            "BHD": "Belfast City",
            "CFU": "Corfu",
            "CMF": "Chambery",
            "DLM": "Dalaman",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "ENF": "Enontekio",
            "GCI": "Guernsey",
            "GLA": "Glasgow",
            "HER": "Heraklion",
            "IBZ": "Ibiza",
            "ISC": "Isles of Scilly",
            "JER": "Jersey",
            "LPA": "Gran Canaria",
            "MAH": "Menorca",
            "NCL": "Newcastle",
            "NWI": "Norwich",
            "PFO": "Paphos",
            "PJA": "Pajala",
            "PMI": "Palma",
            "RHO": "Rhodes",
            "TFS": "Tenerife",
            "ZTH": "Zakynthos",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
