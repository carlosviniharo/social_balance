/* tipoidentificacion */
INSERT INTO
  jtiposidentificaciones (
    codigotipoidentificacion,
    descripciontipoidentificacion,
    status
  )
Values
  ('C', 'Cedula', True),
  ('R', 'Ruc', True),
  ('P', 'Pasaporte', True),
  ('F', 'Refugiados', True),
  ('X', 'Extranjeras', True);

/*genero*/
INSERT INTO
  jgeneros (codigogenero, descripciongenero, status)
Values
  ('M', 'Masculino', True),
  ('F', 'Femenino', True),
  ('N', 'No aplica', True);

/*GEOGRAFIA*/
INSERT INTO
  jgeografia (codigogeografia, nombre, nivel, status)
Values
  ('00', 'Ecuador', 1, True);

INSERT INTO
  jgeografia (
    fkidgeografia,
    codigogeografia,
    nombre,
    nivel,
    status
  )
Values
  (1, '01', 'Azuay', 2, True),
  (1, '02', 'Bolivar', 2, True),
  (1, '03', 'Cañar', 2, True),
  (1, '04', 'Carchi', 2, True),
  (1, '05', 'Cotopaxi', 2, True),
  (1, '06', 'Chimborazo', 2, True),
  (1, '07', 'El Oro', 2, True),
  (1, '08', 'Esmeraldas', 2, True),
  (1, '09', 'Guayas', 2, True),
  (1, '10', 'Imbabura', 2, True),
  (1, '11', 'Loja', 2, True),
  (1, '12', 'Los Rios', 2, True),
  (1, '13', 'Manabi', 2, True),
  (1, '14', 'Morona Santiago', 2, True),
  (1, '15', 'Napo', 2, True),
  (1, '16', 'Pastaza', 2, True),
  (1, '17', 'Pichincha', 2, True),
  (1, '18', 'Tungurahua', 2, True),
  (1, '19', 'Zamora Chinchipe', 2, True),
  (1, '20', 'Galapagos', 2, True),
  (1, '21', 'Sucumbios', 2, True),
  (1, '22', 'Orellana', 2, True),
  (
    1,
    '23',
    'Santo Domingo De Los Tsachilas',
    2,
    True
  ),
  (1, '24', 'Santa Elena', 2, True);

/*jcorporaciones*/
INSERT INTO
  jcorporaciones (
    idgeografia,
    nombrecorporacion,
    descripcioncorporacion,
    representantelegal,
    ruc,
    direccioncorporacion,
    telefonocorporacion,
    status
  )
VALUES
  (
    1,
    'PilahuiTio',
    'Cooperativa de ahorro y credito',
    'Mazabanda',
    '1004145889001',
    'Otavalo',
    '062922066',
    True
  );

/*jsucursales*/
INSERT INTO
  jsucursales (
    idgeografia,
    idcorporacion,
    codigosucursal,
    nombresucursal,
    direccionsucursal,
    telefonosucursal,
    status
  )
Values
  (
    11,
    1,
    '1',
    'Agencia Otavalo',
    'Otavalo',
    '123456789',
    True
  ),
  (
    11,
    1,
    '2',
    'Agencia Ibarra',
    'Ibarra',
    '123456789',
    True
  ),
  (
    11,
    1,
    '3',
    'Agencia Atuntaqui',
    'Atuntaqui',
    '123456789',
    True
  );

/*INSERTAR TABLA DEPARTAMENTOS*/
INSERT INTO
  jdepartamentos (
    idsucursal,
    codigodepartamento,
    nombredepartamento,
    status
  )
Values
  (1, '00', 'Sin Definir', True),
  (1, '01', 'Información', True),
  (1, '02', 'Caja', True),
  (1, '03', 'Inversiones', True),
  (1, '04', 'Creditos', True),
  (1, '05', 'Call center', True),
  (1, '06', 'Secretaria General', True),
  (1, '07', 'Legal interno', True);

