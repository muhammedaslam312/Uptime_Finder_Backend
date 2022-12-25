from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from .serializers import AccountSerializer

from rest_framework import status,generics


# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(user)
        if user:
            token = super().get_token(user)

            # Add custom claims
            
            token['username'] = user.username
            token['email'] = user.email
        
           
            
           
            return token
        else:
            response = Response()

            response.data={
                'message': 'Invalid credential'
            }
            return response


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterAccount(APIView):

    serializer_class =AccountSerializer

    def post(self,request,format=None):
        print('*****')
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)  


#