CREATE TABLE general
  (
     id_general         INT (8) NOT NULL,
     cod_localidad      INT (8),
     id_provincia       INT (2),
     id_departamento    INT (6),
     categoria          VARCHAR,
     provincia          VARCHAR,
     localidad          VARCHAR,
     nombre             VARCHAR,
     domicilio          VARCHAR,
     codigpostal        VARCHAR,
     numero_de_telefono INT(16),
     mail               VARCHAR,
     web                VARCHAR,
     fecha_carga        DATE NOT NULL,
     PRIMARY KEY (id_general)
  ) 