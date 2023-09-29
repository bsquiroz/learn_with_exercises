# DictToArray
En el desarrollo de una aplicación de gestión de usuarios, cada diccionario contiene información detallada sobre los usuarios, incluyendo su ID, nombre, apellido (si está presente), edad y género.

Tu objetivo es crear una función llamada dictToArray que tome como entrada uno de estos conjuntos de datos y realice una transformación específica. La función debe convertir cada diccionario de usuario en una lista de cadenas con un formato clave-valor, donde cada elemento de la lista corresponde a un par clave-valor del diccionario original. Las claves se representarán en formato 'clave -> valor', donde 'clave' es el nombre del atributo y 'valor' es el valor correspondiente del atributo.

<details>
    <summary>Ejemplo 1</summary>

### Entrada
```python
[
    {
        'id': 100,
        'name': 'brayan',
        'lastname': 'muñoz',
        'age': 23,
        'gender': 'male',
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
    ['id -> 100', 'name -> brayan', 'lastname -> muñoz', 'age -> 23', 'gender -> male'], 
    ['id -> 101', 'name -> sara', 'age -> 25', 'gender -> female'], 
    ['id -> 102', 'name -> stiven', 'age -> 18', 'gender -> male'], 
    ['id -> 103', 'name -> valentina', 'age -> 30', 'gender -> female']
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
    ['id -> 110', 'name -> julio', 'age -> 30', 'gender -> male'], 
    ['id -> 111', 'name -> paola', 'age -> 40', 'gender -> female'], 
    ['id -> 112', 'name -> mauricio', 'age -> 35', 'gender -> male'], 
    ['id -> 123', 'name -> estefania', 'age -> 30', 'gender -> female']
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
        'lastname': 'lopez',
        'age': 21,
        'gender': 'female'
    }
]
```

### Salida 
```python
[
    ['id -> 210', 'name -> pablo', 'age -> 35', 'gender -> male'], 
    ['id -> 211', 'name -> paula', 'age -> 20', 'gender -> female'], 
    ['id -> 212', 'name -> carlos', 'age -> 25', 'gender -> male'], 
    ['id -> 223', 'name -> dahiana', 'lastname -> lopez', 'age -> 21', 'gender -> female']
]
```

</details>