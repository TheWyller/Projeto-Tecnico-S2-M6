from rest_framework import serializers
from .models import Home
from utils.converter import converter_CNAB, read_CNAB_json
from interpreters.serializers import InterpreterSerializer
import os
from django.contrib import messages
import ipdb


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

    def create(self, validated_data):
        file = validated_data.get('file')
        if file.name != 'CNAB.txt':
            raise NameError("Nome do arquivo está errado, deve ser CNAB.txt")

        txt_info = Home.objects.create(**validated_data)
        converter_CNAB()

        list_info = read_CNAB_json()
        for info in list_info:
            serializer = InterpreterSerializer(data=info)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if os.path.isfile('infos/CNAB.txt'):
            os.remove('infos/CNAB.txt')
        return txt_info
