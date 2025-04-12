from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet



router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('product/', views.ProductAPIView.as_view(), name='product'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('', include(router.urls))
]

