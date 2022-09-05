from django.db.models import fields
# from fitbit.views import getactivitylog
from .models import *
from  rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user




class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model : CustomUser
        fields = '__all__'
