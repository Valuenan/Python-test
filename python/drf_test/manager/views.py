from datetime import datetime
from decimal import Decimal
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TransactionHistory, Category, User
from .serializers import TransactionSerializer, CreateTransactionSerializer, UserSerializer, CategorySerializer, \
    CreateCategorySerializer
from .service import TransactionFilter



class TransactionCreateView(APIView):
    """ Создание транзакции """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = CreateTransactionSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            user.balance += Decimal(serializer.validated_data['sum'])
            if user.balance < 0:
                return Response({"detail": "Недостаточно средств"}, status=status.HTTP_400_BAD_REQUEST)
            user.save()
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionListView(generics.ListAPIView):
    """ Список транзакций """
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = TransactionFilter
    filter_fields = '__all__'
    ordering = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return TransactionHistory.objects.filter(user=self.request.user.id)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Просмотр, изменение, удаление транзакции """
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return TransactionHistory.objects.filter(user=self.request.user.id)


class UserDetailView(generics.ListAPIView):
    """ Информация о пользователе """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class CategoryListView(generics.ListAPIView):
    """ Информация о пользователе """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Category.objects.filter(user_category__id=self.request.user.id)


class CategoryCreateView(APIView):
    """ Создание категории """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = CreateCategorySerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            category = serializer.save()
            user.category.add(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Category.objects.filter(user_category__id=self.request.user.id)
