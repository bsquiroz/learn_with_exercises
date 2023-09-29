# MessageCode
se te ha encomendado la tarea de desarrollar una función llamada **messageCode** que realizará la codificación de frases utilizando un diccionario de caracteres personalizado llamado **my_dict**. Este diccionario asigna un carácter especial a cada letra del alfabeto, incluyendo tanto letras mayúsculas como minúsculas, además de algunos caracteres especiales comunes.

El objetivo principal de la función **messageCode** es proporcionar una forma de codificar mensajes de texto de manera segura, reemplazando cada letra de la frase original por su correspondiente en el diccionario **my_dict**. La codificación se basa en sustituir cada letra o carácter de la frase original por su respectivo valor en el diccionario.

<details>
<summary>diccionario con el código - **my_dict**</summary>

```python
{
    'a': '!', 
    'b': '@', 
    'c': '#',
    'd': '$', 
    'e': '%', 
    'f': '^', 
    'g': '&', 
    'h': '*', 
    'i': '(', 
    'j': ')', 
    'k': '-', 
    'l': '_', 
    'm': '=', 
    'n': '+', 
    'o': '[', 
    'p': '{', 
    'q': ']', 
    'r': '}', 
    's': '¿', 
    't': ':', 
    'u': ';', 
    'v': ',',
    'w': '.', 
    'x': '<', 
    'y': '>', 
    'z': '?',
    ' ': '~', 
    ',': '|'
}
```
</details>

### Ejemplo 1
- messageCode(myCode,'hola, mundo este es mi mensaje codificado')
- Salida: *[_!|~=;+$[~%¿:%~%¿~=(~=%+¿!)%~#[$(^(#!$[

### Ejemplo 2
- messageCode(myCode,'desde enero se siente que viene diciembre')
- Salida: $%¿$%~%+%}[~¿%~¿(%+:%~];%~,(%+%~$(#(%=@}%

### Ejemplo 3
- messageCode(myCode,'hola soy brayan y te apuesto que si eres capaz')
- Salida: *[_!~¿[>~@}!>!+~>~:%~!{;%¿:[~];%~¿(~%}%¿~#!{!?

### Ejemplo 4
- messageCode(myCode,'holi yo creo que si fuiste capaz')
- Salida: *[_(~>[~#}%[~];%~¿(~^;(¿:%~#!{!?