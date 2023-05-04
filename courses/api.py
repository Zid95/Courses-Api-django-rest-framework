from rest_framework import generics
from .serializers import InstructorSerializer,Instructor,CoursesSerializer,Courses,InstructorDetailSerializer ,CategorySerializer,Category
from .filter import CoursesFilter
from django_filters.rest_framework import DjangoFilterBackend

class InstructorView(generics.ListAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class InstructorDetail(generics.RetrieveAPIView):
    serializer_class = InstructorDetailSerializer
    queryset = Instructor.objects.all()
    

class CoursesListView(generics.ListAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CoursesFilter

class CoursesDetailView(generics.RetrieveAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()