from django_filters import rest_framework as filters, DateFilter, TimeFilter

from .models import TransactionHistory


class TransactionFilter(filters.FilterSet):
    sum = filters.NumericRangeFilter(field_name='sum', lookup_expr='in')
    from_date = DateFilter(field_name='date_stamp', lookup_expr='gte')
    to_date = DateFilter(field_name='date_stamp', lookup_expr='lte')
    from_time = TimeFilter(field_name='time_stamp', lookup_expr='gte')
    to_time = TimeFilter(field_name='time_stamp', lookup_expr='lte')

    class Meta:
        model = TransactionHistory
        fields = ['sum', 'from_date', 'to_date', 'from_time', 'to_time']


