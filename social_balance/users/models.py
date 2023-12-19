from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from .utils.helper import get_public_ip_address, get_mac_address

# dic_group_permissions = {
#     1: Group.objects.get(name='Supervisors'),
#     2: Group.objects.get(name='Usuario')
# }


class Jcorporaciones(models.Model):
    idcorporacion = models.AutoField(primary_key=True)
    idgeografia = models.ForeignKey(
        "Jgeografia", models.DO_NOTHING, db_column="idgeografia", blank=True, null=True
    )
    nombrecorporacion = models.CharField(max_length=200)
    descripcioncorporacion = models.CharField(max_length=500, blank=True, null=True)
    representantelegal = models.CharField(max_length=200)
    ruc = models.CharField(max_length=14)
    direccioncorporacion = models.CharField(max_length=200, blank=True, null=True)
    telefonocorporacion = models.CharField(blank=True, null=True)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address, null=True)
    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "jcorporaciones"

    objects = models.Manager()

    def __str__(self):
        return self.nombrecorporacion


class Jdepartamentos(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    idsucursal = models.ForeignKey(
        "Jsucursales", models.DO_NOTHING, db_column="idsucursal",
    )
    codigodepartamento = models.CharField(max_length=2, blank=True, null=True)
    nombredepartamento = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    descripciondepartamento = models.CharField(max_length=500, blank=True, null=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address, null=True)
    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "jdepartamentos"

    objects = models.Manager()

    def __str__(self):
        return self.nombredepartamento


class Jgeneros(models.Model):
    idgenero = models.AutoField(primary_key=True)
    codigogenero = models.CharField(max_length=2, blank=True, null=True)
    descripciongenero = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "jgeneros"

    objects = models.Manager()

    def __str__(self):
        return self.descripciongenero


class Jgeografia(models.Model):
    idgeografia = models.AutoField(primary_key=True)
    fkidgeografia = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="fkidgeografia", blank=True, null=True
    )
    codigogeografia = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    nivel = models.BigIntegerField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address, null=True
    )
    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "jgeografia"

    objects = models.Manager()

    def __str__(self):
        return self.nombre


class Jroles(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=100)
    descripcionrol = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address, null=True
    )
    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)
    iddepartamento = models.ForeignKey(
        Jdepartamentos, models.DO_NOTHING, db_column="iddepartamento"
    )
    
    class Meta:
        db_table = "jroles"

    objects = models.Manager()

    def __str__(self):
        return self.nombrerol


class Jsucursales(models.Model):
    idsucursal = models.AutoField(primary_key=True)
    idgeografia = models.ForeignKey(
        Jgeografia, models.DO_NOTHING, db_column="idgeografia",
    )
    idcorporacion = models.ForeignKey(
        Jcorporaciones,
        models.DO_NOTHING,
        db_column="idcorporacion"
    )
    codigosucursal = models.CharField(max_length=2, blank=True, null=True)
    nombresucursal = models.CharField(max_length=200)
    descripcionsucursal = models.CharField(max_length=500, blank=True, null=True)
    direccionsucursal = models.CharField(max_length=200)
    telefonosucursal = models.CharField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address, null=True
    )
    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = "jsucursales"

    objects = models.Manager()

    def __str__(self):
        return self.nombresucursal


class Jtiposidentificaciones(models.Model):
    idtipoidentificacion = models.AutoField(primary_key=True)
    codigotipoidentificacion = models.CharField(max_length=2, blank=True, null=True)
    descripciontipoidentificacion = models.CharField(
        max_length=50, blank=True, null=True
    )
    status = models.BooleanField(default=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "jtiposidentificaciones"

    objects = models.Manager()

    def __str__(self):
        return self.descripciontipoidentificacion


class Jpaginas(models.Model):
    idpagina = models.AutoField(primary_key=True)
    codigopagina = models.CharField(max_length=50, blank=True, null=True)
    descripcionpagina = models.CharField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "jpaginas"

    objects = models.Manager()

    def __str__(self):
        return self.codigopagina


class Jprivilegios(models.Model):
    idprivilegio = models.AutoField(primary_key=True)
    idrol = models.ForeignKey(
        Jroles, models.DO_NOTHING, db_column="idrol", blank=True, null=True
    )
    idpagina = models.ForeignKey(
        Jpaginas, models.DO_NOTHING, db_column="idpagina", blank=True, null=True
    )
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "jprivilegios"

    objects = models.Manager()

    def __str__(self):
        return f"{self.idrol} - {self.idpagina}"


class JusuariosManager(BaseUserManager):
    use_in_migration = True
    
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        # user.groups.add(dic_group_permissions.get(user.idrol.idrol, 2))
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # extra_fields.setdefault("idrol", 1)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")
        # if extra_fields.get("idrol") != 1:
        #     raise ValueError("Superuser must have idrol == 1")

        # idrol = extra_fields.pop("idrol", None)
        #
        # if idrol is None:
        #     raise ValueError("The idrol argument is required to create a superuser.")
        #
        # try:
        #     jroles_instance = Jroles.objects.get(pk=idrol)
        #
        # except ObjectDoesNotExist as exc:
        #     raise ValueError(f"Invalid idrol {idrol} instance does not exist.") from exc
        #
        # extra_fields["idrol"] = jroles_instance

        return self._create_user(email, password, **extra_fields)


class Jusuarios(AbstractUser):
    idusuario = models.AutoField(primary_key=True)
    idrol = models.ForeignKey(
        Jroles, models.DO_NOTHING,
        db_column="idrol",
        blank=True,
        null=True
    )
    idgenero = models.ForeignKey(
        Jgeneros, models.DO_NOTHING,
        db_column="idgenero",
        blank=True, null=True
    )
    idtipoidentificacion = models.ForeignKey(
        "Jtiposidentificaciones",
        models.DO_NOTHING,
        db_column="idtipoidentificacion",
        blank=True,
        null=True
    )
    identificacion = models.CharField(max_length=100, unique=True)

    ipmodificacion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    direccion = models.CharField(max_length=500, null=False)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(blank=True, default=True)
    is_staff = models.BooleanField(blank=True, default=True)
    is_superuser = models.BooleanField(blank=True, default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    ipcreacion = models.CharField(
        max_length=50, default=get_public_ip_address
    )
    direccionmac = models.CharField(max_length=100, default=get_mac_address
                                    )
    fechamodificacion = models.DateTimeField(auto_now=True)

    objects = JusuariosManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "jusuarios"
        ordering = ['-date_joined']

    def __str__(self):
        return self.first_name + self.last_name - self.email
