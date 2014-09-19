from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Aplicacion1.views.index', name='home'),
    url(r'^mensaje/$', 'Aplicacion1.views.mensaje', name='mensaje'),
    url(r'^DolaresAPesos/$', 'Aplicacion1.views.DolaresAPesos', name='contacto'),
    url(r'^PesosADolares/$', 'Aplicacion1.views.PesosADolares', name='contacto'),
    url(r'^Seleccion/$', 'Aplicacion1.views.Seleccion'),
    url(r'^Valor/([A-Z]{3})/$', 'Aplicacion1.views.Valor'),
    # url(r'^proyecto3/', include('proyecto3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
