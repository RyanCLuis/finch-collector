from django.shortcuts import render

from .models import Finch

# Create your views here.
# finches = [
#     {'name': 'Birdy', 'breed': 'Star finch', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'House Finch', 'description': 'gentle and loving', 'age': 2},
#     {'name': 'Donut', 'breed': 'GoldFinch', 'description': 'cute but kindof scary', 'age': 0},
# ]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches' : finches })