# from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message' : 'created'}, status=201)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])
        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
        )
        return JsonResponse({'message' : 'created'}, status=201)