
from django.contrib import admin
from django.urls import path, include
from students.views import about

urlpatterns = [
    path('', about, name='home'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
]
