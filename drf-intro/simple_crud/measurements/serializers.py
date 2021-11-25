# TODO: опишите сериализаторы
from rest_framework.serializers import ModelSerializer

from measurements.models import Project, Measurement


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class MeasurementSerializer(ModelSerializer):
    #project = ProjectSerializer(many=True)
    class Meta:
        model = Measurement
        fields = '__all__'