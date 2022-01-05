from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.http import request
from django.core.files.storage import default_storage

import requests

from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from EmployeeApp.security import AuthorizationClient

@csrf_exempt
def departmentApi(request, id = 0):
    token = request.META.get('HTTP_AUTHORIZATION')
    security_response = AuthorizationClient.verifyJwt(token)
    if security_response == 1:
        if request.method == 'GET':
            departments = Department.objects.all()
            departments_serializer = DepartmentSerializer(departments, many = True)
            return JsonResponse(departments_serializer.data, safe = False)
        elif request.method == 'POST':
            department_data = JSONParser().parse(request)
            departments_serializer = DepartmentSerializer(data = department_data)
            if departments_serializer.is_valid():
                departments_serializer.save()
                return JsonResponse("Added successfully", safe = False)
            return JsonResponse("Failed to add", safe = False)
        elif request.method == 'PUT':
            department_data = JSONParser().parse(request)
            department = Department.objects.get(DepartmentId = department_data['DepartmentId'])
            departments_serializer = DepartmentSerializer(department, data = department_data)
            if departments_serializer.is_valid():
                departments_serializer.save()
                return JsonResponse("Updated successfully", safe = False)
            return JsonResponse("Failed to update")
        elif request.method == 'DELETE':
            department = Department.objects.get(DepartmentId = id)
            department.delete()
            return JsonResponse("Deleted successfully", safe = False)
    else:
        return JsonResponse("Token not found or invalid", safe = False)

@csrf_exempt
def employeeApi(request,id=0):
    token = request.META.get('HTTP_AUTHORIZATION')
    security_response = AuthorizationClient.verifyJwt(token)
    if security_response == 1:
        if request.method == 'GET':
            employees = Employee.objects.all()
            employees_serializer = EmployeeSerializer(employees, many = True)
            return JsonResponse(employees_serializer.data,safe = False)
        elif request.method == 'POST':
            employee_data = JSONParser().parse(request)
            employees_serializer = EmployeeSerializer(data = employee_data)
            if employees_serializer.is_valid():
                employees_serializer.save()
                return JsonResponse("Added Successfully",safe = False)
            return JsonResponse("Failed to add", safe = False)
        elif request.method == 'PUT':
            employee_data = JSONParser().parse(request)
            employee = Employee.objects.get(EmployeeId = employee_data['EmployeeId'])
            employees_serializer = EmployeeSerializer(employee, data = employee_data)
            if employees_serializer.is_valid():
                employees_serializer.save()
                return JsonResponse("Updated successfully", safe = False)
            return JsonResponse("Failed to update")
        elif request.method == 'DELETE':
            employee = Employee.objects.get(EmployeeId = id)
            employee.delete()
            return JsonResponse("Deleted successfully", safe = False)
    else:
        return JsonResponse("Token not found or invalid", safe = False)

@csrf_exempt
def saveFile(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    security_response = AuthorizationClient.verifyJwt(token)
    if security_response == 1:
        file=request.FILES['file']
        file_name=default_storage.save(file.name,file)
        return JsonResponse(file_name,safe=False)
    else:
        return JsonResponse("Token not found or invalid", safe = False)

@csrf_exempt
def userApi(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    security_response = AuthorizationClient.verifyJwt(token)
    if security_response == 1:
        if request.method == 'GET':
            response = requests.get('http://localhost:6000/dbtest/user/find').json()
            return JsonResponse(response, safe = False)
        elif request.method == 'POST':
            user_data = JSONParser().parse(request)
            response = requests.post('http://localhost:6000/dbtest/user/save', json = user_data)
            print(response)
            return JsonResponse("User created", safe = False)
    else:
        return JsonResponse("Token not found or invalid", safe = False)
