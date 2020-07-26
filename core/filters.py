import django_filters

from core.models import Terminology

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Terminology
        fields = ["area","word"]