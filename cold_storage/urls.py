"""cold_storage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # General
    path('admin/', admin.site.urls),
    path('users/', include('users.employee.urls')),
    path('accesses/', include('accesses.employee.urls')),
    path('user_permissions/', include('userpermissions.administrator.urls')),
    
    # Supervisor
    path('supervisor/storages/', include('storages.supervisor.urls')),
    path('supervisor/areas/', include('areas.supervisor.urls')),
    path('supervisor/storage_temperatures/', include('temperatures.supervisor.urls')),

    # Manager
    path('manager/pallets/', include('pallets.manager.urls')),

    # Owner
    path('owner/storages/', include('storages.owner.urls')),
    path('owner/companies/', include('companies.owner.urls')),  
    path('owner/branches/', include('branches.owner.urls')),
    path('owner/accesses/', include('accesses.owner.urls')),
    path('owner/sensors/', include('sensors.owner.urls')),

    # Administrator
    path('administrator/provinces/', include('provinces.administrator.urls')),
    path('administrator/districts/', include('districts.administrator.urls')),
    path('administrator/roles/', include('roles.administrator.urls')),
]
