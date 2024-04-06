from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Comment
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class PostView(APIView,PageNumberPagination):
    
    permission_classes = (IsAuthenticated,)
    page_size = 5
    def get(self,request):
        # user_id = request.user.id
        obj = Post.objects.all()
        page = self.paginate_queryset(obj,request)
        
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        data["author"] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class commentView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self,request,post_id):
        obj = Comment.objects.filter(post_on =post_id)
        serializer = CommentSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request,post_id):
        data = request.data
        data["author"] = request.user.id
        try:
            Post.objects.get(pk = post_id)
        except Post.DoesNotExist:
            return Response("post_id not found",status=status.HTTP_404_NOT_FOUND)
        data["post_on"] = post_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class postUpdateDeleteView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self,request,post_id):
        obj = self.get_object(post_id)
        serializer = PostSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,post_id):
        obj = self.get_object(post_id)
        data = request.data
        serializer = PostSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,post_id):
        obj = self.get_object(post_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class commentUpdateDeleteView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        obj = self.get_object(pk)
        serializer = CommentSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        obj = self.get_object(pk)
        data = request.data
        serializer = CommentSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LikesUpdateView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def post(self,request,pk):
        obj = self.get_object(pk)
        user = request.user
        if(request.user in obj.likes.all()):
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
        serializer = PostSerializer(obj)
        return Response({"likes":serializer.data["likes"],
                         "like_counts":obj.likes.count()},
                        status=status.HTTP_200_OK)