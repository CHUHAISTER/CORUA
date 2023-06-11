import requests
from django.contrib.messages import api
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from ..cards_icons.lor_deckcodes.models import LoRDeck
from ..models import *

headers_lor = {
    "X-Riot-Token": "RGAPI-d89a6001-7049-4504-9952-656f9b290e30"
}

def decode_code_deck(deck_code):
    deck = LoRDeck.from_deckcode(deck_code)
    cards = deck.cards
    for i in range(len(cards)):
        cards[i] = [cards[i].count, cards[i].card_code]
    return cards

@csrf_exempt
def find_account(request):
    if request.method == "POST":
        data = json.loads(request.body)
        req = requests.get(
            "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + data['inputValue'] + "/"+
            data['inputTag'],
            headers=headers_lor)
        if ('puuid' in req.json()):
            puuid = req.json()['puuid']
            server = get_server(puuid)
            stat_math = get_matches(puuid, server)

            response_data = {"matches":stat_math, "puuid":puuid}

        else:
            response_data = {"error": "Введи, будь ласка коректні дані:)"}
        return JsonResponse(response_data)


def get_server(puuid):
    return requests.get("https://americas.api.riotgames.com/riot/account/v1/active-shards/by-game/lor/by-puuid/" +
                          puuid, headers=headers_lor).json()['activeShard']

def get_matches(puuid, server):
    matches = requests.get("https://" + server + ".api.riotgames.com/lor/match/v1/matches/by-puuid/" + puuid + "/ids",
                           headers=headers_lor)
    k_mathces = len(matches.json())
    stat_math = {}
    for i in range(3):
        stat_math[str(i)] = {}
    for i in range(3):
        stat_math[str(i)] = (requests.get("https://" + server + ".api.riotgames.com/lor/match/v1/matches/"
                                          + matches.json()[i], headers=headers_lor))
        stat_math[str(i)] = stat_math[str(i)].json()
        stat_math[str(i)] = stat_math[str(i)]['info']['players']
        deck_code = stat_math[str(i)][0]["deck_code"]
        card_list = decode_code_deck(deck_code)

        card_out = []
        for j in range(len(card_list)):
            try:

                card_dict = (Card.objects.get(cardCode=card_list[j][1])).__dict__
            except :
                card_dict = (Card.objects.get(cardCode="07SI002T2")).__dict__
            card_dict.pop('_state', None)
            card_out.append([card_dict, int(card_list[j][0])])

        stat_math[str(i)][0]["card_list"] = card_out
        if len(stat_math[str(i)]) == 2:
            deck_code = stat_math[str(i)][1]["deck_code"]
            card_list = decode_code_deck(deck_code)

            card_out = []
            for j in range(len(card_list)):
                try:
                    card_dict = (Card.objects.get(cardCode=card_list[j][1])).__dict__
                except :
                    print(card_list[j][1])
                    card_dict = (Card.objects.get(cardCode="07SI002T2")).__dict__
                card_dict.pop('_state', None)
                card_out.append([card_dict, int(card_list[j][0])])

            stat_math[str(i)][1]["card_list"] = card_out
    return stat_math
