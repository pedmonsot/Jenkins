# 3.1

## Tarea 1

Primeramente, se crean los archivos que se desean subir a GitHub.
Se desarrolla un programa en Python para la **identificación de direcciones IP maliciosas**, y posteriormente se crea un test unitario que servirá como base para implementar la pipeline en Jenkins.
También se redacta el archivo Jenkinsfile, dejando la siguiente estructura de proyecto:

Jenkins/

    ├── detection.py            ← Código principal
    ├── test_detection.py       ← Test unitario con unittest
    ├── Jenkinsfile             ← Pipeline funcional
    └── README.md               ← Explicación del proyecto

Luego, se procede a instalar Jenkins siguiendo la guía disponible en:  
[https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)

![image](https://github.com/user-attachments/assets/0716aa64-1d10-4fc0-bc16-b9ed33405522)

![image](https://github.com/user-attachments/assets/e535db45-6e23-4c8b-a5bf-aeda50a22d8a)

Posteriormente, se sube la carpeta con los programas desarrollados a mi cuenta de GitHub.

![image](https://github.com/user-attachments/assets/a4f91a9a-01e9-4dc9-9723-eb26485ee646)

Finalmente se configura la pipeline utilizando el script definido en el archivo `Jenkinsfile`.  
Tras resolver varios problemas relacionados con los archivos, se logra ejecutar correctamente el primer *build*.

![image](https://github.com/user-attachments/assets/a6fbe435-f5dc-4e01-9d8c-25563096fce1)

## Tarea 2


Para esta segunda tarea, la idea es **automatizar las ejecuciones**.  
Para hacerlo, desde el apartado de configuración del proyecto en Jenkins, se activa la opción de **"Ejecución Periódica"** y se establece un intervalo de cada **2 minutos**.

![Configuración de ejecución periódica](ruta/a/imagen5.png)

En las siguientes imágenes se puede observar cómo, automáticamente, Jenkins ejecuta los programas cada 2 minutos sin errores:

![Ejecución automática 1](ruta/a/imagen6.png)  
![Ejecución automática 2](ruta/a/imagen7.png)

Para comprobar el funcionamiento del sistema, se modifica temporalmente el test, insertando una función que genera un error de forma intencionada.

![Código modificado para provocar fallo](ruta/a/imagen8.png)

Al revisar la pipeline en Jenkins, se puede ver claramente que el *build* falla:

![Error detectado en pipeline 1](ruta/a/imagen9.png)  
![Error detectado en pipeline 2](ruta/a/imagen10.png)

Finalmente, una vez que se elimina la función modificada y se deja el código como estaba originalmente, Jenkins vuelve a ejecutar el *build* correctamente:

![Build exitoso tras revertir el error](ruta/a/imagen11.png)

# 3.2





