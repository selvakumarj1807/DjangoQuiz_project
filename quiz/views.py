from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"message": "Django API is working!"})

from django.shortcuts import render

def quiz_page(request):
    return render(request, "quiz/index.html")
