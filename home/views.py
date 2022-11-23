from django.shortcuts import render
from rest_framework import generics
from .serializers import HomeSerializer
from .models import Home


class HomeView(generics.CreateAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
