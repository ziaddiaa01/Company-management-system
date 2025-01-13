from django.urls import path
from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CompanyViewSet, basename='company')

urlpatterns = router.urls
