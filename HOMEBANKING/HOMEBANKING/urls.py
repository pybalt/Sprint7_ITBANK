"""HOMEBANKING URL Configuration

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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


from Login.views import login_usuario
from registro.views import registro_usuario
from .views import (landing_page, 
                    main_home,
                    main_cajas,
                    )
from Movimiento.views import (main_transferencia, 
                              main_movimientos)
from Prestamo.views import main_prestamos
from Tarjeta.views import main_tarjetas
from Cuenta.views import (main_cuenta, 
                          main_configuracion,
                          main_actividad)

urlpatterns = [
    path('admin/',                   admin.site.urls,                           name = "admin"),
    path('login',                    include('django.contrib.auth.urls')),
    path('',                         landing_page,                              name = "landing page"),
    path('main/',                    main_home,                                 name = "main"),
    path('main/prestamos/',          main_prestamos,                            name = "prestamos"),
    path('main/transferencia/',      main_transferencia,                        name = "transferencia"),
    path('main/movimientos/',        main_movimientos,                          name = "movimientos"),
    path('main/cajas/',              main_cajas,                                name = "cajas"),
    path('main/tarjetas/',           main_tarjetas,                             name = "tarjetas"),
    path('main/cuenta/',             main_cuenta,                               name = "cuenta"),
    path('main/configuracion/',      main_configuracion,                        name = "configuracion"),
    path('main/actividad/',          main_actividad,                            name = "actividad"),
    path('registrate/',              registro_usuario,                          name = "registrate"),
    path('login/',                   login_usuario,                             name = "login"),
    
]

urlpatterns += staticfiles_urlpatterns()