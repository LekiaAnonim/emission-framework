from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from flare_emission import views

urlpatterns = [
    path('compositions/', views.CompositionList.as_view()),
    path('composition/<int:pk>/', views.CompositionDetail.as_view()),
    path('compounds/', views.CompoundList.as_view()),
    path('compoound/<int:pk>/', views.CompoundDetail.as_view()),
    path('emission-inputs/', views.EmissionInputList.as_view()),
    path('emission-input/<int:pk>/', views.EmissionInputDetail.as_view()),
    path('flare-inputs/', views.FlareInputList.as_view()),
    path('flare-input/<int:pk>/', views.FlareInputDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)