from django.urls import path
from core import views as core_views

app_name = "core"

urlpatterns = [
    # path("", 화면을 연결해주는 컨트롤러, name="home")
    path("", core_views.renderHome, name="home")
]