# sumColumnsAndRows
Imagina que estás trabajando en un programa de análisis de datos para una empresa de logística que se encarga de rastrear el inventario de productos en un almacén. Tienes una matriz bidimensional que representa una disposición de productos en estanterías. Cada fila de la matriz corresponde a una estantería y cada columna representa una posición en la estantería. Tu objetivo es calcular la cantidad total de productos en cada estantería y la cantidad total de productos en cada posición a lo largo de todas las estanterías.

### Ejemplo 1
- sumColumnsAndRows([
    [1,2,3],
    [4,5,6], 
    [7,8,9]
])
- Salida: [[6, 15, 24], [12, 15, 18]]

### Ejemplo 2
- sumColumnsAndRows([
    [10,2,3],
    [4,50,6], 
    [7,8,90]
])
- Salida: [[15, 60, 105], [21, 60, 99]]


### Ejemplo 3
- sumColumnsAndRows([
    [1,2,30],
    [4,50,6], 
    [70,8,9]
])
- Salida: [[33, 60, 87], [75, 60, 45]]