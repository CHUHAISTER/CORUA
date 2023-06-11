from rest_framework import serializers

from .models import *


class vocabTermLORSerialisers(serializers.ModelSerializer):
    class Meta:
        model = vocabTermLOR
        fields = ("description", "name", "nameRef")
class SpellSpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpellSpeed
        fields = ('name', 'nameRef')

class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ('name', 'nameRef')
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('abbreviation', 'iconAbsolutePath', 'name', 'nameRef')
class keywordsSerialisers(serializers.ModelSerializer):
    class Meta:
        model = keywords
        fields = ("description", "name", "nameRef")
class CardSerialisers(serializers.ModelSerializer):
    spellSpeedRef = SpellSpeedSerializer()
    rarityRef = RaritySerializer()
    regionsRefs = RegionSerializer(many=True)

    class Meta:
        model = Card
        fields = '__all__'
