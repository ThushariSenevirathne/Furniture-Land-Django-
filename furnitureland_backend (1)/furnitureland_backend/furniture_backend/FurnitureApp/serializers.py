from rest_framework import serializers
from FurnitureApp.models import User, Furniture

#serializers

#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('UserId', 'UserName', 'Email', 'Password')

#furniture serializer
class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Furniture
        fields=('Id', 'ItemName', 'Price', 'Type', 'Description', 'ImageUrl')