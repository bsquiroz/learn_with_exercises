# SearchMultiples
Imagina que estás trabajando en un proyecto de análisis de datos para una tienda de suministros de oficina en línea. Como parte de tu análisis, necesitas identificar y recopilar información sobre las cantidades de suministros de oficina que se compran en múltiplos de ciertos números clave. Para ayudarte en esta tarea, decides crear una función llamada **searchMultiples**.

La función **searchMultiples** toma dos argumentos: num, que representa el número clave que te interesa (por ejemplo, el número de unidades por paquete), y limit, que es el límite superior del rango dentro del cual deseas buscar múltiplos de num. Por ejemplo, si deseas encontrar los múltiplos de 4 dentro del rango de 1 a 8, utilizarías la función de la siguiente manera: **searchMultiples**(4, 8).

### Ejemplo 1
- print(searchMultiples(4, 8)) 
- Salida: [4, 8, 12, 16, 20, 24, 28, 32, 36]


### Ejemplo 2
- print(searchMultiples(3, 10))
- Salida: [6, 12, 18, 24, 30]

### Ejemplo 3
- print(searchMultiples(7, 7)) 
- Salida: [14, 28, 42, 56]
