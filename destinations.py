"""Exeter Airport (EXT) destinations — verified via Google Flights."""

DESTINATIONS = {
    "EXT": {
        "name": "Exeter",
        "routes": {
            "AGP": "Malaga",
            "ALC": "Alicante",
            "DUB": "Dublin",
            "FAO": "Faro",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
