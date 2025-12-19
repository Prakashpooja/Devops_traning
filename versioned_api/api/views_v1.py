from django.http import JsonResponse

def user_info_v1(request):
    return JsonResponse({
        "version": "v1",
        "name": "Pooja",
    })
