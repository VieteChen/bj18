from django.conf import settings
from  django.http import HttpResponse,JsonResponse

def index (request):
    return HttpResponse('hello')
