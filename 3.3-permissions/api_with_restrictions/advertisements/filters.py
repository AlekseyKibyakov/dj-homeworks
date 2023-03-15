from django_filters import rest_framework as filters

from advertisements.models import Advertisement

class F(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
