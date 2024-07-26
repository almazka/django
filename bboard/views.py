from django.http import HttpResponse, HttpRequest
from typing import Optional


def index(request: Optional[HttpRequest]):
    return HttpResponse("Здесь будет выведен список объявлений!")
