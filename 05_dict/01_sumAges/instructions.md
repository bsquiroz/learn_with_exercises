# sumAges
Has sido asignado a un proyecto de análisis de datos que implica procesar información de usuarios. La información se almacena en una lista de diccionarios, donde cada diccionario representa a un usuario con atributos como ID, nombre, edad y género. Tu tarea es desarrollar una función llamada sumAges que calculará la suma total de las edades de todos los usuarios en la lista.

Esta función tomará como entrada la lista de usuarios y devolverá la suma de todas las edades. Esta información es crucial para comprender la distribución de edades de los usuarios y puede ser utilizada en futuros análisis estadísticos.

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
96

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
135

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
101

</details>



