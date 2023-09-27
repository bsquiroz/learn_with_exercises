# SeasonYear
Imagina que estás desarrollando un innovador calendario inteligente llamado "SmartCal". Este calendario tiene la capacidad de identificar automáticamente la estación del año según el mes ingresado y proporcionar información útil relacionada con el clima y las actividades estacionales. El "SmartCal" es una herramienta esencial para ayudar a las personas a planificar sus actividades según las condiciones climáticas y las festividades estacionales.

Tu tarea es escribir una función llamada **seasonYear** que tome como entrada el nombre de un mes y devuelva un mensaje que indique en qué estación del año nos encontramos. La función **seasonYear** debe seguir la siguiente estructura:

- Si el mes ingresado es "enero", "febrero" o "marzo", el "SmartCal" debe mostrar "Estamos en invierno".
- Si el mes ingresado es "abril", "mayo" o "junio", el "SmartCal" debe mostrar "Estamos en primavera".
- Si el mes ingresado es "julio", "agosto" o "septiembre", el "SmartCal" debe mostrar "Estamos en verano".
- Si el mes ingresado es "octubre", "noviembre" o "diciembre", el "SmartCal" debe mostrar "Estamos en otoño".

### Ejemplo 1
- Entrada => enero a marzo       
- Salida => "Estamos en invierno"

### Ejemplo 2
- Entrada => abril a junio       
- Salida => "Estamos en primavera"

### Ejemplo 3
- Entrada => julio a septiembre  
- Salida => "Estamos en verano"

### Ejemplo 4
- Entrada => octubre a diciembre 
- Salida => "Estamos en otoño"

### Ejemplo 5
- Entrada => cualquier otra cosa 
- Salida => "Mes no válido"