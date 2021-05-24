from django.contrib.auth.decorators import login_required
from django.urls import path

from dashboard.views import SensorListView, ValueListView, DataBasePageView, SensorDetailView, UsersSystemCreateView, \
    export_to_excel

urlpatterns = [
    path('sensor/', SensorListView.as_view(), name='sensor-list'),
    path('value/', ValueListView.as_view(), name='value-list'),
    path('dataBase/', DataBasePageView.as_view(), name='data-base-page'),
    path('detail/<int:id>/', SensorDetailView.as_view(), name='detail-sensor'),
    path('create/employee/', login_required(UsersSystemCreateView.as_view()), name='register_employee'),
    path('export_excel/<int:id>/', login_required(export_to_excel), name='export-excel')
]
