from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        "message": "Welcome to ReadHub API 🚀",
        "endpoints": {
            "auth": "/api/auth/",
            "books": "/api/book/",
            "reading_lists": "/api/reading-list/"
        }

    })