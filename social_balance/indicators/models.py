from django.db import models


# Create your models here.
class Jindicadores(models.Model):
    idindicador = models.AutoField(primary_key=True)
    codigoindicador = models.CharField(max_length=4)
    descriptionindicator = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "jindicadores"

    objects = models.Manager()

    def __str__(self):
        return self.codigoindicador


class Jvalores(models.Model):
    idvalores = models.AutoField(primary_key=True)
    descripcionvalores = models.CharField(max_length=500)
    valor = models.IntegerField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

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
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

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
        db_column="idindicador",
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
    resultado = models.BooleanField()
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "jobjetivosvalores"

    objects = models.Manager()

    def __str__(self):
        return self.resultado
