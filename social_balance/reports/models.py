from django.db import models

from users.models import Jusuarios
from principles.models import JobjetivosValores

types_reports = [("Annual", "Annual"), ("Biannual", "Biannual"), ("Monthly", "Monthly")]


# Create your models here.
class Jreportes(models.Model):

    idreporte = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250, unique=True)
    categoria = models.CharField(max_length=250, choices=[value for value in types_reports])
    autor = models.ForeignKey(
        Jusuarios,
        models.DO_NOTHING,
        db_column="autor",
    )
    status = models.BooleanField(default=True)
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

    class Meta:
        db_table = 'jreportesobjetivosvalores'
        unique_together = ("idreporte", "idobjetivevalue")

    objects = models.Manager()

    def __str__(self):
        return f"{self.idreporte} <- {self.idobjetivevalue}"
