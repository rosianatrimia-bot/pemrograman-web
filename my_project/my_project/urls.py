from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sosmed/', include(('sosmed.urls', 'sosmed'), namespace='sosmed')),
    path('admin/', admin.site.urls),
]
