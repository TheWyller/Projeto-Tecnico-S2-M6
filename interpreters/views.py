from django.shortcuts import render
from rest_framework import generics
from .serializers import InterpreterSerializer
from .models import Interpreter
from django_filters import rest_framework as filters


class InterpreterView(generics.ListCreateAPIView):
    serializer_class = InterpreterSerializer
    queryset = Interpreter.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("store_name",)
