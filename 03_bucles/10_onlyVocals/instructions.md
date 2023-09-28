# GreaterAndLesserNumber
Imagina que estás trabajando en una aplicación de procesamiento de texto que necesita realizar una transformación específica en una frase o texto proporcionado. La función amountVocals que has desarrollado tiene como objetivo realizar esta transformación. Toma una frase como entrada y realiza lo siguiente:

1. Convierte la frase a minúsculas para asegurarse de contar tanto vocales mayúsculas como minúsculas.
2. Reemplaza cada vocal en la frase con la vocal misma.
3. Reemplaza cada espacio en blanco en la frase con un espacio en blanco.
4. Reemplaza todos los demás caracteres en la frase con un guión bajo ('_').

El resultado final es una cadena que conserva las vocales y los espacios en blanco, pero reemplaza todos los demás caracteres con guiones bajos.

### Ejemplo 1
- amountVocals('Esta sera una gran historia') 
- Salida: e__a _e_a u_a __a_ _i__o_ia

### Ejemplo 2
- amountVocals('Hola mundo desde RIWI') 
- Salida: _o_a _u__o _e__e _i_i

### Ejemplo 3
- amountVocals('Esto apenas comienza, esto no para')
- Salida: e__o a_e_a_ _o_ie__a_ e__o _o _a_a
