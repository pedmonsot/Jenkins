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

![Instalación de Jenkins - Parte 1](ruta/a/imagen1.png)  
![Instalación de Jenkins - Parte 2](ruta/a/imagen2.png)

Posteriormente, se sube la carpeta con los programas desarrollados a mi cuenta de GitHub.

![Repositorio subido a GitHub](ruta/a/imagen3.png)

Finalmente se configura la pipeline utilizando el script definido en el archivo `Jenkinsfile`.  
Tras resolver varios problemas relacionados con los archivos, se logra ejecutar correctamente el primer *build*.

![Build exitoso en Jenkins](ruta/a/imagen4.png)

## Tarea 2


