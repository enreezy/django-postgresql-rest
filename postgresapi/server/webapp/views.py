from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemsSerializer

def edit(request, id):
	item = Items.objects.get(pk=id)
	lst = {'itemname':item.itemname, 'quantity': item.quantity, 'price': item.price}
	return JsonResponse(lst)


class ItemsList(APIView):

	def get(self, request):
		items = Items.objects.all()
		serializer = ItemsSerializer(items, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ItemsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, id):
		items = Items.objects.get(id=id)
		serializer = ItemsSerializer(items, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

	def delete(self, request, id):
		items = Items.objects.get(id=id)
		items.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)