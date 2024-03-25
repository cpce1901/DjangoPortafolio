from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from .sitemap import StaticViewSitemap
from .views import robots_txt, error_403_view, error_404_view


#Creacion de diccionario SITEMAP
sitemaps = {
    "static": StaticViewSitemap,
}


#URLs para rastreo e indexacion
url_SEO = [
    # Bots.txt
    path("robots.txt", robots_txt),
    # Sitemaps
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]


#URLs para servicios
url_API = [

]


#URLs propias del sitio
url_BASE = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('apps.iot.urls')),
]


#URLs totales
urlpatterns = url_SEO + url_BASE


#Habilitación ficheros estaticos DEV
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Vistas Errores
handler404 = error_404_view
handler403 = error_403_view


# Nombre Admin
admin.site.site_title = "Panel de control Portafolio CpCe"
admin.site.site_header = "Portafolio CpCe"
admin.site.index_title = "Panel de control Portafolio CpCe"