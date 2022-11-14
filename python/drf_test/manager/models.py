from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """ Создаем пользователя """
        if not email:
            raise ValueError('Не задан email')
        try:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            default_categories = ["Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина",
                                  "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника",
                                  "Продукты", "Проезд"]
            categories = Category.objects.bulk_create(
                [Category(name=category_name) for category_name in default_categories])
            user.save()
            user.category.add(*categories)
            return user
        except:
            raise


    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ Расширенная модель пользователя """
    balance = models.DecimalField(decimal_places=2, max_digits=50, verbose_name='баланс', default=0)
    category = models.ManyToManyField(Category, related_name='user_category', verbose_name='категории', blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username


class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь')
    sum = models.DecimalField(decimal_places=2, max_digits=50, verbose_name='сумма оплаты')
    date_stamp = models.DateField(auto_now_add=True, verbose_name='дата транзакции')
    time_stamp = models.TimeField(auto_now_add=True, verbose_name='время транзакции')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='категория')
    organisation = models.CharField(max_length=100, verbose_name='организация')
    description = models.CharField(max_length=200, verbose_name='описание', null=True, blank=True)

    def __str__(self):
        return self.user.username
