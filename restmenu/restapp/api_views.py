from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.exceptions import ValidationError

from .models import Menu
from .serializer import MenuSerializer, MenuStatSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class MenuPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class MenuList(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    lookup_field = ('name',)
    search_fields = ('name', 'description')
    pagination_class = MenuPagination


class CreateMenu(CreateAPIView):
    serializer_class = MenuSerializer


class MenuRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    lookup_field = 'id'
    serializer_class = MenuSerializer


class MenuStats(GenericAPIView):
    lookup_field = 'id'
    serializer_class = MenuStatSerializer
    queryset = Menu.objects.all()
