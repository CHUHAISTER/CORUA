from django.db import models



class vocabTermLOR(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(unique=True,max_length=50)
    nameRef = models.CharField(unique=True,max_length=50)

class Region(models.Model):
    abbreviation = models.CharField(max_length=10)
    iconAbsolutePath = models.URLField()
    name = models.CharField(unique=True,max_length=50)
    nameRef = models.CharField(unique=True,max_length=50)
class keywords(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    nameRef = models.CharField(max_length=50)

class SpellSpeed(models.Model):
    name = models.CharField(unique=True,max_length=50)
    nameRef = models.CharField(unique=True,max_length=50)

class Rarity(models.Model):
    name = models.CharField(unique=True,max_length=50)
    nameRef = models.CharField(unique=True,max_length=50)
class Card(models.Model):
    associatedCards = models.JSONField(default=list)
    associatedCardRefs = models.JSONField(default=list)
    assets = models.JSONField(default=list)
    regions = models.JSONField(default=list)
    regionsRefs = models.ManyToManyField(Region)
    attack = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    descriptionRaw = models.CharField(max_length=255)
    levelupDescription = models.CharField(max_length=255)
    levelupDescriptionRaw = models.CharField(max_length=255)
    flavorText = models.TextField()
    artistName = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    cardCode = models.CharField(unique=True, max_length=10)
    keywords = models.JSONField(default=list)
    keywordRefs = models.JSONField(default=list)
    spellSpeed = models.CharField(max_length=50)
    spellSpeedRef = models.ForeignKey(SpellSpeed, on_delete=models.CASCADE)
    rarity = models.CharField(max_length=50)
    rarityRef = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    subtypes = models.JSONField(default=list)
    supertype = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    collectible = models.BooleanField(default=False)
    set = models.CharField(max_length=50)
    formats = models.JSONField(default=list)
    formatRefs = models.JSONField(default=list)
