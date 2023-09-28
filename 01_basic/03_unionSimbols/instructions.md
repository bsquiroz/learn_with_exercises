# UnionSimbols
Imagina que estás desarrollando una pequeña utilidad para procesar texto en un programa de procesamiento de lenguaje natural. Tu objetivo es crear una función llamada **unionSimbols** que tome una frase como entrada (**Phrase**) y un símbolo (**Symbol**) y luego devuelva la misma frase con ese símbolo insertado entre cada par de palabras de la frase original. Esta función será útil para formatear texto de manera específica, como reemplazar espacios en blanco entre palabras con un símbolo en particular.

### Ejemplo 1
- unionSimbols('Hola mundo me llamo RIWI', '*')
- Salida: Hola*mundo*me*llamo*RIWI


### Ejemplo 2
- unionSimbols('Este ejercicio está muy fácil', '-') 
- Salida: Este-ejercicio-está-muy-fácil


### Ejemplo 3
- unionSimbols('Aquí sí aprenderé a trabajar', '+')  
- Salida: Aquí+sí+aprenderé+a+trabajar