from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import (ManufacturerSerializer,
                             ShoeSerializer,
                             ShoeColorSerializer,
                             ShoeTypeSerializer
                             )

from shoes.models import (Manufacturer,
                          Shoe,
                          ShoeColor,
                          ShoeType
                          )


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    base_name = 'manufacturer'
    queryset = Manufacturer.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    base_name = 'shoe'
    queryset = Shoe.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    base_name = 'shoe_color'
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    base_name = 'shoe_type'
    queryset = ShoeType.objects.all()
