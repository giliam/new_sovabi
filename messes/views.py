from django.shortcuts import render

from messes.models import Messe

def liste_messes(request):
    messes = Messe.objects.all()

    return render(request, 'messes/liste.html', {
        "messes":messes,
    })