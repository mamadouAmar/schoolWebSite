from django.shortcuts import render

# Create your views here.
def afficher_index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "apropos.html")