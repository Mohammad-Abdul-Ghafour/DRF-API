from django.shortcuts import render
from rest_framework import generics
from .serializers import FavSerialzer
from .models import Favorite

# CR views
class FavList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer

# RUD view
class FavDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer