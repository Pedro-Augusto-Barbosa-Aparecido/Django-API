from vehicle.models import Vehicle, Product
from django.views import View
from django.http import HttpResponse, JsonResponse

import json
from utils.generate_data import generate_slab_number


class VehicleCreateView(View):
    model = Vehicle
    content = {}

    def post(self, request, *args, **kwargs):
        obj = None

        branch = request.GET.get("branch", None)
        type_vehicle = request.GET.get("type_vehicle", None)

        if self.model.validate_branch(self.model, branch=branch) and \
                self.model.validate_type_vehicle(self.model, vehicle_type=type_vehicle):
            obj = self.model.objects.create(branch=branch, type_vehicle=type_vehicle)

            if Vehicle.validate_obj(obj.branch, obj.type_vehicle):
                obj.save()

        if obj:
            qs = self.model.objects.filter()
            self.content.results = []
            self.content.count_obj = qs.count()
            for _obj in qs:
                self.content.results.append({
                    'branch': _obj.branch,
                    'type_vehicle': _obj.type_vehicle
                })
        else:
            self.content.count_obj = 0

        return JsonResponse(
            data=self.content,
            status=200
        )


class ProductCreateView(View):
    model = Product
    content = {}

    def post(self, request, *args, **kwargs):
        obj = None

        price = request.GET.get("price", None)
        name = request.GET.get("name", None)
        model = request.GET.get("model", None)
        color = request.GET.get("color", None)
        description = request.GET.get("description", None)

        branch = request.GET.get("branch", None)
        type_vehicle = request.GET.get("type_vehicle", None)

        if self.model.validate_price(price) and self.model.validate_name(name) and self.model.validate_model(model) and self.model.validate_color(color) and self.model.validate_description(description):
            obj = self.model.objects.create(
                price=price,
                name=name,
                model=model,
                color=color,
                description=description,
                vehicle=self.get_vehicle(branch, type_vehicle),
                chassis=generate_slab_number(15),
                slab=generate_slab_number(5, 'Brazil - ')
            )

        if obj:
            obj.save()
            qs = self.model.objects.all()
            self.content.results = []
            self.content.count = self.model.objects.all().count()

            for _obj in qs:
                self.content.results.append({
                    "vehicle": {
                        "branch": _obj.vehicle.branch,
                        "type_vehicle": _obj.vehicle.type_vehicle
                    },
                    "name": _obj.name,
                    "model": _obj.model,
                    "description": _obj.description,
                    "color": _obj.color,
                    "price": _obj.price,
                    "chassis": _obj.chassis,
                    "slab": _obj.slab
                })
        else:
            self.content.count = 0

        return JsonResponse(
            data=self.content,
            status=200
        )

    def get_vehicle(self, branch=None, type_vehicle=None):
        if not branch or (type(branch) is not str) or not type_vehicle or (type(type_vehicle) is not str):
            raise ValueError("Vehicle invalid!")

        return Vehicle.objects.filter(branch=branch, type_vehicle=type_vehicle)
