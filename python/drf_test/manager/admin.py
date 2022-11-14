from django.contrib import admin

from .models import Category, TransactionHistory, User


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass


@admin.register(TransactionHistory)
class AdminTransactionHistory(admin.ModelAdmin):
    readonly_fields = ['date_stamp', 'time_stamp']
