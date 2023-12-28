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

-- jprinciossubdivisiones -level one
INSERT INTO public.jprinciossubdivisiones(nivel, descripcion, status, idprincipio) VALUES
(1, 'Inclusión de la población vulnerable a los servicios financieros en la entidad', true, 1),
(1, 'Crecimiento de la entidad en coherencia con el aporte al desarrollo local', true, 1),
(1, 'Control democrático', true, 2),
(1, 'Participación económica', true, 3),
(1, 'Autonomía e independencia', true, 4),
(1, 'Crecimiento de la entidad en coherencia con el aporte al desarrollo local', true, 4),
(1, 'Desarrollo integral persona – entidad', true, 5),
(1, 'Fomento e integración del sector económico popular y solidario', true, 6),
(1, 'Reducción de costos y aumento de productividad', true, 6),
(1, 'Integración estructurada con la comunidad', true, 7),
(1, 'Compromiso con el medio ambiente', true, 7),
(1, 'Acuerdos con el Gobierno', true, 7),
(1, 'Interacción con proveedores', true, 7);


-- jprinciossubdivisiones -level two
INSERT INTO public.jprinciossubdivisiones(nivel, descripcion, status, idprincipio,fkidprinciosubdivision) VALUES
(2, 'Nivel de apertura, no discriminación', true, 1,1),
(2, 'Direccionamiento de productos a zonas rurales y urbanas. Existencia de productos para menores de edad. Cobertura poblacional en relación a la PEA, PIB, NBI, SBU (salario básico unificado). Cobertura física en zonas rurales y urbanas.', true, 1, 2),
(2, 'Nivel de participación de los socios y de capital social. Equidad de género. Representación local. Participación de los socios.', true,2, 3),
(2, 'Reciprocidad y crecimiento sostenido a través de niveles de aprobación debidamente adaptados. Concentración de fuentes de fondeo. Nivel de endeudamiento. Promotores de la economía popular y solidario. Participación de capital social. Capacidad de ahorro.', true,3, 4),
(2, 'Capacidad de creación y adaptación de productos y servicios.', true, 4, 5),
(2, 'Generación de planes de auditoría.', true, 4, 5),
(2, 'Transparencia de la información.', true, 4, 6),
(2, 'Seguridad de la información.', true, 4, 6),
(2, 'Nivel de capacitación a sus socios, representantes a asambleas y juntas de socios, vocales de los consejos, representante legal y empleados.', true,5, 7),
(2, 'Formación en principios y valores.', true,5, 7),
(2, 'Formación de representantes a órganos de gobierno, vocales de los consejos.', true,5, 7),
(2, 'Educación en temas del sector de economía popular y solidaria.', true,5, 7),
(2, 'Educación financiera.', true,5, 7),
(2, 'Capacitación específica: derechos humanos, prácticas anticorrupción, medio ambiente, entre otros.', true,5, 7),
(2, 'Desarrollo de proyectos.', true,5, 7),
(2, 'Aporte al fortalecimiento del sector.', true,6, 8),
(2, 'Economías de escala en beneficio colectivo (entidad y socios).', true,6, 9),
(2, 'Accesibilidad a personas con discapacidad. Satisfacción del cliente y socios. Comercio justo.', true,7, 10),
(2, 'Finanzas verdes. Establecer prácticas ambientales.', true,7, 11),
(2, 'Relacionamiento con el Gobierno local y GAD.', true,7, 12),
(2, 'Relación con los proveedores.', true,7, 13);

