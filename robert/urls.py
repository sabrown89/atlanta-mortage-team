from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'glossary/', views.glossary, name='glossary'),
    url(r'borrowers/', views.borrowers, name='borrowers'),
    url(r'contact/', views.contact, name='contact'),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
