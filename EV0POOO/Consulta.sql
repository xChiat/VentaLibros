create table LIBRO
(
IDLIBRO int not null auto_increment,
NOMBRELIBRO VARCHAR(50),
PRECIO INT NOT NULL,
STOCK INT NOT NULL,
primary key (IDLIBRO)
);
CREATE TABLE VENTAS
(
NUMVENTA INT NOT NULL AUTO_INCREMENT,
IDLIBRO INT,
LIBRO VARCHAR(50),
CANTIDAD INT NOT NULL,
TOTAL INT NOT NULL,
PRIMARY KEY(NUMVENTA)
);