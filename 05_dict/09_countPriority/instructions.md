# CountPriority
Imagina que estás trabajando en una aplicación de gestión de tareas. 
Cada conjunto de datos contiene información sobre tareas, incluyendo su nombre y prioridad.

Tu objetivo es crear una función llamada **countPriority** que tome uno de estos conjuntos de datos como entrada y devuelva un diccionario que muestre cuántas tareas hay para cada nivel de prioridad. Las claves del diccionario serán los niveles de prioridad y los valores serán la cantidad de tareas con esa prioridad.

<details>
    <summary>Ejemplo 1</summary>

### Entrada
```python
[
    {'name': 'hacer la cama', 'priority': 'A'},
    {'name': 'hacer el desayuno', 'priority': 'B'},
    {'name': 'hacer el almuerzo', 'priority': 'C'},
    {'name': 'practicar ingles', 'priority': 'A'},
    {'name': 'preparar la clase', 'priority': 'C'},
    {'name': 'dar la clase', 'priority': 'C'},
    {'name': 'ir al gym', 'priority': 'A'}
]
```

### Salida 
```python
{
    'A': 3, 
    'B': 1, 
    'C': 3
}
```

</details>

<details>
    <summary>Ejemplo 2</summary>

### Entrada
```python
[
    {'name': 'hacer la cama', 'priority': 'a'},
    {'name': 'hacer el ejercicio', 'priority': 'c'},
    {'name': 'trapear toda la casa', 'priority': 'c'},
    {'name': 'practicar frances', 'priority': 'a'},
    {'name': 'aprender c#', 'priority': 'c'},
    {'name': 'estudiar la clase del dia anterior', 'priority': 'b'},
    {'name': 'dormir bien a gusto', 'priority': 'b'}
]
```

### Salida 
```python
{
    'a': 2, 
    'c': 3, 
    'b': 2
}
```

</details>

<details>
    <summary>Ejemplo 3</summary>

### Entrada
```python
[
    {'name': 'hacer la cama', 'priority': 'alta'},
    {'name': 'ir a trotar', 'priority': 'alta'},
    {'name': 'barrer toda la casa', 'priority': 'baja'},
    {'name': 'practicar japones', 'priority': 'alta'},
    {'name': 'aprender javascript', 'priority': 'baja'},
    {'name': 'estudiar sobre filosofía y astronomía', 'priority': 'baja'},
    {'name': 'pasar el examen de academlo', 'priority': 'media'}
]
```

### Salida 
```python
{
    'alta': 3, 
    'baja': 3, 
    'media': 1
}
```

</details>