/* tipoidentificacion */
INSERT INTO jtiposidentificaciones (codigotipoidentificacion, descripciontipoidentificacion, status)
Values('C', 'Cedula', True),
('R', 'Ruc', True),
('P', 'Pasaporte', True),
('F', 'Refugiados', True),
('X', 'Extranjeras',True);

/*genero*/
INSERT INTO jgeneros (codigogenero, descripciongenero, status)
Values( 'M', 'Masculino', True),
('F', 'Femenino', True),
('N', 'No aplica', True);

/*GEOGRAFIA*/
INSERT INTO jgeografia (codigogeografia,nombre,nivel, status)
Values('00','Ecuador',1, True);

INSERT INTO jgeografia (fkidgeografia, codigogeografia,nombre,nivel, status)
Values(1, '01','Azuay',2,True),
(1, '02','Bolivar',2, True),
(1, '03','Cañar',2, True),
(1, '04','Carchi',2, True),
(1, '05','Cotopaxi',2, True),
(1, '06','Chimborazo',2, True),
(1, '07','El Oro',2, True),
(1, '08','Esmeraldas',2, True),
(1, '09','Guayas',2, True),
(1, '10','Imbabura',2, True),
(1, '11','Loja',2, True),
(1, '12','Los Rios',2, True),
(1, '13','Manabi',2, True),
(1, '14','Morona Santiago',2, True),
(1, '15','Napo',2, True),
(1, '16','Pastaza',2, True),
(1, '17','Pichincha',2, True),
(1, '18','Tungurahua',2, True),
(1, '19','Zamora Chinchipe',2, True),
(1, '20','Galapagos',2, True),
(1, '21','Sucumbios',2, True),
(1, '22','Orellana',2, True),
(1, '23','Santo Domingo De Los Tsachilas',2, True),
(1, '24','Santa Elena',2, True);

/*jcorporaciones*/
INSERT INTO jcorporaciones (idgeografia, nombrecorporacion, descripcioncorporacion,
             representantelegal, ruc, direccioncorporacion, telefonocorporacion, status)
VALUES (1, 'PilahuiTio', 'Cooperativa de ahorro y credito', 'Mazabanda',
       '1004145889001', 'Otavalo', '062922066', True);

/*jsucursales*/
INSERT INTO jsucursales (idgeografia,idcorporacion,codigosucursal,nombresucursal,direccionsucursal, telefonosucursal, status)
Values(11,1,'1', 'Agencia Otavalo', 'Otavalo', '123456789', True),
	    (11,1,'2', 'Agencia Ibarra', 'Ibarra', '123456789', True),
	    (11,1,'3', 'Agencia Atuntaqui', 'Atuntaqui', '123456789', True);


/*INSERTAR TABLA DEPARTAMENTOS*/
INSERT INTO jdepartamentos (idsucursal,codigodepartamento, nombredepartamento, status)
Values(1,'00'	, 'Sin Definir', True),
(1,'01', 'Información', True),
(1,'02', 'Caja', True),
(1,'03', 'Inversiones', True),
(1,'04', 'Creditos', True),
(1,'05', 'Call center', True),
(1,'06', 'Secretaria General', True),
(1,'07', 'Legal interno', True);

/*jroles */
INSERT INTO jroles (nombrerol, descripcionrol, status, iddepartamento)
Values('Supervisor', 'Asigna', True, 1),
	    ('Asistente', 'Recibe', True, 1),
	    ('Tecnico', 'Soluciona', True, 1);



/*usuarios*/
INSERT INTO public.jusuarios (username,first_name,last_name,identificacion,ipmodificacion,email,telefono,direccion,"password",is_active,is_staff,is_superuser,date_joined,last_login,ipcreacion,direccionmac,fechamodificacion,idgenero,idrol,idtipoidentificacion) VALUES
	 ('maria','MARIA','ANRANGO','1001881835',NULL,'mariaanrango@gmail.com','062926535','otavalo','pbkdf2_sha256$720000$7LOPipS3LRHGsTEs2j6oY4$fKbkVT88BpTBRonDdtaX6XthQsJGoz7VU6cU71Imv6Q=',true,true,false,'2023-12-15 12:09:49.181918-05',NULL,'186.101.60.82','02:00:14:ac:42:02','2023-12-15 12:09:49.181947-05',NULL,NULL,NULL),
	 ('Carlos','','','',NULL,'carlos@admin.com',NULL,'','pbkdf2_sha256$720000$LXQHPmsvmI8EB3awC9bAhJ$6DHkSm5L2FLKtPS/fFjQEEkVRXGnxYYjLhlNXMKHrLk=',true,true,true,'2023-12-15 10:08:16.847147-05','2023-12-15 12:34:11.878437-05','186.101.60.82','91:37:bd:f4:9d:08','2023-12-15 12:34:11.878821-05',NULL,NULL,NULL),
	 ('six','six','Number','6',NULL,'six@real.com','1','Real Number','pbkdf2_sha256$720000$oVItbLG5zPuH1X0UzOIAU3$GZoce9ENojGzh5oT28K4n+RpwOq+VI0uu4q4i6IWKKA=',true,true,false,'2023-12-15 10:25:56.27937-05',NULL,'186.101.60.82','91:37:bd:f4:9d:08','2023-12-15 10:25:56.27937-05',NULL,NULL,NULL),
	 ('gisselvanessa','gissel','cabas','1716247943',NULL,'gisselvanessaa@gmail.com','1','Real Number','pbkdf2_sha256$720000$oCTYfyaHypUUeIh87ECxx7$V+gQbWxwbkjRAIozr0vx9Wn0jyYao7wB+F8+4M42NhE=',true,true,false,'2023-12-15 11:36:06.870184-05',NULL,'186.101.60.82','02:00:14:ac:42:02','2023-12-15 11:36:06.870237-05',NULL,NULL,NULL),
	 ('gessa','gissel','cabascango','1716247944',NULL,'gisselvanessa@hotmail.com','062926535','otavalo','pbkdf2_sha256$720000$7qhKL2CzN7VFrXeWNYRR0N$K+tcANYXIN3pgoek+PT+O+YxBnprcdlFym1fNgkThtI=',true,true,false,'2023-12-15 11:45:03.526974-05',NULL,'186.101.60.82','02:00:14:ac:42:02','2023-12-15 11:45:03.527006-05',NULL,NULL,NULL);
