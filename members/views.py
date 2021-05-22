from django.shortcuts import render
# HttpResponse는 그냥 response랑 똑같은거
# from django.http import HttpResponse
from . import models as member_models


def member_list_view_handler(request):
    
    members = member_models.MemberModel.objects.all()

    for mem in members:
        if mem.pk % 2 == 0:
            print(f"{mem}짝수")
            mem.isEven = True
        else:
            print(f"{mem}홀수")
            mem.isEven = False

    return render(request, "screens/member_list.html", context={"members": members})
    # context={"members": members}
    