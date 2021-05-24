from django.shortcuts import render


def index(request):

    context = {
        'title_page': "Home",
        'home': True
    }

    return render(request, 'home.html', context)
