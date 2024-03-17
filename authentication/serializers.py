from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,min_length =3)
    password = serializers.CharField(max_length=255,min_length=6,write_only=True)

    class Meta :
        model  = User
        fields = ['email','password']
    
    def validate(self, attrs):
        email = attrs['email']
        try:
            user = User.objects.get(email=email)
            if user is not None:
                raise serializers.ValidationError("User with Email exists")
        except User.DoesNotExist :
            return attrs
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)    



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255,min_length=6)
    password = serializers.CharField(max_length=255,min_length = 5,write_only = True)
    token = serializers.SerializerMethodField()

    def get_token(self,attrs):
        user = User.objects.get(email = attrs['email'])
        return user.tokens()

    class Meta:
        model = User
        fields = ['email','password','token']

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        user = authenticate(email=email,password=password)
        if user is None:
            raise AuthenticationFailed("Please provide valid credentials")
        return attrs