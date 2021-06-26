from vehicle.models import Product
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404

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
                "slab": obj.slab,
                "id": obj.pk
            })

        else:
            self.content['count'] = 0

        return JsonResponse(
            data=self.content,
            status=200
        )


class ProductDetailView(View):

    model = Product
    content = {}

    def get(self, request, pk=None):

        ids = request.GET.get("ids", None)

        if pk is None:
            return Http404("Product id is null")

        if ids:
            ids = ids.split(',')

        if pk != 0:
            obj = Product.objects.filter(pk=pk)
            if len(obj) > 0:
                self.content['results'] = [obj[0].attributes]
                self.content['count'] = 1
            else:
                self.content['results'] = [
                    {
                        "message": "No Items on base"
                    }
                ]
                self.content['count'] = 0

            return JsonResponse(
                data=self.content,
                status=200
            )

        if (pk == 0) and (len(ids) > 1):
            qs = Product.objects.filter(pk__in=ids)
            self.content['results'] = []

            for product in qs:
                self.content['results'].append(product.attributes)

            self.content['count'] = qs.count()

            return JsonResponse(
                data=self.content,
                status=200
            )

        return JsonResponse({
            "results": [],
            "count": 0
        }, status=200)


class ProductDeleteView(View):

    model = Product
    content = {}

    def post(self, request, pk=None):
        ids = request.GET.get("ids", None)

        if pk is None:
            return Http404("Invalid request")

        if ids:
            ids = ids.split(',')

        if pk != 0:
            try:
                Product.objects.filter(pk=pk).delete()

                return HttpResponse(status=200, content=f"Model with id: {pk} was deleted!")

            except:
                return HttpResponse("Erroor")

        if pk == 0 and len(ids) > 1:
            try:
                Product.objects.filter(pk__in=ids).delete()

                return HttpResponse(status=200, content=f"Models with ids: {ids} were deleted!")

            except Exception as e:
                return Http404(f"{e.args}")

        return HttpResponse("Error")


class ProductListView(View):
    model = Product
    content = {}

    def get(self, request):

        qs = self.model.objects.all()
        self.content['results'] = [
            obj.attributes for obj in qs
        ]

        self.content['count'] = qs.count()

        return JsonResponse(
            data=self.content,
            status=200
        )


class ProductUpdateView(View):

    model = Product
    content = {}

    def post(self, request, pk):
        name = request.GET.get("name", None)
        slab = request.GET.get("slab", None)
        chassis = request.GET.get("chassis", None)
        price = request.GET.get("price", None)
        model = request.GET.get("model", None)
        color = request.GET.get("color", None)
        branch = request.GET.get("branch", None)
        description = request.GET.get("description", None)

        p = self.model.validate_price(price) if price else False
        n = self.model.validate_name(name) if name else False
        m = self.model.validate_model(model) if model else False
        c = self.model.validate_color(color) if color else False
        d = self.model.validate_description(description) if description else False
        b = self.model.validate_branch(branch) if branch else False
        s = True if slab else False
        e = True if chassis else False

        if pk is None:
            return Http404("Error")

        if pk != 0:
            obj = self.model.objects.filter(pk=pk)
            obj = obj[0]

            if p:
                obj.update(name=name)
            if n:
                obj.update(price=price)
            if m:
                obj.update(model=model)
            if c:
                obj.update(color=color)
            if d:
                obj.update(description=description)
            if b:
                obj.update(branch=branch)
            if s:
                obj.update(slab=slab)
            if e:
                obj.update(chassis=chassis)

            obj.save()

            self.content['results'] = [obj.attributes]
            self.content['count'] = 1

            return JsonResponse(
                data=self.content,
                status=200
            )


