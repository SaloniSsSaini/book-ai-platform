from django.http import JsonResponse
from .services import answer_question

def ask(request):
    q = request.GET.get("q")
    return JsonResponse(answer_question(q))