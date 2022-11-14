from rest_framework import serializers

from .models import TransactionHistory, Category, User


class TransactionSerializer(serializers.ModelSerializer):
    """ Сериалайзер для получения, изменения и удаления транзакции """

    class Meta:
        model = TransactionHistory
        fields = '__all__'


class CreateTransactionSerializer(serializers.ModelSerializer):
    """ Сериалайзер создания транзакции """

    class Meta:
        model = TransactionHistory
        fields = ('sum', 'category', 'organisation', 'description')


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер пользователя """

    class Meta:
        model = User
        fields = ('balance',)


class CreateCategorySerializer(serializers.ModelSerializer):
    """ Сериалайзер создания категории пользователя """

    class Meta:
        model = Category
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    """ Сериалайзер категорий пользователя """

    class Meta:
        model = Category
        fields = '__all__'
