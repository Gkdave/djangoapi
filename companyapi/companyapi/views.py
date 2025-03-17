

from django.http import JsonResponse


def index(request):
    friends=[
        'Gajendra',
        'bhawana',
        'Rashmi'
    ]
    return JsonResponse(friends,safe=False)