/*jpaginas */
INSERT INTO public.jpaginas (codigopagina,descripcionpagina,status) VALUES
	 ('profile','Ingreso al perfil de usuario',true),
	 ('geography','Admin->Geografia: Acceso al modulo de Geografia',true),
	 ('corporation','Admin->Corporacion: Acceso al modulo de Corporacion',true),
	 ('privileges','Admin->Roles y Privilegios: Acceso a generar roles y otorgar Provilegios en el sistema',true),
	 ('department','Admin->Departamentos: Acceso al modulo de departamentos',true),
	 ('person','Admin->Personas: Acceso al modulo de Personas',true);

/*usuarios*/
INSERT INTO
  jusuarios (
    username,
    first_name,
    last_name,
    identificacion,
    ipmodificacion,
    email,
    telefono,
    direccion,
    "password",
    is_active,
    is_staff,
    is_superuser,
    date_joined,
    last_login,
    ipcreacion,
    direccionmac,
    fechamodificacion,
    idgenero,
    idrol,
    idtipoidentificacion
  )
VALUES
  (
    'maria',
    'MARIA',
    'ANRANGO',
    '1001881835',
    NULL,
    'mariaanrango@gmail.com',
    '062926535',
    'otavalo',
    'pbkdf2_sha256$720000$7LOPipS3LRHGsTEs2j6oY4$fKbkVT88BpTBRonDdtaX6XthQsJGoz7VU6cU71Imv6Q=',
    true,
    true,
    false,
    '2023-12-15 12:09:49.181918-05',
    NULL,
    '186.101.60.82',
    '02:00:14:ac:42:02',
    '2023-12-15 12:09:49.181947-05',
    NULL,
    NULL,
    NULL
  ),
  (
    'Carlos',
    '',
    '',
    '',
    NULL,
    'carlos@admin.com',
    NULL,
    '',
    'pbkdf2_sha256$720000$LXQHPmsvmI8EB3awC9bAhJ$6DHkSm5L2FLKtPS/fFjQEEkVRXGnxYYjLhlNXMKHrLk=',
    true,
    true,
    true,
    '2023-12-15 10:08:16.847147-05',
    '2023-12-15 12:34:11.878437-05',
    '186.101.60.82',
    '91:37:bd:f4:9d:08',
    '2023-12-15 12:34:11.878821-05',
    NULL,
    NULL,
    NULL
  ),
  (
    'six',
    'six',
    'Number',
    '6',
    NULL,
    'six@real.com',
    '1',
    'Real Number',
    'pbkdf2_sha256$720000$oVItbLG5zPuH1X0UzOIAU3$GZoce9ENojGzh5oT28K4n+RpwOq+VI0uu4q4i6IWKKA=',
    true,
    true,
    false,
    '2023-12-15 10:25:56.27937-05',
    NULL,
    '186.101.60.82',
    '91:37:bd:f4:9d:08',
    '2023-12-15 10:25:56.27937-05',
    NULL,
    NULL,
    NULL
  ),
  (
    'gisselvanessa',
    'gissel',
    'cabas',
    '1716247943',
    NULL,
    'gisselvanessaa@gmail.com',
    '1',
    'Real Number',
    'pbkdf2_sha256$720000$oCTYfyaHypUUeIh87ECxx7$V+gQbWxwbkjRAIozr0vx9Wn0jyYao7wB+F8+4M42NhE=',
    true,
    true,
    false,
    '2023-12-15 11:36:06.870184-05',
    NULL,
    '186.101.60.82',
    '02:00:14:ac:42:02',
    '2023-12-15 11:36:06.870237-05',
    NULL,
    NULL,
    NULL
  ),
  (
    'gessa',
    'gissel',
    'cabascango',
    '1716247944',
    NULL,
    'gisselvanessa@hotmail.com',
    '062926535',
    'otavalo',
    'pbkdf2_sha256$720000$7qhKL2CzN7VFrXeWNYRR0N$K+tcANYXIN3pgoek+PT+O+YxBnprcdlFym1fNgkThtI=',
    true,
    true,
    false,
    '2023-12-15 11:45:03.526974-05',
    NULL,
    '186.101.60.82',
    '02:00:14:ac:42:02',
    '2023-12-15 11:45:03.527006-05',
    NULL,
    NULL,
    NULL
  );
 -- Jprincipios
