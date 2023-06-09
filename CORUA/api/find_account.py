from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def find_account(request):
    if request.method == "POST":
        data = json.loads(request.body)
        input_value = data.get("inputValue")
        response_data = {"message": "i live" + input_value}
        return JsonResponse(response_data)


    # Handle other request methods if needed
