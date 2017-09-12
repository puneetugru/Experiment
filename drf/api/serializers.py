from .models import School
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'description')

    def create(self, validated_data):
        name = validated_data.get('name', None)
        description = validated_data.get('description', None)
        return School.objects.create(name=name, description='description')
