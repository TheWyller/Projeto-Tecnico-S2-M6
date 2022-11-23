from rest_framework import serializers
from .models import Interpreter
import ipdb


class InterpreterSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(max_length=19)
    sum_all = serializers.SerializerMethodField()

    class Meta:
        model = Interpreter
        fields = '__all__'

    def create(self, validated_data):
        return Interpreter.objects.get_or_create(**validated_data)[0]

    def get_sum_all(self, obj):
        list_obj = Interpreter.objects.filter(store_name=obj.store_name)
        sum = 0
        for obj in list_obj:
            if (
                    obj.type.type != 2 and
                    obj.type.type != 3 and
                    obj.type.type != 9):
                sum += obj.value
            else:
                sum -= obj.value
        return str(sum)
