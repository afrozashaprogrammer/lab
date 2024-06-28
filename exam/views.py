from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
# Create your views here.
@api_view(['GET'])
def index(request):
    friend = {
        "name": "Bithe",
        "address": "Jenidah",
        "phone": "01303456677"
    }
    return Response(friend)

@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request, id):
    todo =get_object_or_404(Todo, id=id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)