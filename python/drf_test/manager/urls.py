from django.urls import path, include

from .views import TransactionCreateView, TransactionListView, TransactionDetailView, CategoryDetailView, \
    UserDetailView, CategoryCreateView, CategoryListView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('transaction/create/', TransactionCreateView.as_view()),
    path('transaction/list/', TransactionListView.as_view()),
    path('transaction/detail/<int:pk>/', TransactionDetailView.as_view()),
    path('user/', UserDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
]
