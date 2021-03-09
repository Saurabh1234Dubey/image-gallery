from django.urls import path
from .ajax_views import GetImage
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('filter-image/', csrf_exempt(GetImage), name="filter_image"),



]