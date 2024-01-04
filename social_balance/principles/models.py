from django.contrib.postgres.fields import ArrayField
from django.db import models

from users.models import Jusuarios


# Create your models here.
class Jindicadores(models.Model):
    idindicador = models.AutoField(primary_key=True)
    idprinciosubdivision = models.ForeignKey(
        "Jprinciossubdivisiones",
        models.DO_NOTHING,
        db_column="idprinciosubdivision",
        blank=True,
        null=True,
    )
    codigoindicador = models.CharField(max_length=4)
    descripcionindicador = models.CharField(max_length=500)
    operacion = models.CharField()
    variables = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    validezinicio = models.DateTimeField(null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jindicadores"

    objects = models.Manager()

    def __str__(self):
        return self.codigoindicador


class Jvalores(models.Model):
    idvalores = models.AutoField(primary_key=True)
    descripcionvalores = models.CharField(max_length=500)
    tipovalor = models.CharField(max_length=250)
    valor = models.CharField()
    status = models.BooleanField(default=True)
    validezinicio = models.DateTimeField(auto_now_add=True, null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jvalores"

    objects = models.Manager()

    def __str__(self):
        return self.descripcionvalores


class Jobjetivos(models.Model):
    idobjectivo = models.AutoField(primary_key=True)

    idindicador = models.ForeignKey(
        "Jindicadores",
        models.DO_NOTHING,
        db_column="idindicador",
        blank=True,
        null=True,
    )
    meta = models.IntegerField()
    status = models.BooleanField(default=True)
    validezinicio = models.DateTimeField(auto_now_add=True, null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jobjetivos"

    objects = models.Manager()

    def __str__(self):
        return self.meta


class JobjetivosValores(models.Model):
    idobjetivevalue = models.AutoField(primary_key=True)
    idobjectivo = models.ForeignKey(
        "Jobjetivos",
        models.DO_NOTHING,
        db_column="idobjectivo",
        blank=True,
        null=True,
    )
    idnumerador = models.ForeignKey(
        Jvalores,
        models.DO_NOTHING,
        db_column="idnumerador",
        related_name="jobjetivosvalores_idnumerador_set",
        blank=True,
        null=True,
    )
    iddenominador = models.ForeignKey(
        Jvalores,
        models.DO_NOTHING,
        db_column="iddenominador",
        related_name="jobjetivosvalores_iddenominador_set",
        blank=True,
        null=True,
    )
    idusuario = models.ForeignKey(
        Jusuarios,
        models.DO_NOTHING,
        db_column="idusuario",
        blank=True,
        null=True,
    )
    resultado = models.CharField()
    cumplimiento = models.BooleanField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "jobjetivosvalores"

    objects = models.Manager()

    def __str__(self):
        return self.resultado


class Jprincipios(models.Model):
    idprincipio = models.AutoField(primary_key=True)
    codigoprincipio = models.CharField(max_length=50)
    descripcionprincipio = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    validezinicio = models.DateTimeField(null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jprincipios"
        ordering = ['codigoprincipio']

    objects = models.Manager()

    def __str__(self):
        return self.codigoprincipio


class Jprinciossubdivisiones(models.Model):
    idprinciosubdivision = models.AutoField(primary_key=True)
    idprincipio = models.ForeignKey(
        Jprincipios,
        models.DO_NOTHING,
        db_column="idprincipio",
        blank=True,
        null=True,
    )
    fkidprinciosubdivision = models.ForeignKey(
        "self", models.DO_NOTHING,
        db_column="fkidprinciosubdivision",
        blank=True,
        null=True
    )
    nivel = models.IntegerField()
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    validezinicio = models.DateTimeField(null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jprinciossubdivisiones"

    objects = models.Manager()

    def __str__(self):
        return self.descripcion


# Database Views for the principles application

class Vindicators(models.Model):
    idindicador = models.AutoField(primary_key=True)
    codigoindicador = models.CharField(max_length=255)
    descripcionindicador = models.TextField()
    operacion = models.CharField(max_length=255)
    variables = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    idvalor_denominador = models.IntegerField()
    valor_denominador = models.CharField(max_length=255)
    idvalor_numerador = models.IntegerField()
    valor_numerador = models.CharField(max_length=255)
    status = models.BooleanField()
    fechacreacion = models.DateTimeField()
    fechamodificacion = models.DateTimeField()
    validezinicio = models.DateTimeField()
    validezfin = models.DateTimeField()
    idlineamiento = models.IntegerField()
    descripcionlineamiento = models.CharField(max_length=255)
    idcaracteristica = models.IntegerField()
    descripcioncaracteristica = models.CharField(max_length=255)
    idclasificacion = models.IntegerField()
    descripcionclasificacion = models.CharField(max_length=255)
    idprincipio = models.IntegerField()
    codigoprincipio = models.CharField(max_length=255)
    descripcionprincipio = models.TextField()

    class Meta:
        managed = False
        db_table = 'vindicators'

    objects = models.Manager()


class Vobjectivesvalues(models.Model):
    idobjetivevalue = models.IntegerField(primary_key=True)
    idobjectivo = models.IntegerField()
    meta = models.CharField(max_length=255)
    idnumerador = models.IntegerField()
    descripcion_numerador = models.CharField(max_length=255)
    valor_numerador = models.IntegerField()
    iddenominador = models.IntegerField()
    descripcion_denominador = models.CharField(max_length=255)
    valor_denominador = models.IntegerField()
    idusuario = models.IntegerField()
    fullname = models.CharField(max_length=255)
    resultado = models.CharField(max_length=255)
    cumplimiento = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    fechacreacion = models.DateTimeField()
    fechamodificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vobjectivesvalues'

    objects = models.Manager()

