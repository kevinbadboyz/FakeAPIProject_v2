from rest_framework import serializers
from web_app.models import (
    User, Game, UserModel
)
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db.models import Avg, Max, Min, Sum 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'price', 'status')

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields =('id', 'firstName', 'lastName', 'gender', 'image')
    