-- jprinciossubdivisiones -level three
INSERT INTO public.jprinciossubdivisiones(nivel, descripcion, status, idprincipio, fkidprinciosubdivision) VALUES
(3, 'Permitir que toda persona acceda a los productos y servicios, y ser parte de la entidad de acuerdo con su estatuto y la legislación vigente. Considerar la libre adhesión según el vínculo y naturaleza de su actividad para las entidades cerradas. Considerar como acciones positivas la inclusión de personas o grupos vulnerables.', true, 1, 14),
(3, 'Orientar productos y servicios al crecimiento del sector rural de manera prioritaria y/o urbana, dentro de su zona de influencia, impulsando al desarrollo local y las finanzas populares. Impulsar la creación y el uso de productos y servicios orientados a menores de edad, con el fin de fomentar la apropiación de los socios y la sostenibilidad de la entidad en el tiempo. Enfocar productos y servicios para promover la inclusión de la población vulnerable, con la finalidad de mejorar su situación socioeconómica y de la localidad.', true, 1, 15),
(3, 'Asegurar que todos los socios activos tengan derecho a participar en asambleas y órganos de gobierno y que cumplan con el mínimo requerido en certificados de aportación. Promover la participación igualitaria y equitativa de género en asambleas y órganos de gobierno. Promover la participación de acuerdo con las zonas de influencia de la entidad para los procesos eleccionarios.', true, 2, 16),
(3, 'Incluir niveles de aprobación adecuados dentro de los manuales y políticas internas para los productos y servicios, los mismos que faciliten la inclusión de la población vulnerable. Priorizar que las principales fuentes de fondeo provengan de los socios y entidades del sector económico popular y solidario. Mantener niveles de endeudamiento que no comprometan las decisiones de la entidad, así como garantizar la licitud de la procedencia de los fondos.', true, 3, 17),
(3, 'Desarrollar productos y servicios, con la finalidad de promover la inclusión e igualdad de personas, priorizando a aquellas en estado de vulnerabilidad. ', true, 4, 18),
(3, 'Generar y ejecutar planes de auditoría (Consejo de Vigilancia, auditor interno o externo) para garantizar buenas prácticas de control interno. ', true, 4, 19),
(3, 'Comunicar la información relevante de la entidad según su alcance y naturaleza.', true, 4, 19),
(3, 'Cumplir los límites de tasas, cargos, comisiones y tarifas de los productos y servicios financieros. ', true, 4, 20),
(3, 'Determinar la existencia de procesos y políticas que garanticen la seguridad de la información.', true, 4, 21),
(3, 'Generar y ejecutar planes de capacitación enfocados a la educación en temas de economía popular y solidaria y prácticas de buen gobierno. ', true, 5, 22),
(3, 'Generar y ejecutar planes de capacitación y concientización de principios y valores direccionado a empleados y socios. Crear y ejecutar procesos de formación de futuros representantes a órganos de gobierno, vocales de consejos. Crear, socializar y difundir el mensaje institucional y del sector de la economía popular y solidaria, así como los planes de difusión.', true, 5, 23),
(3, 'Crear y ejecutar procesos de formación de futuros representantes a órganos de gobierno, vocales de consejos.', true, 5, 24),
(3, 'Crear, socializar y difundir  el mensaje institucional y del sector de la economía popular y solidaria, así como los planes de difusión', true, 5, 25),
(3, 'Establecer programas de educación financiera a los socios, clientes y otras personas involucradas. ', true, 5, 26),
(3, 'Generar espacios de capacitación identificando temas de interés de la localidad y zonas de influencia, a través de talleres, conferencias, entre otros. ', true, 5, 27),
(3, 'Potenciar el desarrollo local y de sus zonas de influencia mediante el impulso de proyectos sociales y ambientales.', true, 5, 28),
(3, 'Promover acuerdos o convenios de cooperación e integración con los participantes del sector de la economía popular y solidaria. Priorizar el consumo entre los actores del sector de la economía popular y solidaria. Promover acuerdos o convenios que le permitan a la entidad participar activamente en organismos de integración y similares. Generar y mantener proyectos y convenios interinstitucionales en aspectos económicos, sociales y ambientales, con los actores del sector de la economía popular y solidaria. Fomentar el intercambio y generación conjunta del conocimiento. Impulsar el desarrollo tecnológico en beneficio de los socios.', true, 6, 29),
(3, 'Establecer acuerdos o convenios interinstitucionales con la finalidad de generar economías de escala.', true, 6, 30),
(3, 'Garantizar la atención a personas con discapacidad, de manera que puedan acceder a todos los productos y servicios de la entidad. Aplicar instrumentos de medición en lo referente a satisfacción de productos y servicios de la entidad, enfocadas a mejorar su calidad. Mantener políticas de comercio justo con la finalidad de generar diálogo, transparencia, respeto y equidad priorizando a los actores de la economía popular y solidaria.', true, 7, 31),
(3, 'Establecer productos y servicios enfocados en proyectos de carácter ecológico. Fomentar la participación e involucramiento de la comunidad, con el fin de impulsar proyectos de desarrollo ecológico local. Desarrollar y aplicar buenas prácticas ambientales internas y externas.', true, 7, 32),
(3, 'Promover alianzas y convenios con gobiernos locales y GAD, en beneficio del desarrollo local y de la sostenibilidad interinstitucional. ', true, 7, 33),
(3, 'Establecer políticas que prioricen a los proveedores de la localidad y de sus zonas de influencia, tomando en cuenta las prácticas de comercio justo.', true, 7, 34);

-- jindicadores
INSERT INTO public.jindicadores(codigoindicador,descripcionindicador,operacion, status, idprinciosubdivision) VALUES
 ('P101','Porcentaje de socios activos', 'División', true, 35),
 ('P102','Porcentaje del valor de certificados de aportación en relación al SBU', 'División', true, 35),
 ('P103','Porcentaje de socias mujeres', 'División', true, 35),
 ('P104','Porcentaje de socios que residen en áreas rurales', 'División', true, 35),
 ('P105','Porcentaje de socios pertenecientes a minorías étnicas', 'División', true, 35),
 ('P106','Porcentaje de socios con ingresos menores o iguales al SBU', 'División', true, 35),
 ('P107','Porcentaje de agencias con acceso a personas con discapacidad', 'División',true, 35),
 ('P108','Manuales y procesos adecuados a la inclusión de población vulnerable, aprobados y actualizados.', 'Cumplimiento', true, 35),
 ('P109','Porcentaje de socios con ingresos menores o iguales al SBU', 'División', true, 35);

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

-- vindicators
CREATE VIEW vindicators AS
SELECT
    ind.idindicador,
    ind.codigoindicador,
    ind.descripcionindicador,
    ind.operacion,
    ind.status,
    ind.fechacreacion,
    ind.fechamodificacion,
    ind.validezinicio,
    ind.validezfin,
    linsub.idprinciosubdivision AS idlineamiento,
	linsub.descripcion AS descripcionlineamiento,
    carasub.idprinciosubdivision AS idcaracteristica,
	carasub.descripcion AS descripcioncaracteristica,
	clasub.idprinciosubdivision AS idclasificacion,
    clasub.descripcion AS descripcionclasificacion,
    prin.idprincipio,
    prin.codigoprincipio,
    prin.descripcionprincipio
FROM jindicadores ind
LEFT JOIN jprinciossubdivisiones linsub ON linsub.idprinciosubdivision = ind.idprinciosubdivision
LEFT JOIN jprinciossubdivisiones carasub ON carasub.fkidprinciosubdivision = linsub.idprinciosubdivision
LEFT JOIN jprinciossubdivisiones clasub ON clasub.fkidprinciosubdivision = carasub.idprinciosubdivision
LEFT JOIN jprincipios prin ON prin.idprincipio = clasub.idprincipio;
