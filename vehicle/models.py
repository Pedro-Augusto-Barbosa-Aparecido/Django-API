from django.db import models
from django.db.models import Model

# Create your models here


class Vehicle(Model):

    CAR = "CAR"
    TRUCK = "CAM"
    MOTO = "MOT"
    CAMINHONETE = "CRM"

    __TYPE_VEHICLES = (
        "Carro",
        "Caminhão",
        "Moto",
         "Caminhonete",
    )

    __BRANCH_POSSIBLES = (
        'VOLKSWAGEN', 'GUERRA', 'SCANIA', 'MERCEDES BENZ',
        'LOIBRELATTO', 'FACCHINI', 'RANDON', 'LIBRELATTO', 'FORD', 'VOLVO',
        'FACHINI', 'JARDINOX', 'RECRUSUL', 'MERCEDES-BENZ', 'IVECO',
        'KRONE', 'MAN', 'TRIEL', 'RODOLINEA', 'FIBRASIL', 'NOMA', 'SOUFER',
        'SCHIFFER', 'RANSON', 'LIBRELATO', 'MARINO', 'GURRA', 'MANN',
        'MERCEDZ BENS', 'FACCHINI TANQUE', 'FACCIHINI', 'RANDONSP', 'GUERA',
        'ELLFEN', 'LIBERATO', 'DAF', 'VOVLO', 'IDAF', 'MERCEDES BENZA',
        'RANDN', 'FACCHIN', 'VOLKSWAGEM', 'RAMDON', 'RODOTECNICA', 'FORS',
        'THERMOSUL', 'NOMAQ', 'FACHIN'
    )

    branch = models.CharField(max_length=40, blank=False, null=False)
    type_vehicle = models.CharField(max_length=3, blank=False, null=False)

    class Meta:
        ordering = ("branch", )
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return f"{self.branch} - {self.type_vehicle}"

    @staticmethod
    def validate_branch(self, branch=None):
        if not branch or (type(branch) is not str):
            raise ValueError("Branch invalid!")

        for _branch in self.__BRANCH_POSSIBLES:
            if branch.upper() == _branch:
                return True

        return False

    @staticmethod
    def validate_type_vehicle(self, vehicle_type=None):
        if not vehicle_type or (type(vehicle_type) is not str):
            raise ValueError(f'{vehicle_type} is a vehicle invalid!')

        for type_vehicle in self.__TYPE_VEHICLES:
            if vehicle_type.capitalize() == type_vehicle:
                return True

        return False

    @classmethod
    def validate_obj(cls, obj_branch, obj_type):
        if cls.objects.filter(branch=obj_branch, type_vehicle=obj_type):
            raise Exception(f'The object with branch: {obj_branch} and type: {obj_type}, already exist!')
        else:
            return True


class Product(Model):
    COLORS = (
        "Vermelho",
        "Amarelo",
        "Verde",
        "Cinza",
        "Preto"
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT,)
    price = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=30, blank=False, null=False)
    color = models.CharField(max_length=3, blank=False, null=False)
    slab = models.CharField(max_length=9, blank=False, null=False)
    chassis = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ("name", )
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f'{self.name} - Marca: {self.vehicle.branch} - Modelo: {self.model}'

    @staticmethod
    def validate_price(price=None):
        if not price or (type(price) is not str):
            raise ValueError(f"The price: {price} is invalid!")

        value = price[(price.find('$') + 2):]
        value = value.replace(',', '.')

        try:
            float(value)
            return True
        except Exception as e:
            print(e.args)
            raise ValueError(f"Value of coin {price} is invalid!")

    @staticmethod
    def validate_name(name=None):
        if not name or (type(name) is not str):
            raise ValueError(f"The name {name} is invalid!")

        return True

    @staticmethod
    def validate_model(model=None):
        if not model or (type(model) is not str):
            raise ValueError(f"The model {model} is invalid!")

        return True

    @staticmethod
    def validate_color(color=None):
        if not color or (type(color) is not str):
            raise ValueError(f"The color {color} is invalid!")

        for cor in Product.COLORS:
            if cor == color:
                return True

        return False

    @staticmethod
    def validate_description(description=None):
        if type(description) is not str:
            raise ValueError(f"The description {description} is invalid!")

        return True
