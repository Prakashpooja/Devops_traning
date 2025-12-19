from django.http import JsonResponse

def user_info_v2(request):
    return JsonResponse({
        "version": "v2",
        "name": "Pooja",
        "email": "pooja@example.com",
        "address": "123 Main St",
        "phone": "555-1234",
        "gender": "Female"
    })
