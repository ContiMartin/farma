"""organizandor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from medicamentos import views as mviews
from organizaciones import views as oviews
from pedidos import views as pviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^$', views.inicio, name="inicio"),
    url(r'^login', views.login_user, name="login"),
    url(r'^logout', views.logout_user, name="logout"),

    # ****** MEDICAMENTOS ******
    url(r'^monodrogas/$', mviews.monodrogas, name="monodrogas"),
    url(r'^monodrogas/add/$', mviews.monodroga_add, name="monodroga_add"),
    url(r'^monodrogas/update/(?P<id_monodroga>\d+)/$', mviews.monodroga_update, name="monodroga_update"),
    url(r'^monodrogas/delete/(?P<id_monodroga>\d+)/$', mviews.monodroga_delete, name="monodroga_delete"),

    url(r'^medicamentos/$',mviews.medicamentos, name="medicamentos"),
    url(r'^medicamentos/add/$', mviews.medicamento_add, name="medicamento_add"),
    url(r'^medicamentos/delete/(?P<id_medicamento>\d+)/$', mviews.medicamento_delete, name="medicamento_delete"),
    url(r'^medicamentos/update/(?P<id_medicamento>\d+)/$', mviews.medicamento_update, name="medicamento_update"),
    #
    # url(r'^altaMedicamento/$', views.altaMedicamento, name="altaMedicamento"),
    url(r'^nombresFantasia/$', mviews.nombresFantasia, name="nombresFantasia"),
    url(r'^nombresFantasia_add/$', mviews.nombresFantasia_add, name="nombresFantasia_add"),
    url(r'^nombresFantasia/update/(?P<id_nombreFantasia>\d+)/$', mviews.nombresFantasia_update, name="nombresFantasia_update"),
    url(r'^nombresFantasia/delete/(?P<id_nombreFantasia>\d+)/$', mviews.nombresFantasia_delete, name="nombresFantasia_delete"),

    url(r'^Presentacion/$', mviews.presentacion, name="presentacion"),
    url(r'^Presentacion_add/$', mviews.presentacion_add, name="presentacion_add"),
    url(r'^Presentacion/update/(?P<id_presentacion>\d+)/$', mviews.presentacion_update, name="presentacion_update"),
    url(r'^Presentacion/delete/(?P<id_presentacion>\d+)/$', mviews.presentacion_delete, name="presentacion_delete"),

    #============================================inicio desde m====================================================
     # ****** PEDIDOS DE FARMACIA ******
    url(r'^pedidosDeFarmacia/$', pviews.pedidosDeFarmacia, name="pedidosDeFarmacia"),
    url(r'^pedidosDeFarmacia/add/$', pviews.pedidoF_add, name="pedidoF_add"),
    url(r'^pedidosDeFarmacia/add/detalles-pedido/$', pviews.detalles_pedidoF, name="detalles_pedidoF"),
    url(r'^pedidosDeFarmacia/add/detalles-pedido/add/$', pviews.add_detalle_pedido_farmacia, name="add_detalle_pedido_farmacia"),
    url(r'^pedidosDeFarmacia/add/detalles-pedido/update/(?P<id_detalle>\d+)/$', pviews.update_detalle_pedido_farmacia, name="update_detalle_pedido_farmacia"),
    url(r'^pedidosDeFarmacia/add/detalles-pedido/delete/(?P<id_detalle>\d+)/$', pviews.delete_detalle_pedido_farmacia, name="delete_detalle_pedido_farmacia"),
    url(r'^pedidosDeFarmacia/add/registrar-pedido/$', pviews.registrar_pedido_farmacia, name="registrar_pedido_farmacia"),
    url(r'^pedidosDeFarmacia/ver/(?P<id_pedido>\d+)/$', pviews.ver_pedidoF, name="ver_pedidoF"),

    #============================================fin desde m=====================================================



#====================================================INICIO CORRECTOS=======================================================0

    # ****** PEDIDOS ******
    #url(r'^pedidoDeFarmacia/$', pviews.pedidoDeFarmacia, name="pedidoDeFarmacia"),

    url(r'^pedidoDeClinica/$', views.pedidoDeClinica,name="pedidoDeClinica"),
    url(r'^devolucionMedicamentosVencidos/$', views.devolucionMedicamentosVencidos,name="devolucionMedicamentosVencidos"),
    url(r'^recepcionReemplazoMedicamentos/$', views.recepcionReemplazoMedicamentos,name="recepcionReemplazoMedicamentos"),

    # ****** PEDIDOS A LABORATORIO ******
    url(r'^pedidoAlaboratorios/verRenglones/(?P<id>\d+)/$', pviews.pedidoAlaboratorios_verRenglones, name="pedidoAlaboratorios_verRenglones"),
    url(r'^pedidoAlaboratorios/agregarRenglones/$', pviews.pedidoAlaboratorios_agregarRenglones, name="pedidoAlaboratorios_agregarRenglones"),
    url(r'^ListPedidoALaboratorio/$', pviews.ListPedidoALaboratorio, name="ListPedidoALaboratorio"),
    url(r'^pedidoAlaboratorios/add/$', pviews.PedidoLaboratorio_add, name="PedidoLaboratorio_add"),
    url(r'^recepcionPedidoDeLaboratorio/$', pviews.recepcionPedidoDeLaboratorio, name="recepcionPedidoDeLaboratorio"),
    url(r'^pedidoAlaboratorios/registrarRecepcionPedido/(?P<id>\d+)/$', pviews.pedidoAlaboratorios_RecepcionPedidoLab, name="pedidoAlaboratorios_registrarRecepcionPedido"),
    url(r'^pedidoAlaboratorios/agregarLotes/$', pviews.pedidoAlaboratorios_agregarLotes, name="pedidoAlaboratorios_agregarLotes"),


    # ****** PEDIDOS DE CLINICA ******
    url(r'^pedidosDeClinica/$', pviews.pedidosDeClinica, name="pedidosDeClinica"),
    url(r'^pedidosDeClinica/add/$', pviews.pedido_de_clinica_add, name="pedido_de_clinica_add"),
    url(r'^pedidosDeClinica/add/detalles-pedido/$', pviews.pedido_de_clinica_detalles, name="pedido_de_clinica_detalles"),
    url(r'^pedidosDeClinica/add/detalles-pedido/add/$', pviews.add_detalle_pedido_de_clinica, name="add_detalle_pedido_de_clinica"),
    url(r'^pedidosDeClinica/add/detalles-pedido/update/(?P<id_detalle>\d+)/$', pviews.update_detalle_pedido_de_clinica, name="update_detalle_pedido_de_clinica"),
    url(r'^pedidosDeClinica/add/detalles-pedido/delete/(?P<id_detalle>\d+)/$', pviews.delete_detalle_pedido_de_clinica, name="delete_detalle_pedido_de_clinica"),
    url(r'^pedidosDeClinica/add/registrar-pedido/$', pviews.registrar_pedido_de_clinica, name="registrar_pedido_de_clinica"),
    url(r'^pedidosDeClinica/ver/(?P<id_pedido>\d+)/$', pviews.ver_pedido_de_clinica, name="ver_pedido_de_clinica"),


    # ****** FARMACIAS ******
    url(r'^farmacias/$',oviews.farmacias, name="farmacias"),
    url(r'^farmacias/add/$', oviews.farmacia_add, name="farmacia_add"),
    url(r'^farmacias/update/(?P<id_farmacia>\d+)/$', oviews.farmacia_update, name="farmacia_update"),
    url(r'^farmacias/delete/(?P<id_farmacia>\d+)/$', oviews.farmacia_delete, name="farmacia_delete"),
    
    
    # ****** CLINICAS ******
    url(r'^clinicas/$',oviews.clinicas, name="clinicas"),
    url(r'^clinicas/add/$', oviews.clinica_add, name="clinica_add"),
    url(r'^clinicas/update/(?P<id_clinica>\d+)/$', oviews.clinica_update, name="clinica_update"),
    url(r'^clinicas/delete/(?P<id_clinica>\d+)/$', oviews.clinica_delete, name="clinica_delete"),
    

    # ****** LABORATORIOS ******
    url(r'^laboratorios/$',oviews.laboratorios, name="laboratorios"),
    url(r'^laboratorios/add/$', oviews.laboratorio_add, name="laboratorio_add"),
    url(r'^laboratorios/update/(?P<id_laboratorio>\d+)/$', oviews.laboratorio_update, name="laboratorio_update"),
    url(r'^laboratorios/delete/(?P<id_laboratorio>\d+)/$', oviews.laboratorio_delete, name="laboratorio_delete"),
    
    
    # ****** OTROS ******
    url(r'^obrasSociales/$',views.paginaEnConstruccion, name="paginaEnConstruccion"),


]
