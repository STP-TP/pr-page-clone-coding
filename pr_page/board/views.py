from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("board index")
    return render(request, 'pr_page/index.html')