INSERT INTO public.jprincipios(codigoprincipio,descripcionprincipio,status) VALUES
    ('Principio 1','Adhesión libre y voluntaria', true),
    ('Principio 2','Control democrático', true),
    ('Principio 3','Participación económica', true),
    ('Principio 4','Autonomía e independencia', true),
    ('Principio 5','Educación, capacitación e información', true),
    ('Principio 6','Cooperación e integración del sector económico popular y solidario', true),
    ('Principio 7','Compromiso con la comunidad', true);

-- jprinciosclasificaciones
INSERT INTO public.jprinciosclasificaciones(clasificacion, idprincipio, status) VALUES
('Inclusión de la población vulnerable a los servicios financieros en la entidad', 1, true),
('Crecimiento de la entidad en coherencia con el aporte al desarrollo local', 1, true),
('Control democrático', 2, true),
('Participación económica', 3, true),
('Autonomía e independencia', 4, true),
('Crecimiento de la entidad en coherencia con el aporte al desarrollo local', 4, true),
('Desarrollo integral persona – entidad', 5, true),
('Fomento e integración del sector económico popular y solidario', 6, true),
('Reducción de costos y aumento de productividad', 6, true),
('Integración estructurada con la comunidad', 7, true),
('Compromiso con el medio ambiente', 7, true),
('Acuerdos con el Gobierno', 7, true),
('Interacción con proveedores', 7, true);


-- jindicadores
INSERT INTO public.jindicadores(codigoindicador,descriptionindicator,operacion, status, idprincioclasificacione) VALUES
	 ('P101','Porcentaje de socios activos', 'División', true, 1),
	 ('P102','Porcentaje del valor de certificados de aportación en relación al SBU', 'División', true, 1),
	 ('P103','Porcentaje de socias mujeres', 'División', true, 1),
	 ('P104','Porcentaje de socios que residen en áreas rurales', 'División', true, 1),
	 ('P105','Porcentaje de socios pertenecientes a minorías étnicas', 'División', true, 1),
	 ('P106','Porcentaje de socios con ingresos menores o iguales al SBU', 'División', true, 1),
	 ('P107','Porcentaje de agencias con acceso a personas con discapacidad', 'División',true, 1),
	 ('P108','Manuales y procesos adecuados a la inclusión de población vulnerable, aprobados y actualizados.', 'Cumplimiento', true, 1),
	 ('P109','Porcentaje de socios con ingresos menores o iguales al SBU', 'División', true, 1);

--view vusers
CREATE VIEW vusers AS
 SELECT
    users.idusuario,
    users.idrol,
    rol.nombrerol,
    users.idgenero,
    gen.descripciongenero AS genero,
    users.idtipoidentificacion,
    ide.descripciontipoidentificacion AS tipoidentificacion,
    users.identificacion,
    users.email,
    users.telefono,
    users.celular,
    users.direccion,
    users.password,
    users.is_active,
    users.first_name,
    users.last_name,
    users.username,
    users.date_joined AS fechacreacion,
    users.fechamodificacion,
    rol.iddepartamento,
    dep.nombredepartamento,
    dep.idsucursal,
    sucr.nombresucursal,
    sucr.idcorporacion,
    corp.nombrecorporacion
   FROM jusuarios users
     LEFT JOIN jroles rol ON rol.idrol = users.idrol
     LEFT JOIN jdepartamentos dep ON dep.iddepartamento = rol.iddepartamento
     LEFT JOIN jsucursales sucr ON sucr.idsucursal = dep.idsucursal
     LEFT JOIN jcorporaciones corp ON corp.idcorporacion = sucr.idcorporacion
     LEFT JOIN jgeneros gen ON gen.idgenero = users.idgenero
     LEFT JOIN jtiposidentificaciones ide ON ide.idtipoidentificacion = users.idtipoidentificacion;

