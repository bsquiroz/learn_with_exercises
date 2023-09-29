# Welcome
En el desarrollo de una aplicación de gestión de usuarios, cada diccionario contiene información detallada sobre los usuarios, incluyendo su ID, nombre, edad, género y una lista de sus hobbies.

Tu tarea consiste en crear una función llamada getUniqueHobbies que tome uno de estos conjuntos de datos como entrada y devuelva una lista que contenga todos los hobbies únicos de los usuarios. La función debe eliminar cualquier repetición de hobbies y garantizar que solo aparezca una vez cada hobby en la lista de salida.

La obtención de hobbies únicos es importante para proporcionar a los usuarios una visión clara y sin duplicados de las actividades que les interesan. Esto puede ser valioso para personalizar sus experiencias en la aplicación.

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
['lavar cocina', 'hacer la cama', 'comer', 'cantar', 'dormir', 'cocinar', 'caminar']
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
['correr', 'jugar futbol', 'lol', 'dormir', 'comer', 'cantar', 'escalar', 'descolgar', 'bailar', 'tomar malas decisiones']
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
['viajar', 'conocer pueblitos', 'aprender', 'codear', 'que el codigo no compile', 'llorar por un bug', 'estar feliz porque arregle el codigo']
```

</details>