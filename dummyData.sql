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
INSERT INTO public.jindicadores(codigoindicador,descripcionindicador,operacion, variables, status, idprinciosubdivision) VALUES
 ('P101','Porcentaje de socios activos', 'División', ARRAY['Número de socios activos', 'Número total de socios'], true, 35),
 ('P102','Porcentaje del valor de certificados de aportación en relación al SBU', 'División', ARRAY['Valor mínimo de aportación dispuesto por la entidad', 'Valor del Salario Básico Unificado'],true, 35),
 ('P103','Porcentaje de socias mujeres', 'División', ARRAY['Número de socias activas mujeres', 'Número total de socios'],true,35),
 ('P104','Porcentaje de socios que residen en áreas rurales', 'División', ARRAY['Número de socios que residen en una zona rural', 'Número total de socios'], true, 35),
 ('P105','Porcentaje de socios pertenecientes a minorías étnicas', 'División', ARRAY['Número de socios que pertenecen a minorías étnicas', 'Número total de socios'],true, 35),
 ('P106','Porcentaje de socios con ingresos menores o iguales al SBU', 'División', ARRAY['Número de socios con ingresos menores o iguales al SBU', 'Número total de socios'], true, 35),
 ('P107','Porcentaje de agencias con acceso a personas con discapacidad', 'División', ARRAY['Número de agencias con accesos para personas con discapacidad', 'Número de agencias registradas de la entidad'],true, 35),
 ('P108','Manuales y procesos adecuados a la inclusión de población vulnerable, aprobados y actualizados.', 'Cumplimiento', ARRAY['¿Tienen manuales aprobados por el CAD y actualizados que beneficien la inclusión financiera de personas vulnerables?'], true, 35),
 ('P109','Porcentaje de socios con ingresos menores o iguales al SBU', 'División',  ARRAY['Número de socios activos que posean carné de discapacidad emitido por la institución competente', 'Número total de socios'],true, 35),
 ('P110', 'Promedio de ahorros', 'División', ARRAY['Saldo elemento 21', 'Número de socios activos al corte'], true, 36),
 ('P111', 'Porcentaje de saldo de cartera de crédito destinado a mujeres', 'División', ARRAY['Saldo de cartera de crédito otorgada a mujeres al corte', 'Saldo cuenta 14-1499'], true, 36),
 ('P112', 'Porcentaje de créditos otorgados por valores inferiores o iguales al SBU', 'División', ARRAY['Número de créditos otorgados por valores inferiores o iguales al SBU en el año', 'Número de créditos vigentes al corte'], true, 36),
 ('P113', 'Porcentaje del saldo de cartera de crédito destinado a personas con residencia rural', 'División', ARRAY['Saldo de crédito otorgado a socios que residen en una zona rural al corte', 'Saldo cuenta 14-1499'], true, 36),
 ('P114', 'Porcentaje de personas con residencia rural que tienen operaciones de crédito', 'División', ARRAY['Número de créditos otorgado a socios que residen en una zona rural al corte', 'Número total de créditos vigentes al corte'], true, 36),
 ('P115', 'Porcentaje de cartera de microcrédito', 'División', ARRAY['Número de créditos vigentes del segmento microcrédito al corte', 'Número total de créditos vigentes al corte'], true, 36),
 ('P116', 'Desembolsos de CDH', 'Igual', ARRAY['Número de desembolsos realizados por concepto de CDH en el año'], true, 36),
 ('P117', 'Pagos de BDH', 'Igual', ARRAY['Número de pagos realizados por concepto de BDH en el año'], true, 36),
 ('P118', 'Monto promedio de créditos asociativos', 'División', ARRAY['Monto otorgado bajo la metodología de créditos asociativos en el año', 'Número de socios que han accedido a montos bajo la metodología de créditos asociativos en el año'], true, 36),
 ('P119', 'Monto promedio de microcrédito', 'División', ARRAY['Saldo cuenta 1404+1412+1420+1428+ 1436+1444+1452+1460+ 1468', 'Número de socios que mantienen créditos vigentes del segmento microcrédito al corte'], true, 36),
 ('P120', 'Porcentaje de menores de edad con cuentas de ahorro', 'División', ARRAY['Número de personas menores de 18 años que disponen a una o más cuentas al corte', 'Número total de socios al corte'], true, 36),
 ('P201', 'Porcentaje de socios o representantes que asisten a Asambleas Generales', 'División', ARRAY['Número de socios o representantes asistentes en el año', 'Número de socios o representantes al corte'], true, 37),
 ('P202', 'Porcentaje de representantes que participan en elecciones (por agencia)', 'División', ARRAY['Número de representantes que asiste a votar en el año', 'Número de representantes por agencia al corte'], true, 37),
 ('P203', 'Porcentaje de socios que participan en elecciones de representantes', 'División', ARRAY['Número de socios que asisten a votar por representantes en el año', 'Número de socios activos al corte'], true, 37),
 ('P204', 'Porcentaje de mujeres en Consejos', 'División', ARRAY['Número de mujeres que son vocales titulares y suplentes al corte', 'Número de vocales titulares y suplentes al corte'], true, 37),
 ('P205', 'Porcentaje de mujeres representantes', 'División', ARRAY['Número de mujeres que son representantes al corte', 'Número de representantes al corte'], true, 37),
 ('P206', 'Porcentaje de vocales procedentes de zonas de influencia', 'División', ARRAY['Número de vocales titulares y suplentes procedentes de zonas de influencia al corte', 'Número de vocales titulares y suplentes al corte'], true, 37),
 ('P207', 'Presencia de jóvenes en órganos de gobierno', 'División', ARRAY['Número de vocales titulares y suplentes menores a 30 años de edad al corte', 'Número de vocales titulares y suplentes al corte'], true, 37),
 ('P208', 'Porcentaje de vocales que pertenecen a minoría étnicas', 'División', ARRAY['Número de vocales titulares y suplentes que pertenecen a minoría étnicas al corte', 'Número de vocales titulares y suplentes al corte'], true, 37),
 ('P209', 'Políticas de inclusión y participación democrática actualizadas', 'Cumplimiento', ARRAY['¿Existe un documento de política de inclusión y participación democrática?'], true, 37),
 ('P210', 'Manuales y procesos adecuados a participación democrática aprobados y actualizados.', 'Cumplimiento', ARRAY['¿Tienen manuales aprobados por el CAD y actualizados que mantengan procesos adecuados de participación democrática?'], true, 37),
 ('P211', 'Porcentaje de socios o representantes asistentes a Asambleas que pertenecen a grupos priorizados', 'División', ARRAY['Número de socios o representantes que asisten a Asambleas y son personas vulnerables en el año', 'Número de socios o representantes al corte'], true, 37),
 ('P301', 'Porcentaje de capital en relación al patrimonio', 'División', ARRAY['Saldo elemento 31', 'Saldo grupo 3'], true, 38),
 ('P302', 'Reservas de cada socio', 'División', ARRAY['Saldo elemento 33', 'Número total de socios al corte'], true, 38),
 ('P303', 'Capital social por socio', 'División', ARRAY['Saldo elemento 31', 'Número total de socios al corte'], true, 38),
 ('P304', 'Fondo irrepartible de reserva legal por socio', 'División', ARRAY['Saldo cuenta 3301', 'Número total de socios al corte'], true, 38),
 ('P305', 'Porcentaje del presupuesto anual destinado a balance social', 'División', ARRAY['Monto destinado para realizar actividades de balance social en el año', 'Monto presupuesto de la entidad en el año'], true, 38),
 ('P306', 'Porcentaje de gastos administrativos en relación al gasto total', 'División', ARRAY['Saldo elemento 45', 'Saldo grupo 4'], true, 38),
 ('P307', 'Promedio de transacciones por periodo', 'División', ARRAY['Número de transacciones por producto', 'Número de socios activos al corte'], true, 38),
 ('P308', 'Promedio de tasas activas y pasivas por rangos de valor', 'Igual', ARRAY['Cálculo de tasas activas y pasivas'], true, 38),
 ('P309', 'Porcentaje de fondeo proveniente de socios en relación al total de fondeo', 'División', ARRAY['Saldo grupo 21', 'Saldo grupos 21 + 26'], true, 38),
 ('P310', 'Porcentaje de pasivos en relación al patrimonio', 'División', ARRAY['Saldo elemento 2', 'Saldo elemento 3'], true, 38),
 ('P311', 'Mantiene actualizada la normativa y procedimientos de prevención de lavado de activos relacionada con la procedencia de fondos', 'Cumplimiento', ARRAY['¿Tiene actualizado y aprobado por el CAD sobre la validación de la procedencia lícita de fondos?'], true, 38),
 ('P312', 'Porcentaje de socios con el mínimo de certificados de aportación', 'División', ARRAY['Número de socios registrados en la entidad con aportes inferiores al mínimo establecido en el Estatuto al corte', 'Número total de socios al corte'], true, 38),
 ('P313', 'Porcentaje de socios con participación superior al 5% del capital social', 'División', ARRAY['Número de socios registrados con participación superior al 5% del capital social al corte', 'Número total de socios al corte'], true, 38),
 ('P401', 'Productos financieros desarrollados por la cooperativa acorde a la misión y principios de la entidad', 'Igual', ARRAY['Número de productos financieros enfocados en la misión y principios desarrollados en el año'], true, 39),
 ('P402', 'Productos financieros desarrollados por la cooperativa para personas vulnerables', 'Igual', ARRAY['Número de productos financieros para personas con vulnerabilidad en el año'], true, 39),
 ('P403', 'Mantiene actualizada las políticas para productos y servicios financieros', 'Cumplimiento', ARRAY['¿Tiene una política aprobada por el CAD y actualizada que contiene el diseño de productos y servicios financieros?'], true, 39),
 ('P404', 'Porcentaje de acceso a productos financieros de socios con residencia rural', 'División', ARRAY['Número de socios que tienen residencia rural y han realizado transacciones en el año', 'Número total de socios que han realizado transacciones en el año'], true, 39),
 ('P405', 'Porcentaje de productos financieros financiados con captaciones de los socios', 'División', ARRAY['Saldo cuenta 21-2102-2104', 'Saldo cuenta 14-1499'], true, 39),
 ('P406', 'Transacciones realizadas por personas vulnerables', 'Igual', ARRAY['Número de transacciones realizadas por personas vulnerables en el año, incluye transacciones de BDH'], true, 39),
 ('P407', 'Operaciones de crédito concedidas a personas vulnerables', 'Igual', ARRAY['Número de créditos desembolsados a personas vulnerables en el año, incluye desembolsos de CDH'], true, 39),
 ('P408', 'Porcentaje de cumplimiento de estrategias levantadas con nivel de riesgo alto y crítico determinado en los Informes de auditoría externa', 'División', ARRAY['Número de estrategias de auditor externo cumplidas con nivel de riesgo alto y crítico en el año', 'Número de estrategias de auditor externo cumplidas más incumplidas con nivel de riesgo alto y crítico en el año'], true, 40),
 ('P409', 'Porcentaje de cumplimiento de las estrategias con nivel de riesgo alto y crítico levantadas en los informes de auditoría interna o por el PCV', 'División', ARRAY['Número de estrategias de auditor interno o PCV cumplidas con nivel de riesgo alto y crítico en el año', 'Número de estrategias de auditor interno o PCV cumplidas más incumplidas con nivel de riesgo alto y crítico en el año'], true, 40),
 ('P410', 'Porcentaje de cumplimiento de actividades del plan de trabajo de auditoría interna o PCV', 'División', ARRAY['Número de actividades del plan de trabajo del auditor interno o PCV cumplidas a tiempo en el año', 'Número total de actividades del plan de trabajo del auditor interno o PCV en el año'], true, 40),
 ('P411', 'Manual y políticas de procesos actualizados y definidos de los responsables de control interno', 'Cumplimiento', ARRAY['¿Tiene manuales o documentos aprobados por el CAD y actualizados en los cuales defina los responsables de control interno?'], true, 40),
 ('P412', 'Políticas y procedimientos para contratación de auditor interno y externo', 'Cumplimiento', ARRAY['¿Tiene políticas y procedimientos aprobados por el CAD y actualizados con respecto a la contratación de auditor interno y externo?'], true, 40),
 ('P413', 'Políticas y procedimientos para elección y designación del consejo de vigilancia', 'Cumplimiento', ARRAY['¿Tiene políticas y procedimiento para la elección y designación del consejo de vigilancia?'], true, 40),
 ('P414', 'Medios de comunicación utilizados por la entidad para dar a conocer las tasas, costos y tarifas', 'Texto', ARRAY['Enlistar los medios de comunicación utilizados para difundir las tasas, costos y tarifas en el año'], true, 41),
 ('P415', 'Porcentaje del presupuesto en materiales para promover la transparencia de la información', 'División', ARRAY['Monto del gasto destinado a materiales visuales (POP, medios visuales, entre otros) en el año', 'Monto presupuesto de la entidad en el año'], true, 41),
 ('P416', 'Reuniones realizadas anualmente por los miembros del CAD', 'Igual', ARRAY['Número de reuniones realizadas por el CAD en el año'], true, 41),
 ('P417', 'Reuniones realizadas anualmente por los miembros del CV', 'Igual', ARRAY['Número de reuniones realizadas por el CV en el año'], true, 41),
 ('P418', 'Asambleas generales realizadas', 'Igual', ARRAY['Número de asambleas generales de socios o representantes realizadas en el año'], true, 41),
 ('P419', 'Porcentaje de socios o representantes que participan en las asambleas generales', 'División', ARRAY['Número de socios o representantes asistentes en el año', 'Número de socios o representantes al corte'], true, 41),
 ('P420', 'Porcentaje de los miembros del CAD que participan en reuniones', 'División', ARRAY['Número de miembros del CAD que participan en reuniones en el año', 'Número de miembros del CAD al corte'], true, 41),
 ('P421', 'Porcentaje de los miembros del CV que participan en reuniones', 'División', ARRAY['Número de miembros del CV que participan en reuniones en el año', 'Número de miembros del CV al corte'], true, 41),
 ('P422', 'Metodología para el cálculo de la tasa de interés efectiva anual', 'Cumplimiento', ARRAY['¿Tiene una metodología para el cálculo de la tasa de interés efectiva anual?'], true, 42),
 ('P423', 'Metodología para determinar la tasa de interés pasiva', 'Cumplimiento', ARRAY['¿Tiene una metodología para determinar la tasa de interés pasiva?'], true, 42),
 ('P424', 'Tarifas de servicios financieros establecidos', 'Cumplimiento', ARRAY['¿Cumple con las tarifas de servicios financieros vigentes establecidos?'], true, 42),
 ('P425', 'Límites de tasas de interés para productos de colocación conforme lo establecido por el Banco Central del Ecuador', 'Cumplimiento', ARRAY['¿Cumple con los límites de tasas de interés para productos de colocación conforme lo establecido por el Banco Central del Ecuador?'], true, 42),
 ('P426', 'Definición y actualización de líneas de negocio', 'Cumplimiento', ARRAY['¿Tiene definidas y actualizadas las líneas de negocio?'], true, 43),
 ('P427', 'Políticas de independencia y segregación de funciones', 'Cumplimiento', ARRAY['¿Actualiza las políticas de independencia y segregación de funciones?'], true, 43),
 ('P428', 'Base de datos de funcionarios de la entidad', 'Cumplimiento', ARRAY['¿Actualiza la base de datos de funcionarios de la entidad?'], true, 43),
 ('P429', 'Acuerdos de confidencialidad con todo el personal de la entidad', 'Cumplimiento', ARRAY['¿Tiene acuerdos de confidencialidad con todo el personal que incluya la protección de información de los socios de la entidad?'], true, 43),
 ('P430', 'Políticas, procesos, procedimientos y metodología para la administración de TI', 'Cumplimiento', ARRAY['¿Actualiza las políticas, procesos, procedimientos y metodología para la administración de TI?'], true, 43),
 ('P431', 'Plan de continuidad de negocio de la entidad', 'Cumplimiento', ARRAY['¿Tiene actualizado el plan de continuidad de negocio de la entidad?'], true, 43),
 ('P501', 'Planificación anual de capacitaciones sobre EPS', 'Cumplimiento',  ARRAY['¿Tiene una planificación anual de programas de capacitación sobre EPS?'], true, 44),
 ('P502', 'Porcentaje de capacitaciones ejecutadas sobre EPS', 'División', ARRAY['Número de capacitaciones planificadas en el año total', 'Número de capacitaciones ejecutadas en el año total'], true, 44),
 ('P503', 'Porcentaje de capacitaciones sobre EPS dirigidas a empleados', 'División', ARRAY['Número de capacitaciones planificadas en el año empleados', 'Número de capacitaciones ejecutadas en el año empleados'], true, 44),
 ('P504', 'Porcentaje de capacitaciones sobre EPS dirigidas a dirigidas a socios o representantes', 'División', ARRAY['Número de capacitaciones planificadas en el año socios o representantes', 'Número de capacitaciones ejecutadas en el año socios o representantes'], true, 44),
 ('P505', 'Porcentaje del presupuesto destinado a capacitaciones sobre EPS', 'División', ARRAY['Monto del presupuesto destinado a capacitaciones en el año', 'Monto presupuesto de la entidad en el año'], true, 44),
 ('P506', 'Porcentaje de cumplimiento presupuestario en capacitaciones sobre EPS', 'División', ARRAY['Monto del gasto utilizado en capacitaciones en el año', 'Monto del presupuesto destinado a capacitación en el año'], true, 44),
 ('P507', 'Porcentaje de representantes capacitados sobre EPS', 'División', ARRAY['Número de representantes capacitados en el año', 'Número de representantes al corte'], true, 44),
 ('P508', 'Porcentaje de empleados capacitados sobre EPS', 'División', ARRAY['Número de empleados capacitados en el año', 'Número total de empleados al corte'], true, 44),
 ('P509', 'Porcentaje de socios capacitados sobre EPS', 'División', ARRAY['Número de socios capacitados en el año', 'Número total de socios al corte'], true, 44),
 ('P510', 'Porcentaje de satisfacción de las capacitaciones realizadas a socios, representantes y empleados', 'Igual', ARRAY['Promedio del porcentaje de satisfacción de las capacitaciones realizadas a socios, representantes y empleados en el año'], true, 44),
 ('P511', 'Planificación anual de programas de capacitación sobre principios y valores', 'Cumplimiento', ARRAY['¿Tiene una planificación anual de programas de capacitación sobre principios y valores?'], true, 45),
 ('P512', 'Porcentajes de socios, representantes y empleados capacitados sobre principios y valores', 'División', ARRAY['Número de socios, representantes y empleados capacitados en el año', 'Número de socios, representantes y empleados al corte'], true, 45),
 ('P513', 'Porcentaje de satisfacción de las capacitaciones realizadas a socios, representantes y empleados', 'Igual', ARRAY['Promedio del porcentaje de satisfacción de las capacitaciones realizadas a socios, representantes y empleados en el año'], true, 45),
 ('P514', 'Planificación anual de programas de formación de futuros representantes', 'Cumplimiento', ARRAY['¿Tiene una planificación anual de programas de formación de futuros representantes?'], true, 46),
 ('P515', 'Porcentaje de socios (futuros representantes) capacitados', 'División', ARRAY['Número de socios capacitados en el año', 'Número total de socios al corte'], true, 46),
 ('P516', 'Porcentaje de socios que pasaron a formar parte de los órganos de gobierno', 'División', ARRAY['Número de socios que pasaron a formar parte de los órganos de gobierno en el año', 'Número de representantes al corte'], true, 46),
 ('P517', 'Planificación anual de programas de capacitación enfocados en la EPS', 'Cumplimiento', ARRAY['¿Tiene una planificación anual de programas de educación financiera enfocada en temas de EPS?'], true, 47),
 ('P518', 'Medios de difusión de productos, servicios y programas sociales', 'Cumplimiento', ARRAY['¿Utiliza medios de comunicación para difundir sus productos, servicios y programas sociales?'], true, 47),
 ('P519', 'Porcentaje del presupuesto asignado y ejecutado en programas sociales', 'División', ARRAY['Monto presupuesto destinado a programas sociales de la entidad en el año', 'Monto presupuesto de la entidad en el año'], true, 47),
 ('P520', 'Planificación anual de programas de capacitación enfocado en educación financiera', 'Cumplimiento', ARRAY['¿Tiene una planificación anual de programas de capacitación enfocado en educación financiera?'], true, 48),
 ('P521', 'Porcentaje de socios capacitados', 'División', ARRAY['Número de socios capacitados en el año', 'Número total de socios al corte'], true, 48),
 ('P522', 'Porcentaje de satisfacción de las capacitaciones realizadas a socios', 'Igual', ARRAY['Promedio del porcentaje de satisfacción de las capacitaciones realizadas a socios'], true, 48),
 ('P523', 'Planificación anual de programas de capacitación sobre temas de interés local o comunitario', 'Cumplimiento', ARRAY['¿Tiene una planificación anual de programas de capacitación sobre temas de interés local o comunitario?'], true, 49),
 ('P524', 'Convenios vigentes con organizaciones externas sobre temas de interés local o comunitario', 'Igual', ARRAY['Número de convenios vigentes con organizaciones externas sobre temas de interés local o comunitario al corte'], true, 49),
 ('P525', 'Capacitación interna sobre temas de interés local o comunitario', 'Cumplimiento', ARRAY['¿Han efectuado eventos de capacitación interna sobre temas de interés local o comunitario?'], true, 49),
 ('P526', 'Porcentaje de proyectos elaborados y ejecutados en temas sociales y medioambientales', 'División', ARRAY['Número de proyectos ejecutados sobre temas sociales y medioambientales', 'Número de proyectos elaborados sobre temas sociales y medioambientales'], true, 50),
 ('P527', 'Productos y servicios desarrollados para el financiamiento de proyectos sociales y medioambientales', 'Cumplimiento', ARRAY['¿Tiene desarrollados productos y servicios dirigidos al financiamiento de proyectos sociales y medioambientales?'], true, 50),
 ('P528', 'Presupuesto para desarrollo de proyectos sociales y medioambientales', 'Cumplimiento', ARRAY['¿Han destinado parte del presupuesto al desarrollo de proyectos sociales y medioambientales?'], true, 50),
 ('P529', 'Porcentaje del presupuesto ejecutado en el desarrollo de proyecto sociales y medioambientales', 'División', ARRAY['Monto de presupuesto ejecutado en el desarrollo de proyectos sociales y medioambientales en el año', 'Total del presupuesto planificado para el desarrollo de proyectos sociales y medioambientales en el año'], true, 50),
 ('P601', 'Convenios de asociación como administrador', 'Igual', ARRAY['Número de convenios vigentes como administrador en el SFPS al corte'], true, 51),
 ('P602', 'Porcentaje de socios capacitados', 'Igual', ARRAY['Número de convenios vigentes como asistida en el SFPS al corte'], true, 51),
 ('P603', 'Convenios de asociación gestionados en el SFPS', 'Igual', ARRAY['Número de convenios de asociación gestionados en el SFPS al corte'], true, 51),
 ('P604', 'Convenios de asociación ejecutados en el SFPS', 'Igual', ARRAY['Número de convenios de asociación ejecutados en el SFPS al corte'], true, 51),
 ('P605', 'Porcentaje de inversiones en entidades del SFPS', 'División', ARRAY['Saldo invertido en entidades del SFPS al corte', 'Saldo elemento 13'], true, 51),
 ('P606', 'Convenios con organizaciones de la EPS', 'Igual', ARRAY['Número de convenios o proyectos contraídos con actores de la EPS en el año'], true, 51),
 ('P607', 'Compra de cartera de entidades del SFPS en liquidación', 'Igual', ARRAY['Monto de cartera adquirida de entidades del SFPS en liquidación en el año'], true, 51),
 ('P608', 'Pasantías realizadas por estudiantes de colegios y universidades', 'Igual', ARRAY['Número de pasantes admitidos en el año'], true, 51),
 ('P609', 'Servicios o productos brindados a entidades del SFPS', 'Igual', ARRAY['Número de servicios o productos brindados a entidades del SFPS en el año'], true, 51),
 ('P610', 'Proveedores de la EPS', 'Igual', ARRAY['Número de proveedores de la EPS contratados en el año'], true, 51),
 ('P611', 'Porcentaje destinado a contratos con proveedores de la EPS', 'División', ARRAY['Monto del gasto por contratos con proveedores de la EPS en el año', 'Saldo elemento 45'], true, 51),
 ('P612', 'Empleados capacitados por organismos de integración', 'Igual', ARRAY['Número de empleados capacitados por organismos de integración en el año'], true, 51),
 ('P613', 'Participación en organismos de integración', 'Igual', ARRAY['Número de organismos de integración a los que pertenece y participa la entidad al corte'], true, 51),
 ('P614', 'Servicios electrónicos disponibles para socios', 'Igual', ARRAY['Número de servicios electrónicos que oferta la entidad al corte'], true, 51),
 ('P615', 'Socios que utilizan canales electrónicos', 'Igual', ARRAY['Número de socios que utilizan servicios electrónicos en el año'], true, 51),
 ('P616', 'Transacciones por canales electrónicos', 'Igual', ARRAY['Número de transacciones realizadas por usuarios a través de canales electrónicos en el año'], true, 51),
 ('P617', 'Visitas a la página web de la entidad', 'Igual', ARRAY['Número de visitas a la página web de la entidad en el año'], true, 51),
 ('P618', 'Medios tecnológicos diseñados para personas vulnerables', 'Cumplimiento', ARRAY['¿Tienen medios tecnológicos diseñados para personas vulnerables?'], true, 51),
 ('P619', 'Variación cartera productivo-comercial', 'División - 1', ARRAY['Saldo cuenta año actual 1405+1413+1421+1429+1437+1445+1453+1461+1469+1401+1406+1409+1414+1417+1422+1425+1430+1433+1438+1441+1446+1449+1454+1457+1462+1465+1470', 'Saldo cuenta año anterior 1405+1413+1421+1429+1437+1445+1453+1461+1469+1401+1406+1409+1414+1417+1422+1425+1430+1433+1438+1441+1446+1449+1454+1457+1462+1465+1470'], true, 52),
 ('P620', 'Variación cartera consumo', 'División - 1', ARRAY['Saldo cuenta año actual 1402+1407+1410+1415+1418+1423+1426+1431+1434+1439+1442+1447+1450+1455+1458+1463+1466+1471', 'Saldo cuenta año anterior1402+1407+1410+1415+1418+1423+1426+1431+1434+1439+1442+1447+1450+1455+1458+1463+1466+1471'], true, 52),
 ('P621', 'Variación cartera educativo', 'División - 1', ARRAY['Saldo cuenta año actual 1473+1475+1477+1479+1481+1483+1485+1487+1489', 'Saldo cuenta año anterior 1473+1475+1477+1479+1481+1483+1485+1487+1489'], true, 52),
 ('P622', 'Variación cartera vivienda de interés público e inmobiliario', 'División - 1', ARRAY['Saldo cuenta año actual 1408+1416+1424+1432+1440+1448+1456+1464+1472', 'Saldo cuenta año anterior 1408+1416+1424+1432+1440+1448+1456+1464+1472'], true, 52),
 ('P623', 'Variación cartera microcrédito', 'División - 1', ARRAY['Saldo cuenta año actual 1404+1412+1420+1428+1436+1444+1452+1460+1468', 'Saldo cuenta año anterior 1404+1412+1420+1428+1436+1444+1452+1460+1468'], true, 52),
 ('P624', 'Corresponsales solidarios', 'Igual', ARRAY['Número de corresponsales solidarios creados en el año'], true, 52),
 ('P625', 'Transacciones realizadas en corresponsales solidarios', 'Igual', ARRAY['Número de transacciones realizadas en corresponsales solidarios en el año'], true, 52),
 ('P626', 'Acuerdo para el desarrollo tecnológico', 'Cumplimiento', ARRAY['¿Tiene un acuerdo para el desarrollo tecnológico (Software o canales electrónicos)?'], true, 52),
 ('P627', 'Transacciones con costo (tarifa máxima)', 'Igual', ARRAY['Número de transacciones realizadas con tarifa máxima en el año'], true, 52),
 ('P628', 'Transacciones con costo (tarifa diferenciada)', 'Igual', ARRAY['Número de transacciones realizadas con tarifa diferenciada en el año'], true, 52),
 ('P629', 'Transacciones con costo (tarifa cero)', 'Igual', ARRAY['Número de transacciones realizadas con tarifa cero en el año'], true, 52),
 ('P630', 'Aperturas de cuentas básicas', 'Igual', ARRAY['Número de cuentas básicas aperturadas en el año'], true, 52),
 ('P631', 'Transacciones con servicios financieros asociados a cuenta básica', 'Igual', ARRAY['Número de transacciones asociadas a cuentas básicas en el año'], true, 52);

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
CREATE OR REPLACE VIEW public.vindicators
AS SELECT ind.idindicador,
    ind.codigoindicador,
    ind.descripcionindicador,
    ind.operacion,
    ind.variables,
    val_d.idvalores AS idvalor_denominador,
    val_d.valor AS valor_denominador,
    val_n.idvalores AS idvalor_numerador,
    val_n.valor AS valor_numerador,
    ind.status,
    obj.idobjectivo,
    obj.meta,
    obj.validezinicio AS objetivo_validezinicio,
    COALESCE(obj.is_applicable, true) AS is_applicable,
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
     LEFT JOIN jprinciossubdivisiones carasub ON carasub.idprinciosubdivision = linsub.fkidprinciosubdivision
     LEFT JOIN jprinciossubdivisiones clasub ON clasub.idprinciosubdivision = carasub.fkidprinciosubdivision
     LEFT JOIN jprincipios prin ON prin.idprincipio = clasub.idprincipio
     LEFT JOIN jvalores val_n ON ind.variables[1]::text = val_n.descripcionvalores::text AND val_n.status = true
     LEFT JOIN jvalores val_d ON ind.variables[2]::text = val_d.descripcionvalores::text AND val_d.status = true
     LEFT JOIN jobjetivos obj ON obj.idindicador = ind.idindicador AND obj.status = true;

-- vobjectivesvalues
CREATE OR REPLACE VIEW public.vobjectivesvalues
AS SELECT objval.idobjetivevalue,
    objval.idobjectivo,
    obj.meta,
    objval.idnumerador,
    val_n.descripcionvalores AS descripcion_numerador,
    val_n.valor AS valor_numerador,
    objval.iddenominador,
    val_d.descripcionvalores AS descripcion_denominador,
    val_d.valor AS valor_denominador,
    objval.idusuario,
    (users.first_name::text || ' '::text) || users.last_name::text AS fullname,
    objval.resultado,
    objval.cumplimiento,
    objval.status,
    objval.fechacreacion,
    objval.fechamodificacion
   FROM jobjetivosvalores objval
     LEFT JOIN jobjetivos obj ON obj.idobjectivo = objval.idobjectivo
     LEFT JOIN jvalores val_n ON val_n.idvalores = objval.idnumerador
     LEFT JOIN jvalores val_d ON val_d.idvalores = objval.iddenominador
     LEFT JOIN jusuarios users ON users.idusuario = objval.idusuario;
