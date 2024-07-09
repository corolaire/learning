from rest_framework import serializers
from .models import User, Photo

class Userserializer(serializers.ModelSerializer):
    class Meta():
        model:User
        fields:'id , user_name ,user_phone ,user_lastname'

class Photoserializer(serializers.ModelSerializer):
    class Meta():
       model=Photo
       fields= 'id ,name'