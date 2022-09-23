from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type

# Create your tests here.

# Listar
# query = Type.objects.all()
# print(query)

#inserccion
# t = Type()
# t.id = 3
# t.name = 'Prueba'
# t.save()

#edicion
# t = Type.objects.get(id=1)
# t.name = 'Accionista01'
# t.save()

#eliminacion
# t = Type.objects.get(id=3)
# t.delete()

obj = Type.objects.filter(name__icontains='p')
print(obj)