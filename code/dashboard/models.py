from django.db import models


class Sensor(models.Model):

    NO_COLOR = 'v'
    RED = 'r'
    GREEN = 'g'
    BLUE = 'b'

    COLOR = 'C'
    CURRENT = 'A'
    VOLTAGE = 'V'
    LEVEL = 'L'
    FLOW_RATE = 'F'
    TEMPERATURE = 'T'

    TYPES_SENSORS = [
        (COLOR, "COR"),
        (CURRENT, "CORRENTE"),
        (VOLTAGE, "TENSÃO"),
        (LEVEL, "NÍVEL"),
        (FLOW_RATE, "VAZÃO"),
        (TEMPERATURE, "TEMPERATURA"),
    ]

    SENSOR_COLOR_CHOICE = [
        (NO_COLOR, 'Sem Cor'),
        (RED, 'Vermelho'),
        (GREEN, 'Verde'),
        (BLUE, 'Azul'),
    ]

    model = models.CharField(null=False, blank=False, max_length=20)
    type_sensor = models.CharField(null=True, blank=True, max_length=25, choices=TYPES_SENSORS)
    type_sensor_str = ''

    @staticmethod
    def __str_type(type_sensor=None):
        if not(type_sensor is None):
            if type_sensor == 'C':
                return "Cor"
            if type_sensor == 'A':
                return "Amperagem"
            if type_sensor == 'V':
                return "Voltagem"
            if type_sensor == 'L':
                return "Nível"
            if type_sensor == 'F':
                return "Vazão"
            if type_sensor == 'T':
                return "Temperatura"
        return f'None Type'

    @staticmethod
    def return_class_style(type_sensor=None):
        if not(type_sensor is None):
            if type_sensor == 'C':
                return "table-primary"
            if type_sensor == 'A':
                return "table-secondary"
            if type_sensor == 'V':
                return "table-success"
            if type_sensor == 'L':
                return "table-info"
            if type_sensor == 'F':
                return "table-warning"
            if type_sensor == 'T':
                return "table-light"
        return 'table-danger'

    @property
    def type_sensor_str(self):
        return self.__str_type(self.type_sensor)

    def __str__(self):
        return f'{self.model}'


class UsersSystem(models.Model):

    TRAINEE = 'T'
    SPECIALIST = 'S'
    PROFESSIONAL = 'P'
    JANITOR = 'J'
    COUNTER = 'C'
    WRITER = 'W'
    LAYER = 'L'
    DEVELOPER = 'D'

    OFFICES = [
        (TRAINEE, 'ESTÁGIARIO'),
        (SPECIALIST, 'ESPECIALISTA'),
        (PROFESSIONAL, 'PROFICIONAL'),
        (JANITOR, 'FAXINEIRO'),
        (COUNTER, 'CONTADOR'),
        (WRITER, 'PO'),
        (LAYER, 'ADVOGADO'),
        (DEVELOPER, 'DESENVOLVEDOR'),
    ]

    name = models.CharField(null=False, blank=False, max_length=255, default="", verbose_name="Nome do Funcionário:")
    email = models.EmailField(blank=False, null=False, max_length=255, verbose_name="Email")
    password = models.CharField(blank=False, null=False, max_length=20, verbose_name="Senha")
    confirmation_password = models.CharField(blank=False, null=False, max_length=20, verbose_name="Confirmação de Senha")
    office = models.CharField(blank=False, null=False, max_length=20, verbose_name="Cargo na Empresa", default=TRAINEE, choices=OFFICES)

    def __str__(self):
        return self.name


class Value(models.Model):

    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,)
    value = models.CharField(blank=False, null=False, max_length=10)
    value_show = ''

    @property
    def value_show(self):
        return f'Valor: {self.value}'

    def __str__(self):
        return f'Valor do sensor {self.id_sensor.model}'
