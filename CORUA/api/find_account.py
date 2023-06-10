import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .global_var import headers_lor


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
            response_data = {"matches":stat_math}
        else:
            response_data = {"error": "puuid not found"}
        return JsonResponse(response_data)


def get_server(puuid):
    return requests.get("https://americas.api.riotgames.com/riot/account/v1/active-shards/by-game/lor/by-puuid/" +
                          puuid, headers=headers_lor).json()['activeShard']

def get_matches(puuid, server):
    matches = requests.get("https://" + server + ".api.riotgames.com/lor/match/v1/matches/by-puuid/" + puuid + "/ids",
                           headers=headers_lor)
    k_mathces = len(matches.json())
    stat_math = {}
    for i in range(1, k_mathces):
        stat_math[str(i)] = {}
    for i in range(k_mathces):
        stat_math[str(i)] = (requests.get("https://" + server + ".api.riotgames.com/lor/match/v1/matches/"
                                          + matches.json()[i], headers=headers_lor).json())
    return stat_math
