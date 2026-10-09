# Словарь формул для конвертации единиц
CONVERSIONS = {
    "Километры → мили": lambda value: value * 0.621371,
    "Килограммы → фунты": lambda value: value * 2.20462,
    "°C → °F": lambda value: value * 9 / 5 + 32,
}

def convert_units(conversion_name, value):
    """Выполняет конвертацию по заданному имени правила."""
    if conversion_name in CONVERSIONS:
        return CONVERSIONS[conversion_name](value)
    raise ValueError("Неизвестное направление конвертации")