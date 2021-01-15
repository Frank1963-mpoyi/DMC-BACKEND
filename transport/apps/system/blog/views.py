from django.shortcuts import render
from .models import DestinationCompany



def home(request):
    template_name = 'blog/index.html'
    dests = DestinationCompany.objects.all()
    context ={'dests' :  dests }
    
    return render (request, template_name, context )
