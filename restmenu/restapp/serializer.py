from .models import Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    description = serializers.CharField(min_length=2, max_length=200)
    price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(min_value=1.00, max_value=100000, max_digits=None, decimal_places=2)

    class Meta:
        model = Menu
#        fields = ['price', 'course', 'name']
        fields = '__all__'


class MenuStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child= serializers.ListField(
            child=serializers.IntegerField(),
        )
    )