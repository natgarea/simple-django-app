from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first_view(request):
    # return HttpResponse("Saludos")

    context = {
        'sample_var': "ejemplo"
    }

    return render(request, 'beers.html', context)
