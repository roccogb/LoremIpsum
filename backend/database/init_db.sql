-- Crear base de datos
CREATE DATABASE IF NOT EXISTS foodyba_dbb;
USE foodyba_dbb;

-- Tabla: usuario_comercio
CREATE TABLE usuario_comercio (
    id_usr_comercio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100),
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100)
);

-- Tabla: usuario_consumidor
CREATE TABLE usuario_consumidor (
    id_usr INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100),
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100)
    -- Implementar un campo que describa la cantidad de reservas que canceló
);

-- Tabla: comercio
CREATE TABLE comercios (
    id_comercio INT PRIMARY KEY AUTO_INCREMENT,
    id_usr_comercio INT,
    nombre_comercio VARCHAR(100),
    categoria VARCHAR(50),
    tipo_de_cocina VARCHAR(100),
    telefono VARCHAR(20),
    ubicacion VARCHAR(255),
    tiempo_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    pdf_menu_link TEXT,
    calificacion FLOAT,                                                 
    horarios VARCHAR(100),
    -- Implementar un campo de 'tags' puede ser un array
    -- Defino la FK de esta tabla
    FOREIGN KEY (id_usr_comercio) REFERENCES usuario_comercio(id_usr_comercio) ON DELETE CASCADE
    -- La caracteristica 'ON DELETE CASCADE' indica que si se borra el registro 'padre' los 'hijos' se eliminan automaticamente
);

-- Tabla: resenias
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
    telefono VARCHAR(20),
    cant_personas INT,
    fecha_reserva DATETIME,
    solicitud_especial TEXT,
    -- Campo que indica el estado de la reserva
    FOREIGN KEY (id_usr) REFERENCES usuario_consumidor(id_usr) ON DELETE CASCADE,
    FOREIGN KEY (id_comercio) REFERENCES comercios(id_comercio) ON DELETE CASCADE
);
