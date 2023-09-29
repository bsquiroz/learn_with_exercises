# femaleAndMale
Estás trabajando en un proyecto de análisis de datos en el que se maneja información detallada sobre varios usuarios. Los datos se almacenan en una lista de diccionarios llamada data, donde cada diccionario representa a un usuario con atributos como ID, nombre, edad y género. Tu objetivo es crear una función llamada **femaleAndMale** que tomará como entrada esta lista de usuarios y devolverá un diccionario que clasifique a los usuarios en dos categorías principales: "female" (mujeres) y "male" (hombres).

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
{
    'female': [
        {'id': 101, 'name': 'sara', 'age': 25, 'gender': 'female'}, 
        {'id': 103, 'name': 'valentina', 'age': 30, 'gender': 'female'}
        ], 
    'male': [
        {'id': 100, 'name': 'brayan', 'age': 23, 'gender': 'male'}, 
        {'id': 102, 'name': 'stiven', 'age': 18, 'gender': 'male'}
        ]
}
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
{
    'female': [
        {'id': 111, 'name': 'paola', 'age': 40, 'gender': 'female'}, 
        {'id': 123, 'name': 'estefania', 'age': 30, 'gender': 'female'}
        ], 
    'male': [
        {'id': 110, 'name': 'julio', 'age': 30, 'gender': 'male'},
        {'id': 112, 'name': 'mauricio', 'age': 35, 'gender': 'male'}
        ]
}
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
{
    'female': [
        {'id': 211, 'name': 'paula', 'age': 20, 'gender': 'female'}, 
        {'id': 223, 'name': 'dahiana', 'age': 21, 'gender': 'female'}
        ], 
    'male': [
        {'id': 210, 'name': 'pablo', 'age': 35, 'gender': 'male'}, 
        {'id': 212, 'name': 'carlos', 'age': 25, 'gender': 'male'}
        ]
}
```

</details>
