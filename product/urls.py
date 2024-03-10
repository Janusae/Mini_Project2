from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path("" , views.ProductView.as_view(), name = "ProductView"),
    path("add-product" , views.AddForView.as_view(), name = "add_product"),
    path("<int:pk>" , views.Product_DetailView.as_view(), name = "DetailView")
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)