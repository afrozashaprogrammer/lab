from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import *
from .models import *
from .pagination import *

# Create your views here.
@api_view(['GET'])
def index(request):
    friend = {
        "name": "Bithe",
        "address": "Jenidah",
        "phone": "01303456677"
    }
    return Response(friend)

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        
        paginator = TodoPagination()
        page = paginator.paginate_queryset(todos, request)
        if page is not None:
            serializer = TodoListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        data = request.data
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BED_REQUEST)


@api_view(['GET'])
def todo_detail(request, id):
    todo =get_object_or_404(Todo, id=id)
    serializer = TodoDetailSerializer(todo)
    return Response(serializer.data)