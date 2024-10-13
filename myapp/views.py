from django.shortcuts import render
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)    


def drink_detail(request, id):

    try:

       drinks = Drinks.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status= status.HTTP_404_NOTFOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drinks )
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass        
