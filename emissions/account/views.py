from django.shortcuts import render

# Create your views here.
from account.models import Profile, IndustryCategory, Account, SubscriptioPlan, EmissionPackage
from API.serializers import ProfileSerializer, IndustryCategorySerializer, AccountSerializer, SubscriptioPlanSerializer, SubscriptionPackageSerializer, EmissionPackageSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class IndustryCategoryList(generics.ListCreateAPIView):
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategorySerializer


class IndustryCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategorySerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class SubscriptioPlanList(generics.ListCreateAPIView):
    queryset = SubscriptioPlan.objects.all()
    serializer_class = SubscriptioPlanSerializer


class SubscriptioPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptioPlan.objects.all()
    serializer_class = SubscriptioPlanSerializer

# class SubscriptionPackageList(generics.ListCreateAPIView):
#     queryset = SubscriptionPackage.objects.all()
#     serializer_class = SubscriptionPackageSerializer


# class SubscriptionPackageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SubscriptionPackage.objects.all()
#     serializer_class = SubscriptionPackageSerializer

class EmissionPackageList(generics.ListCreateAPIView):
    queryset = EmissionPackage.objects.all()
    serializer_class = EmissionPackageSerializer


class EmissionPackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmissionPackage.objects.all()
    serializer_class = EmissionPackageSerializer