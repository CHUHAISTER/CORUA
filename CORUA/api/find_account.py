import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .global_var import headers_lor


@csrf_exempt
def find_account(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        req = requests.get(
            "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + data['inputValue'] + "/"+
            data['inputTag'],
            headers=headers_lor)
        puuid = req.json()['puuid']
        lor = requests.get("https://europe.api.riotgames.com/lor/match/v1/matches/by-puuid/" + puuid + "/ids",
                           headers=headers_lor)
        response_data = {"message": puuid, "maths":lor.json()}

        return JsonResponse(response_data)


    # Handle other request methods if needed
