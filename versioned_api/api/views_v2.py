from django.http import JsonResponse

def user_info_v2(request):
    return JsonResponse({
        "version": "v2",
        "name": "Pooja",
        "role": "Developer",
        "location": "India"
    })
