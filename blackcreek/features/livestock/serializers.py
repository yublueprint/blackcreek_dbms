from rest_framework import serializers
from .models import Livestock

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'

    def __str__(self):
        return f"LivestockSerializer for {self.Meta.model.__name__}"