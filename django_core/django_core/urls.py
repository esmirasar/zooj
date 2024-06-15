from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include('inform.urls')),
    path('api/', include('favorite.urls')),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html'))
]
