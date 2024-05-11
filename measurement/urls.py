from django.urls import path
from .views import SensorDetailView, MeasurementCreateView, SensorListView

urlpatterns = [
    path('sensors/<int:sensor_id>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/', SensorListView.as_view()),
]
