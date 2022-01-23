from django.http import HttpResponse
from testApi.models import Author, Books

def index(request):
    # a= Author.objects.create(name = "Varun", email = "Varun@char.com")
    # a.save()
    a = Author.objects.get(id=2)
    b = Books.objects.create(title = "chat story", reporter = a)
    b.save()
    return HttpResponse("Hello, world. You're at the polls index.")
