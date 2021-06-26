from vehicle.models import Product
from django.views import View
from django.http import HttpResponse, JsonResponse

import json
from utils.generate_data import generate_slab_number


class ProductCreateView(View):
    model = Product
    content = {}

    def post(self, request, *args, **kwargs):
        obj = None

        name = request.GET.get("name", None)
        price = request.GET.get("price", None)
        model = request.GET.get("model", None)
        color = request.GET.get("color", None)
        branch = request.GET.get("branch", None)
        description = request.GET.get("description", None)

        p = self.model.validate_price(price)
        n = self.model.validate_name(name)
        m = self.model.validate_model(model)
        c = self.model.validate_color(color)
        d = self.model.validate_description(description)
        b = self.model.validate_branch(branch)

        if p and n and m and c and d and b:
            obj = self.model.objects.create(
                price=price,
                name=name,
                model=model,
                color=color,
                description=description,
                branch=branch,
                chassis=generate_slab_number(15),
                slab=generate_slab_number(4, 'BRA')
            )

        if obj:
            obj.save()
            self.content['results'] = []
            self.content['count'] = 1

            self.content['results'].append({
                "branch": obj.branch,
                "name": obj.name,
                "model": obj.model,
                "description": obj.description,
                "color": obj.color,
                "price": obj.price,
                "chassis": obj.chassis,
                "slab": obj.slab
            })

        else:
            self.content['count'] = 0

        return JsonResponse(
            data=self.content,
            status=200
        )
