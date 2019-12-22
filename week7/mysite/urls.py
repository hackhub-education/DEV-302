from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('turntable/', include('turntable.urls')),
    path('admin/', admin.site.urls),
]
