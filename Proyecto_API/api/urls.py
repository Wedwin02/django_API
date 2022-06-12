from django.urls import path
from .views import CompanyView,EmpleadosView
urlpatterns={
    path('companies/',CompanyView.as_view(),name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(),name='companies_process'),
    #url de empleados
    path('empleados/',EmpleadosView.as_view(),name='empleados_list'),
    path('empleados/<int:id>',EmpleadosView.as_view(),name='empleados_process')
}