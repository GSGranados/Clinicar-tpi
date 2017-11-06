from django.conf.urls import include, url
from .views import PacienteList,PacienteDetail, PacienteDelete, AntecedenteList
from .views import index, nuevoPaciente, expediente


urlpatterns = [
	url(r'^$', index,),
	url(r'^pacientes$', PacienteList.as_view(), name='listarPaciente'),
	url(r'^listarAntecedentes/(?P<expedienteId>\d+)$', AntecedenteList, name='listarAntecedentes'),
	url(r'^detallePaciente/(?P<pk>\d+)$', PacienteDetail.as_view(), name='detallePaciente'),
	url(r'^eliminarPaciente/(?P<pk>\d+)$', PacienteDelete.as_view(), name='eliminarPaciente'),
	url(r'^nuevoPaciente/$', nuevoPaciente, name='nuevoPaciente'),
	url(r'^expediente/$', expediente),
]
