from django.db import models
from django.core.validators import MinValueValidator

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class Paciente(models.Model):
    nombre = models.CharField('Nombres del paciente', max_length=40, blank=False, null=False)
    apellido = models.CharField('Apellidos del paciente', max_length=40, blank=False, null=False)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', help_text='Formato: DD/MM/AAAA', blank=False, null=False)
    telefono = models.CharField('Número de teléfono', max_length=9, help_text='Formato: XXXX-XXXX', blank=False, null=False, unique=True)
    direccion = models.CharField('Dirección', max_length=80, help_text='Dirección de su residencia', blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)

    class Meta:
        ordering = ['expediente']
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Expediente(models.Model):
    paciente = models.OneToOneField(Paciente, null=False, help_text='Expediente asignado')
    fecha_apertura = models.DateField('Fecha de apertura', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format('Expediente de', self.paciente)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'


class Antecedente(models.Model):
    fk_antecedente_expediente = models.ForeignKey(Expediente, null=True, blank=True)
    enfermedad = models.CharField('Enfermedad', max_length=32, blank=False, null=False, help_text='Enfermedad que padece')
    familiar = models.BooleanField('¿Algún familiar también padece esta enfermedad?', default=False)
    tratamiento = models.BooleanField('¿Le ha sido administrado algún tratamiento?', default=False)
    medicamento_asignado = models.CharField('Medicamento asignado', max_length=256, blank=False, null=False)

    def __str__(self):
        return self.enfermedad

    class Meta:
        ordering = ["id"]
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'


class ConsultaMedica(models.Model):
    fk_consulta_expediente = models.ForeignKey(Expediente, null=False, blank=False)
    fecha = models.DateField('Fecha', auto_now_add=True)
    hora = models.TimeField('Hora de Consulta', blank=False, null=False)
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])
    talla = models.DecimalField('Talla', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])
    ta = models.CharField('Tensión arterial', max_length=6, blank=False, null=False, help_text='Tensión arterial ###/##')
    fc = models.DecimalField('Frecuencia cardíaca', max_digits=5, decimal_places=2, blank=False, null=False, help_text='Frecuencia cardíaca', validators=[MinValueValidator(0)])
    problema = models.CharField('Historia del problema', max_length=256, blank=False, null=False, help_text='Motivo de consulta')
    diagnostico = models.CharField('Diagnostico', max_length=256, blank=False, null=False)
    prox_control = models.DateTimeField(blank=True, null=True)
    precio_consulta = models.DecimalField('Precio de la Consulta', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return '{}: {}'.format('Consulta del expediente', self.fk_consulta_expediente)

    def get_edad(self):
        diff = (self.fecha - self.fk_consulta_expediente.paciente.fecha_nacimiento).days
        edad = str(int(diff / 365))
        cantidad_tiempo = 'años'
        if edad == '0':
            edad = str(int(diff / 12))
            cantidad_tiempo = 'meses'
        return '{} {}'.format(self.edad, self.cantidad_tiempo)

    class Meta:
        ordering = ["fecha", "hora"]
        verbose_name = 'Cita Médica'
        verbose_name_plural = 'Citas Médicas'


class Receta(models.Model):
    fk_receta_consulta = models.ForeignKey(ConsultaMedica, null=False, blank=False)
    fecha_hora = models.DateTimeField('Fecha y hora de prescripción', auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.fecha_hora, self.fk_receta_consulta)

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'


class DetalleReceta(models.Model):
    fk_detalle_receta = models.ForeignKey(Receta, null=False, blank=False)
    medicamento = models.CharField('Medicamento', max_length=256, blank=False, null=False)
    indicaciones = models.CharField('Indicaciones', max_length=256, blank=False, null=False)

    class Meta:
        ordering = ['fk_detalle_receta']
        verbose_name = 'Detalle de Receta'
        verbose_name_plural = 'Detalles de Recetas'
