import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import company,EmpleadoClases
# Create your views here.
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id=0):
        if(id>0):
            # se encontro un solo registro
            companies = list(company.objects.filter(id=id).values())
            if len(companies)>0:
                #Solo uno
                Company = companies[0]
                datos = {'message': "Success",'Company':Company}
            else:
                datos = {'message': "Companies not founds.."}
            return JsonResponse(datos)
        else:
            # Lista de datos encorntada 
            companies = list(company.objects.values())
            if len(companies)>0:
                datos = {'message': "Success",'companies':companies}
            else:
                datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)


    def post(self,request):
        #Convertido a un diccionario de python
        jd = json.loads(request.body)
        company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos = {'message': "Success"}
        return JsonResponse(datos)



    def put(self,request,id):
        jd = json.loads(request.body)
        companies = list(company.objects.filter(id=id).values())
        if len(companies)>0:
            #En este punto se conoce que almenos uno esta 
            Company = company.objects.get(id=id)
            Company.name=jd['name'],
            Company.website=jd['website'],
            Company.foundation=jd['foundation']
            Company.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)


    def delete(self,request,id):
        companies = list(company.objects.filter(id=id).values())
        if len(companies)>0:
            company.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)

class EmpleadosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            # se encontro un solo registro
            empleado = list(EmpleadoClases.objects.filter(id=id).values())
            if len(empleado)>0:
                #Solo uno
                Empleado = empleado[0]
                datos = {'message': "Success",'Company':Empleado}
            else:
                datos = {'message': "Companies not founds.."}
            return JsonResponse(datos)
        else:
            # Lista de datos encorntada 
            Empleado = list(EmpleadoClases.objects.values())
            if len(Empleado)>0:
                datos = {'message': "Success",'companies':Empleado}
            else:
                datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        EmpleadoClases.objects.create(lastname=jd['lastname'],firstname=jd['firstname'],email=jd['email'],FechaNaciemiento=jd['FechaNaciemiento'])
        datos = {'message': "Success"}
        return JsonResponse(datos)


    def put(self,request,id):
        jd = json.loads(request.body)
        Empleado = list(EmpleadoClases.objects.filter(id=id).values())
        if len(Empleado)>0:
            #En este punto se conoce que almenos uno esta 
            empleado = EmpleadoClases.objects.get(id=id)
            empleado.lastname = jd['lastname'],
            empleado.firstname = jd['firstname'],
            empleado.email = jd['email'],
            empleado.FechaNaciemiento = jd['FechaNaciemiento']
            empleado.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)



    def delete(self,request,id):
        Empleado = list(EmpleadoClases.objects.filter(id=id).values())
        if len(Empleado)>0:
            EmpleadoClases.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Companies not founds.."}
        return JsonResponse(datos)