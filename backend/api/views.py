from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cats.models import Breed, Cat, Rating
from .permissions import IsAuthorOrReadOnly
from .serializers import BreedSerializer, CatSerializer, RatingSerializer

User = get_user_model()


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer
    permission_classes = (
        IsAuthenticated, IsAuthorOrReadOnly,
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsAuthenticated,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (
        IsAuthenticated, IsAuthorOrReadOnly,
    )

    def get_cat(self):
        return get_object_or_404(
            Cat, id=self.kwargs.get('cat_id')
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, cat=self.get_cat())

    def get_queryset(self):
        return Rating.objects.filter(
            user=self.request.user, cat=self.get_cat()
        )
