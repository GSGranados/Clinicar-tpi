from django.conf.urls import include, url
from . import views
from .views import PacienteList,PacienteDetail, PacienteDelete, AntecedenteList


urlpatterns = [
	
	url(r'^$', views.index,),
	url(r'^listarPaciente$',PacienteList.as_view(), name='listarPaciente'),
	url(r'^listarAntecedentes/(?P<expedienteId>\d+)$',views.AntecedenteList, name='listarAntecedentes'),
	url(r'^detallePaciente/(?P<pk>\d+)$',PacienteDetail.as_view(), name='detallePaciente'),
	url(r'^eliminarPaciente/(?P<pk>\d+)$',PacienteDelete.as_view(), name='eliminarPaciente'),
	url(r'^nuevoPaciente/$',views.nuevoPaciente, name='nuevoPaciente'),
	url(r'^expediente/$',views.expediente),
]
