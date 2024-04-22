from rest_framework import serializers
from members.models import Task

class Memberserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'