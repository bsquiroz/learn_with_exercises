def hourlyGreeting(hour):
    if 1 <= hour <= 5:
        return "Deberías estar durmiendo"
    if 6 <= hour <= 11:
        return "Buenos días"
    if 12 <= hour <= 18:
        return "Buenas tardes"
    if 19 <= hour <= 24:
        return "Buenas noches"
    
    return "Hora no soportada"
    