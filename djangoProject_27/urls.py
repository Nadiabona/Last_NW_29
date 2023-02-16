from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.views import ok, CategoryDetailView, CatListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ok/', ok),
    path('cat/', views.CatListCreateView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('ads/', views.AdsListCreateView.as_view()),
    path('ad/<int:pk>', views.AdsDetailView.as_view()),
]
