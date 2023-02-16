import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

import ads
from ads.models import Category, Ads


def ok(request):
    return JsonResponse({"status":"ok"})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.pk,
            "name": category.name
        })
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            "id": ads.pk,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })

@method_decorator(csrf_exempt, name='dispatch')
class AdsListCreateView(View):
    def get(self, request):
        ads_list = Ads.objects.all()

        response = []
        for ads in ads_list:
            response.append({
                "id": ads.pk,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        new_ads = Ads.objects.create(**ads_data)
        return JsonResponse({
            "id": new_ads.pk,
            "name": new_ads.name,
            "author": new_ads.author,
            "price": new_ads.price,
            "description": new_ads.description,
            "address": new_ads.address,
            "is_published": new_ads.is_published
        })

@method_decorator(csrf_exempt, name='dispatch')
class CatListCreateView(View):
    def get(self, request):
        cat_list = Category.objects.all()

        response = []
        for cat in cat_list:
            response.append({
                "id": cat.pk,
                "name": cat.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        new_cat = Category.objects.create(**cat_data)
        return JsonResponse({
            "id": new_cat.pk,
            "name": new_cat.name,
                    })