### Actividad: Pruebas BDD con behave en español

Este proyecto es un ejemplo de cómo utilizar **behave**, una herramienta para pruebas de desarrollo dirigido por comportamiento (Behavior-Driven Development - BDD) en Python, para escribir y ejecutar pruebas en español. Simula el comportamiento de un estómago (`Belly`) que gruñe o no en función de la cantidad de pepinos consumidos y el tiempo de espera.

### Objetivos de aprendizaje

Esta actividad tiene como propósito:
- Implementar los pasos de los escenarios BDD en Python, conectando las especificaciones de negocio con el código.
- Desarrollar pruebas unitarias con **Pytest**, aplicando principios de **TDD**.
- Estructurar correctamente un proyecto con **carpetas separadas para código fuente, pruebas unitarias y pruebas BDD**.
- Diseñar funciones capaces de interpretar y validar entradas humanas como descripciones de tiempo (ej. "dos horas y media").
- Manejar correctamente **errores y validaciones de entrada**, incluyendo casos fraccionarios o no válidos.
- Experimentar un ciclo completo de desarrollo: **historia de usuario → criterios de aceptación → pruebas → código → validación**.

### Estructura del proyecto
El proyecto tiene la siguiente estructura de directorios:

```
.
├── .github/workflows
│	└── ci.yml
├── features
│   ├── belly.feature
│   ├── environment.py
│   └── steps
│       └── belly_steps.py
├── src
│   └── belly.py
├── tests
│   └── unit_tests
│		├── test_parser.py
│		└── test_belly.py
├── requirements.txt
└── .gitignore
```

- **features**: Contiene los archivos relacionados con Behave.
    - **belly.feature**: Archivo que describe las características y escenarios en lenguaje Gherkin.
    - **environment.py**: Archivo de configuración para inicializar el contexto de Behave.
    - **steps**: Carpeta que contiene las definiciones de los pasos.
        - **steps.py**: Implementación de los pasos definidos en `belly.feature`.
- **src**: Contiene el código fuente del proyecto.
    - **belly.py**: Implementación de la clase `Belly`.

#### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**

**Objetivo**
- Ampliar la funcionalidad para reconocer tiempos de espera expresados en horas, minutos y segundos.

**Instrucciones**
1. **Modifica** la función que maneja el tiempo de espera en `steps.py` (o donde parsees el tiempo) para que acepte:
    - "1 hora y 30 minutos"
    - "90 minutos"
    - "3600 segundos"
    - **Variaciones** que incluyan segundos (por ejemplo, `"1 hora, 30 minutos y 45 segundos"`).
2. **Implementa** un escenario de prueba en Gherkin (`belly.feature`) que valide que el estómago gruñe o no según estas variaciones de tiempo.
3. **Considera** también crear pruebas unitarias con Pytest para la lógica de parsing (función que convierte el texto de tiempo en horas decimales).
4. **En un entorno DevOps**:
    - Agrega la ejecución de `behave` y `pytest` en tu _pipeline_ de CI/CD, de modo que al hacer push de los cambios se ejecuten automáticamente las pruebas.

**Solución**
Dentro de un proyecto ya contamos con un soporte para el proceso de expresiones regulares que incluyan horas con minutos y solamente minutos; sin embargo, falta aquella que maneja solo segundos y mezclas entre ellos.
Editaremos dentro de la función `step_when_wait_time_description`, para añadir la aceptación de expresiones regulares con segundos.

![](images/excercise_1_1.png)

Además también configuramos que la descripción del tiempo pueda descartar comas para prevenir posibles errores.

![](images/excercise_1_2.png)

Así mismo añadimos nuevos escenarios dentro de nuestro archivo `belly.feature` como se muestra en la siguiente imagen.

![](images/excercise_1_4.png)

Junto con ellos también definimos la carpeta `tests/unit_tests` donde guardamos los archivos definidos con la clase `pytest` para la prueba directa de algunas funciones, en este caso nos aseguramos de que el parseador opere con normalidad.

![](images/excercise_1_5.png)

Por último estamos definiendo nuestro entorno DevOps con la integración de pruebas unitarias y pruebas BDD dentro de la carpeta `.github/workflows` en el archivo `ci.yml`

![](images/excercise_1_3.png)

#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**

**Objetivo**

- Permitir que el sistema acepte cantidades fraccionarias de pepinos (decimales).

**Instrucciones**

