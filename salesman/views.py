from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from salesman.models import Salesman, Sell
from vehicle.models import Product


class SalesmanCreateView(View):

    def post(self, request):
        content = {}

        name = request.GET.get("name", None)

        if name:
            obj = Salesman.objects.create(name=name)

            content['results'] = [obj.attribute]
            content['count'] = 1

            return JsonResponse(
                data=content,
                status=200
            )

        return HttpResponse("Impossible create Salesman", status=200)


class SalesmanDetailView(View):

    def get(self, request, pk):
        return JsonResponse(
            data=Salesman.objects.filter(pk=pk)[0].attribute
            , status=200)


class SalesmanDeleteView(View):

    def post(self, request, pk):
        try:
            Salesman.objects.filter(pk=pk)[0].delete()
            return HttpResponse(f"Salesman {pk} was deleted")
        except:
            return HttpResponse(f"Were impossible delete salesman {pk}")


class SalesmanListView(View):
    def get(self, request):
        qs = Salesman.objects.all()

        return JsonResponse(
            data={
                "results": [obj.attribute for obj in qs],
                "count": qs.count()
            }, status=200)


class SellCreateView(View):
    def post(self, request):
        product_pk = request.GET.get("product_pk", None)
        salesman_pk = request.GET.get("salesman_pk", None)
        quantity = request.GET.get("quantity", 1)

        if product_pk and salesman_pk:
            price = Product.objects.filter(pk=product_pk)[0].price

            price = Sell.get_price(price)
            fn_price = price * float(quantity)

            sell = Sell.objects.create(
                product=Product.objects.filter(pk=product_pk)[0],
                salesman=Salesman.objects.filter(pk=salesman_pk)[0],
                finally_price=fn_price,
                quantity=quantity
            )

            return JsonResponse(
                data={
                    "results": sell.attribute,
                    "count": 1
                }, status=200)

        return HttpResponse(status=500)


class SellDetailView(View):
    def get(self, request, pk):
        return JsonResponse(
            data={
                "results": Sell.objects.filter(pk=pk)[0].attribute,
                "count": 1
            }, status=200)


class SellListView(View):
    def get(self, request):
        qs = Sell.objects.all()

        return JsonResponse(data={
            "results": [obj.attribute for obj in qs],
            "count": qs.count()
        }, status=200)


class SellListViewBySalesman(View):
    def get(self, request, pk):
        if pk:
            qs = Sell.objects.filter(salesman_id=pk)

            return JsonResponse(
                data={
                    "results": [obj.attribute for obj in qs],
                    "count": qs.count()
                }
            )

        else:
            return HttpResponse(status=500)
