from django.shortcuts import render
from rest_framework  import generics
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *

# Create your views here.
class vocabTermLORView(generics.ListAPIView):
    queryset = vocabTermLOR.objects.all()
    serializer_class = vocabTermLORSerialisers

class RarityView(generics.ListAPIView):
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer

class RegionView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class SpellSpeedView(generics.ListAPIView):
    queryset = SpellSpeed.objects.all()
    serializer_class = SpellSpeedSerializer


class keywordsView(generics.ListAPIView):
    queryset = keywords.objects.all()
    serializer_class = keywordsSerialisers

class CardPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CardRView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerialisers
    pagination_class = CardPagination

