from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from home.models import *

class RegisterAuthSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    cpassword = serializers.CharField(write_only=True)
    class Meta:
        model = Auth
        fields = ('username','password','Name','Gender','Is_worker','Is_customer','cpassword')

    def validate(self, attrs):
        error = ''
        if attrs['Is_worker'] and attrs['Is_customer']:
            error = "User cannot be both worker and customer"
            raise serializers.ValidationError(error)
        if not attrs['password'] or not attrs['cpassword']:
            error = "Password and Confirm Password must be filled"
            raise serializers.ValidationError(error)
        if attrs['password'] != attrs['cpassword']:
            error = "Password and Confirm Password must be same"
            raise serializers.ValidationError(error)
        if not attrs['Is_worker'] and not attrs['Is_customer']:
            error = "User must be either worker or customer"
            raise serializers.ValidationError(error)
        if Auth.objects.filter(username=attrs['username']).exists():
            error = "Username already exists"
            raise serializers.ValidationError(error)
        return attrs
    
    
    def create(self, validated_data):
        auth = Auth.objects.create(
            username = validated_data['username'],
            Name = validated_data['Name'],
            Gender = validated_data['Gender'],
            Is_worker = validated_data['Is_worker'],
            Is_customer = validated_data['Is_customer'],
        )
        
        auth.set_password(validated_data['password'])
        auth.save()
        return auth
    
    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        data = {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }
        return data
    
    def get_id (self):
        id = Auth.objects.get(username=self.validated_data['username']).id
        return id

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = (AllowAny,)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['Name'] = user.Name
        token['Gender'] = user.Gender
        token['Is_worker'] = user.Is_worker
        token['Is_customer'] = user.Is_customer
        
        # ...

        return token