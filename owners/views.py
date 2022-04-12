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

    def get(self, request):
        owners = Owner.objects.all() # owner테이블의 모든 레코드를 불러온다.
        results  = [] # owner를 출력할 리스트
        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        # owner = Owner.objects.get(name=data['owner'])
        owner = Owner.objects.get(id=data['owner'])
        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
        )
        return JsonResponse({'message' : 'created'}, status=201)
# http -v GET 127.0.0.1:8000/owners

    def get(self, request):
        owners = Owner.objects.all()
        dogs = Dog.objects.all() # owner테이블의 모든 레코드를 불러온다.
        results  = [] # owner를 출력할 리스트
        # for owner in owners:
        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name #주인 이름
                }
            )
        return JsonResponse({'results':results}, status=200)
# http -v GET 127.0.0.1:8000/owners/dogs

class OwnersDogView(View):
    def get(self, request):
        owners = Owner.objects.all()
        dogs = Dog.objects.all()
        results  = [] # owner를 출력할 리스트
        for dog in dogs:
            for owner in owners:
                if owner.id == dog.owner_id:
                    results.append(
                        {
                            "name" : owner.name,
                            "age" : owner.age,
                            "email" : owner.email,
                            "dog_name" : dog.name,
                            "dog_age" : dog.age
                        }
                    )
        return JsonResponse({'results':results}, status=200)