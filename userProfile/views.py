from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import userRegisterSerializer
from rest_framework.views import APIView

class UserRegister(APIView):

    def post(self,requset):
        data = requset.data
        serializer = userRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Status":"Account Created with username: {}".format(
                    serializer.data["username"])},
                    status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        

class CheckGet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        print(request.user)
        return Response("just for checking")


