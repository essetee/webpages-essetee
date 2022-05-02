from django.http import HttpResponse
from django.shortcuts import render


data = {
    'pages':
    [
        {
            'id': 5,
            'fileName': 'test.php',
            'url_description': 'dit is een link tekst naar test.php',
        },
        {
            'id': 6,
            'fileName': 'example.php',
            'url_description': 'dit is een link tekst naar example.php',
        },
        {
            'id': 7,
            'fileName': 'voorbeeld.php',
            'url_description': 'dit is een link tekst naar voorbeeld.php',
        }
    ]
}


def webpages(request):
    return render(request, "webpages/webpages.html", data)


def home(request):
    return HttpResponse("Homepage")
