from django.urls import path
from rest_framework.routers import SimpleRouter

from ads import views

# urlpatterns = [
#     path('', views.CategoryListView.as_view(), name = 'category_list'),
#     path('create/', views.CategoryCreateView.as_view(), name='category_create'),
#     path('<int:pk>/', views.CategoryDetailView.as_view(), name = 'category_detail'),
#     path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
#     path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
# ]

from ads.views import CatViewSet

cat_router = SimpleRouter()
cat_router.register('', CatViewSet)

urlpatterns = cat_router.urls