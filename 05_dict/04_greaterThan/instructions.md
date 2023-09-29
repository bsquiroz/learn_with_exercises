# GreaterThan
Imagina que estás trabajando en el desarrollo de un sistema de gestión de usuarios para una aplicación.
Cada conjunto de datos contiene información detallada sobre los usuarios, incluyendo su ID, nombre, edad y género.

Tu tarea es crear una función llamada **greaterThan** que tomará uno de estos conjuntos de datos como entrada y devolverá una lista de usuarios que sean mayores de 25 años. Cada usuario en la lista de salida se representará como un diccionario que conserva todos sus atributos, como ID, nombre, edad y género.

<details>
    <summary>Ejemplo 1</summary>

### Entrada
```python
[
    {
        'id': 100,
        'name': 'brayan',
        'age': 23,
        'gender': 'male'
    },
    {
        'id': 101,
        'name': 'sara',
        'age': 25,
        'gender': 'female'
    },
    {
        'id': 102,
        'name': 'stiven',
        'age': 18,
        'gender': 'male'
    },
    {
        'id': 103,
        'name': 'valentina',
        'age': 30,
        'gender': 'female'
    }
]
```

### Salida 
```python
[
    {'id': 103, 'name': 'valentina', 'age': 30, 'gender': 'female'}
]
```

</details>

<details>
    <summary>Ejemplo 2</summary>

### Entrada
```python
[
    {
        'id': 110,
        'name': 'julio',
        'age': 30,
        'gender': 'male'
    },
    {
        'id': 111,
        'name': 'paola',
        'age': 40,
        'gender': 'female'
    },
    {
        'id': 112,
        'name': 'mauricio',
        'age': 35,
        'gender': 'male'
    },
    {
        'id': 123,
        'name': 'estefania',
        'age': 30,
        'gender': 'female'
    }
]
```

### Salida 
```python
[
    {'id': 110, 'name': 'julio', 'age': 30, 'gender': 'male'}, 
    {'id': 112, 'name': 'mauricio', 'age': 35, 'gender': 'male'}, 
    {'id': 123, 'name': 'estefania', 'age': 30, 'gender': 'female'}
]
```

</details>

<details>
    <summary>Ejemplo 3</summary>

### Entrada
```python
[
    {
        'id': 210,
        'name': 'pablo',
        'age': 35,
        'gender': 'male'
    },
    {
        'id': 211,
        'name': 'paula',
        'age': 20,
        'gender': 'female'
    },
    {
        'id': 212,
        'name': 'carlos',
        'age': 25,
        'gender': 'male'
    },
    {
        'id': 223,
        'name': 'dahiana',
        'age': 21,
        'gender': 'female'
    }
]
```

### Salida 
```python
[
    {'id': 210, 'name': 'pablo', 'age': 35, 'gender': 'male'}
]
```

</details>
