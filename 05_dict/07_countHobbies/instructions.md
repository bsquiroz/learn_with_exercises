# CountHobbies
En el contexto de una aplicación de gestión de usuarios, Cada diccionario contiene información detallada sobre los usuarios, incluyendo su ID, nombre, edad, género y una lista de sus hobbies.

Tu tarea es crear una función llamada **countHobbies** que tome uno de estos conjuntos de datos como entrada y devuelva un diccionario que muestre cuántas veces se repite cada hobby en los datos de los usuarios. Cada clave del diccionario será un hobby y su valor asociado será la cantidad de veces que aparece en la lista de hobbies de los usuarios.

El recuento de hobbies es esencial para entender las preferencias y patrones de interés de los usuarios en la aplicación. Esto puede ayudar a la personalización de contenido y recomendaciones.

<details>
    <summary>Ejemplo 1</summary>

### Entrada
```python
[
    {
        'id': 100,
        'name': 'brayan',
        'age': 23,
        'gender': 'male',
        'hobbies': [
            'lavar cocina', 
            'hacer la cama',
            'comer'
        ]
    },
    {
        'id': 101,
        'name': 'sara',
        'age': 25,
        'gender': 'female',
        'hobbies': [
            'lavar cocina', 
            'hacer la cama',
            'comer',
            'cantar',
            'dormir'
        ]
    },
    {
        'id': 102,
        'name': 'stiven',
        'age': 18,
        'gender': 'male',
        'hobbies': [
            'cocinar',
            'lavar cocina', 
            'hacer la cama',
            'comer',
            'cantar',
            'dormir'
        ]
    },
    {
        'id': 103,
        'name': 'valentina',
        'age': 30,
        'gender': 'female', 
        'hobbies': [
            'cocinar',
            'lavar cocina', 
            'hacer la cama',
            'comer',
            'cantar',
            'dormir', 
            'caminar'
        ]
    }
]
```

### Salida 
```python
{
    'lavar cocina': 4, 
    'hacer la cama': 4, 
    'comer': 4, 
    'cantar': 3, 
    'dormir': 3, 
    'cocinar': 2, 
    'caminar': 1
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
        'gender': 'male', 
        'hobbies': [
            'correr',
            'jugar futbol', 
            'lol'
        ]
    },
    {
        'id': 111,
        'name': 'paola',
        'age': 40,
        'gender': 'female',
        'hobbies': [
            'correr',
            'jugar futbol', 
            'lol',
            'dormir',
            'comer',
            'cantar'
        ]
    },
    {
        'id': 112,
        'name': 'mauricio',
        'age': 35,
        'gender': 'male',
        'hobbies': [
            'correr',
            'jugar futbol', 
            'lol',
            'dormir',
            'comer',
            'cantar',
            'escalar',
            'descolgar'
        ]
    },
    {
        'id': 123,
        'name': 'estefania',
        'age': 30,
        'gender': 'female',
        'hobbies': [
            'correr',
            'jugar futbol', 
            'lol',
            'dormir',
            'comer',
            'cantar',
            'escalar',
            'descolgar', 
            'bailar', 
            'tomar malas decisiones'
        ]
    }
]
```

### Salida 
```python
{
    'correr': 4, 
    'jugar futbol': 4, 
    'lol': 4, 
    'dormir': 3, 
    'comer': 3, 
    'cantar': 3, 
    'escalar': 2, 
    'descolgar': 2, 
    'bailar': 1, 
    'tomar malas decisiones': 1
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
        'gender': 'male',
        'hobbies': [
            'viajar',
            'conocer pueblitos', 
            'aprender',
        ]
    },
    {
        'id': 211,
        'name': 'paula',
        'age': 20,
        'gender': 'female',
        'hobbies': [
            'viajar',
            'conocer pueblitos', 
            'aprender',
            'codear', 
            'que el codigo no compile'
        ]
    },
    {
        'id': 212,
        'name': 'carlos',
        'age': 25,
        'gender': 'male',
        'hobbies': [
            'viajar',
            'conocer pueblitos', 
            'aprender',
            'codear', 
            'que el codigo no compile', 
            'llorar por un bug'
        ]
    },
    {
        'id': 223,
        'name': 'dahiana',
        'age': 21,
        'gender': 'female', 
        'hobbies': [
            'viajar',
            'conocer pueblitos', 
            'aprender',
            'codear', 
            'que el codigo no compile', 
            'llorar por un bug', 
            'estar feliz porque arregle el codigo'
        ]
        
    }
]
```

### Salida 
```python
{
    'viajar': 4, 
    'conocer pueblitos': 4, 
    'aprender': 4, 
    'codear': 3, 
    'que el codigo no compile': 3, 
    'llorar por un bug': 2,
    'estar feliz porque arregle el codigo': 1
}
```

</details>