--view vgeography

CREATE VIEW vgeography AS
SELECT
  geo.idgeografia,
  geo.codigogeografia,
  geo.nombre,
  geo.nivel,
  geo.status,
  geo.fechacreacion,
  geo.fechamodificacion,
  geo.ipcreacion,
  geo.fkidgeografia,
  frk.nombre AS belong_name
FROM
  jgeografia geo
  LEFT JOIN jgeografia frk ON frk.idgeografia = geo.fkidgeografia;

  --view vcorporations

CREATE VIEW vcorporations AS
SELECT
  corp.idcorporacion,
  corp.idgeografia,
  geo.nombre AS belong_name,
  corp.nombrecorporacion,
  corp.descripcioncorporacion,
  corp.representantelegal,
  corp.ruc,
  corp.direccioncorporacion,
  corp.telefonocorporacion,
  corp.status,
  corp.fechacreacion,
  corp.fechamodificacion,
  corp.ipcreacion
FROM
  jcorporaciones corp
  LEFT JOIN jgeografia geo ON geo.idgeografia = corp.idgeografia;

  --view vbranches

CREATE VIEW vbranches AS
SELECT
  suc.idsucursal,
  suc.idgeografia,
  geo.nombre AS belong_name,
  suc.idcorporacion,
  corp.nombrecorporacion,
  suc.codigosucursal,
  suc.nombresucursal,
  suc.descripcionsucursal,
  suc.direccionsucursal,
  suc.telefonosucursal,
  suc.status,
  suc.fechacreacion,
  suc.fechamodificacion,
  suc.ipcreacion
FROM
  jsucursales suc
  LEFT JOIN jgeografia geo ON geo.idgeografia = suc.idgeografia
  LEFT JOIN jcorporaciones corp ON corp.idcorporacion = suc.idcorporacion;

--view vdepartments

CREATE VIEW vdepartments AS
 SELECT dep.iddepartamento,
    suc.idgeografia,
    geo.nombre AS belong_name,
    suc.idcorporacion,
    corp.nombrecorporacion,
    dep.idsucursal,
    suc.nombresucursal,
    dep.codigodepartamento,
    dep.nombredepartamento,
    dep.status,
    dep.fechacreacion,
    dep.fechamodificacion,
    dep.ipcreacion
   FROM jdepartamentos dep
     LEFT JOIN jsucursales suc ON suc.idsucursal = dep.idsucursal
     LEFT JOIN jcorporaciones corp ON corp.idcorporacion = suc.idcorporacion
     LEFT JOIN jgeografia geo ON geo.idgeografia = suc.idgeografia;

--view vroles

CREATE VIEW vroles AS
 SELECT rol.idrol,
    rol.nombrerol,
    rol.descripcionrol,
    rol.status,
    rol.fechacreacion,
    rol.fechamodificacion,
    rol.ipcreacion,
    rol.iddepartamento,
    dep.nombredepartamento,
    dep.idsucursal,
    suc.nombresucursal,
    suc.idcorporacion,
    corp.nombrecorporacion,
    suc.idgeografia,
    geo.nombre AS belong_name
   FROM jroles rol
     LEFT JOIN jdepartamentos dep ON dep.iddepartamento = rol.iddepartamento
     LEFT JOIN jsucursales suc ON suc.idsucursal = dep.idsucursal
     LEFT JOIN jcorporaciones corp ON corp.idcorporacion = suc.idcorporacion
     LEFT JOIN jgeografia geo ON geo.idgeografia = suc.idgeografia;

 --view vprivileges

CREATE VIEW vprivileges AS
SELECT priv.idprivilegio,
    priv.status,
    rol.idrol,
    rol.nombrerol,
    page.idpagina,
    page.codigopagina,
    page.descripcionpagina
   FROM jprivilegios priv
     LEFT JOIN jroles rol ON rol.idrol = priv.idrol
     LEFT JOIN jpaginas page ON page.idpagina = priv.idpagina;