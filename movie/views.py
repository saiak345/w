from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from .serializers import MovieSerializers

from .models import *

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home.html', context)

@api_view(['GET'])
def movielist(request):
    movies=Movie.objects.all()
    serializer=MovieSerializers(movies,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def MovieCreate(request):
    serializer = MovieSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
