from django.contrib.postgres.fields import ArrayField
from django.db import models

from users.models import Jusuarios
from principles.models import JobjetivosValores

types_reports = [("Annual", "Annual"), ("Biannual", "Biannual"), ("Monthly", "Monthly")]


# Create your models here.
class Jreportes(models.Model):

    idreporte = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250, unique=True, null=True)
    categoria = models.CharField(max_length=250, choices=[value for value in types_reports], default="Annual")
    autor = models.ForeignKey(
        Jusuarios,
        models.DO_NOTHING,
        db_column="autor",
    )
    principiosincluidos = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    status = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)
    objetivosvalores = models.ManyToManyField(JobjetivosValores, through='JreportesObjetivosValores')

    class Meta:
        db_table = 'jreportes'

    objects = models.Manager()

    def __str__(self):
        return self.titulo


class JreportesObjetivosValores(models.Model):
    idreporteobjetivosvalores = models.AutoField(primary_key=True)
    idreporte = models.ForeignKey(
        Jreportes,
        models.DO_NOTHING,
        db_column="idreporte",
    )
    idobjetivevalue = models.ForeignKey(
        JobjetivosValores,
        models.DO_NOTHING,
        db_column="idobjetivevalue",
    )
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'jreportesobjetivosvalores'

    objects = models.Manager()

    def __str__(self):
        return f"{self.idreporte} <- {self.idobjetivevalue}"


# Views of the application reports

class Vprinciplesbyreports(models.Model):
    idreporte = models.IntegerField(primary_key=True)
    titulo = models.CharField()
    categoria = models.CharField()
    autor = models.CharField()
    idprincipio = models.IntegerField()
    codigoprincipio = models.CharField()
    descripcionprincipio = models.CharField()
    in_report = models.BooleanField()
    status = models.BooleanField()
    is_complete = models.BooleanField()
    fechacreacion = models.DateTimeField()
    fechamodificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vprinciplesbyreports'

    objects = models.Manager()


class Vreports(models.Model):
    idreporte = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    principiosincluidos = ArrayField(models.CharField(max_length=255))
    idobjectivo = models.IntegerField()
    meta = models.CharField(max_length=255)
    idnumerador = models.CharField()
    descripcion_numerador = models.CharField(max_length=255)
    valor_numerador = models.CharField()
    iddenominador = models.CharField()
    descripcion_denominador = models.CharField(max_length=255)
    valor_denominador = models.CharField()
    resultado_indicador = models.CharField(max_length=255)
    cumplimiento = models.BooleanField()
    commentario = models.TextField()
    graficotipo = models.CharField(max_length=255)
    graficocontenido = models.TextField()
    operacion = models.CharField(max_length=255)
    idindicador = models.IntegerField()
    codigoindicador = models.CharField(max_length=255)
    descripcionindicador = models.CharField(max_length=255)
    idprincipio = models.IntegerField()
    codigoprincipio = models.CharField(max_length=255)
    descripcionprincipio = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vreports'

    objects = models.Manager()
