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


