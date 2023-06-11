from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(vocabTermLOR)
admin.site.register(Region)
admin.site.register(keywords)
admin.site.register(SpellSpeed)
admin.site.register(Rarity)
admin.site.register(Card)

