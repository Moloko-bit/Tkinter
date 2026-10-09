# Словарь формул для конвертации различных единиц
CONVERSIONS = {
    # Длина
    "Километры → мили": lambda v: v * 0.621371,
    "Мили → километры": lambda v: v / 0.621371,
    "Метры → футы": lambda v: v * 3.28084,
    
    # Масса
    "Килограммы → фунты": lambda v: v * 2.20462,
    "Фунты → килограммы": lambda v: v / 2.20462,
    
    # Температура
    "°C → °F": lambda v: v * 9 / 5 + 32,
    "°F → °C": lambda v: (v - 32) * 5 / 9,
    
    # Валюты (пример с фиксированным курсом)[cite: 21]
    "USD → KZT": lambda v: v * 480.0,
    "KZT → USD": lambda v: v / 480.0,
}

def convert_units(conversion_name, value):
    """Выполняет конвертацию по заданному имени правила."""
    if conversion_name in CONVERSIONS:
        return CONVERSIONS[conversion_name](value)
    raise ValueError("Неизвестное направление конвертации")

def swap_units(current_selection):
    """Меняет местами единицы в названии (например, 'Километры → мили' -> 'Мили → километры')."""
    if "→" in current_selection:
        parts = current_selection.split("→")
        left = parts[0].strip()
        right = parts[1].strip()
        
        # Ищем обратную пару в словаре
        inverse_name = f"{right} → {left}"
        if inverse_name in CONVERSIONS:
            return inverse_name
    return current_selection