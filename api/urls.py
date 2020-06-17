from django.conf.urls import include, url

from api.views import (ManufacturerViewSet,
                       ShoeViewSet,
                       ShoeColorViewSet,
                       ShoeTypeViewSet,
                       )

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'shoe', ShoeViewSet, basename='shoe')
router.register(r'shoe_color', ShoeColorViewSet, basename='shoe_color')
router.register(r'shoe_type', ShoeTypeViewSet, basename='shoe_type')

urlpatterns = [
    url(r'^api/', include(router.urls))
]
