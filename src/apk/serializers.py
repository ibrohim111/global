from rest_framework import serializers
from .models import GlobalData

class GlobalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalData
        fields = ['id', 'file', 'text', 'number', 'created_at']
