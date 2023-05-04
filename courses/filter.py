from django_filters import rest_framework as filters
from .models import Courses

class CoursesFilter(filters.FilterSet):
    class Meta:
        model = Courses
        fields = {
            'name':['icontains'],
            'instructor__name':['icontains'],
            'price':['lte','gte','range'],
            'category':['exact'],
        }