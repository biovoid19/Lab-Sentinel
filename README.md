# Sistema de control de acceso con reconocimiento con tarjeta RFID
## _SentinelAB!._

## Introducción.
Los sistemas de control de acceso con reconocimiento de tarjeta RFID, son una tecnología avanzada utilizada para gestionar y supervisar el acceso a edificios, áreas restringidas o recursos sensibles. Estos sistemas se basan en la comunicación inalámbrica entre una tarjeta RFID y un lector o receptor, lo que permite la identificación y autenticación de individuos de manera eficiente y segura.

El lector RFID es el dispositivo que emite una señal de radiofrecuencia para activar la tarjeta RFID cercana y recibir la información almacenada en el chip. Una vez que la tarjeta responde a la señal, se establece una comunicación entre la tarjeta y el lector, permitiendo la transferencia de datos de identificación y autenticación. El sistema puede ser configurado para permitir o denegar el acceso según los privilegios y permisos asignados a cada tarjeta.

## Propósito.
El proposito de este proyecto es mantener un ambiente seguro y controlado, se implementaría un sistema de control de acceso con reconocimiento de tarjeta RFID en varias áreas de la unniversidad , como edificios académicos, biblioteca y laboratorios.

## Objetivos.
- Implementación de Infraestructura RFID:
Diseñar e implementar un sistema de control de acceso con reconocimiento de tarjeta RFID en áreas clave de la universidad, incluyendo edificios académicos, la biblioteca y laboratorios, garantizando la cobertura y funcionalidad adecuadas.
-  Asignación de Tarjetas RFID Personalizadas:
Emitir tarjetas RFID personalizadas a estudiantes, profesores y personal de la universidad, estableciendo perfiles únicos para cada usuario y asignando niveles de acceso específicos de acuerdo con sus roles y necesidades


## Material necesario

Para realizar el prototipo se necesitan los siguientes materiales:

- Sensor RFID
- Raspberry pi 4
- LED rojo
- LED verde
- relevador
- Buzzer
- ceradurra
- GPIO 
- Protoboard
- Jumpers de conexión
- MYSQL
- [Python](https://www.python.org/)

### Material de referencia
En los siguientes enlaces puedes encontrar los enlaces en la plataforma de edu.codigoiot.com que te permitirán realizar las configuraciones necesarias 

- [Instalación de Raspbery Pi OS en Raspberry Pi 4](https://edu.codigoiot.com/mod/subcourse/view.php?id=3924)
- [Lectura y escritura de tarjetas RFID con Raspberry Pi](https://edu.codigoiot.com/mod/subcourse/view.php?id=3927)

## Instalacion.
### Para ejecutar la aplicacion de la cerradura instala las dependencias.

 Instala el framework Flask para crear la aplicacion web en Python.
 ```sh
pip install flask
```
 Agrega SQLAlchemy a Flask para facilitar la interacción con bases de datos.
 ```sh
pip install flask-sqlalchemy
```
  Integra Marshmallow en Flask para manejar la serialización y deserialización de datos en aplicaciones web.
  ```sh 
pip install flack-marshmallow
```
  Extiende Marshmallow para trabajar fácilmente con objetos SQLAlchemy en aplicaciones Flask.
  ```sh
pip install marshmallow-sqlalchemy
```
   Proporciona una forma de conectarse a bases de datos MySQL desde aplicaciones Python.
```sh
pip install pymysql
```

Para poder iniciar la aplicacion.
```sh
python 
python app.py
```
> Nota: `lectira.py` es requerido para poder leer los RFID.
> Nota: `app.py` es requerido para poder cuardar la informacion en la base de datos.

### instalacion de Mysql.
```sh
Install MySQL: sudo apt install mariadb-server php-mysql -y
Create User Query: CREATE USER ‘admin’@’localhost’ IDENTIFIED BY ‘password’;
Grant User Permissions: GRANT ALL PRIVILEGES ON . to ‘admin’@’localhost’ WITH GRANT OPTION;
```
#### instalacion de phpMyAdmin.
```sh
Install PHPMyAdmin: sudo apt-get install phpmyadmin
Edit Apache Config: sudo nano /etc/apache2/apache2.conf
Add PHP Config to Apache: Include /etc/phpmyadmin/apache.conf
```

### Creación de la Base de Datos sentinelab

```sql
-- Crear la base de datos
CREATE DATABASE sentinelab;

-- Usar la base de datos recién creada
USE sentinelab;

-- Crear la tabla de usuarios
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contraseña VARCHAR(50) NOT NULL
);

-- Crear la tabla de récords
CREATE TABLE records (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    fecha DATE,
    puntuacion INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Crear la tabla de asociaciones
CREATE TABLE asociaciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);
```

## Rutas de la API
#### Url predeterminada del api
```sh
127.0.0.1:500
```
#### obtener lista usuarios
```http
  GET /tarjetas
```
| Parametro | Type     |
| :-------- | :------- |
| `id_usuario` | `string` |
| `id_tarjeta` | `string` | 
| `nombre_usuario` | `string` | 
####  registrar acceso de usuarios
```http
  POST /registro_acceso
 ```
 | Parametro | Type     |
| :-------- | :------- |
| `id_usuario` | `string` |
| `fecha_hora` | `datetime` |

## Resultados
A continuación, podra verse una vista previa del sistema, del ensamble del circuito.
 

# Créditos
Desarrollado por:
- [@Victor Galindo](https://www.github.com/biovoid19)
- [@Raul Rodriguez](https://www.github.com/RaulRodriguez050221)
- [@Carlos Flores](https://www.github.com/carlossf12)

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)