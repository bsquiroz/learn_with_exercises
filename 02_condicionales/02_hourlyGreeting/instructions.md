# HourlyGreeting
Imagina que estás desarrollando software para un innovador reloj inteligente llamado "SmartTime". Una de las características más interesantes de "SmartTime" es su capacidad para dar un saludo personalizado en función de la hora actual. El reloj es capaz de identificar el momento del día y saludar al usuario de acuerdo con la hora.
Tu tarea es escribir una función llamada **hourlyGreeting** que tome como entrada la hora actual en formato de 24 horas (un número entero) y devuelva un mensaje de saludo apropiado según la hora del día. La función hourlyGreeting debe seguir la siguiente estructura:

- Si la hora es entre 1 y 5, el reloj debe mostrar "Deberías estar durmiendo".
- Si la hora es entre 6 y 11, el reloj debe mostrar "Buenos días".
- Si la hora es entre 12 y 18, el reloj debe mostrar "Buenas tardes".
- Si la hora es entre 19 y 24, el reloj debe mostrar "Buenas noches".

### Ejemplo 1
- Entrada => 1 a 5   
- Salida => "Deberias estar durmiendo"

### Ejemplo 2
- Entrada => 6 a 11 
- Salida => "Buenos días"

### Ejemplo 3
- Entrada => 12 a 18 
- Salida => "Buenas tardes"

### Ejemplo 4
- Entrada => 19 a 24 
- Salida => "Buenas noches"

### Ejemplo 5 
- Entrada => cualquier otra cosa 
- Salida => "Hora no soportada"