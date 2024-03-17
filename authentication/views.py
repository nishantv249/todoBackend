from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer
    

    def post(self, request):
        serilizer = self.get_serializer(data = request.data)
        serilizer.is_valid(raise_exception = True)
        return Response(serilizer.data,status=status.HTTP_200_OK)