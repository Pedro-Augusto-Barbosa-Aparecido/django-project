import csv
import os

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.shortcuts import render
from django.http import Http404, HttpResponse, FileResponse

# Create your views here.
from dashboard.forms import UsersSystemForm
from dashboard.models import Sensor, Value

import pandas as pd
import io


class SensorListView(ListView):
    model = Sensor
    template_name = 'dashboard/listObjects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Lista de sensores"
        context['header_table_0'] = 'Modelo'
        context['header_table_1'] = 'Tipo'
        context['title_page'] = "List Sensor"
        context['type_object'] = 'sensors'
        context['type'] = 0
        context['mensage'] = 'sensore cadastrados na Empresa'

        return context


class ValueListView(ListView):
    model = Value
    template_name = 'dashboard/listObjects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_page'] = 'Values List'
        context['title'] = "Listagem dos valores lidos"
        context['type_object'] = 'value'
        context['type'] = 1
        context['mensage'] = "valores lidos pelos sensores cadastrados na Empresa"
        context['header_table_0'] = 'Sensor'
        context['header_table_1'] = 'Valor lido'

        return context


class SensorDetailView(View):

    @staticmethod
    def get(request, id):
        sensor = Sensor.objects.get(pk=id)

        context = {
            'title_page': 'Sensor Detail',
            'titulo': f'Detail of Sensor {sensor}',
            'sensor': sensor,
            'values': SensorDetailView.get_values_sensor(sensor),
            'home': False
        }

        return render(request, 'dashboard/SensorDetail.html', context)

    @classmethod
    def get_values_sensor(cls, sensor: Sensor):
        values = Value.objects.filter(id_sensor__id=sensor.pk)

        return values


class DataBasePageView(View):

    @staticmethod
    def get(request):

        qs_sensor = Sensor.objects.all()
        qs_values = Value.objects.all()

        context = {
            'sensors': qs_sensor if len(qs_sensor) < 5 else qs_sensor[:5],
            'values': qs_values if len(qs_values) < 5 else qs_values[:5],
            'title_page': "Data Base",
            'home': True
        }

        return render(request, 'dashboard/ChoiceDataPage.html', context)


class UsersSystemCreateView(View):

    @staticmethod
    def get(request):
        template_name = 'dashboard/RegisterEmployee.html'
        form = UsersSystemForm()

        context = {
            'title_page': 'Register Employee',
            'home': False,
            'form': form
        }

        return render(request, template_name, context)

    # @staticmethod
    # def post(request):
    #     new_employee = request.POST
    #
    #     return


def export_to_excel(request, id):
    def __how_many_duplicates_in_sensor_df(df: pd.DataFrame):
        df_aux = df.drop_duplicates()
        list_sensor = list(df_aux['model'])
        __return = []
        for i in range(len(list_sensor)):
            _aux = df['model'] == list_sensor[i]
            __return.append(df[_aux].shape[0])

        return __return

    qs_sensor = Sensor.objects.all().values_list(flat=True)
    qs_values = Value.objects.all().values_list(flat=True)

    if id == 0:
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="export.csv"'},
        )

        df = pd.DataFrame(qs_sensor, columns=['model', 'type_sensor'])

        duplicates = __how_many_duplicates_in_sensor_df(df=df)
        df.drop_duplicates(inplace=True)
        df.index = range(df.shape[0])

        data = pd.DataFrame([duplicates], columns=['Quantidade'])

        file = pd.concat([df, data])
        file.to_csv(path_or_buf='exports/export.csv', sep=';')

        response.headers['Content-Disposition'] = f'attachment; filename="exports/export.csv"'

        return response




