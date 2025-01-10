from django.urls import path, include
from rest_framework.routers import DefaultRouter
from companies.views import CompanyViewSet
from departments.views import DepartmentViewSet
from employees.views import EmployeeViewSet
from projects.views import ProjectViewSet
from reviews.views import PerformanceReviewViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('departments', DepartmentViewSet, basename='department')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('projects', ProjectViewSet, basename='project')
router.register('reviews', PerformanceReviewViewSet, basename='review')

urlpatterns = [
    path('api/', include(router.urls)),
]
