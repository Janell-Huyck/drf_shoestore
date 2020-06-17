from rest_framework.serializers import HyperlinkedModelSerializer

from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('id', 'style')


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color_name')


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id',
                  'size',
                  'brand_name',
                  'manufacturer',
                  'color',
                  'material',
                  'shoe_type',
                  'fasten_type'
                  )
