-- Crear base de datos
CREATE DATABASE IF NOT EXISTS foodyba_dbb;
USE foodyba_dbb;

-- Cuando se registre un usuario del tipo comercio se van a completar datos en la tabla 'usuario_comercio' y 'comercios'

-- Tabla: usuario_comercio
CREATE TABLE usuario_comercio (
    id_usr_comercio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_apellido VARCHAR(100),
    DNI BIGINT UNIQUE,                          
    CUIT BIGINT UNIQUE,
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100)
);

-- Tabla: usuario_consumidor
CREATE TABLE usuario_consumidor (
    id_usr INT PRIMARY KEY AUTO_INCREMENT,
    nombre_apellido VARCHAR(100),                       
    usuario VARCHAR(100) UNIQUE,
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100),
    numero_telefono BIGINT UNIQUE,
    cant_reservas_canceladas INT DEFAULT 0
);

-- Tabla: comercio
CREATE TABLE comercios (
    id_comercio INT PRIMARY KEY AUTO_INCREMENT,
    id_usr_comercio INT,
    ruta_imagen VARCHAR(100), 
    nombre_comercio VARCHAR(100),
    categoria VARCHAR(50),
    tipo_cocina VARCHAR(100),
    telefono BIGINT UNIQUE,
    latitud FLOAT,                      -- (UBICACIÓN)Coordenada X
    longitud FLOAT,                     -- (UBICACIÓN)Coordenada Y
    tiempo_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    pdf_menu_link TEXT,
    calificacion FLOAT DEFAULT 0.0,     -- Esto se va completar por un promedio
    dias TEXT,                          -- El formato va a ser -> Ej='[lunes,miercoles,sabado,....]'
    horarios TEXT,                      -- El formato va a ser -> Ej='[7-11,12-15,...]'
    etiquetas TEXT,                     -- El formato va a ser -> Ej='[apto_mascotas,delivery,...]'
    -- Defino la FK de esta tabla
    FOREIGN KEY (id_usr_comercio) REFERENCES usuario_comercio(id_usr_comercio) ON DELETE CASCADE
    -- La caracteristica 'ON DELETE CASCADE' indica que si se borra el registro 'padre' los 'hijos' se eliminan automaticamente
);

-- Tabla: reseñas
CREATE TABLE resenias (
    id_comercio INT,
    id_usr INT,
    comentario TEXT,
    calificacion INT CHECK (calificacion BETWEEN 1 AND 5),
    tiempo_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_comercio) REFERENCES comercios(id_comercio) ON DELETE CASCADE,
    FOREIGN KEY (id_usr) REFERENCES usuario_consumidor(id_usr) ON DELETE CASCADE
);

-- Tabla: reservas
CREATE TABLE reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_usr INT,
    id_comercio INT,
    nombre_bajo_reserva VARCHAR(100),
    email VARCHAR(100),
    telefono BIGINT,
    cant_personas INT,
    fecha_reserva DATETIME,
    solicitud_especial TEXT,
    estado_reserva BOOLEAN,             -- El estado de esta columna va a depender si el consumidor escanea un QR brindado por el comercio
    FOREIGN KEY (id_usr) REFERENCES usuario_consumidor(id_usr) ON DELETE CASCADE,
    FOREIGN KEY (id_comercio) REFERENCES comercios(id_comercio) ON DELETE CASCADE
);
