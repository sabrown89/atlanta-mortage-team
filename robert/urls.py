from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from blog import views as blog_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'glossary/', views.glossary, name='glossary'),
    url(r'^blog/', include('blog.urls')),
    url(r'admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
