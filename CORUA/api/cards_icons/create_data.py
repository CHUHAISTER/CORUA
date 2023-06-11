import json

from ..models import *


def create_card(item):
    card = Card()
    card.associatedCards = item.get("associatedCards", [])
    card.associatedCardRefs = item.get("associatedCardRefs", [])
    card.assets = item.get("assets", [])
    card.attack = item.get("attack", 0)
    card.cost = item.get("cost", 0)
    card.regions = item.get("regions", [])
    card.health = item.get("health", 0)
    card.description = item.get("description", "")
    card.descriptionRaw = item.get("descriptionRaw", "")
    card.levelupDescription = item.get("levelupDescription", "")
    card.levelupDescriptionRaw = item.get("levelupDescriptionRaw", "")
    card.flavorText = item.get("flavorText", "")
    card.artistName = item.get("artistName", "")
    card.name = item.get("name", "")
    card.cardCode = item.get("cardCode", "")
    card.keywords = item.get("keywords", [])
    card.keywordRefs = item.get("keywordRefs", [])
    card.spellSpeed = item.get("spellSpeed", "")
    card.rarity = item.get("rarity", "")
    card.subtypes = item.get("subtypes", [])
    card.supertype = item.get("supertype", "")
    card.type = item.get("type", "")
    card.collectible = item.get("collectible", False)
    card.set = item.get("set", "")
    card.formats = item.get("formats", [])
    card.formatRefs = item.get("formatRefs", [])

    regions = item.get("regions", [])
    spellSpeedRef = item.get("spellSpeedRef", "")


    spell_speed_ref = SpellSpeed.objects.get(nameRef=spellSpeedRef)
    card.spellSpeedRef = spell_speed_ref


    rarityRef = item.get("rarityRef", "")


    rarity_ref = Rarity.objects.get(nameRef=rarityRef)
    card.rarityRef = rarity_ref
    card.save()
    regions_refs = Region.objects.filter(name__in=regions)
    card.regionsRefs.add(*regions_refs)

    card.save()


    return card

def create_all_card():
    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set1-lite-en_us\\en_us\\data\\set1-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()



    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set2-lite-en_us\\en_us\\data\\set2-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()

    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set3-lite-en_us\\en_us\\data\\set3-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()

    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set4-lite-en_us\\en_us\\data\\set4-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()

    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set5-lite-en_us\\en_us\\data\\set5-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()

    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set6cde-lite-en_us\\en_us\\data\\set6cde-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()

    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set7-lite-en_us\\en_us\\data\\set7-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()


def create_vocab_terms(data):
    for item in data["vocabTerms"]:
        vocab = vocabTermLOR(description=item["description"], name=item["name"], nameRef=item["nameRef"])
        vocab.save()


def create_keywords(data):
    for item in data["keywords"]:
        keyword = keywords(description=item["description"], name=item["name"], nameRef=item["nameRef"])
        keyword.save()


def create_regions(data):
    for item in data["regions"]:
        region = Region(abbreviation=item["abbreviation"], iconAbsolutePath=item["iconAbsolutePath"],
                        name=item["name"], nameRef=item["nameRef"])
        region.save()


def create_spell_speeds(data):
    for item in data["spellSpeeds"]:
        spellspeed = SpellSpeed(name=item["name"], nameRef=item["nameRef"])
        spellspeed.save()


def create_rarities(data):
    for item in data["rarities"]:
        rarity = Rarity(name=item["name"], nameRef=item["nameRef"])
        rarity.save()


def create_support_data():
    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\core-en_us\\en_us\\data\\globals-en_us.json') as file:
        data = json.load(file)

        create_vocab_terms(data)
        create_keywords(data)
        create_regions(data)
        create_spell_speeds(data)
        create_rarities(data)
def create_6sett():
    with open('F:\\веб\\course_job\\CORUA\\api\\cards_icons\\set6-lite-en_us\\en_us\\data\\set6-en_us.json',
              encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            card = create_card(item)
            card.save()


#create_support_data()
#create_all_card()
create_6sett()
#from api.cards_icons.create_data import *
