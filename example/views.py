from django.shortcuts import render
from django.http import response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Review, Recipe
from .serializers import ReviewSerializer, RecipeSerializer
from rest_framework.permissions import AllowAny

@api_view(['GET', 'POST'])
def apiOverview(request):
	api_urls = {
		'Main':'/main/',
		'Reviews':'/reviews/',
        'About': '/About/',
        'Recipes': '/recipes/'
		}

	return Response(api_urls)


@api_view(['GET', 'POST'])
def getReviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        review = Review.objects.create(
        name=data['name'],
        email=data['email'],
        review=data['review']
        )
        serializer = ReviewSerializer(review, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)
     