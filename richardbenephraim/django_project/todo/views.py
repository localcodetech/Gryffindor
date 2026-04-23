from django.shortcuts import render
from .models import Category, Channel

# Create your views here.

def index(request):
    content = Channel.objects.all()
    cat_content = Category.objects.all()

    response = render(request, 'index.html', context={'channels': content})

    return response
