from django import forms
from .models import Paciente, Expediente, Antecedente

class nuevoPacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			'nombre',
			'apellido',
			'sexo',
			'fecha_nacimiento',
			'telefono',
			'direccion',
		]
		labels = {
			'nombre': 'Nombres',
			'apellido': 'Apellidoss',
			'sexo': 'Sexo',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'telefono': 'Teléfono',
			'direccion': 'Dirección',
		}
		widget = {
			'nombre': forms.TextInput(),
			'apellido': forms.TextInput(),
			'sexo': forms.RadioSelect(),
			'fecha_nacimiento': forms.DateInput(),
			'telefono': forms.TextInput(),
			'direccion': forms.Textarea(),
		}

class nuevoExpedienteForm(forms.ModelForm):
	class Meta:
		model = Expediente
		fields = [
			'paciente',
		]
		labels = {
			'paciente': 'Paciente',
		}
		widget = {
			'paciente': forms.Select(),			
		}

class nuevoAntecedenteForm(forms.ModelForm):
	class Meta:
		model = Antecedente
		fields = [
			'enfermedad',
			'familiar',
			'tratamiento',
			'medicamento_asignado',
		]
		labels = {
			'enfermedad':'Enfermedad',
			'familiar':'Familiar',
			'tratamiento':'Tratamiento',
			'medicamento_asignado':'Medicamento Asignado',
		}
		widget = {
			'enfermedad':forms.TextInput(),
			'familiar':forms.RadioSelect(),
			'tratamiento':forms.RadioSelect(),
			'medicamento_asignado':forms.TextInput(),
		}