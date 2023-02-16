# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import statistics
from django.http import JsonResponse
from rest_framework import generics, viewsets

from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    def post(self, request):
        data = request.data
        Sensor.objects.create(name=data.get('name'), description=data.get('description'))
        return Response(data=data)
    
    
    
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer  

    def post(self, request):
        data = request.data
        Measurement.objects.create(sensor=data.get('sensor'), temperature=data.get('temperature'))
        return Response(data=data)

class SensorDetailViewSet(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer  
    
    def patch(self, request, pk):
        data = request.data
        name, description = data.get('name'), data.get('description')
        sensor = Sensor.objects.filter(id=pk).all()
        if name:
            sensor.update(name=name)
        if description:
            sensor.update(description=description)
        return Response(data=data)  
        