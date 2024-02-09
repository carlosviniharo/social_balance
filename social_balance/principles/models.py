from django.contrib.postgres.fields import ArrayField
from django.db import models

from users.models import Jusuarios

types_operators = [
    ("greater_than", "greater_than"),
    ("equal_greater_than", "equal_greater_than"),
    ("equal", "equal"),
    ("equal_less_than", "equal_less_than"),
    ("less_than", "less_than")
]


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
    relacionproporcion = models.CharField(null=True)
    variables = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    variablesunidades = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    variablesgrafico = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    variablesgraficounidades = ArrayField(models.CharField(max_length=255), blank=True, null=True)
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


class Jobjetivos(models.Model):
    idobjectivo = models.AutoField(primary_key=True)

    idindicador = models.ForeignKey(
        "Jindicadores",
        models.DO_NOTHING,
        db_column="idindicador",
        blank=True,
        null=True,
    )
    meta = models.CharField()
    unidades = models.CharField(blank=True, null=True)
    logica = models.CharField(
        max_length=250,
        choices=[value for value in types_operators],
        null=True,
        default="default"
    )
    status = models.BooleanField(default=True)
    is_applicable = models.BooleanField(default=True)
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
    )
    idnumerador = models.ForeignKey(
        "Jvalores",
        models.DO_NOTHING,
        db_column="idnumerador",
        related_name="jobjetivosvalores_idnumerador_set",
        null=True,
    )
    iddenominador = models.ForeignKey(
        "Jvalores",
        models.DO_NOTHING,
        db_column="iddenominador",
        related_name="jobjetivosvalores_iddenominador_set",
        null=True,
    )
    idusuario = models.ForeignKey(
        Jusuarios,
        models.DO_NOTHING,
        db_column="idusuario",
    )
    resultado = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    cumplimiento = models.BooleanField(null=True)
    commentario = models.TextField(blank=True)
    graficotipo = models.CharField(null=True)
    graficocontenido = models.TextField(null=True)
    is_complete = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)
    fechamodificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "jobjetivosvalores"

    objects = models.Manager()

    def __str__(self):
        return str(self.idobjetivevalue)


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


class Jvalores(models.Model):
    idvalores = models.AutoField(primary_key=True)
    descripcionvalores = models.CharField(max_length=500)
    tipovalor = models.CharField(max_length=250)
    unidades = models.CharField(blank=True, null=True)
    valor = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    validezinicio = models.DateTimeField(auto_now_add=True, null=True)
    validezfin = models.DateTimeField(null=True)

    class Meta:
        db_table = "jvalores"

    objects = models.Manager()

    def __str__(self):
        return self.descripcionvalores


# Database Views for the principles application

class Vindicators(models.Model):
    idindicador = models.AutoField(primary_key=True)
    codigoindicador = models.CharField(max_length=255)
    descripcionindicador = models.TextField()
    operacion = models.CharField(max_length=255)
    relacionproporcion = models.CharField(max_length=255)
    variables = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    idvalor_denominador = models.IntegerField()
    valor_denominador = models.CharField(max_length=255)
    unidades_denominador = models.CharField()
    idvalor_numerador = models.IntegerField()
    valor_numerador = models.CharField(max_length=255)
    unidades_numerador = models.CharField()
    status = models.BooleanField()
    idobjectivo = models.IntegerField()
    units_result = models.CharField()
    meta = models.CharField()
    logica = models.CharField()
    objetivo_validezinicio = models.DateTimeField()
    is_applicable = models.BooleanField()
    idobjetivevalue = models.IntegerField()
    is_complete = models.BooleanField()
    idreporte = models.IntegerField()
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
        ordering = ['codigoindicador']

    objects = models.Manager()


class Vobjectivesvalues(models.Model):
    idobjetivevalue = models.IntegerField(primary_key=True)
    idobjectivo = models.IntegerField()
    meta = models.CharField(max_length=255)
    logica = models.CharField()
    idnumerador = models.IntegerField()
    descripcion_numerador = models.CharField(max_length=255)
    unidades_numerador = models.CharField(max_length=255)
    valor_numerador = models.CharField()
    iddenominador = models.IntegerField()
    descripcion_denominador = models.CharField(max_length=255)
    unidades_denominador = models.CharField()
    valor_denominador = models.CharField()
    idusuario = models.IntegerField()
    fullname = models.CharField(max_length=255)
    resultado_indicador = models.CharField()
    unidades_indicador = models.CharField()
    variablesgrafico = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    resultado_grafico = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    cumplimiento = models.BooleanField(max_length=255)
    commentario = models.CharField()
    graficotipo = models.CharField()
    graficocontenido = models.TextField()
    is_complete = models.BooleanField()
    operacion = models.CharField()
    relacionproporcion = models.CharField()
    idindicador = models.IntegerField()
    codigoindicador = models.CharField()
    descripcionindicador = models.CharField()
    idclasificacion = models.IntegerField()
    descripcionclasificacion = models.CharField()
    idprincipio = models.IntegerField()
    codigoprincipio = models.CharField()
    descripcionprincipio = models.CharField()
    status = models.BooleanField(max_length=255)
    fechacreacion = models.DateTimeField()
    fechamodificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vobjectivesvalues'

    objects = models.Manager()
