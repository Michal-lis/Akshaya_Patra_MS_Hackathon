from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hackathon/', include('hackathon.urls')),
    path('admin/', admin.site.urls),
]