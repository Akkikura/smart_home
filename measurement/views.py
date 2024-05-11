from datetime import datetime

from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer


class SensorDetailView(APIView):
    def get(self, request, sensor_id):
        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"error": "Датчик с указанным ID не найден"}, status=status.HTTP_404_NOT_FOUND)

        sensor_data = SensorSerializer(sensor).data
        measurements = Measurement.objects.filter(sensor=sensor)
        measurement_data = MeasurementSerializer(measurements, many=True).data
        sensor_data['measurements'] = measurement_data

        return Response(sensor_data)
    def patch(self, request, sensor_id):
        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"error": "Датчик с указанным ID не найден"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SensorSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementCreateView(APIView):
    def post(self, request):
        sensor_id = request.data.get('sensor')
        temperature = request.data.get('temperature')

        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"error": "Датчик с указанным ID не найден"}, status=status.HTTP_404_NOT_FOUND)
        measurement_data = {
            "sensor": sensor_id,
            "temperature": temperature
        }

        serializer = MeasurementSerializer(data=measurement_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorListView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
