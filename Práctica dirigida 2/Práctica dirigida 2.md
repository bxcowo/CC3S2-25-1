### Actividad: Exploración y administración avanzada de Git mediante un script interactivo

#### Materiales necesarios

- Un entorno de terminal (Linux, macOS o Windows con Git Bash).
- Un repositorio Git (puede ser uno de prueba).
- El script interactivo (por ejemplo, `git_avanzado.sh`).

> Puedes revisar una versión del script interactivo [aquí](https://github.com/kapumota/DS/blob/main/2025-1/git_avanzado.sh).

#### Instrucciones previas

1. **Descarga y guarda el script:**
   - Copia el contenido del script proporcionado (el ejemplo extendido) y guárdalo en un archivo llamado `git_avanzado.sh`.

2. **Asignar permisos de ejecución:**
   - Abre la terminal en el directorio donde guardaste el archivo y ejecuta:
     ```bash
     chmod +x git_avanzado.sh
     ```

3. **Ubicación:**
   - Asegúrate de ejecutar el script dentro de la raíz de un repositorio Git, ya que el script interactúa con el entorno Git.

![[Pasted image 20250423053053.png]]
### Procedimiento de la actividad

A continuación se muestra un ejemplo de uso que ilustra una sesión interactiva con el script. Este ejemplo simula cómo un usuario podría interactuar con algunas de las opciones
del menú. Recuerda que, al ejecutarlo, verás mensajes en tiempo real en la terminal y deberás ingresar las opciones y datos solicitados.

1. **Inicio del script**

   Tras darle permisos de ejecución y ejecutar el script desde la raíz de un repositorio Git, se muestra el siguiente menú en la terminal:

   ```
   ====== Menú avanzado de Git ======
   2) Listar reflog y restaurar un commit
   3) Agregar un submódulo
   4) Agregar un subtree
   5) Gestión de ramas
   6) Gestión de stashes
   7) Mostrar estado y últimos commits
   8) Gestión de tags
   9) Gestión de Git Bisect
   10) Gestión de Git Diff
   11) Gestión de Hooks
   12) Salir
   Seleccione una opción:
   ```

![[Pasted image 20250423053202.png]]

13. **Opción: agregar un submódulo (Opción 2)**

   - **Usuario:** Ingresa `2` y presiona Enter.
   - El script pide:
     ```
     Ingrese la URL del repositorio para el submódulo:
     ```
   - **Usuario:** Escribe, por ejemplo:  
     `https://github.com/usuario/repositorio-submodulo.git`
   - El script solicita:
     ```
     Ingrese el directorio donde se ubicará el submódulo:
     ```
   - **Usuario:** Escribe, por ejemplo:  
     `libs/submodulo`
   - **Script:** Ejecuta:
     ```bash
     git submodule add https://github.com/usuario/repositorio-submodulo.git libs/submodulo
     git submodule update --init --recursive
     ```
   - **Salida esperada:**  
     El mensaje confirmando que el submódulo ha sido agregado:
     ```
     Submódulo agregado en: libs/submodulo
     ```

![[Pasted image 20250423053251.png]]

3. **Opción: Gestión de ramas (Opción 4)**

   - **Usuario:** Regresa al menú principal y escoge la opción `4`.
   - El script despliega un submenú:
     ```
     === Gestión de ramas ===
     a) Listar ramas
     b) Crear nueva rama y cambiar a ella
     c) Cambiar a una rama existente
     d) Borrar una rama
     e) Volver al menú principal
     Seleccione una opción:
     ```
   - **Ejemplo A: Listar ramas (Opción a)**
     - **Usuario:** Ingresa `a` y presiona Enter.
     - **Script:** Ejecuta `git branch` y muestra la lista de ramas:
       ```
         master
       * feature/nueva-funcionalidad
       ```
   - **Ejemplo B: Crear una nueva rama (Opción b)**
     - **Usuario:** Ingresa `b`, luego el script pregunta:
       ```
       Ingrese el nombre de la nueva rama:
       ```
     - **Usuario:** Escribe `feature/login`.
     - **Script:** Ejecuta `git checkout -b feature/login` y confirma:
       ```
       Rama 'feature/login' creada y activada.
       ```

![[Pasted image 20250423053329.png]]

4. **Opción: Gestión de git diff (Opción 9)**

   - **Usuario:** Selecciona la opción `9` del menú principal.
   - El submenú de diff se muestra:
     ```
     === Gestión de git diff ===
     a) Mostrar diferencias entre el working tree y el área de staging (git diff)
     b) Mostrar diferencias entre el área de staging y el último commit (git diff --cached)
     c) Comparar diferencias entre dos ramas o commits
     d) Volver al menú principal
     Seleccione una opción:
     ```
   - **Ejemplo:**  
     - **Usuario:** Ingresa `c` para comparar dos revisiones.  
       El script solicita:
       ```
       Ingrese el primer identificador (rama o commit):
       ```
     - **Usuario:** Escribe `master`.
     - El script luego pregunta:
       ```
       Ingrese el segundo identificador (rama o commit):
       ```
     - **Usuario:** Escribe `feature/login`.
     - **Script:** Ejecuta `git diff master feature/login` y muestra las diferencias entre ambas ramas en la terminal.

![[Pasted image 20250423053614.png]]

5. **Opción: Gestión de hooks (Opción 10)**

   - **Usuario:** Escoge la opción `10` para gestionar hooks.
   - Se despliega el submenú de hooks:
     ```
     === Gestión de hooks ===
     a) Listar hooks disponibles
     b) Crear/instalar un hook (ej. pre-commit)
     c) Editar un hook existente
     d) Borrar un hook
     e) Volver al menú principal
     Seleccione una opción:
     ```
   - **Ejemplo:** Crear un hook pre-commit.
     - **Usuario:** Ingresa `b`.
     - El script pregunta:
       ```
       Ingrese el nombre del hook a instalar (por ejemplo, pre-commit):
       ```
     - **Usuario:** Escribe `pre-commit`.
     - Luego el script solicita:
       ```
       Ingrese el contenido del hook (una línea, se agregará '#!/bin/bash' al inicio):
       ```
     - **Usuario:** Escribe una línea, por ejemplo:
       `echo "Ejecutando pre-commit hook..." && exit 0`
     - **Script:** Crea el archivo `.git/hooks/pre-commit`, lo hace ejecutable y confirma:
       ```
       Hook 'pre-commit' instalado.
       ```

![[Pasted image 20250423053804.png]]

6. **Finalizar la sesión**

   - **Usuario:** Cuando termine de utilizar las opciones deseadas, regresa al menú principal y selecciona `11` para salir:
     ```
     Saliendo del script.
     ```

### Preguntas

- **¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante reflog?**

Después de restaurar un commit con reflog, el historial no muestra ningún registro de la operación de restauración en sí. El commit restaurado simplemente aparece como si nunca hubiera sido eliminado, pero no hay señales del proceso que usaste para recuperarlo. Esto puede generar confusiones a otros colaboradores, pero también puede resultar ser sumamente útil en entornos donde se prefiera mantener un historial mas limpio.


- **¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?**

Los submódulos mantienen repos separados que apuntan a commits específicos, lo que proporciona estabilidad; sin embargo, pueden complicar la actualización y la revisión de código por parte de colaboradores.
Por otro lado, los subtrees integran todo el proyecto en un solo repositorio facilitando el acceso al código, pero mezclan los historiales y complican posibles contribuciones futuras al proyecto original.


- **¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?**

La implementación de hooks acelera el proceso de desarrollo al proporcionar herramientas de automatización frente a triggers de distintas acciones como commits, pushes y merges; son particularmente útiles para asegurarse que las nuevas integraciones cumplan con los estándares de la empresa y que no reproduzcan errores al momento de ejecutarlos. 


- **¿De qué manera el uso de `git bisect` puede acelerar la localización de un error introducido recientemente?**

Al implementar una búsqueda binaria que sistemáticamente reduce a la mitad el espacio de búsqueda con cada prueba al etiquetar commits como 'buenos' o 'malos', se pueden ahorrar dolores de cabeza y horas pérdidas de pruebas y errores inconclusos, obteniéndose así el commit problemático rápidamente.


- **¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?**

Sin una convención clara acerca del uso de comandos como git merge, rebase y stash; los proyectos tienden a salirse de control muy fácilmente. Pueden haber múltiples conflictos entre más contribuyentes hayan modificando el código en paralelo; además, de que siempre existirá un desafío organizacional sobre las nuevas características a implementar.


### Ejercicios 

1 . Extiende el menú de gestión de ramas para incluir la funcionalidad de renombrar ramas.

**Instrucciones:**

1. **Investiga** el comando `git branch -m` que permite renombrar una rama.
2. **Modifica** la función de "Gestión de ramas" para agregar una nueva opción (por ejemplo, "f) Renombrar una rama").
3. **Implementa** la lógica para solicitar al usuario el nombre de la rama actual y el nuevo nombre.
4. **Verifica** que, tras el cambio, la rama se renombre correctamente.  
   **Pista:** Considera cómo se comporta el cambio si la rama en uso es la que se desea renombrar.

**Ejemplo de salida esperada:**

```
Ingrese el nombre de la rama actual: feature/login
Ingrese el nuevo nombre para la rama: feature/authentication
Rama 'feature/login' renombrada a 'feature/authentication'
```

![[Pasted image 20250423054528.png]]

![[Pasted image 20250423054618.png]]

2 . Amplia la sección de "Gestión de git diff" para permitir ver las diferencias de un archivo específico entre dos commits o ramas.

**Instrucciones:**

1. **Investiga** cómo usar `git diff` con la opción `--` para especificar un archivo (por ejemplo, `git diff commit1 commit2 -- path/to/file`).
2. **Agrega** al submenú de diff una nueva opción (por ejemplo, "e) Comparar diferencias de un archivo específico").
3. **Solicita** al usuario ingresar dos identificadores (ramas o commits) y luego la ruta del archivo.
4. **Ejecuta** el comando `git diff` para mostrar únicamente las diferencias para ese archivo y presenta el resultado en pantalla.

**Ejemplo de salida esperada:**

```
Ingrese el primer identificador (rama o commit): master
Ingrese el segundo identificador (rama o commit): feature/login
Ingrese la ruta del archivo: src/app.js
[Mostrará el diff solo de 'src/app.js' entre las dos revisiones]
```

![[Pasted image 20250423055224.png]]

![[Pasted image 20250423055407.png]]

3 . Crea una función que permita instalar automáticamente un hook que, por ejemplo, verifique si se han agregado comentarios de documentación en cada commit.

**Instrucciones:**

1. **Investiga** el hook pre-commit, que se ejecuta antes de que se realice un commit.
2. **Escribe** un pequeño script en Bash que verifique si se han modificado archivos y, para cada archivo modificado, compruebe si existen comentarios de documentación. Puedes establecer una regla simple, por ejemplo, que cada función definida en un archivo debe tener un comentario anterior.
3. **Integra** la función en el submenú de "Gestión de Hooks" o crea una nueva opción en el menú principal para instalar este hook.
4. **Prueba** la funcionalidad creando o modificando un commit sin la documentación requerida y verifica que el hook evite completar el commit.

**Ejemplo de contenido del hook:**

```bash
#!/bin/bash
# Hook pre-commit para verificar documentación en funciones

# Lista de archivos modificados
files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.c\|\.h\|\.js')
for file in $files; do
    # Ejemplo simplificado: verificar si existe al menos una línea con comentario ('//')
    if ! grep -q "//" "$file"; then
        echo "Error: El archivo '$file' no contiene comentarios de documentación."
        exit 1
    fi
done
exit 0
```

![[Pasted image 20250423061008.png]]

![[Pasted image 20250423061131.png]]

4 . Implementa una opción en el script que realice un merge automatizado de una rama determinada en la rama actual, incluyendo la resolución automática de conflictos (siempre que sea posible).

**Instrucciones:**

1. **Investiga** las opciones de `git merge` y cómo utilizar el parámetro `--strategy-option` (por ejemplo, `-X theirs` o `-X ours`) para la resolución automática de conflictos.
2. **Añade** una nueva opción en el menú principal (por ejemplo, "12) Merge automatizado de una rama").
3. **Solicita** al usuario el nombre de la rama que se desea fusionar.
4. **Ejecuta** el comando de merge con una estrategia de resolución automática, por ejemplo:
   ```bash
   git merge -X theirs <rama_a_fusionar>
   ```
5. **Valida** la operación mostrando el estado final tras el merge.

**Ejemplo de salida esperada:**

```
Ingrese el nombre de la rama a fusionar: feature/login
Merge completado automáticamente utilizando la estrategia 'theirs'.
```

![[Pasted image 20250423062108.png]]

![[Pasted image 20250423062246.png]]

5 . Implementa una opción en el script que genere un reporte con información relevante del repositorio (estado, ramas, últimos commits, stashes, etc.) y lo guarde en un archivo.

**Instrucciones:**

1. **Agrega** una nueva opción al menú principal (por ejemplo, "13 Generar reporte de estado del repositorio").
2. **Crea** una función que ejecute varios comandos de Git (ej. `git status`, `git branch`, `git log -n 5`, `git stash list`) y redirija la salida a un archivo, por ejemplo `reporte_git.txt`.
3. **Agrega** mensajes claros en el reporte que indiquen qué información corresponde a cada comando.
4. **Verifica** que el archivo se cree correctamente y que contenga la información esperada.

**Ejemplo de salida esperada:**

Al ejecutar la función, se debe crear el archivo `reporte_git.txt` con contenido similar a:
```
=== Estado del repositorio ===
[Salida de git status]

=== Ramas existentes ===
[Salida de git branch]

=== Últimos 5 commits ===
[Salida de git log -n 5]

=== Lista de stashes ===
[Salida de git stash list]
```

![[Pasted image 20250423062834.png]]

![[Pasted image 20250423062804.png]]