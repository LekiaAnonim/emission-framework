from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/<int:pk>/', views.AccountDetail.as_view()),
    path('emission-packages/', views.EmissionPackageList.as_view()),
    path('emission-package/<int:pk>/', views.EmissionPackageDetail.as_view()),
    path('industry-categories/', views.IndustryCategoryList.as_view()),
    path('industry-category/<str:slug>/', views.IndustryCategoryDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profile/<str:slug>/', views.ProfileDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profile/<str:slug>/', views.ProfileDetail.as_view()),
    # path('subscription-packages/', views.SubscriptionPackageList.as_view()),
    # path('subscription-package/<int:pk>/', views.SubscriptionPackageDetail.as_view()),
    path('subscription-plans/', views.SubscriptioPlanList.as_view()),
    path('subscription-plan/<int:pk>/', views.SubscriptioPlanDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)