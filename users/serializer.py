from .models import CustomUser

from rest_framework import serializers


class CustomUserSerilizer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
# __all__ => 
# actually does internally
# Django REST Framework:
# Reads model fields
# Maps them to serializer fields
# Applies validation
# Generates API schema