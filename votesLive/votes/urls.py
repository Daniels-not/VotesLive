from django.urls import path

from . import views

app_name = "voteLive"

urlpatterns = [
    path('', views.index, name="index"),  # index router
    path('<int:question_id>/', views.choice, name='choice'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
