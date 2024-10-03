from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, BreedViewSet, RatingViewSet

app_name = 'api'

api_router = DefaultRouter()

api_router.register('cats', CatViewSet, basename='cats')
api_router.register('cats/(?P<cat_id>\\d+)/rate',
                    RatingViewSet, basename='rating')
api_router.register('breeds', BreedViewSet, basename='breeds')

urlpatterns = [
    path('', include(api_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
