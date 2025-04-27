from django.shortcuts import render
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.


class CreateEmployeeView(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

