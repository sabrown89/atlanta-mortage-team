from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'glossary/', views.glossary, name='glossary'),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
