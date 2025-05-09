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

![image](https://github.com/user-attachments/assets/875132da-6afb-4d7a-ac24-47ddcc8c7c77)

![image](https://github.com/user-attachments/assets/15390503-b357-4069-aff3-83a05fcf66f3)

Posteriormente, se sube la carpeta con los programas desarrollados a mi cuenta de GitHub.

![image](https://github.com/user-attachments/assets/d283b687-f309-4045-ab19-f0c8f6733672)

Finalmente se configura la pipeline utilizando el script definido en el archivo `Jenkinsfile`.  
Tras resolver varios problemas relacionados con los archivos, se logra ejecutar correctamente el primer *build*.

![image](https://github.com/user-attachments/assets/b36a488f-7636-42c3-9f4d-7d4a920395a6)

## Tarea 2

Para esta segunda tarea, la idea es **automatizar las ejecuciones**.  
Para hacerlo, desde el apartado de configuración del proyecto en Jenkins, se activa la opción de **"Ejecución Periódica"** y se establece un intervalo de cada **2 minutos**.

![image](https://github.com/user-attachments/assets/f35786b6-889d-4122-9a7c-a482d518fecd)

En las siguientes imágenes se puede observar cómo, automáticamente, Jenkins ejecuta los programas cada 2 minutos sin errores:

![image](https://github.com/user-attachments/assets/0fefcd80-dec2-4f2c-b78b-c4e8bc43297c)

![image](https://github.com/user-attachments/assets/cf8461d7-ebe0-453f-a746-373d8d0554c6)

Para comprobar el funcionamiento del sistema, se modifica temporalmente el test, insertando una función que genera un error de forma intencionada.

![image](https://github.com/user-attachments/assets/b691a0ec-5aa7-4f9b-bec4-28a95f113a90)

Al revisar la pipeline en Jenkins, se puede ver claramente que el *build* falla:

![image](https://github.com/user-attachments/assets/2a01eddf-1327-4c92-8d75-50adc8f286a4)

![image](https://github.com/user-attachments/assets/c42fa01c-d215-40df-b58c-e9003405317f)

Finalmente, una vez que se elimina la función modificada y se deja el código como estaba originalmente, Jenkins vuelve a ejecutar el *build* correctamente:

![image](https://github.com/user-attachments/assets/ed92fd3c-1c70-4300-a6bb-c5bd62973e27)

## 3.2

Para este apartado, se crean **3 archivos adicionales** aparte de los que ya teníamos, con el objetivo de construir una imagen de Docker.  
Los archivos creados son:

- `Dockerfile`
- `docker-compose.yml`
- `Jenkinsfile.docker`

![image](https://github.com/user-attachments/assets/1dc572f8-ce6a-4ba2-80f7-814f53600940)

Es necesario instalar los **plugins de Docker en Jenkins** para que funcione correctamente, ya que se está ejecutando Docker dentro de Docker (Docker-in-Docker).  
Sin embargo, aún así aparecieron algunos errores debido a que también se debe tener instalado y configurado **Docker Compose** en el contenedor.

![image](https://github.com/user-attachments/assets/e25ec608-d53b-4978-8fcd-ecd4fad0b56b)

![image](https://github.com/user-attachments/assets/2a8f4621-8dc5-421c-8fdc-cdc47145b1d3)

Finalmente, se logra ejecutar todas las pipelines correctamente, teniendo ya integradas todas las herramientas necesarias.

![image](https://github.com/user-attachments/assets/42d864c5-8214-4a08-b79e-b2166943f3fd)





