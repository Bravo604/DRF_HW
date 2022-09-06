from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Category, Company, Item
from .serializers import CategorySerializer, CompanySerializer, ItemSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin


class ItemGenericViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CompanyGenericViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin,
                            UpdateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
