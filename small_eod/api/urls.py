from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet, GroupViewSet, AddressDataViewSet, InstitutionViewSet, CaseViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('address', AddressDataViewSet)
router.register('institution', InstitutionViewSet)
router.register('case', CaseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]