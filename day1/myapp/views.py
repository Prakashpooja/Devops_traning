import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Student1, Student2
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


# ---------- Function Based Views ----------

# def hello(request):
#     return HttpResponse("Hello, World!")


# def bye(request):
#     return HttpResponse("Bye")


# @csrf_exempt
# def echo(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'POST only'}, status=405)
#     data = json.loads(request.body or '{}')
#     return JsonResponse({'received': data}, status=201)


# @csrf_exempt
# def update_echo(request):
#     if request.method == 'PUT':
#         data = json.loads(request.body or '{}')
#         return JsonResponse({'action': 'updated', 'received': data})
#     return JsonResponse({'error': 'PUT only'}, status=405)


# @csrf_exempt
# def delete_echo(request):
#     if request.method == 'DELETE':
#         return JsonResponse({'status': 'deleted', 'user': 'nitesh'})
#     return JsonResponse({'error': 'DELETE only'}, status=405)


# # ---------- Class Based View ----------

# @method_decorator(csrf_exempt, name='dispatch')
# class SimplePostView(View):
#     def post(self, request):
#         data = json.loads(request.body or '{}')
#         return JsonResponse({'received': data})

#     def get(self, request):
#         return JsonResponse({'received': 'get'})


# # ---------- DRF APIView ----------

# class UserAPI(APIView):
#     def get(self, request):
#         return Response({"message": "GET request received"})

#     def post(self, request):
#         return Response(request.data, status=201)


# # ---------- DRF ViewSet ----------

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student1.objects.all()
#     serializer_class = StudentSerializer

#----------------------------------------------


def simple_page(request):
    # Data without model
    products = [
        {'name': 'Book', 'price': 299, 'description': 'A good book'},
        {'name': 'Pen', 'price': 19, 'description': 'Blue ink pen'},
    ]
    return render(request, 'simple_product.html', {'products': products})


@csrf_exempt
def student_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Student2.objects.create(
            name=data['name'],
            age=data['age']
        )
        return JsonResponse({'id': student.id, 'name': student.name, 'age': student.age}, status=201)
    
    elif request.method == 'GET':
        students = Student2.objects.all()
        students_data = [{'id': s.id, 'name': s.name, 'age': s.age} for s in students]
        return JsonResponse({'students': students_data})
    


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)   # creates session
            return redirect("/myapp/home/")
    return render(request, "login.html")

def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not logged in")
    return HttpResponse(f"Hello {request.user.username}")



class ProfileAPI(APIView):
    def get(self, request):
        return Response({"user": request.user.username})
    




