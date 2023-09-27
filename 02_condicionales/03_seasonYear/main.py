def seasonYear(month):
    if month in ["enero", "febrero", "marzo"]:
        return "Estamos en invierno"
    if month in ["abril", "mayo", "junio"]:
        return "Estamos en primavera"
    if month in ["julio", "agosto", "septiembre"]:
        return "Estamos en verano"
    if month in ["octubre", "noviembre", "diciembre"]:
        return "Estamos en otoño"

    return "Mes no válido"