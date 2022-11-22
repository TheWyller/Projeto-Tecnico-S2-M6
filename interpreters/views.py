from django.shortcuts import render
from rest_framework import generics
from .serializers import InterpreterSerializer
from .models import Interpreter


class InterpreterView(generics.ListCreateAPIView):
    serializer_class = InterpreterSerializer
    queryset = Interpreter.objects.all()
