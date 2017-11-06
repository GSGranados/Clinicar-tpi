from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Paciente, Expediente, Antecedente
from .forms import nuevoPacienteForm, nuevoExpedienteForm, nuevoAntecedenteForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import json

# Create your views here.

def index(request):
	return render(request, 'integral/index.html',{})

def nuevoPaciente(request):
	pacientes = Paciente.objects.all()
	paginator = Paginator(pacientes,15)
	page = request.GET.get('page')
	try:
		pacientes = paginator.page(page)
	except PageNotAnInteger:
		pacientes = paginator.page(1)
	except EmptyPage:
		pacientes = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = nuevoPacienteForm(request.POST)
		if form.is_valid():
			form.save()
			ultimoPaciente = Paciente.objects.first()
			Expediente.objects.create(paciente = ultimoPaciente)
			formAntecedente = nuevoAntecedenteForm()
			return HttpResponse("<p>Paciente guardado y expediente asignado!!!</p><br><p>PASO 2:INGRESE ANTECEDENTES</p><br>"+formAntecedente.as_p()+"<br><input type=submit value='Guardar Antecedente' id='btnGuardarAntecedente'></input><input type=submit value='Ver Antecedentess' id='btnObtenerAntecedentes'></input>")
		else:
			data = json.dumps([v for k , v in form.errors.items()]+[' ¡Error!'])
			return HttpResponse(data, content_type='application/json')
	else:
		form = nuevoPacienteForm()
	return render(request, 'integral/nuevoPaciente.html',{'form': form,'pacientes':pacientes})

def expediente(request):
	expedientes = Expediente.objects.all()
	paginator = Paginator(expedientes,15)
	page = request.GET.get('page')
	try:
		expedientes = paginator.page(page)
	except PageNotAnInteger:
		expedientes = paginator.page(1)
	except EmptyPage:
		expedientes = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = nuevoExpedienteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("GUARDADO!")
		else:
		    data = json.dumps([v for k , v in form.errors.items()]+[' ¡Error!'])
		return HttpResponse(data, content_type='application/json')
	else:
		form = nuevoExpedienteForm()
	return render(request, 'integral/expediente/expediente.html',{'form':form,'expedientes':expedientes})

def AntecedenteList(request,expedienteId):
	antecedentes = Antecedente.objects.filter(fk_antecedente_expediente=expedienteId)
	return render(request, 'integral/antecedente_list.html',{'antecedentes':antecedentes})

class PacienteList(ListView):
	model = Paciente

class PacienteDetail(DetailView):
	model = Paciente

class PacienteDelete(DeleteView):
	model = Paciente
	success_url = reverse_lazy('integral:listarPaciente')

#class AntecedenteList(ListView):
#	model = Antecedente