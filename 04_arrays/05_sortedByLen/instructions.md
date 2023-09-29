# SortedByLen
Imagina que estás trabajando en una aplicación que maneja una lista de nombres y necesita ordenar estos nombres de acuerdo con su longitud, tanto en orden ascendente como en orden descendente. La función sortedByLen que has desarrollado tiene como objetivo realizar esta tarea de ordenamiento. Toma una lista de nombres como entrada y devuelve dos listas: una lista ordenada por longitud de nombres de forma ascendente (de nombres más cortos a nombres más largos) y otra lista ordenada por longitud de nombres de forma descendente (de nombres más largos a nombres más cortos).

### Ejemplo 1
- sortedByLen(['juan', 'pedro', 'brayan', 'alex', 'ana'])
- Salida: 
    ```python
    [
        ['ana', 'juan', 'alex', 'pedro', 'brayan'], 
        ['brayan', 'pedro', 'juan', 'alex', 'ana']
    ]
    ```


### Ejemplo 2
- sortedByLen(['alexander', 'pedronel', 'maurico', 'alex', 'ana'])
- Salida: 

    ```python
    [
        ['ana', 'alex', 'maurico', 'pedronel', 'alexander'], 
        ['alexander', 'pedronel', 'maurico', 'alex', 'ana']
    ]
    ```

### Ejemplo 3
- sortedByLen(['karen', 'carlos', 'maurico', 'agustous', 'ana'])
- Salida: 

    ```python
    [
        ['ana', 'karen', 'carlos', 'maurico', 'agustous'], 
        ['agustous', 'maurico', 'carlos', 'karen', 'ana']
    ]
    ```
