from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Photo
from .serializers import UserSerializer, PhotoSerializer

# En views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Photo
from .serializers import UserSerializer, PhotoSerializer

@api_view(['get','post'])
def user_list(request):#te trae el dato de la request
    if request.method=='get':#si se pidio agregar
        user=user.object.all()#accede a la tabla user y trae todo la data
        serializer=UserSerializer(user,may=True)
        #te compacta los datos en un json en el serializer
        return Response(serializer.data)
    # te devuelve esos datos en un json
    elif request.method('post'):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.http_404_bad_request)
        