import django_filters
from .models import *


class ResultFilter(django_filters.FilterSet):
    class Meta:
        model = Result
        fields = ["lessthan_85", "lessthan_65"]