1. **Modifica** el sistema (la clase `Belly` y los steps en Behave) para que acepte entradas como `"0.5"`, `"2.75"`.
2. **Implementa** un nuevo escenario en Gherkin donde se ingiera una cantidad fraccionaria y verifica el comportamiento.
3. **Valida** que el sistema lance una excepción o error si se ingresa una cantidad negativa de pepinos.
4. **Pruebas unitarias**:
    - Cubre el caso de pepinos fraccionarios en `test_belly.py`.
    - Cubre también el caso de pepinos negativos (se espera un error).

**Ejemplo Gherkin**:

```gherkin
Escenario: Comer una cantidad fraccionaria de pepinos
  Dado que he comido 0.5 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir
```

**En un entorno DevOps**:

- Asegúrate de que la falla (excepción por valor negativo) sea reportada como _falla de build_ si ocurre.
- Configura notificaciones (por correo/Slack/Teams) si alguna de las pruebas falla.

**Solución**
Para los requerimientos de esta pregunta modificamos la clase Belly de la siguiente forma:

![](images/excercise_2_1.png)

Dentro del archivo `belly_steps.py` definimos un tipo de valor personalizado para reproducir errores y permitir solo cierto tipo de valores para aquellos que sean designados como número de pepinos a comer:

![](images/excercise_2_2.png)

Modificamos el archivo `belly.features` para agregar nuevas pruebas que validen estas nuevas restricciones.

![](images/excercise_2_3.png)

Por último, generamos el archivo `test_belly.py` que establezca pruebas unitarias para la verificación de los cambios hechos dentro de `belly.py`.

![](images/excercise_2_4.png)

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**

**Objetivo**
- Aceptar descripciones de tiempo en distintos idiomas (español e inglés).

**Instrucciones**

1. **Modifica** el parsing de tiempo para que reconozca palabras clave en inglés, además de español (por ejemplo, `"two hours"`, `"thirty minutes"`).
2. **Escribe** al menos dos escenarios de prueba en Gherkin que usen tiempos en inglés.
3. **Implementa** una función que convierta las palabras en inglés a valores numéricos (similar a la que se usa para el español).
4. **En un pipeline DevOps**, podrías:
    - Dividir los escenarios en distintos _tags_ (`@spanish`, `@english`) y ejecutar cada conjunto en etapas diferentes, o en paralelo.

**Ejemplo Gherkin**:

```gherkin
Escenario: Esperar usando horas en inglés
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir
```

Hemos modificado el archivo `belly_steps.py` para que admitiese valores en ingles y en español para las descripciones de tiempos con nuevas conversiones y cambios dentro del patron de regex.

![](images/image1.png)

También añadimos 2 nuevos escenarios en `belly.feature` y ambos fueron admitidos correctamente:

![](images/image2.png)

![](images/image3.png)


#### Ejercicio 4: **Manejo de tiempos aleatorios**

**Objetivo**
- Permitir ingresar rangos de tiempo (por ejemplo, "entre 1 y 3 horas") y escoger un tiempo aleatorio dentro de ese rango.

**Instrucciones**
1. **Crea** una función que, dada una expresión como "entre 1 y 3 horas", devuelva un valor aleatorio entre 1 y 3 horas.
2. **Implementa** un escenario en Gherkin que verifique que, tras comer pepinos y esperar un tiempo aleatorio, el estómago puede gruñir.
3. **Imprime** (en consola o logs) el tiempo aleatorio elegido para que el resultado sea rastreable en tu pipeline.
4. **En un pipeline DevOps**:
   - Considera utilizar un *seed* de aleatoriedad fijo para evitar *flakiness* (tests intermitentes).
   - O, si manejas aleatoriedad real, acepta el riesgo de pruebas no deterministas y monitorea cuidadosamente.

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer pepinos y esperar un tiempo aleatorio
  Dado que he comido 25 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 5: **Validación de cantidades no válidas**

**Objetivo**
- Manejar y reportar adecuadamente errores al ingresar cantidades no válidas.

**Instrucciones**
1. **Añade** validaciones para evitar que el usuario ingrese < 0 pepinos o > 100 pepinos.
2. **Modifica** la lógica para arrojar un error (excepción) si la cantidad no es válida.
3. **Implementa** un escenario de prueba que verifique el comportamiento de error.
4. **En tu pipeline**, verifica que la excepción se maneje y el test falle de manera controlada si el sistema no lanza la excepción esperada.

**Ejemplo Gherkin**:
```gherkin
Escenario: Manejar una cantidad no válida de pepinos
  Dado que he comido -5 pepinos
  Entonces debería ocurrir un error de cantidad negativa.
```


