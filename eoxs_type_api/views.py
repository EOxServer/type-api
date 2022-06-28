from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from eoxserver.resources.coverages import models

from . import serializers



class MaskTypeViewSet(viewsets.ModelViewSet):
    queryset = models.MaskType.objects.all()
    serializer_class = serializers.MaskTypeSerializer


class CoverageTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CoverageType.objects.all()
    serializer_class = serializers.CoverageTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer


class CollectionTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CollectionType.objects.all()
    serializer_class = serializers.CollectionTypeSerializer


class BrowseTypeViewSet(viewsets.ModelViewSet):
    queryset = models.BrowseType.objects.all()
    serializer_class = serializers.BrowseTypeSerializer
