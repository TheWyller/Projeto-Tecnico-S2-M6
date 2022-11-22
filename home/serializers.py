from rest_framework import serializers
from .models import Home
from utils.converter import converter_CNAB, read_CNAB_json
from interpreters.serializers import InterpreterSerializer


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

    def create(self, validated_data):
        txt_info, _ = Home.objects.get_or_create(validated_data)
        converter_CNAB()
        list_info = read_CNAB_json()
        for info in list_info:
            serializer = InterpreterSerializer(data=info)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return txt_info
