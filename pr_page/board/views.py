from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("board index")
    categories = ['테스트1', '테스트2', '쇼핑몰', 'a', '목록1', '목록2', '목록3', '목록4']
    content = {'categories': categories}
    return render(request, 'pr_page/index.html', content)
