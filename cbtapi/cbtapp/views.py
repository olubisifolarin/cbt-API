from contextlib import redirect_stderr
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .serializer import *
from .models import *



# Create your views here.

permission_classes = (permissions)

class QuizzesView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
        return Response(serializer.data)
    
class AnswerView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Answer.objects.all()
        serializer = Answerserializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = Answerserializer(data=request.data)
        if serializer.is_valid():    
            serializer.save
        return Response(serializer.data)
        
        
    
    
        
        

        

            
            
        
        
    
    
