from django.shortcuts import render

# Create your views here.
def index(request):
    thing = "Thing Name"
    number= 1
    return render(request, 'index.html', { 'number': number, 'thing': thing, })
