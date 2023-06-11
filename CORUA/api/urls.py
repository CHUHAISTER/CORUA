from django.urls import path

from .operations.find_account import find_account
from .views import  *

urlpatterns = [

    path('find_account', find_account, name='find_account'),
    path('keyw', keywordsView.as_view()),
    path('region', RegionView.as_view() ),
    path('vocab',vocabTermLORView.as_view() ),
    path('card', CardRView.as_view()),
    path('spellspeed', SpellSpeedView.as_view()),
    path('rarity', RarityView.as_view()),


]
