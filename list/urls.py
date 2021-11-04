from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.apiOverview, name='apiOverview'),
    path('api/product-list',views.productList, name='productList'),
    path('api/product-detail/<str:pk>/',views.productDetail,name='productDetail'),
    path('api/product-create/',views.productCreate,name='productCreate'),
    path('api/product-update/<str:pk>/',views.productUpdate,name='productUpdate'),
]