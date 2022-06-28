from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'mask-types', views.MaskTypeViewSet)
router.register(r'coverage-types', views.CoverageTypeViewSet)
router.register(r'product-types', views.ProductTypeViewSet)
router.register(r'collection-types', views.CollectionTypeViewSet)
router.register(r'browse-types', views.BrowseTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]