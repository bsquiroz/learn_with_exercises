# GeneratePasswordUsers
Imagina que estás trabajando en el desarrollo de un sistema de gestión de usuarios para una aplicación. Para aumentar la seguridad de los datos de usuario y garantizar que cada cuenta tenga una contraseña única, se te ha encomendado la tarea de crear una función llamada **generatePasswordUsers**. Esta función tomará como entrada un conjunto de datos de usuarios que se representa como una lista de diccionarios, donde cada diccionario contiene información como el ID del usuario, su nombre, edad y género.

La función **generatePasswordUsers** tiene la responsabilidad de agregar un nuevo campo llamado 'password' a cada diccionario de usuario en el conjunto de datos. Esta contraseña se generará de manera simple, concatenando el nombre del usuario con su ID. Esta práctica proporcionará contraseñas únicas para cada usuario, lo que es esencial para proteger sus cuentas.

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
    {'id': 100, 'name': 'brayan', 'age': 23, 'gender': 'male', 'password': 'brayan100'}, 
    {'id': 101, 'name': 'sara', 'age': 25, 'gender': 'female', 'password': 'sara101'}, 
    {'id': 102, 'name': 'stiven', 'age': 18, 'gender': 'male', 'password': 'stiven102'}, 
    {'id': 103, 'name': 'valentina', 'age': 30, 'gender': 'female', 'password': 'valentina103'}
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
    {'id': 110, 'name': 'julio', 'age': 30, 'gender': 'male', 'password': 'julio110'}, 
    {'id': 111, 'name': 'paola', 'age': 40, 'gender': 'female', 'password': 'paola111'}, 
    {'id': 112, 'name': 'mauricio', 'age': 35, 'gender': 'male', 'password': 'mauricio112'}, 
    {'id': 123, 'name': 'estefania', 'age': 30, 'gender': 'female', 'password': 'estefania123'}
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
    {'id': 210, 'name': 'pablo', 'age': 35, 'gender': 'male', 'password': 'pablo210'}, 
    {'id': 211, 'name': 'paula', 'age': 20, 'gender': 'female', 'password': 'paula211'}, 
    {'id': 212, 'name': 'carlos', 'age': 25, 'gender': 'male', 'password': 'carlos212'}, 
    {'id': 223, 'name': 'dahiana', 'age': 21, 'gender': 'female', 'password': 'dahiana223'}
]
```

</details>
