# ArrayToDict
Imagina que trabajas en un proyecto de procesamiento de datos en Python, Cada lista interna contiene información sobre diferentes aspectos de un usuario, como ID, nombre, apellido, edad y género, pero está en formato de lista en lugar de diccionario.

Tu tarea es crear una función llamada **arrayToDict** que tome una de estas listas de listas como entrada y la convierta en una lista de diccionarios. Cada elemento de la lista de diccionarios representará un usuario con todas sus propiedades como pares clave-valor en el diccionario.

Este proceso de conversión es esencial porque los diccionarios son más fáciles de manejar y proporcionan un acceso más eficiente a los datos que las listas.

<details>
    <summary>Ejemplo 1</summary>

### Entrada
```python
[
    ['id -> 100', 'name -> brayan', 'lastname -> muñoz', 'age -> 23', 'gender -> male'], 
    ['id -> 101', 'name -> sara', 'age -> 25', 'gender -> female'], 
    ['id -> 102', 'name -> stiven', 'age -> 18', 'gender -> male'], 
    ['id -> 103', 'name -> valentina', 'age -> 30', 'gender -> female']
]
```

### Salida 
```python
[
    {
        'id ': ' 100', 
        'name ': ' brayan', 
        'lastname ': ' muñoz', 
        'age ': ' 23', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 101', 
        'name ': ' sara', 
        'age ': ' 25', 
        'gender ': ' female'
    }, 
    {
        'id ': ' 102', 
        'name ': ' stiven', 
        'age ': ' 18', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 103', 
        'name ': ' valentina', 
        'age ': ' 30', 
        'gender ': 
        ' female'
    }
]
```

</details>

<details>
    <summary>Ejemplo 2</summary>

### Entrada
```python
[
    ['id -> 110', 'name -> julio', 'age -> 30', 'gender -> male'], 
    ['id -> 111', 'name -> paola', 'age -> 40', 'gender -> female'], 
    ['id -> 112', 'name -> mauricio', 'age -> 35', 'gender -> male'], 
    ['id -> 123', 'name -> estefania', 'age -> 30', 'gender -> female']
]
```

### Salida 
```python
[
    {
        'id ': ' 110', 
        'name ': ' julio',
        'age ': ' 30', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 111', 
        'name ': ' paola', 
        'age ': ' 40', 
        'gender ': ' female'
    }, 
    {
        'id ': ' 112', 
        'name ': ' mauricio', 
        'age ': ' 35', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 123', 
        'name ': ' estefania', 
        'age ': ' 30', 
        'gender ': ' female'
    }
]
```

</details>

<details>
    <summary>Ejemplo 3</summary>

### Entrada
```python
[
    ['id -> 210', 'name -> pablo', 'age -> 35', 'gender -> male'], 
    ['id -> 211', 'name -> paula', 'age -> 20', 'gender -> female'], 
    ['id -> 212', 'name -> carlos', 'age -> 25', 'gender -> male'], 
    ['id -> 223', 'name -> dahiana', 'lastname -> lopez', 'age -> 21', 'gender -> female']
]
```

### Salida 
```python
[
    {
        'id ': ' 210', 
        'name ': ' pablo', 
        'age ': ' 35', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 211', 
        'name ': ' paula', 
        'age ': ' 20', 
        'gender ': ' female'
    }, 
    {
        'id ': ' 212', 
        'name ': ' carlos', 
        'age ': ' 25', 
        'gender ': ' male'
    }, 
    {
        'id ': ' 223', 
        'name ': ' dahiana', 
        'lastname ': ' lopez', 
        'age ': ' 21', 
        'gender ': ' female'
    }
]
```

</details>