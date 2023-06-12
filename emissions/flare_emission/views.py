from django.shortcuts import render

# Create your views here.
from flare_emission.models import Compound, Composition, EmissionInput, FlareInput
from API.serializers import CompoundSerializer, CompositionSerializer, EmissionInputSerializer, FlareInputSerializer
from rest_framework import generics


class CompoundList(generics.ListCreateAPIView):
    queryset = Compound.objects.all()
    serializer_class = CompoundSerializer


class CompoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compound.objects.all()
    serializer_class = CompoundSerializer

class CompositionList(generics.ListCreateAPIView):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class CompositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class EmissionInputList(generics.ListCreateAPIView):
    queryset = EmissionInput.objects.all()
    serializer_class = EmissionInputSerializer


class EmissionInputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmissionInput.objects.all()
    serializer_class = EmissionInputSerializer

class FlareInputList(generics.ListCreateAPIView):
    queryset = FlareInput.objects.all()
    serializer_class = FlareInputSerializer


class FlareInputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlareInput.objects.all()
    serializer_class = FlareInputSerializer