#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**

**Objetivo**
- Asegurar que el sistema no falle ni se ponga lento con cantidades y tiempos muy grandes.

**Instrucciones**
1. **Añade** soporte para manejar cantidades de pepinos como 1000 (más allá del límite de validación anterior, o ajusta ese límite para pruebas internas).
2. **Implementa** un escenario en Gherkin para comer 1000 pepinos y esperar 10 horas.
3. **Verifica** que el sistema sigue comportándose correctamente (sin timeouts ni errores de rendimiento).
4. **En un pipeline DevOps**:
   - Ejecuta pruebas de estrés o de larga duración (puedes simular) para garantizar la robustez.
   - Mide el tiempo de ejecución para asegurarte de que no aumente drásticamente.

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer 1000 pepinos y esperar 10 horas
  Dado que he comido 1000 pepinos
  Cuando espero 10 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 7: **Descripciones de tiempo complejas**

**Objetivo**
- Ampliar la lógica para manejar descripciones avanzadas tipo `"1 hora, 30 minutos y 45 segundos"`.

**Instrucciones**
1. **Refuerza** la expresión regular y parsing para que soporte múltiples separadores (comas, "y", espacios, etc.).
2. **Implementa** escenarios que cubran al menos 2-3 variaciones complejas en Gherkin.
3. **Valida** que el total en horas sea exacto (suma de horas, minutos, segundos).
4. **En un pipeline**:
   - Puedes analizar la cobertura de pruebas (coverage) para asegurarte de que la nueva lógica de parsing está completamente testeada.

**Ejemplo Gherkin**:
```gherkin
Escenario: Manejar tiempos complejos
  Dado que he comido 50 pepinos
  Cuando espero "1 hora, 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir
```

#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**

**Objetivo**
- Practicar el paso de una prueba unitaria técnica a un escenario BDD comprensible por el negocio.

**Instrucciones**
1. **Escribe** un test unitario básico con Pytest que valide que si se han comido más de 10 pepinos y se espera 2 horas, el estómago gruñe.
2. **Convierte** ese test unitario en un escenario Gherkin, con la misma lógica, pero más orientado al usuario.
3. **Implementa** los pasos en Behave (si no existen).
4. **En un pipeline DevOps**:
   - Ejecuta primero los tests unitarios (rápidos) y luego los tests de Behave (que pueden ser más lentos y de nivel de integración).

**Ejemplo de test unitario** (TDD):
```python
def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin** (BDD):
```gherkin
Escenario: Comer muchos pepinos y esperar el tiempo suficiente
  Dado que he comido 15 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir
```

#### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**

**Objetivo**
- Traducir una historia de usuario en criterios de aceptación claros y escenarios BDD.

**Instrucciones**
1. **Toma** la historia de usuario:
   > "Como usuario que ha comido pepinos, quiero saber si mi estómago va a gruñir después de esperar un tiempo suficiente, para poder tomar una acción."
2. **Identifica** los criterios de aceptación (por ejemplo, cuántos pepinos y cuánto tiempo se debe esperar).
3. **Escribe** escenarios Gherkin que reflejen esos criterios.
4. **Implementa** los pasos en Behave.
5. **En un pipeline**:
   - Asegúrate de vincular (por ejemplo, en GitLab Issues o GitHub Issues) los escenarios con la historia de usuario para tener *traceability* (rastreabilidad).

**Ejemplo de escenarios Gherkin**:
```gherkin
Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

Escenario: Comer pocos pepinos y no esperar suficiente tiempo
  Dado que he comido 5 pepinos
  Cuando espero 1 hora
  Entonces mi estómago no debería gruñir
```

#### Ejercicio 10: **Escribir pruebas unitarias antes de escenarios BDD**

**Objetivo**
- Demostrar la secuencia TDD (tests unitarios) → BDD (escenarios).

**Instrucciones**
1. **Escribe** un test unitario para una nueva función, por ejemplo, `pepinos_comidos()`, que retorna el total de pepinos ingeridos.
2. **Crea** un escenario Gherkin que describe este comportamiento desde el punto de vista del usuario.
3. **Implementa** los pasos en Behave y verifica que pase la misma validación.
4. **En un pipeline**:
   - Ejecución secuencial: 1) Pytest, 2) Behave.
   - O en etapas separadas para un mejor feedback.

**Ejemplo de test unitario**:
```python
def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Saber cuántos pepinos he comido
  Dado que he comido 15 pepinos
  Entonces debería haber comido 15 pepinos
