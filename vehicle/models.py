from django.db import models
from django.db.models import Model

# Create your models here


class Product(Model):
    __COLORS = (
        "Vermelho",
        "Amarelo",
        "Verde",
        "Cinza",
        "Preto"
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

    price = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=30, blank=False, null=False)
    color = models.CharField(max_length=10, blank=False, null=False)
    slab = models.CharField(max_length=9, blank=False, null=False)
    chassis = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    branch = models.CharField(max_length=40, blank=False, null=False)

    class Meta:
        ordering = ("name", )
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f'{self.name} - Marca: {self.branch} - Modelo: {self.model}'

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

        for cor in Product.__COLORS:
            if cor == color:
                return True

        return False

    @staticmethod
    def validate_description(description=None):
        if type(description) is not str:
            raise ValueError(f"The description {description} is invalid!")

        return True

    @staticmethod
    def validate_branch(branch=None):
        if not branch or (type(branch) is not str):
            raise ValueError("Branch invalid!")

        for _branch in Product.__BRANCH_POSSIBLES:
            if branch.upper() == _branch:
                return True

        return False

    @property
    def attributes(self):
        return {
            "branch": self.branch,
            "name": self.name,
            "model": self.model,
            "description": self.description,
            "color": self.color,
            "price": self.price,
            "chassis": self.chassis,
            "slab": self.slab,
            "id": self.pk
        }
