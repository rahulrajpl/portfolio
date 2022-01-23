from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import index, register
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='index',),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls')),
    path('register/', register, name='register'),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()