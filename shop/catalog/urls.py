from django.urls import path
from .views import ProductListView, ProductDetail, SearchResultsView

app_name = 'catalog'

urlpatterns = [
    path('<str:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail',),
    path('<str:category_slug>/', ProductListView.as_view(), name='product_list_by_category',),

]
