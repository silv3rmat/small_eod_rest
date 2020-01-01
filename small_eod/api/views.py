from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from django.conf import settings


from api.models import AddressData, Institution, Case
from api.serializers import UserSerializer, GroupSerializer, AddressDataSerializer, InstitutionSerializer, CaseSerializer

# User = settings.USER_MODEL

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AddressDataViewSet(viewsets.ModelViewSet):
    queryset = AddressData.objects.all()
    serializer_class = AddressDataSerializer



class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer