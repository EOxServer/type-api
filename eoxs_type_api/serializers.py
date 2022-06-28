from rest_framework import serializers
from eoxserver.resources.coverages import models


class MaskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MaskType
        fields = '__all__'


class CoverageTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CoverageType
        fields = '__all__'


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductType
        fields = '__all__'


class CollectionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CollectionType
        fields = '__all__'


class BrowseTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BrowseType
        fields = '__all__'

