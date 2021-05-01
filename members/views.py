from django.shortcuts import render
# HttpResponse는 그냥 response랑 똑같은거
from django.http import HttpResponse


def all_member_views(request):
    return HttpResponse("<h1>Hello World</h1>")