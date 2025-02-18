import django_filters
from .models import Figure

class FigureFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    category = django_filters.ModelChoiceFilter(queryset=Figure.objects.all().values_list('category__name', flat=True).distinct(), label='Категория')
    price = django_filters.RangeFilter(label='Цена')

    class Meta:
        model = Figure
        fields = ['name', 'category', 'price']