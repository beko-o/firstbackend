from django.urls import path, include
from rest_framework import routers
from films.views import FilmViewSet

router = routers.DefaultRouter()
router.register(r'/api/films', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
