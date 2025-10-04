from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('your-endpoint',views.calculate_power,name="calculate_power"),
]
