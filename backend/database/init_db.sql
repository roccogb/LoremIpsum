-- Crear base de datos
CREATE DATABASE IF NOT EXISTS sistema_reservas;
USE sistema_reservas;

-- Tabla: usuario_comercio
CREATE TABLE usuario_comercio (
    id_usr_comercio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100),
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100)
);

-- Tabla: usuario_final
CREATE TABLE usuario_final (
    id_usr INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100),
    email_usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100)
);

-- Tabla: restaurantes
CREATE TABLE restaurantes (
    id_restaurante INT PRIMARY KEY AUTO_INCREMENT,
    id_usr_comercio INT,
    nombre_restaurante VARCHAR(100),
    categoria VARCHAR(50),
    tipo_de_cocina VARCHAR(100),
    telefono VARCHAR(20),
    ubicacion VARCHAR(255),
    tiempo_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    pdf_menu_link TEXT,
    FOREIGN KEY (id_usr_comercio) REFERENCES usuario_comercio(id_usr_comercio)
);

-- Tabla: calificaciones
CREATE TABLE calificaciones (
    id_restaurante INT,
    id_usr INT,
    comentario TEXT,
    calificacion INT CHECK (calificacion BETWEEN 1 AND 5),
    tiempo_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_restaurante, id_usr),
    FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id_restaurante),
    FOREIGN KEY (id_usr) REFERENCES usuario_final(id_usr)
);

-- Tabla: reservas
CREATE TABLE reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_usr INT,
    id_restaurante INT,
    nombre_bajo_reserva VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    cant_personas INT,
    fecha_reserva DATETIME,
    solicitud_especial TEXT,
    FOREIGN KEY (id_usr) REFERENCES usuario_final(id_usr),
    FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id_restaurante)
);
