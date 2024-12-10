from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/users/',include('djoser.urls.authtoken')),
    path("api/", include("patients.urls")),
    path("api/",  include("doctors.urls")), 
    path("api/", include("appointments.urls"))

]


