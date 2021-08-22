from rest_framework import serializers
from .models import Students
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator


class StudentSerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user'''

    class Meta:
        
        model = Students
        fields = '__all__'
    
        '''validators = [
                UniqueTogetherValidator(
                    queryset=User.objects.all(),
                    fields = ['username', 'email']
                )
            ]'''