```


#### Ejercicio 11: **Refactorización guiada por TDD y BDD**

**Objetivo**
- Refactorizar código existente sin romper funcionalidades, validado por pruebas unitarias y escenarios BDD.

**Instrucciones**
1. **Elige** una funcionalidad ya existente (por ejemplo, `esta_gruñendo()`).
2. **Escribe** (o asegura que existen) pruebas unitarias que cubran los casos clave.
3. **Refactoriza** el código (`Belly` o funciones auxiliares) para mejorar eficiencia, legibilidad o reducir duplicación.
4. **Valida** que todas las pruebas unitarias y escenarios BDD siguen pasando sin cambios.
5. **En un pipeline**:
   - Activa la medición de **coverage** para asegurarte de que la refactorización no rompa funcionalidades no cubiertas.

**Ejemplo de test unitario**:
```python
def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**

**Objetivo**
- Desarrollar una nueva funcionalidad *desde cero* con TDD (prueba unitaria) y BDD (escenarios Gherkin).

**Instrucciones**
1. **Imagina** una nueva funcionalidad, por ejemplo, "Predecir si el estómago gruñirá con una cantidad dada de pepinos y un tiempo de espera".
2. **Escribe** primero la prueba unitaria.
3. **Conviértelo** en una historia de usuario y escribe el escenario BDD.
4. **Implementa** y verifica que tanto la prueba unitaria como el escenario Gherkin pasen.
5. **En tu pipeline**, revisa que no haya *regresiones* en otros tests.

**Ejemplo de test unitario**:
```python
def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Predecir si mi estómago gruñirá tras comer y esperar
  Dado que he comido 12 pepinos
  Cuando espero 1.5 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 13: **Añadir criterios de aceptación claros**

**Objetivo**
- Definir con precisión los criterios de aceptación de una nueva funcionalidad y plasmarlos en Gherkin.

**Instrucciones**
1. **Define** una nueva historia de usuario (por ejemplo, "Ver cuántos pepinos me faltan para gruñir").
2. **Identifica** al menos 2-3 criterios de aceptación.
3. **Convierte** esos criterios en escenarios BDD.
4. **Implementa** los pasos.
5. **En un pipeline**, agrupa los escenarios bajo un mismo *tag* (`@criterio_nuevo`) para ejecutarlos juntos.

**Ejemplo**:
```gherkin
Escenario: Ver cuántos pepinos puedo comer antes de que el estómago gruña
  Dado que he comido 8 pepinos
  Cuando pregunto cuántos pepinos más puedo comer
  Entonces debería decirme que puedo comer 2 pepinos más
```


#### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**

**Objetivo**
- Demostrar cómo inyectar dependencias simuladas en tu clase `Belly` y usarlas en pruebas BDD y TDD.

**Instrucciones**
1. **Crea** un archivo `clock.py` (por ejemplo) con una función `get_current_time()`.
2. **Modifica** `Belly` para aceptar un `clock_service` opcional que se inyecta.
3. **Crea** un test unitario con Pytest que use `unittest.mock` para simular el paso del tiempo.
4. **En Behave**, usa `environment.py` para inyectar un mock o stub del reloj en el `before_scenario`.
5. **En un pipeline DevOps**:
   - Asegúrate de no depender de la hora real, así evitas inestabilidad en las pruebas.

**Ejemplo**:
```python
def before_scenario(context, scenario):
    from unittest.mock import MagicMock
    from src.belly import Belly

    fake_clock = MagicMock()
    fake_clock.return_value = 10000  # tiempo fijo
    context.belly = Belly(clock_service=fake_clock)
```


#### Ejercicio 15: **Despliegue y validación continua en un entorno de integración (CI/CD)**

**Objetivo**
- Completar el ciclo DevOps: Cada push al repositorio **desencadena** pruebas automáticas BDD y TDD.

**Instrucciones**
1. **Configura** un pipeline (por ejemplo, en GitHub Actions o GitLab CI) con estos pasos:
   - Instalar dependencias (Python, Behave, Pytest).
   - Ejecutar pruebas unitarias (Pytest).
   - Ejecutar pruebas de comportamiento (Behave).
   - Generar reportes (HTML, JUnit) y publicarlos como *artifacts*.
2. **Incluye** verificación de calidad de código (por ejemplo, flake8 o black).
3. **Al aprobarse** el pipeline, **despliega** (si corresponde) tu aplicación o *script* a un entorno de staging/producción.
