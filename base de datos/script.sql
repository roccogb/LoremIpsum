CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100),
    mail VARCHAR(100) UNIQUE,
    contraseña VARCHAR(100),
    tipo_de_usuario VARCHAR(50)
);

CREATE TABLE Restaurantes (
    id_restaurante INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    nombre_restaurante VARCHAR(100),
    categoria VARCHAR(50),
    tipo_de_cocina VARCHAR(100),
    telefono VARCHAR(20),
    ubicacion VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Platos (
    id_plato INT PRIMARY KEY AUTO_INCREMENT,
    id_restaurante INT,
    nombre_plato VARCHAR(100),
    info_plato TEXT,
    FOREIGN KEY (id_restaurante) REFERENCES Restaurantes(id_restaurante)
);

CREATE TABLE Calificaciones (
    id_calificacion INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_restaurante INT,
    puntaje INT CHECK (puntaje BETWEEN 1 AND 5),
    comentario TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_restaurante) REFERENCES Restaurantes(id_restaurante)
);
