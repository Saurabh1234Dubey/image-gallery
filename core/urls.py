from django.urls import path, include
from .views import Index, ImageUploadView, AddCategoryView


urlpatterns = [
    path('', Index, name="index"),
    path('upload-image/', ImageUploadView.as_view(), name="image_upload"),
    path('add-category/', AddCategoryView.as_view(), name="add_category"),

    # To include ajax_url for ajax call
    path('ajax/', include('core.ajax_urls')),

]